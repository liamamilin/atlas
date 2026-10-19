import {test,expect} from '@playwright/test';
const type='task-management-application';
async function mockStatus(page:import('@playwright/test').Page){
  await page.route('**/api/factory/status',r=>r.fulfill({json:{cli:{available:true,version:'test-version',models:['test/deepseek-flash']},runtime:{available:true,version:'test-engine'}}}));
}

test('factory catalog saves, confirms, pins and cancels a batch without a provider call',async({page})=>{
  await mockStatus(page);
  await page.route('**/api/factory/status',r=>r.fulfill({json:{cli:{available:true,version:'test',models:['test/deepseek-flash']},runtime:{available:false}}}));
  const errors:string[]=[];page.on('pageerror',e=>errors.push(e.message));
  await page.goto(`/factory?leaf=${type}`);
  await expect(page.getByRole('heading',{level:1})).toContainText('应用场景');
  await page.getByLabel('场景名称',{exact:true}).fill('浏览器工厂验收');
  await page.getByLabel('目标用户',{exact:true}).fill('个人用户');
  await page.getByLabel('用户目标',{exact:true}).fill('在本地管理任务');
  await page.getByLabel('核心流程（每行一步）').fill('添加任务\n完成任务');
  await page.getByLabel('验收条件（每行一条）').fill('添加后能看到任务');
  await page.getByLabel('场景状态',{exact:true}).selectOption('ready');
  await page.getByRole('button',{name:'保存场景',exact:true}).click();
  await expect(page.getByRole('heading',{name:'浏览器工厂验收',exact:true})).toBeVisible();
  await page.getByRole('checkbox',{name:'选择 浏览器工厂验收',exact:true}).check();
  const response=page.waitForResponse(r=>r.request().method()==='POST'&&r.url().endsWith('/api/factory/batches'));
  await page.getByRole('button',{name:'生产代码模板（1）',exact:true}).click();
  expect((await response).status()).toBe(202);
  await expect(page.getByRole('tab',{name:'任务批次'})).toHaveAttribute('aria-selected','true');
  await expect(page.getByText('排队中 · 发现候选 · 尝试 1')).toBeVisible();
  page.once('dialog',d=>d.accept());await page.getByRole('button',{name:'取消批次',exact:true}).click();
  await expect(page.getByText('已取消 · 发现候选 · 尝试 1')).toBeVisible();
  await page.reload();await page.getByRole('tab',{name:'任务批次'}).click();
  await expect(page.getByText('已取消 · 发现候选 · 尝试 1')).toBeVisible();
  expect(errors).toEqual([]);
});

test('catalog groups scenarios by type and preserves cross-group selection through collapse, search and refresh',async({page})=>{
  await mockStatus(page);
  const scenes=[
    {id:'scn_group_task_draft',leaf:type,leaf_name:'任务管理',name:'团队任务排期',status:'draft'},
    {id:'scn_group_task_archived',leaf:type,leaf_name:'任务管理',name:'旧任务方案',status:'archived'},
    {id:'scn_group_bookmark_ready',leaf:'bookmark-manager',leaf_name:'书签管理',name:'灵感链接收藏',status:'ready'},
  ].map(s=>({...s,audience:'个人用户',objective:'保存并整理内容',workflow:['保存','查看'],acceptance:['刷新后保留'],revision:1,updated_at:new Date().toISOString()}));
  let reads=0;
  await page.route('**/api/factory/catalog',r=>{reads++;return r.fulfill({json:scenes});});
  await page.goto('/factory');
  await expect(page.getByText('2 个叶子 · 3 个场景',{exact:true})).toBeVisible();
  const task=page.getByRole('region').filter({has:page.locator(`button[aria-controls="scenarios-${type}"]`)});
  const bookmarks=page.getByRole('region').filter({has:page.locator('button[aria-controls="scenarios-bookmark-manager"]')});
  const toggle=task.getByRole('button',{expanded:false}).first();
  await expect(toggle).toHaveAttribute('aria-expanded','false');
  await expect(page.getByRole('heading',{name:'团队任务排期',exact:true})).not.toBeVisible();
  await expect(task.getByText('草案 1',{exact:true})).toBeVisible();
  await expect(task.getByText('已归档 1',{exact:true})).toBeVisible();
  await task.getByRole('button',{name:'选择本组可审阅场景',exact:true}).click();
  await bookmarks.getByRole('button',{name:'选择本组可审阅场景',exact:true}).click();
  await expect(page.getByRole('button',{name:'审阅所选场景（2）',exact:true})).toBeEnabled();
  await expect(page.getByRole('button',{name:'生产代码模板（1）',exact:true})).toBeEnabled();
  await toggle.click();
  await expect(page.getByRole('checkbox',{name:'选择 团队任务排期',exact:true})).toBeChecked();
  await expect(page.getByRole('checkbox',{name:'选择 旧任务方案',exact:true})).toBeDisabled();
  const priorReads=reads;
  await expect.poll(()=>reads,{timeout:10000}).toBeGreaterThan(priorReads);
  await expect(task.locator('button[aria-controls]')).toHaveAttribute('aria-expanded','true');
  await page.getByRole('button',{name:'全部收起',exact:true}).click();
  await expect(page.getByRole('heading',{name:'团队任务排期',exact:true})).not.toBeVisible();
  await expect(task.getByText('已选 1',{exact:true})).toBeVisible();
  await page.getByLabel('搜索场景',{exact:true}).fill('灵感');
  await expect(page.getByText('1 个叶子 · 1 个场景',{exact:true})).toBeVisible();
  await expect(page.getByRole('heading',{name:'灵感链接收藏',exact:true})).toBeVisible();
  await expect(page.getByRole('status')).toContainText('其中 1 个不在当前筛选结果中');
  await expect(page.getByRole('checkbox',{name:'选择 灵感链接收藏',exact:true})).toBeChecked();
  await page.getByRole('button',{name:'选择当前已确认场景',exact:true}).click();
  await expect(page.getByRole('button',{name:'审阅所选场景（2）',exact:true})).toBeEnabled();
  await page.getByLabel('搜索场景',{exact:true}).fill('');
  await page.getByRole('button',{name:'全部展开',exact:true}).click();
  await expect(page.getByRole('checkbox',{name:'选择 团队任务排期',exact:true})).toBeChecked();
  await task.getByRole('button',{name:'清空本组选择',exact:true}).click();
  await expect(page.getByRole('checkbox',{name:'选择 团队任务排期',exact:true})).not.toBeChecked();
  await expect(page.getByRole('checkbox',{name:'选择 灵感链接收藏',exact:true})).toBeChecked();
  await page.setViewportSize({width:375,height:812});
  await page.getByRole('button',{name:'切换到英文',exact:true}).click();
  await expect(page.getByText('2 types · 3 scenarios',{exact:true})).toBeVisible();
  await expect(page.getByRole('button',{name:'Collapse all',exact:true})).toBeVisible();
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth)).toBe(true);
  await page.getByLabel('Application type',{exact:true}).selectOption('bookmark-manager');
  await expect(page.getByRole('heading',{name:'灵感链接收藏',exact:true})).toBeVisible();
  await expect(page.getByRole('checkbox',{name:'Select 灵感链接收藏',exact:true})).toBeChecked();
});

