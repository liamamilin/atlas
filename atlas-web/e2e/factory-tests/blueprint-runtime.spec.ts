import {test,expect} from '@playwright/test';

const digest='a'.repeat(64);
const artifact={
  artifact_type:'product-blueprint',id:'tpl_0123456789abcdef0123456789abcdef',job_id:'job_blueprint',leaf:'bookmark-manager',scenario_name:'书签管理',scenario_revision:1,
  digest,level:'L0',state:'draft',created_at:new Date().toISOString(),manifest:{name:'Bookmark blueprint',description:'Store bookmarks',version:'1.0',feature_count:1,decision_count:0,phase_count:1,acceptance_count:1,phases:[{id:'P0',title:'Core'}]},
  provenance:{},formal_checks:[],acceptance_jobs:[],acceptances:[],reports:[],
};
const adapter={supported:true,reason:null,protocol:'atlas.acceptance-runner.v1',result_schema:'atlas.acceptance-result.v1',network:'none'};

async function setup(page:import('@playwright/test').Page,supported=true,acceptances:unknown[]=[]){
  await page.route('**/api/factory/catalog',r=>r.fulfill({json:[]}));
  await page.route('**/api/factory/batches',r=>r.fulfill({json:[]}));
  await page.route('**/api/factory/status',r=>r.fulfill({json:{cli:{available:false,models:[]},runtime:{available:false}}}));
  await page.route('**/api/factory/artifacts',r=>r.fulfill({json:[{...artifact,acceptances}]}));
  await page.route(`**/api/factory/artifacts/${artifact.id}/blueprint`,r=>r.fulfill({json:{digest,spec:{phases:[],decisions:[],features:[],sources:[],evidence:[]},documents:{},runtime_acceptance:supported?adapter:{...adapter,supported:false,reason:'No frozen runner adapter is available for this blueprint.'}}}));
  await page.goto('/factory');
  const language=page.getByRole('button',{name:'切换到英文',exact:true});
  if(await language.count()) await language.click();
  await page.getByRole('tab',{name:'Artifacts',exact:true}).click();
}

test('blueprint runtime submission requires adapter, source ZIP and execution consent, without a model field',async({page})=>{
  await setup(page,true);
  const card=page.getByRole('article',{name:/Cognitive template Bookmark blueprint/});
  await card.getByRole('button',{name:'Read cognitive content',exact:true}).click();
  const submit=card.getByRole('button',{name:'Submit and run frozen acceptance',exact:true});
  await expect(submit).toBeDisabled();
  await expect(card.getByText('delivery.json and archive instructions',{exact:true})).toBeVisible();
  await card.getByText('delivery.json and archive instructions',{exact:true}).click();
  await expect(card.getByText('"schema": "atlas.application-delivery.v1"')).toBeVisible();
  await expect(card.getByText('"port": 8000')).toBeVisible();
  await card.getByLabel('Application source ZIP',{exact:true}).setInputFiles({name:'source.zip',mimeType:'application/zip',buffer:Buffer.from('zip-fixture')});
  await expect(submit).toBeDisabled();
  await card.getByLabel('I acknowledge that uploaded application code and frozen acceptance programs will execute in managed offline containers.').check();
  await expect(submit).toBeEnabled();
  let body:Record<string,unknown>|undefined;
  await page.route(`**/api/factory/artifacts/${artifact.id}/accept`,async route=>{body=route.request().postDataJSON();await route.fulfill({status:202,json:{job:{id:'job_runtime',kind:'blueprint-runtime',state:'queued'}}});});
  await submit.click();
  await expect.poll(()=>body).toMatchObject({method:'blueprint-runtime',expected_digest:digest,phase:'P0',timeout:900,language:'en',execution_confirmed:true});
  expect(body).not.toHaveProperty('model');
  expect(String(body?.source_archive_base64)).toBe(Buffer.from('zip-fixture').toString('base64'));
});

test('runtime deep link exposes startup diagnostics, case evidence and cleanup errors',async({page})=>{
  await setup(page,true,[{id:'acc_runtime',job_id:'job_runtime',digest,method:'blueprint-runtime',outcome:'blocked',scope:'Frozen cases for P0',created_at:new Date().toISOString(),failure:'web application did not pass HTTP readiness',startup:{status:'blocked',captured_output:{stdout:'server booting',stderr:'Traceback: bind failed'},readiness:{passed:false,output:'HTTP 500 during readiness'}},case_results:[{id:'A01',status:'failed',reason:'an assertion failed',output:'HTTP 500 from /health',assertions:[{id:'health-response',passed:false,detail:'expected 200 but observed 500'}]}],cleanup:{status:'failed',errors:['container remained after cleanup']}}]);
  await page.goto(`/factory?view=artifacts&artifact_id=${artifact.id}&runtime_run_id=acc_runtime`);
  const card=page.getByRole('article',{name:/Cognitive template Bookmark blueprint/});
  await card.getByRole('button',{name:'Read cognitive content',exact:true}).click();
  const runtime=card.getByRole('region',{name:'Independent runtime acceptance'});
  await expect(runtime.getByText('Frozen cases for P0',{exact:true})).toBeVisible();
  await runtime.getByText('Startup diagnostics',{exact:true}).click();
  await expect(runtime.getByText('Traceback: bind failed',{exact:true})).toBeVisible();
  await expect(runtime.getByText('HTTP 500 during readiness',{exact:true})).toBeVisible();
  await expect(runtime.getByText('Failure: web application did not pass HTTP readiness',{exact:true})).toBeVisible();
  await runtime.getByText(/^A01 · Failed/).click();
  await expect(runtime.getByText('A01 · Failed · an assertion failed',{exact:true})).toBeVisible();
  await expect(runtime.getByText('HTTP 500 from /health',{exact:true})).toBeVisible();
  await expect(runtime.getByText(/health-response/)).toBeVisible();
  await expect(runtime.getByText(/expected 200 but observed 500/)).toBeVisible();
  await runtime.getByText('Cleanup errors (1)',{exact:true}).click();
  await expect(runtime.getByText('container remained after cleanup',{exact:true})).toBeVisible();
});

test('blueprint with no frozen runner adapter explains runtime acceptance is unavailable',async({page})=>{
  await setup(page,false);
  const card=page.getByRole('article',{name:/Cognitive template Bookmark blueprint/});
  await card.getByRole('button',{name:'Read cognitive content',exact:true}).click();
  await expect(card.getByText('No frozen runner adapter is available for this blueprint.',{exact:true})).toBeVisible();
  await expect(card.getByRole('button',{name:'Submit and run frozen acceptance',exact:true})).toHaveCount(0);
});
