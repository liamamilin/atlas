import fs from 'node:fs/promises';
import http from 'node:http';
import crypto from 'node:crypto';
import {createRequire} from 'node:module';
const require=createRequire(import.meta.url);
const {chromium}=require('/Users/milin/2026/软件开发/application-atlas/atlas-web/node_modules/@playwright/test');
const args=Object.fromEntries(process.argv.slice(2).reduce((a,x,i,xs)=>i%2?a:[...a,[x.slice(2),xs[i+1]]],[]));
const base=args['base-url'];
const hash=s=>crypto.createHash('sha256').update(s).digest('hex');
const attemptedTitle='T'.repeat(1001000);
const url='https://example.com/diagnostic/oversized-form';
let browser,proxy;
const blocked=[];
try {
  proxy=http.createServer((req,res)=>{
    let target;try{target=new URL(req.url);}catch{res.writeHead(403);res.end();return;}
    if(target.origin!==base){blocked.push(target.origin);res.writeHead(403);res.end();return;}
    const upstream=http.request(target,{method:req.method,headers:{...req.headers,host:target.host}},up=>{res.writeHead(up.statusCode,up.headers);up.pipe(res);});
    upstream.on('error',()=>{res.writeHead(502);res.end();});req.pipe(upstream);
  });
  proxy.on('connect',(req,socket)=>socket.end('HTTP/1.1 403 Forbidden\r\nConnection: close\r\n\r\n'));
  await new Promise(resolve=>proxy.listen(0,'127.0.0.1',resolve));
  browser=await chromium.launch({headless:true,proxy:{server:`http://127.0.0.1:${proxy.address().port}`},args:['--proxy-bypass-list=<-loopback>']});
  const page=await browser.newPage();
  await page.goto(base+'/');
  const saveForm=()=>page.locator('form.save-form');
  async function submit(form){
    const pending=page.waitForResponse(r=>r.request().method()==='POST'&&new URL(r.url()).origin===base);
    await form.locator('button[type=submit]').click();
    const response=await pending;await response.finished();await page.waitForLoadState('domcontentloaded');
    return response;
  }
  async function save(link,title){
    await page.locator('#save-url').fill(link);
    await page.locator('#save-title').fill(title);
    return await submit(saveForm());
  }
  await save('https://example.com/diagnostic/existing','原有记录保持完整');
  const categoryChecks=[];
  const create=()=>page.locator('form.category-create-form');
  if(await create().count()){
    for(const [label,name] of [['blank','   '],['create','诊断分类'],['duplicate','诊断分类']]){
      await create().locator('input[name=name]').fill(name);
      await submit(create());
      const feedback=await page.locator('.form-error').allTextContents();
      categoryChecks.push({label,name,feedback,retainedInput:await create().locator('input[name=name]').inputValue(),
        actualCategoryLinkCount:await page.getByRole('link',{name:'诊断分类',exact:true}).count()});
      await page.goto(base+'/');
    }
    const existing=()=>page.locator('li.record-card').filter({has:page.locator('a.record-open',{hasText:'原有记录保持完整'})});
    for(const label of ['诊断分类','未分类（以后看看）']){
      await existing().locator('select[name=category_id]').selectOption({label});
      await submit(existing().locator('form.move-form'));
      categoryChecks.push({label:'move',destination:label,readback:await existing().locator('.record-category').innerText()});
    }
  }
  const before=await page.locator('li.record-card').evaluateAll(ns=>ns.map(n=>({url:n.dataset.url,title:n.querySelector('a.record-open')?.textContent})));
  const response=await save(url,attemptedTitle);
  const posted=response.request().postData()??'';
  const submittedTitle=new URLSearchParams(posted).get('title')??'';
  const immediateBody=await page.locator('body').innerText();
  await page.screenshot({path:args.evidence+'/oversized-feedback.png',fullPage:false});
  await page.goto(base+'/');
  const after=await page.locator('li.record-card').evaluateAll(ns=>ns.map(n=>({url:n.dataset.url,titleLength:n.querySelector('a.record-open')?.textContent.length})));
  const found=after.find(r=>r.url===url);
  const result={
    kind:'posthoc diagnostic plus repair category negative checks; not a change to R01-R09',categoryChecks,
    attemptedTitleLength:attemptedTitle.length,attemptedTitleSha256:hash(attemptedTitle),
    submittedTitleLength:submittedTitle.length,submittedTitleSha256:hash(submittedTitle),
    submittedBodyBytes:Buffer.byteLength(posted),httpStatus:response.status(),
    immediateBody:immediateBody.slice(0,4000),before,after,
    fullSubmissionVerified:submittedTitle===attemptedTitle,
    existingRecordPreserved:after.some(r=>r.url===before[0]?.url&&r.titleLength===before[0]?.title.length),
    outcome:submittedTitle!==attemptedTitle?'submission_not_verified':found?(found.titleLength===attemptedTitle.length?'full_value_accepted':'accepted_partial_value'):response.status()===413?'explicitly_rejected_413_no_new_record':'not_saved_inspect_feedback',
    blockedOrigins:blocked,
  };
  await fs.writeFile(args.evidence+'/result.json',JSON.stringify(result,null,2)+'\n');
  console.log(JSON.stringify(result));
}finally{
  if(browser)await browser.close();
  if(proxy)await new Promise(resolve=>proxy.close(resolve));
}