test('visible generation entry filters covered leaves, marks zero additions and blocks active generation',async({page})=>{
  await mockStatus(page);
  const base={audience:'个人',objective:'记录内容',workflow:['添加','查看'],acceptance:['重新打开仍保留'],status:'draft',revision:1,updated_at:new Date().toISOString()};
  const catalog=[{...base,id:'scn_note',leaf:'note-taking-application',leaf_name:'笔记应用',name:'笔记已有场景'}];
  const config={name:'fixture generation history',kind:'scenarios',model:'test/deepseek-flash',concurrency:1,timeout:900,repair_attempts:1};
  const job=(slug:string,state:string,kind='scenarios')=>({id:`job_${slug}`,kind,state,stage:'scenarios',attempt:1,error:null,snapshot:{leaf:{slug,name:slug,name_zh:slug},scenario:null,config}});
  const batches=[{id:'bat_fixture',state:'running',config,jobs:[job('read-it-later-application','completed'),job('budgeting-application','queued'),job('calendar-application','running'),job('time-tracking-application','queued','scenario-review')]}];
  await page.route('**/api/factory/catalog',r=>r.fulfill({json:catalog}));
  let submitted:Record<string,unknown>|undefined;
  await page.route('**/api/factory/batches',r=>{
    if(r.request().method()==='POST'){
      submitted=r.request().postDataJSON();
      const next={id:'bat_new',state:'running',config,jobs:(submitted!.leaves as string[]).map(slug=>job(slug,'queued'))};
      batches.unshift(next);return r.fulfill({status:202,json:next});
    }
    return r.fulfill({json:batches});
  });
  await page.goto('/factory');
  const panel=page.getByRole('region',{name:'生成应用场景',exact:true});
  await expect(panel.getByRole('heading',{name:'生成应用场景',exact:true})).toBeVisible();
  await expect(panel.getByRole('button',{name:'生成场景草案（0 类型）',exact:true})).toBeDisabled();
  await expect(panel.getByLabel('场景生成状态',{exact:true})).toHaveValue('new');
  await panel.getByLabel('搜索生产叶子',{exact:true}).fill('笔记');
  await expect(panel.getByRole('checkbox',{name:'选择叶子 笔记应用',exact:true})).toHaveCount(0);
  await expect(page.getByLabel('搜索场景',{exact:true})).toHaveValue('');
  await panel.getByLabel('场景生成状态',{exact:true}).selectOption('all');
  const note=panel.getByRole('checkbox',{name:'选择叶子 笔记应用',exact:true});
  await expect(note).toBeDisabled();
  await expect(panel.getByText('已有 1 个场景',{exact:true})).toBeVisible();
  const allow=panel.getByRole('checkbox',{name:'允许为已有场景或已调研叶子补充生成（会再次调用模型）',exact:true});
  await allow.check();await note.check();
  await expect(panel.getByRole('button',{name:'生成场景草案（1 类型）',exact:true})).toBeEnabled();
  await allow.uncheck();
  await expect(panel.getByRole('button',{name:'生成场景草案（0 类型）',exact:true})).toBeDisabled();
  await expect(panel.getByText('1 个选择已有场景或正在生成，本次会跳过。',{exact:true})).toBeVisible();
  await panel.getByRole('button',{name:'清空叶子选择',exact:true}).click();
  await panel.getByLabel('搜索生产叶子',{exact:true}).fill('');
  await panel.getByLabel('场景生成状态',{exact:true}).selectOption('generated');
  await expect(panel.getByText('已调研，暂无场景',{exact:true})).toBeVisible();
  await expect(panel.getByRole('checkbox',{name:'选择叶子 稍后阅读应用',exact:true})).toBeDisabled();
  await panel.getByLabel('场景生成状态',{exact:true}).selectOption('active');
  await expect(panel.getByRole('checkbox',{name:'选择叶子 预算应用',exact:true})).toBeDisabled();
  await expect(panel.getByRole('checkbox',{name:'选择叶子 日历应用',exact:true})).toBeDisabled();
  await allow.check();
  await expect(panel.getByRole('checkbox',{name:'选择叶子 日历应用',exact:true})).toBeDisabled();
  await allow.uncheck();
  await panel.getByLabel('场景生成状态',{exact:true}).selectOption('new');
  await panel.getByLabel('搜索生产叶子',{exact:true}).fill('待办');
  await panel.getByRole('checkbox',{name:'选择叶子 待办事项应用',exact:true}).check();
  await panel.getByLabel('搜索生产叶子',{exact:true}).fill('时间跟踪');
  await panel.getByRole('checkbox',{name:'选择叶子 时间跟踪应用',exact:true}).check();
  await expect(panel.getByText('本批已选 2 个叶子：待办事项应用、时间跟踪应用',{exact:true})).toBeVisible();
  await panel.getByRole('button',{name:'生成场景草案（2 类型）',exact:true}).click();
  await expect.poll(()=>submitted).toMatchObject({kind:'scenarios',skip_generated:true,leaves:['to-do-list-application','time-tracking-application'],language:'zh'});
  await expect(page.getByRole('tab',{name:'任务批次',exact:true})).toHaveAttribute('aria-selected','true');
  await page.getByRole('tab',{name:'生产目录',exact:true}).click();
  await panel.getByLabel('搜索生产叶子',{exact:true}).fill('待办');
  await expect(panel.getByRole('checkbox',{name:'选择叶子 待办事项应用',exact:true})).toHaveCount(0);
  await page.setViewportSize({width:375,height:812});
  await page.getByRole('button',{name:'切换到英文',exact:true}).click();
  const english=page.getByRole('region',{name:'Generate application scenarios',exact:true});
  await expect(english.getByLabel('Scenario generation status',{exact:true})).toHaveValue('new');
  await english.getByLabel('Search types to generate',{exact:true}).fill('');
  await english.getByLabel('Scenario generation status',{exact:true}).selectOption('generated');
  await expect(english.getByText('Researched, no scenarios',{exact:true})).toBeVisible();
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth)).toBe(true);
});

