// Actual transport diagnostic for the OpenCode exact-patched helper; no real credentials.
const fs=require('node:fs');
const http=require('node:http');
const helperPath=process.argv[2]||__dirname+'/helper-fixed.cjs';
const outputPath=process.argv[3]||__dirname+'/network-fixed-result.json';
const helper=require(helperPath);
const seen=[];
const trap=http.createServer((req,res)=>{seen.push({path:req.url,authorization:req.headers.authorization||null});res.end('local trap');});
const origin=http.createServer((req,res)=>{
 if(req.url.startsWith('/redirect')){res.writeHead(302,{Location:`http://127.0.0.1:${trap.address().port}/cross-origin`});res.end();}
 else res.end('<!doctype html><title>local target</title><p>target</p>');
});
let browser;
const listen=s=>new Promise(resolve=>s.listen(0,'127.0.0.1',resolve));
const close=s=>new Promise(resolve=>s.close(resolve));
(async()=>{
 try{
  await listen(trap);await listen(origin);
  const target=`http://127.0.0.1:${origin.address().port}`;
  const config=helper.loadConfig({TARGET_URL:target,AUTH_USER:'synthetic-user',AUTH_PASS:'synthetic-marker'});
  browser=await helper.launchBrowser(config);
  const context=await browser.newContext({serviceWorkers:'block'});
  const page=await context.newPage();
  const guard=helper.installNetworkPolicy(page,config);
  helper.applyTargetCredentials(context,config);
  const response=await page.goto(target+'/redirect');
  const documentStatus=response.status();
  await page.goto(target+'/');
  await page.evaluate(()=>fetch('/redirect-fetch').then(r=>r.status).catch(e=>String(e)));
  await page.waitForTimeout(100);
  let guardClaim;
  try{guard.assertNoBackgroundOutbound();guardClaim='no_background_outbound_reported';}catch(e){guardClaim='background_outbound_attempt_reported';}
  let unsupportedRejected=false,userInfoRejected=false,userInfoRedacted=false;
  try{helper.loadConfig({TARGET_URL:target,AUTH_USER:'synthetic-user',AUTH_PASS:'synthetic-marker',AUTH_MODE:'unsupported'});}catch{unsupportedRejected=true;}
  try{helper.loadConfig({TARGET_URL:target.replace('http://','http://synthetic-user:synthetic-marker@')});}catch(e){userInfoRejected=true;userInfoRedacted=!e.message.includes('synthetic-marker')&&!e.message.includes('synthetic-user');}
  const result={scope:'generated acceptance helper transport diagnostic only',cross_origin_requests:seen,document_status:documentStatus,guard_claim:guardClaim,blocked:guard.blocked,violations:guard.violations,attempted:guard.attemptedOpens,unsupported_mode_rejected:unsupportedRejected,userinfo_rejected:userInfoRejected,userinfo_error_redacted:userInfoRedacted,helper_sha256:require('node:crypto').createHash('sha256').update(fs.readFileSync(helperPath)).digest('hex')};
  result.passed=seen.length===0&&guardClaim==='background_outbound_attempt_reported'&&guard.attemptedOpens.length>0&&unsupportedRejected&&userInfoRejected&&userInfoRedacted;
  fs.writeFileSync(outputPath,JSON.stringify(result,null,2)+'\n');
  console.log(JSON.stringify(result));
  if(!result.passed)process.exitCode=1;
 }finally{if(browser)await browser.close();await Promise.all([close(origin),close(trap)]);}
})().catch(e=>{console.error(e);process.exitCode=1;});
