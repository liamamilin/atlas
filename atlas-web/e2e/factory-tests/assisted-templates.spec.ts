import {expect,test,type Page} from '@playwright/test';
const leaf={slug:'meal-planning-application',name:'Meal planning',name_zh:'膳食计划',aliases_zh:[],section_id:'food',section_name:'Food',overview:'Meals',dc:'',how:'',rules:'',variants:'',products:'',relations:[],apps:[]};
const scenario={id:'scn_example',revision:1,leaf:leaf.slug,name:'Weekly dinners',objective:'Plan dinner quantities',audience:'Home cook',workflow:['Plan','Shop'],status:'draft'};
const item={artifact_id:'tpl_'+'a'.repeat(32),digest:'d'.repeat(64),key:'meal',title:'Weekly dinner template',leaf:leaf.slug,scenario,capabilities:['Scale ingredients','Pause plans'],limits:['Local only'],cases:[{case_id:'case:meal',revision:1,digest:'c'.repeat(64),app_id:'app:meal',sources:[{repository:'https://github.com/mealie-recipes/mealie',commit_sha:'b'.repeat(40),license_files:['LICENSE']}]}],runtime:{status:'core_verified',scope:'Five core journeys and same-directory restart',recorded_date:'2026-10-21',online_status:'not_checked',strict_acceptance:false},files:{development:{available:true,url:'/api/factory/assisted-templates/demo/files/development'},guide:{available:true,url:'/api/factory/assisted-templates/demo/files/guide'},source:{available:true,url:'/api/factory/assisted-templates/demo/files/source'},evidence:{available:true,url:'/api/factory/assisted-templates/demo/files/evidence'}}};
const artifact={artifact_type:'product-blueprint',id:item.artifact_id,job_id:'job',leaf:leaf.slug,scenario_name:scenario.name,scenario_revision:1,digest:item.digest,level:'L0',state:'draft',manifest:{name:item.title,description:scenario.objective,phases:[{id:'P0',title:'Core'}]},provenance:{origin:'assisted-trial',shared_case_refs:[{case_id:'case:meal',revision:1,digest:'c'.repeat(64),app_id:'app:meal'}]},acceptances:[],reports:[],formal_checks:[]};
async function setup(page:Page,notRun=false){
 await page.addInitScript(()=>localStorage.setItem('atlas-lang','en'));
 const value=notRun?{...item,runtime:{...item.runtime,status:'not_run',scope:'No app run'},files:{development:item.files.development}}:item;
 await page.route('**/data/leaves/'+leaf.slug+'.json',r=>r.fulfill({json:leaf}));
 await page.route('**/api/factory/assisted-templates**',r=>r.request().url().endsWith('/files/guide')?r.fulfill({contentType:'text/markdown',body:'# Example guide\nStart with a new data directory.'}):r.fulfill({json:{items:[value],unavailable:[],counts:{total:1,core_verified:notRun?0:1,not_run:notRun?1:0}}}));
 await page.route('**/api/factory/catalog**',r=>r.fulfill({json:[scenario]}));
 await page.route('**/api/factory/batches',r=>r.fulfill({json:[]}));
 await page.route('**/api/factory/status',r=>r.fulfill({json:{cli:{available:false,models:[]},runtime:{available:false}}}));
 await page.route('**/api/factory/artifacts**',r=>r.fulfill({json:r.request().url().includes('published=1')?[]:[artifact]}));
}
test('leaf → scenario → assisted template → case and standard package, without formal publication',async({page})=>{
 await setup(page);await page.goto('/types/'+leaf.slug);
 await expect(page.getByText('Core example verified',{exact:true})).toBeVisible();
 await expect(page.getByText('No published templates for this type yet.',{exact:false})).toBeVisible();
 await page.getByRole('link',{name:scenario.name,exact:true}).click();
 await expect(page).toHaveURL(/scenario_id=scn_example/);
 await expect(page.getByRole('heading',{name:item.title})).toBeVisible();
 const info=page.getByRole('region',{name:'Assisted template information '+item.title});
 await expect(info.getByText('Home cook',{exact:true})).toBeVisible();
 await expect(info.getByRole('link',{name:'Download standard development package'})).toHaveAttribute('href',item.files.development.url);
 await expect(info.getByRole('link',{name:'Read shared case · r1'})).toHaveAttribute('href',/case_id=case%3Ameal/);
 await info.getByText('Start with Codex',{exact:true}).click();
 await expect(info.getByLabel('Codex start instruction')).toHaveValue(/HANDOFF.md.*CURRENT_PHASE.json/s);
 await expect(info.getByRole('button',{name:'Copy Codex instruction'})).toBeVisible();
 await info.getByRole('button',{name:'Read application guide'}).click();
 await expect(info.getByRole('heading',{name:'Example guide'})).toBeVisible();
 await expect(info.getByText(/currently running local service/)).toBeVisible();
});
test('not-run template has no example source, guide or runtime evidence links',async({page})=>{
 await setup(page,true);await page.goto('/types/'+leaf.slug);
 const info=page.getByRole('region',{name:'Assisted template information '+item.title});
 await expect(info.getByText('Application not run',{exact:true})).toBeVisible();
 await expect(info.getByRole('link',{name:'Download example source'})).toHaveCount(0);
 await expect(info.getByRole('button',{name:'Read application guide'})).toHaveCount(0);
 await expect(info.getByRole('link',{name:'Read runtime evidence file'})).toHaveCount(0);
 await expect(info.getByRole('link',{name:'Download standard development package'})).toBeVisible();
});
test('Go model static review does not turn an unrun app into a runtime example',async({page})=>{
 await setup(page,true);
 await page.route('**/api/factory/assisted-templates**',r=>r.fulfill({json:{items:[{...item,
  production:{mode:'opencode-cli-go',model:'opencode-go/deepseek-v4.1-flash',review_status:'passed',review_input_digest:'e'.repeat(64)},
  runtime:{...item.runtime,status:'not_run',scope:'No app run'},files:{development:item.files.development}}],
  unavailable:[],counts:{total:1,core_verified:0,not_run:1}}}));
 await page.goto('/types/'+leaf.slug);
 const info=page.getByRole('region',{name:'Assisted template information '+item.title});
 await expect(info.getByText(/opencode-go\/deepseek-v4.1-flash/)).toBeVisible();
 await expect(info.getByText(/Separate-session static review passed/)).toBeVisible();
 await expect(info.getByText('Application not run',{exact:true})).toBeVisible();
 await expect(info.getByRole('link',{name:'Download example source'})).toHaveCount(0);
});
test('failed complete-material review remains inspectable and is not offered as a usable package',async({page})=>{
 await setup(page,true);
 await page.route('**/api/factory/assisted-templates**',r=>r.fulfill({json:{items:[{...item,
  production:{mode:'opencode-cli-go',model:'opencode-go/deepseek-v4.1-flash',review_status:'needs_changes',review_input_digest:'e'.repeat(64),issues:['Stale update baseline']},
  runtime:{...item.runtime,status:'not_run',scope:'No app run'},files:{development:{available:false,reason:'assisted_review_needs_changes'}}}],
  unavailable:[],counts:{total:1,core_verified:0,not_run:1}}}));
 await page.goto('/types/'+leaf.slug);
 const info=page.getByRole('region',{name:'Assisted template information '+item.title});
 await expect(info.getByText(/Complete-material review: changes required/)).toBeVisible();
 await expect(info.getByRole('link',{name:'Download standard development package'})).toHaveCount(0);
 await info.getByText('Read revision findings',{exact:true}).click();
 await expect(info.getByText('Stale update baseline')).toBeVisible();
 await page.route('**/api/factory/artifacts**',r=>r.fulfill({json:[{...artifact,state:'withdrawn'}]}));
 await page.goto('/factory?view=artifacts&artifact_id='+item.artifact_id);
 await expect(page.getByRole('button',{name:'Create development package',exact:true})).toBeDisabled();
 await expect(page.getByRole('link',{name:'Download frozen bundle',exact:true})).toBeVisible();
});
test('assisted catalog outage does not hide formal template or claim zero verified evidence',async({page})=>{
 await setup(page);await page.route('**/api/factory/assisted-templates**',r=>r.fulfill({status:503,json:{error:'unavailable'}}));
 await page.route('**/api/factory/artifacts?**',r=>r.fulfill({json:[{...artifact,id:'formal',provenance:{},state:'published'}]}));
 await page.goto('/types/'+leaf.slug);
 await expect(page.getByRole('heading',{name:item.title})).toBeVisible();
 await expect(page.getByText('Assisted catalog unavailable; formal publication is unaffected.')).toBeVisible();
});