test('leaf exposes confirmed scenarios and links to factory',async({page,request})=>{
  await request.post('/api/factory/scenarios',{data:{leaf:type,name:'叶子场景验收',audience:'个人',objective:'管理任务',workflow:['添加任务'],acceptance:['看到任务'],status:'ready'}});
  await mockStatus(page);await page.goto(`/types/${type}`);
  const section=page.locator('section').filter({has:page.getByRole('heading',{name:'应用场景与模板',exact:true})});
  await expect(section.getByText('叶子场景验收',{exact:true})).toBeVisible();
  await section.getByRole('link',{name:'打开模板工厂'}).click();
  await expect(page).toHaveURL(new RegExp(`/factory\\?leaf=${type}`));
});

test('draft scenarios can queue an independent pinned review without confirmation or provider calls',async({page,request})=>{
  const response=await request.post('/api/factory/scenarios',{data:{leaf:type,name:'场景审阅排队验收',audience:'个人',objective:'管理任务',workflow:['添加任务','完成任务'],acceptance:['添加后看到任务','完成后状态保留'],status:'draft'}});
  const scene=await response.json();
  await mockStatus(page);await page.goto(`/factory?leaf=${type}`);
  const card=page.locator('article').filter({has:page.getByRole('heading',{name:scene.name,exact:true})});
  await expect(card.getByRole('checkbox',{name:`选择 ${scene.name}`,exact:true})).toBeEnabled();
  await card.getByRole('checkbox',{name:`选择 ${scene.name}`,exact:true}).check();
  await expect(page.getByRole('button',{name:'生产代码模板（0）',exact:true})).toBeDisabled();
  await expect(page.getByRole('button',{name:'生产认知模板（0）',exact:true})).toBeDisabled();
  const queued=page.waitForResponse(r=>r.request().method()==='POST'&&r.url().endsWith('/api/factory/batches'));
  await page.getByRole('button',{name:'审阅所选场景（1）',exact:true}).click();
  const result=await queued;
  expect(result.status()).toBe(202);
  expect(result.request().postDataJSON()).toMatchObject({kind:'scenario-review',language:'zh',scenario_ids:[scene.id],scenario_revisions:{[scene.id]:scene.revision}});
  const batch=await result.json();
  expect(batch.jobs[0]).toMatchObject({kind:'scenario-review',state:'queued',snapshot:{scenario:{id:scene.id,revision:scene.revision}}});
  await page.getByRole('tab',{name:'生产目录',exact:true}).click();
  await expect(card.getByText('场景独立审阅 · 排队中',{exact:true})).toBeVisible();
  await expect(card.getByRole('button',{name:'等待审阅',exact:true})).toBeDisabled();
  await expect(card.getByText('草案 · r1',{exact:true})).toBeVisible();
});

