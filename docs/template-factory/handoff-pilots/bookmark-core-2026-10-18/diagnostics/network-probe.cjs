// Tests the generated acceptance helper, not the downstream app. Synthetic credentials only.
const fs=require('node:fs');
const path=require('node:path');
const http=require('node:http');
const {chromium}=require('/Users/milin/2026/软件开发/application-atlas/atlas-web/node_modules/playwright');
const here=__dirname;
const result=JSON.parse(fs.readFileSync(path.join(here,'../production/blueprint-code-1/result.json'),'utf8'));
fs.writeFileSync(path.join(here,'helper-original.cjs'),result.content);
const helper=require('./helper-original.cjs');
const seen=[];
let browser;
const trap=http.createServer((req,res)=>{seen.push({path:req.url,authorization:req.headers.authorization||null});res.end('<p>local trap</p>');});
const origin=http.createServer((req,res)=>{if(req.url==='/redirect'){res.writeHead(302,{Location:`http://127.0.0.1:${trap.address().port}/cross-origin`});res.end();}else res.end('<p>local target</p>');});
const proxy=http.createServer((req,res)=>{res.writeHead(502);res.end();});
proxy.on('connect',(_,socket)=>socket.end('HTTP/1.1 502 Denied\r\n\r\n'));
const listen=s=>new Promise(resolve=>s.listen(0,'127.0.0.1',resolve));
const close=s=>new Promise(resolve=>s.close(resolve));
(async()=>{
 try{
  await listen(trap);await listen(origin);await listen(proxy);
  browser=await chromium.launch({headless:true,proxy:{server:`http://127.0.0.1:${proxy.address().port}`,bypass:'127.0.0.1,localhost'}});
  const context=await browser.newContext({serviceWorkers:'block'});
  const page=await context.newPage();
  const target=`http://127.0.0.1:${origin.address().port}`;
  const config=helper.loadConfig({TARGET_URL:target,AUTH_USER:'synthetic-user',AUTH_PASS:'synthetic-marker'});
  const guard=helper.installNetworkPolicy(page,config);
  helper.applyTargetCredentials(context,config);
  await page.goto(target+'/redirect');
  await page.waitForTimeout(100);
  let guardClaim;
  try{guard.assertNoBackgroundOutbound();guardClaim='no_background_outbound_reported';}catch(e){guardClaim=String(e);}
  const output={scope:'acceptance helper diagnostic, not app acceptance',fixtures:'two owned loopback origins, synthetic Basic marker, deny-only proxy',cross_origin_requests:seen,guard_claim:guardClaim,violations:guard.violations,attempted:guard.attemptedOpens};
  fs.writeFileSync(path.join(here,'network-result.json'),JSON.stringify(output,null,2)+'\n');
  console.log(JSON.stringify(output));
 }finally{if(browser)await browser.close();await Promise.all([close(origin),close(trap),close(proxy)]);}
})().catch(e=>{console.error(e);process.exitCode=1;});
