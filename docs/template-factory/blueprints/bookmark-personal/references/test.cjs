const fs=require('node:fs');const path=require('node:path');const http=require('node:http');const assert=require('node:assert/strict');const {pathToFileURL}=require('node:url');const {chromium}=require('playwright');
(async()=>{
 const {normalizeBookmarkUrl}=await import(pathToFileURL(path.join(__dirname,'url-policy.mjs')));
 assert.equal(normalizeBookmarkUrl('  https://EXAMPLE.com/path?q=1#part  '),'https://example.com/path?q=1#part');
 for(const value of ['javascript:alert(1)','data:text/html,bad','file:///etc/passwd','/relative','https://user:secret@example.com/',null])assert.throws(()=>normalizeBookmarkUrl(value));
 const server=http.createServer((req,res)=>{if(req.url==='/atomic-idb.mjs'){res.setHeader('Content-Type','text/javascript');res.end(fs.readFileSync(path.join(__dirname,'atomic-idb.mjs')));}else{res.setHeader('Content-Type','text/html');res.end('<!doctype html><title>Reference test</title>');}});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const origin='http://127.0.0.1:'+server.address().port;
 let browser;try{
  browser=await chromium.launch({headless:true});const page=await browser.newPage();await page.goto(origin);
  const result=await page.evaluate(async()=>{
   const {writeRecords}=await import('/atomic-idb.mjs');
   const db=await new Promise((resolve,reject)=>{const r=indexedDB.open('atlas-reference-test',1);r.onupgradeneeded=()=>r.result.createObjectStore('records',{keyPath:'id'});r.onsuccess=()=>resolve(r.result);r.onerror=()=>reject(r.error);});
   await writeRecords(db,'records',[{id:'before',value:1}]);
   const read=()=>new Promise((resolve,reject)=>{const r=db.transaction('records').objectStore('records').getAll();r.onsuccess=()=>resolve(r.result);r.onerror=()=>reject(r.error);});
   const first=await read();const original=db.transaction.bind(db);
   db.transaction=(...args)=>{const tx=original(...args);if(args[1]==='readwrite')queueMicrotask(()=>tx.abort());return tx;};
   let rejected=false;try{await writeRecords(db,'records',[{id:'before',value:99},{id:'partial',value:2}]);}catch{rejected=true;}
   db.transaction=original;const after=await read();db.close();return {first,rejected,after};
  });
  assert.deepEqual(result.first,[{id:'before',value:1}]);assert.equal(result.rejected,true);assert.deepEqual(result.after,result.first);
  console.log(JSON.stringify({scope:'Atlas-authored reference modules only',passed:true,checks:['URL normalization and dangerous-input rejection','write commit persists','aborted multi-record write rejects and preserves previous records']}));
 }finally{if(browser)await browser.close();await new Promise(r=>server.close(r));}
})().catch(e=>{console.error(e);process.exitCode=1;});