test('review actions distinguish first, repeat and retry; passed drafts still need human confirmation',async({page})=>{
  await mockStatus(page);
  const base={leaf:type,leaf_name:'任务管理',audience:'个人',objective:'管理任务',workflow:['添加任务','完成任务'],acceptance:['添加后保留'],status:'draft',revision:1,updated_at:new Date().toISOString()};
  const report={id:'scv_fixture',scenario_revision:1,outcome:'passed',summary:'范围内通过',current:true,checks:[],leaf_quotes:[],related_scenario_ids:[],suggestions:[],peer_scenarios:[],model:'test/flash',created_at:new Date().toISOString()};
  const job=(state:string)=>({id:'job_fixture',state,current:true,error:null,scenario_revision:1});
  let scenes=[
    {...base,id:'scn_passed',name:'通过但待人工确认',reviews:[report]},
    {...base,id:'scn_ready',name:'已确认案例',status:'ready',reviews:[report]},
    {...base,id:'scn_outdated',name:'过期结论案例',reviews:[{...report,current:false}]},
    {...base,id:'scn_failed',name:'审阅失败案例',reviews:[],review_jobs:[job('failed')]},
    {...base,id:'scn_new',name:'尚未审阅案例',reviews:[]},
    {...base,id:'scn_queued',name:'排队案例',reviews:[],review_jobs:[job('queued')]},
    {...base,id:'scn_running',name:'运行案例',reviews:[],review_jobs:[job('running')]},
    {...base,id:'scn_changes',name:'需要修改案例',reviews:[{...report,outcome:'needs_changes'}]},
  ];
  await page.route('**/api/factory/catalog',r=>r.fulfill({json:scenes}));
  let saved:Record<string,unknown>|undefined;
  await page.route('**/api/factory/scenarios/scn_passed',r=>{
    saved=r.request().postDataJSON();
    scenes=scenes.map(s=>s.id==='scn_passed'?{...s,status:String(saved!.status),revision:2,reviews:[{...report,current:false}]}:s);
    return r.fulfill({json:scenes[0]});
  });
  await page.goto('/factory');
  const card=(name:string)=>page.locator('article').filter({has:page.getByRole('heading',{name,exact:true})});
  await expect(page.getByLabel('Agent 审阅汇总').getByText('通过 2',{exact:true})).toBeVisible();
  await expect(page.getByLabel('Agent 审阅汇总').getByText('已过期 1',{exact:true})).toBeVisible();
  await expect(page.getByLabel('Agent 审阅汇总').getByText('未完成 1',{exact:true})).toBeVisible();
  const passed=card('通过但待人工确认');
  await expect(passed.getByText('待人工确认 · r1',{exact:true})).toBeVisible();
  await expect(passed.getByText('Agent 审阅已通过 · 待你人工确认',{exact:true})).toBeVisible();
  await expect(passed.getByRole('button',{name:'重新审阅场景',exact:true})).toBeEnabled();
  await expect(card('过期结论案例').getByRole('button',{name:'重新审阅场景',exact:true})).toBeEnabled();
  await expect(card('审阅失败案例').getByRole('button',{name:'重试场景审阅',exact:true})).toBeEnabled();
  await expect(card('尚未审阅案例').getByRole('button',{name:'发起场景审阅',exact:true})).toBeEnabled();
  await expect(card('排队案例').getByRole('button',{name:'等待审阅',exact:true})).toBeDisabled();
  await expect(card('运行案例').getByRole('button',{name:'审阅中',exact:true})).toBeDisabled();
  await passed.getByRole('checkbox').check();
  await expect(page.getByRole('button',{name:'生产代码模板（0）',exact:true})).toBeDisabled();
  await expect(page.getByRole('button',{name:'生产认知模板（0）',exact:true})).toBeDisabled();
  await passed.getByRole('button',{name:'编辑 / 确认场景',exact:true}).click();
  await expect(page.getByLabel('场景状态',{exact:true})).toHaveValue('draft');
  await page.getByLabel('场景状态',{exact:true}).selectOption('ready');
  await page.getByRole('button',{name:'保存场景',exact:true}).click();
  await expect.poll(()=>saved).toMatchObject({status:'ready',expected_revision:1});
  await expect(passed.getByText('已确认 · r2',{exact:true})).toBeVisible();
  await expect(page.getByRole('button',{name:'生产代码模板（1）',exact:true})).toBeEnabled();
  await expect(passed.getByText('Agent 审阅已通过 · 待你人工确认',{exact:true})).not.toBeVisible();
  await expect(page.getByLabel('Agent 审阅汇总').getByText('通过 1',{exact:true})).toBeVisible();
  await page.setViewportSize({width:375,height:812});
  await page.getByRole('button',{name:'切换到英文',exact:true}).click();
  await expect(card('需要修改案例').getByRole('button',{name:'Review scenario again',exact:true})).toBeVisible();
  await expect(card('审阅失败案例').getByRole('button',{name:'Retry scenario review',exact:true})).toBeVisible();
  await expect(page.getByLabel('Agent review summary').getByText('Outdated 2',{exact:true})).toBeVisible();
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth)).toBe(true);
});

test('scenario review displays reasons, revisions, failed attempts and bilingual stale evidence',async({page})=>{
  const id='scn_'+'a'.repeat(32),peer='scn_'+'b'.repeat(32);
  const review={id:'scv_'+'a'.repeat(32),scenario_id:id,scenario_revision:1,job_id:'job_'+'a'.repeat(32),outcome:'needs_changes',summary:'完成任务后的持久化验收缺失。',current:true,checks:[{dimension:'testability',outcome:'needs_changes',reason:'流程包含完成任务，但验收只有添加。'}],leaf_quotes:['管理任务'],leaf_evidence:[{start_line:3,end_line:3}],related_scenario_ids:[peer],suggestions:['补充完成任务后刷新仍保留完成状态。'],peer_scenarios:[{id:peer,name:'相近的待办场景',revision:1}],model:'test/deepseek-flash',created_at:new Date().toISOString(),scope:'fixture review'};
  let scene={id,leaf:type,leaf_name:'任务管理',name:'审阅说明展示',audience:'个人',objective:'管理任务',workflow:['添加任务','完成任务'],acceptance:['添加后看到任务'],status:'draft',revision:1,updated_at:new Date().toISOString(),reviews:[review],review_jobs:[] as unknown[]};
  await mockStatus(page);await page.route('**/api/factory/catalog',r=>r.fulfill({json:[scene]}));
  await page.goto('/factory');
  await expect(page.getByText('场景独立审阅 · 需要修改',{exact:true})).toBeVisible();
  await page.getByRole('button',{name:'查看审阅理由与建议',exact:true}).click();
  await expect(page.getByText('流程包含完成任务，但验收只有添加。',{exact:true})).toBeVisible();
  await expect(page.getByText('类型正文行号：3–3',{exact:true})).toBeVisible();
  await expect(page.getByText('补充完成任务后刷新仍保留完成状态。',{exact:true})).toBeVisible();
  await expect(page.getByText('重叠场景：相近的待办场景',{exact:true})).toBeVisible();
  scene={...scene,revision:2,reviews:[{...review,current:false}],review_jobs:[{id:'job_'+'b'.repeat(32),state:'failed',error:'provider connection unavailable',scenario_revision:2,current:true}]};
  await page.reload();
  await expect(page.getByText('场景独立审阅 · 需要修改（已过期，需重新审阅）',{exact:true})).toBeVisible();
  await expect(page.getByRole('status')).toContainText('最近一次审阅未完成');
  await expect(page.getByRole('button',{name:'重试场景审阅',exact:true})).toBeEnabled();
  await page.setViewportSize({width:375,height:812});
  await page.getByRole('button',{name:'切换到英文',exact:true}).click();
  await expect(page.getByText('Independent scenario review · Needs changes (outdated; review again)',{exact:true})).toBeVisible();
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth)).toBe(true);
});