test('scenario link retains formally published artifacts outside the assisted index',async({page})=>{
 await setup(page);
 await page.route('**/api/factory/assisted-templates**',r=>r.fulfill({json:{items:[],unavailable:[],counts:{total:0,core_verified:0,not_run:0}}}));
 await page.route('**/api/factory/artifacts**',r=>r.fulfill({json:[{...artifact,scenario_id:scenario.id,provenance:{},state:'published'}]}));
 await page.goto('/types/'+leaf.slug);
 await page.getByRole('link',{name:scenario.name,exact:true}).click();
 await expect(page.getByRole('heading',{name:item.title})).toBeVisible();
 await expect(page.getByText('Cognitive template · Published in catalog',{exact:false})).toBeVisible();
});

test('recovered refresh clears its alert while a user action error remains visible',async({page})=>{
 await setup(page);let failNext=false;let calls=0;
 await page.route('**/api/factory/catalog',r=>{calls++;if(failNext){failNext=false;return r.fulfill({status:503,json:{error:'transient'}});}return r.fulfill({json:[scenario]});});
 await page.goto('/factory?view=artifacts');
 await expect(page.getByRole('heading',{name:item.title})).toBeVisible();
 failNext=true;
 await expect(page.getByRole('alert')).toContainText('Refresh failed',{timeout:10000});
 await expect(page.getByRole('alert')).toHaveCount(0,{timeout:10000});
 await page.route('**/api/factory/blueprints/sample',r=>r.fulfill({status:409,json:{error:'Manual action rejected'}}));
 await page.getByRole('button',{name:'Load bookmark cognition sample'}).click();
 await expect(page.getByRole('alert')).toContainText('Manual action rejected');
 const before=calls;await expect.poll(()=>calls,{timeout:10000}).toBeGreaterThan(before);
 await expect(page.getByRole('alert')).toContainText('Manual action rejected');
});
