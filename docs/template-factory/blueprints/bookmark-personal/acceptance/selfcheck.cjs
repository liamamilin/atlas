// Deliberately nonfunctional target. Success means the acceptance tool rejects it.
const http=require('node:http');const {spawn}=require('node:child_process');const fs=require('node:fs');const os=require('node:os');const path=require('node:path');const assert=require('node:assert/strict');
(async()=>{
 const dir=fs.mkdtempSync(path.join(os.tmpdir(),'atlas-bookmark-harness-'));const result=path.join(dir,'result.json');
 const html='<!doctype html><html lang="zh"><meta charset="utf-8"><title>Deliberately broken target</title><form novalidate><label>标题<input></label><label>链接地址<input></label><label>分类<input></label><button>保存书签</button></form></html>';
 const server=http.createServer((req,res)=>{res.setHeader('Content-Type','text/html; charset=utf-8');res.end(html);});await new Promise(r=>server.listen(0,'127.0.0.1',r));
 try{
  const command=[path.join(__dirname,'run.cjs'),'--base-url','http://127.0.0.1:'+server.address().port,'--phase','P0','--case','A01','--out',result];
  const code=await new Promise((resolve,reject)=>{const child=spawn(process.execPath,command,{env:{...process.env,BOOKMARK_TEST_TIMEOUT_MS:'1200'},stdio:['ignore','ignore','inherit']});child.on('error',reject);child.on('close',resolve);});
  const report=JSON.parse(fs.readFileSync(result));assert.equal(code,1);assert.equal(report.passed,false);assert.equal(report.cases[0].id,'A01');assert.equal(report.cases[0].status,'failed');
  console.log(JSON.stringify({scope:'acceptance harness selfcheck only; deliberately nonfunctional target',passed:true,detected:'A01 failed on a target that does not save any bookmarks',product_acceptance:'not_run'}));
 }finally{await new Promise(r=>server.close(r));fs.rmSync(dir,{recursive:true,force:true});}
})().catch(e=>{console.error(e);process.exitCode=1;});