test('covered types can complete without new drafts and explain their pinned output language',async({page})=>{
  await mockStatus(page);
  const config={name:'覆盖充分的类型',model:'test/deepseek-flash',concurrency:1,timeout:900,repair_attempts:1,kind:'scenarios',language:'zh'};
  await page.route('**/api/factory/batches',r=>r.fulfill({json:[{id:'bat_'+'9'.repeat(32),state:'completed',config,created_at:new Date().toISOString(),jobs:[{id:'job_'+'9'.repeat(32),kind:'scenarios',state:'completed',stage:'completed',attempt:1,error:null,snapshot:{leaf:{slug:type,name:'Task management',name_zh:'任务管理'},scenario:null,config},generation_result:{count:0,reason:'现有场景已经覆盖可区分的使用流程。',scenario_ids:[]}}]}]}));
  await page.goto('/factory');
  await expect(page.getByText('场景输出语言：中文（随当前界面语言）',{exact:true})).toBeVisible();
  await page.getByRole('tab',{name:'任务批次',exact:true}).click();
  await expect(page.getByText('未新增场景（已有覆盖或没有合适的独立场景）',{exact:true})).toBeVisible();
  await expect(page.getByText('现有场景已经覆盖可区分的使用流程。',{exact:true})).toBeVisible();
  await expect(page.getByText('本批场景输出语言：中文',{exact:true})).toBeVisible();
  await page.getByRole('button',{name:'切换到英文',exact:true}).click();
  await expect(page.getByText('Pinned output language: Chinese',{exact:true})).toBeVisible();
  await expect(page.getByText('No new scenarios (existing coverage or no suitable distinct addition)',{exact:true})).toBeVisible();
});

test('factory supports mobile, English, empty artifacts and recoverable errors',async({page})=>{
  await mockStatus(page);await page.setViewportSize({width:375,height:812});await page.goto('/factory');
  await expect(page.getByRole('heading',{level:1})).toBeVisible();
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth)).toBe(true);
  await page.getByRole('tab',{name:'模板制品',exact:true}).click();
  await expect(page.getByText('还没有候选模板',{exact:true})).toBeVisible();
  await page.getByRole('button',{name:'切换到英文',exact:true}).click();
  await expect(page.getByRole('tab',{name:'Artifacts',exact:true})).toBeVisible();
  await expect(page.getByText('No candidate templates yet',{exact:true})).toBeVisible();
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth)).toBe(true);
  await page.route('**/api/factory/catalog',r=>r.fulfill({status:503,json:{error:'Factory temporarily unavailable',code:'factory_unavailable'}}));
  await page.reload();await expect(page.getByRole('alert')).toContainText('Factory temporarily unavailable');
  await expect(page.getByRole('button',{name:'Retry loading',exact:true})).toBeVisible();
});


test('artifact distinguishes source review from runtime acceptance and can instantiate L0',async({page})=>{
  await mockStatus(page);
  const artifact={id:'tpl_'+'a'.repeat(32),job_id:'job_'+'b'.repeat(32),leaf:type,scenario_name:'待办案例',scenario_revision:1,digest:'c'.repeat(64),level:'L0',state:'draft',created_at:new Date().toISOString(),manifest:{name:'候选待办模板',description:'冻结制品',render_files:['index.html']},provenance:{repository:'https://github.com/example/todo',commit:'d'.repeat(40),license:'MIT',model:'test/flash',change_summary:'example'},reports:[],formal_checks:[{project_name:'alpha',passed:true,scope:'rendering only'}],acceptances:[]};
  await page.route('**/api/factory/artifacts',r=>r.fulfill({json:[artifact]}));
  await page.route('**/api/factory/status',r=>r.fulfill({json:{cli:{available:true,version:'test',models:['test/deepseek-flash']},runtime:{available:false}}}));
  let requestBody:unknown;
  await page.route('**/api/factory/artifacts/*/accept',async r=>{requestBody=r.request().postDataJSON();Object.assign(artifact,{acceptance_jobs:[{id:'job_'+'c'.repeat(32),kind:'harness-review',state:'queued',stage:'acceptance',updated_at:new Date().toISOString()}]});await r.fulfill({status:202,json:{}});});
  await page.route('**/api/factory/artifacts/*/instantiate',r=>r.fulfill({status:201,json:{download_url:'/api/factory/downloads/'+'e'.repeat(32)}}));
  await page.goto('/factory');await page.getByRole('tab',{name:'模板制品',exact:true}).click();
  await expect(page.getByText('形式检查：结构与两组名称渲染通过（未运行应用）',{exact:true})).toBeVisible();
  await expect(page.getByText('Harness 审阅: 未执行',{exact:true})).toBeVisible();
  await expect(page.getByRole('button',{name:'发起运行验收',exact:true})).toBeDisabled();
  await expect(page.getByRole('button',{name:'审阅并发布',exact:true})).toBeDisabled();
  await page.getByRole('button',{name:'发起 Harness 审阅',exact:true}).click();
  expect(requestBody).toMatchObject({method:'harness-review',expected_digest:artifact.digest});
  await expect(page.getByText('Harness 审阅: 排队中',{exact:true})).toBeVisible();
  await expect(page.getByRole('button',{name:'发起 Harness 审阅',exact:true})).toBeDisabled();
  await page.getByRole('button',{name:'创建应用包',exact:true}).click();
  await expect(page.getByRole('link',{name:'下载应用',exact:true})).toBeVisible();
  const revisions:unknown[]=[];
  await page.route('**/api/factory/artifacts/*/repair',r=>{revisions.push(r.request().postDataJSON());return r.fulfill({status:202,json:{}});});
  await page.getByText('根据问题生产修订版',{exact:true}).click();
  await page.getByLabel('修复要求',{exact:true}).fill('修复实际构建错误');
  const replan=page.getByRole('checkbox',{name:'同时修订运行验收计划（仅用于计划或运行环境有误）',exact:true});
  await expect(replan).not.toBeChecked();
  await page.getByRole('button',{name:'生产修订版',exact:true}).click();
  await expect.poll(()=>revisions.length).toBe(1);
  expect(revisions[0]).toMatchObject({expected_digest:artifact.digest,replan:false});
  await replan.check();
  await page.getByRole('button',{name:'生产修订版',exact:true}).click();
  await expect.poll(()=>revisions.length).toBe(2);
  expect(revisions[1]).toMatchObject({expected_digest:artifact.digest,replan:true});
  await page.evaluate(()=>window.scrollTo(0,0));
  await page.screenshot({path:'/tmp/atlas-factory-artifact-ui.png',fullPage:true});
});

test('leaf published template creates an application and explains review scope',async({page})=>{
  const id='tpl_'+'f'.repeat(32);
  await page.route('**/api/factory/artifacts?*',r=>r.fulfill({json:[{id,leaf:type,scenario_name:'每日待办',level:'L1',manifest:{name:'发布待办',description:'example'},acceptances:[{method:'harness-review',outcome:'passed'}]}]}));
  await page.route('**/api/factory/artifacts/*/instantiate',r=>r.fulfill({status:201,json:{download_url:'/api/factory/downloads/'+'c'.repeat(32)}}));
  await page.goto(`/types/${type}`);
  const section=page.locator('section').filter({has:page.getByRole('heading',{name:'应用场景与模板',exact:true})});
  await expect(section.getByText('已通过 Harness 源码审阅，尚未通过运行验收。',{exact:true})).toBeVisible();
  await section.getByLabel('发布待办 应用名称',{exact:true}).fill('my-task-board');
  const response=page.waitForResponse(r=>r.request().method()==='POST'&&r.url().endsWith(`/artifacts/${id}/instantiate`));
  await section.getByRole('button',{name:'创建应用包',exact:true}).click();
  expect((await response).request().postDataJSON()).toEqual({project_name:'my-task-board'});
  await expect(section.getByRole('link',{name:'下载应用包',exact:true})).toBeVisible();
});

test('cognitive sample imports once, reads definitions and exports a phased development handoff without provider calls',async({page})=>{
  await mockStatus(page);
  const errors:string[]=[];page.on('pageerror',e=>errors.push(e.message));
  await page.goto('/factory');
  await page.getByRole('tab',{name:'模板制品',exact:true}).click();
  const entry=page.getByRole('region',{name:'认知模板入口',exact:true});
  await expect(entry).toContainText('自动生产请在生产目录选择已确认场景');
  await entry.getByRole('button',{name:'载入书签认知样板',exact:true}).click();
  const card=page.getByRole('article',{name:'认知模板 生活待购与灵感收藏夹：个人本地认知模板',exact:true});
  await expect(card).toBeVisible();
  await expect(card).toContainText('18 项能力 · 8 个决策 · 3 个阶段 · 17 个验收用例');
  await expect(card).toContainText('不等于工厂重新验收');
  await expect(card).toContainText('从 HANDOFF.md 开始');
  await expect(card).toContainText('旧包阶段可能未覆盖完整场景');
  await expect(card.getByRole('button',{name:'审阅并发布',exact:true})).toHaveCount(0);
  await card.getByRole('button',{name:'查看认知内容',exact:true}).click();
  await expect(card.getByRole('region',{name:'认知内容',exact:true})).toBeVisible();
  await expect(card.getByRole('heading',{name:'P0 · 可用个人收藏闭环',exact:true})).toBeVisible();
  await card.getByLabel('阅读章节',{exact:true}).selectOption('ARCHITECTURE.md');
  await expect(card.getByRole('region',{name:'章节正文',exact:true})).toContainText('IndexedDB');
  await card.getByText('人工决策与默认值',{exact:true}).click();
  await expect(card.getByRole('heading',{name:'D01 · 部署与数据归属',exact:true})).toBeVisible();
  await card.getByLabel('开发项目名称',{exact:true}).fill('../bad');
  await expect(card.getByRole('button',{name:'创建开发包',exact:true})).toBeDisabled();
  await card.getByLabel('开发项目名称',{exact:true}).fill('browser-cognitive-project');
  await card.getByLabel('本次开发阶段',{exact:true}).selectOption('P0');
  const response=page.waitForResponse(r=>r.url().endsWith('/development-package')&&r.request().method()==='POST');
  await card.getByRole('button',{name:'创建开发包',exact:true}).click();
  const payload=await(await response).json();
  expect(payload.artifact_type).toBe('product-blueprint');expect(payload.phase).toBe('P0');
  const download=card.getByRole('link',{name:'下载开发包',exact:true});await expect(download).toBeVisible();
  const archive=await page.request.get((await download.getAttribute('href'))!);
  expect(archive.ok()).toBe(true);expect(archive.headers()['content-type']).toContain('application/zip');
  expect((await archive.body()).subarray(0,2).toString()).toBe('PK');
  await card.getByLabel('本次开发阶段',{exact:true}).selectOption('P1');
  await expect(download).toHaveCount(0);
  await entry.getByRole('button',{name:'载入书签认知样板',exact:true}).click();
  await expect(card).toHaveCount(1);
  await page.reload();await page.getByRole('tab',{name:'模板制品',exact:true}).click();
  await expect(card).toHaveCount(1);
  await page.setViewportSize({width:375,height:812});
  await page.getByRole('button',{name:'切换到英文',exact:true}).click();
  await expect(page.getByRole('heading',{name:'Cognitive templates: define the product before development',exact:true})).toBeVisible();
  await expect(page.getByRole('button',{name:'Create development package',exact:true})).toBeVisible();
  await expect(page.getByRole('region',{name:'Create cognitive development package',exact:true})).toContainText('Start with HANDOFF.md');
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
  expect(errors).toEqual([]);
});

test('invalid cognitive ZIP shows an error and keeps imported candidates',async({page})=>{
  await mockStatus(page);await page.goto('/factory');await page.getByRole('tab',{name:'模板制品',exact:true}).click();
  const entry=page.getByRole('region',{name:'认知模板入口',exact:true});
  await entry.getByRole('button',{name:'载入书签认知样板',exact:true}).click();
  await expect(page.getByRole('article',{name:'认知模板 生活待购与灵感收藏夹：个人本地认知模板',exact:true})).toBeVisible();
  await entry.getByText('导入其他认知包',{exact:true}).click();
  await entry.getByLabel('认知模板 ZIP',{exact:true}).setInputFiles({name:'bad.zip',mimeType:'application/zip',buffer:Buffer.from('not a zip')});
  await entry.getByRole('button',{name:'校验并导入',exact:true}).click();
  await expect(page.getByRole('alert')).toContainText('认知包无法读取');
  await expect(page.getByRole('article',{name:'认知模板 生活待购与灵感收藏夹：个人本地认知模板',exact:true})).toBeVisible();
});

test('cognitive document reader does not load remote images or execute embedded HTML',async({page})=>{
  await mockStatus(page);
  const outbound:string[]=[];
  page.on('request',request=>{if(request.url().startsWith('https://cognition-tracker.invalid'))outbound.push(request.url());});
  await page.route('https://cognition-tracker.invalid/**',route=>route.abort());
  await page.route('**/api/factory/artifacts/*/blueprint',async route=>{
    const response=await route.fetch();const details=await response.json();
    details.documents['PRODUCT.md']='# 仅正文\n\n![追踪图片](https://cognition-tracker.invalid/pixel)\n\n<img src="https://cognition-tracker.invalid/html" onerror="document.title=\'injected\'">\n\n[危险链接](javascript:alert(1))';
    await route.fulfill({response,json:details});
  });
  await page.goto('/factory');await page.getByRole('tab',{name:'模板制品',exact:true}).click();
  await page.getByRole('button',{name:'载入书签认知样板',exact:true}).click();
  const card=page.getByRole('article',{name:'认知模板 生活待购与灵感收藏夹：个人本地认知模板',exact:true});
  await card.getByRole('button',{name:'查看认知内容',exact:true}).click();
  const chapter=card.getByRole('region',{name:'章节正文',exact:true});
  await expect(chapter.getByRole('heading',{name:'仅正文',exact:true})).toBeVisible();
  await expect(chapter.locator('img,script,iframe')).toHaveCount(0);
  await expect(chapter.getByRole('link')).toHaveCount(0);
  await expect(page).not.toHaveTitle('injected');
  expect(outbound).toEqual([]);
});

test('confirmed scenarios queue pinned cognition production separately from code templates',async({page})=>{
  await mockStatus(page);
  const created=await page.request.post('/api/factory/scenarios',{data:{leaf:'bookmark-manager',name:'认知生产浏览器场景',audience:'个人用户',objective:'保存、检索并返回链接',workflow:['保存链接','重新查找并打开'],acceptance:['刷新后仍能找到并打开链接'],status:'ready'}});
  expect(created.status()).toBe(201);const scene=await created.json();
  await page.goto('/factory?leaf=bookmark-manager');
  await page.getByRole('checkbox',{name:'选择 认知生产浏览器场景',exact:true}).check();
  const response=page.waitForResponse(r=>r.url().endsWith('/api/factory/batches')&&r.request().method()==='POST');
  await page.getByLabel('认知模板补充要求（可选）',{exact:true}).fill('补齐单条删除与恢复的用户流程');
  await page.getByRole('button',{name:'生产认知模板（1）',exact:true}).click();
  const received=await response;expect(received.status()).toBe(202);
  expect(received.request().postDataJSON()).toMatchObject({kind:'blueprint-production',scenario_ids:[scene.id],source_url:'',cognition_guidance:'补齐单条删除与恢复的用户流程',scenario_revisions:{[scene.id]:scene.revision}});
  const batch=await received.json();expect(batch.jobs[0].snapshot.scenario.revision).toBe(scene.revision);
  expect(batch.jobs[0].kind).toBe('blueprint-production');
  await page.request.post(`/api/factory/batches/${batch.id}/cancel`,{data:{}});
});

test('cognitive review queues independently, can retry after cancellation and produces a new pinned revision',async({page})=>{
  await mockStatus(page);await page.goto('/factory');await page.getByRole('tab',{name:'模板制品',exact:true}).click();
  await page.getByRole('button',{name:'载入书签认知样板',exact:true}).click();
  const card=page.getByRole('article',{name:'认知模板 生活待购与灵感收藏夹：个人本地认知模板',exact:true});
  const wait=page.waitForResponse(r=>r.url().endsWith('/accept')&&r.request().method()==='POST');
  await card.getByRole('button',{name:'发起认知审阅',exact:true}).click();
  const response=await wait;expect(response.status()).toBe(202);expect(response.request().postDataJSON()).toMatchObject({method:'cognitive-review',language:'zh'});
  const reviewBatch=await response.json();expect(reviewBatch.jobs[0].kind).toBe('cognitive-review');
  await expect(card.getByRole('button',{name:'等待认知审阅',exact:true})).toBeDisabled();
  await page.request.post(`/api/factory/batches/${reviewBatch.id}/cancel`,{data:{}});
  await expect(card.getByRole('button',{name:'重试认知审阅',exact:true})).toBeEnabled();
  const artifacts=await (await page.request.get('/api/factory/artifacts')).json();
  const cognitive=artifacts.find((a:{artifact_type?:string})=>a.artifact_type==='product-blueprint');
  cognitive.acceptance_jobs=[{id:'job_unavailable',kind:'cognitive-review',state:'needs_review',stage:'acceptance',updated_at:new Date().toISOString()}];
  cognitive.acceptances=[{id:'acc_unavailable',job_id:'job_unavailable',method:'cognitive-review',outcome:'unavailable',scope:'未完成实际审阅',protocol_note:'报告仅校正外层格式，原文保留',error:'provider 连接失败，未形成结论',created_at:new Date().toISOString()}];
  await page.route('**/api/factory/artifacts',r=>r.fulfill({json:artifacts}));
  await page.reload();await page.getByRole('tab',{name:'模板制品',exact:true}).click();
  await expect(card.getByRole('button',{name:'重试认知审阅',exact:true})).toBeEnabled();
  await card.getByText(/^未完成 · /).click();
  await expect(card.getByText('provider 连接失败，未形成结论',{exact:true})).toBeVisible();
  await expect(card.getByText('报告仅校正外层格式，原文保留',{exact:true})).toBeVisible();
  await card.getByText('按冻结场景生产认知修订版',{exact:true}).click();
  await card.getByLabel('认知修订要求',{exact:true}).fill('补充存储异常验收，并保留原场景');
  const repair=page.waitForResponse(r=>r.url().endsWith('/repair')&&r.request().method()==='POST');
  await card.getByRole('button',{name:'生产认知修订版',exact:true}).click();
  const repairResponse=await repair;expect(repairResponse.status()).toBe(202);const repairBatch=await repairResponse.json();
  expect(repairBatch.jobs[0].kind).toBe('blueprint-production');expect(repairBatch.jobs[0].snapshot.cognitive_repair.note).toContain('存储异常');
  await page.request.post(`/api/factory/batches/${repairBatch.id}/cancel`,{data:{}});
  await expect(card.getByRole('heading',{name:'生活待购与灵感收藏夹：个人本地认知模板',exact:true})).toBeVisible();
});


test('规范预审阻断可见，意见可带回生产补充要求',async({page})=>{
  await mockStatus(page);
  const config={name:'认知模板生产批次',kind:'blueprint-production',model:'test/deepseek-flash',language:'zh',concurrency:1,timeout:900,repair_attempts:1};
  const job={id:'job_'+'f'.repeat(32),batch_id:'bat_'+'f'.repeat(32),kind:'blueprint-production',state:'failed',stage:'blueprint-spec-review-1',attempt:1,error:'规范预审未通过，尚未生成验收文件',updated_at:new Date().toISOString(),snapshot:{leaf:{slug:'bookmark-manager',name:'Bookmarks',name_zh:'书签管理器'},scenario:null,config},events:[],design_reviews:[{stage:'blueprint-spec-review-1',outcome:'blocked',summary:'单条删除只有 API，用户界面没有入口。',scope:'Specification only; no programs executed.',checks:[{dimension:'product_completeness',outcome:'blocked',files:['DRAFT.md'],reason:'缺少可恢复的单条删除用户流程。'}],suggestions:['补上列表删除控件与回收站恢复路径。']}]};
  await page.route('**/api/factory/batches',route=>route.fulfill({json:[{id:job.batch_id,state:'failed',config,created_at:new Date().toISOString(),jobs:[job]}]}));
  await page.route('**/api/factory/jobs/'+job.id,route=>route.fulfill({json:job}));
  await page.goto('/factory');await page.getByRole('tab',{name:'任务批次',exact:true}).click();
  await expect(page.getByText('失败 · 认知规范预审 · 尝试 1',{exact:true})).toBeVisible();
  await page.getByRole('button',{name:'详情',exact:true}).click();
  const review=page.getByRole('region',{name:'规范预审记录',exact:true});
  await review.getByText('需要修订规范',{exact:true}).click();
  await expect(review).toContainText('单条删除只有 API');await expect(review).toContainText('补上列表删除控件');
  await expect(review).toContainText('不代表验收程序或应用已运行');
  await page.getByRole('tab',{name:'生产目录',exact:true}).click();
  await page.getByLabel('认知模板补充要求（可选）',{exact:true}).fill('补上列表删除控件与回收站恢复路径。');
  await expect(page.getByLabel('认知模板补充要求（可选）',{exact:true})).toHaveValue('补上列表删除控件与回收站恢复路径。');
});
