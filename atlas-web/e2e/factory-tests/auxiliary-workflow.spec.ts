import {test,expect} from '@playwright/test';

test('auxiliary workflow shows leaf progress, reuse, calls and filters details',async({page})=>{
  const requests:string[]=[];
  const plan={id:'plan/demo one',status:'running',reason:'fixture plan',model:'fixture/model',baseline:2,max_calls:10,new_calls:3,active_calls:1,remaining_calls:6,total:2,handled:1,counts:{ready_not_run:1,reused:1},started:1792520000,gate:{mode:'validation',leaves:['task-manager'],status:'running'}};
  const item={leaf:'task-manager',display_name:'任务管理',state:'running',artifact_id:'artifact/abc',current_attempt:'2',steps:[{step:'scenario',state:'completed',attempt:'1',outputs:[]},{step:'generation',state:'running',attempt:'2',outputs:[{path:'template.zip',sha256:'abc123',url:'/api/factory/artifacts/artifact%2Fabc/download'}]}],calls:[{id:'call-1',stage:'generation',status:'running',requested_model:'fixture/model'}]};
  await page.route('**/api/**',route=>{
    const url=new URL(route.request().url());requests.push(`${url.pathname}${url.search}`);
    if(url.pathname.endsWith('/auxiliary-workflows'))return route.fulfill({json:{plans:[plan]}});
    if(url.pathname.includes('/auxiliary-workflows/'))return route.fulfill({json:{plan,items:[item,{leaf:'calendar',display_name:'日历',state:'reused',steps:[],calls:[]}],pagination:{offset:Number(url.searchParams.get('offset')||0),limit:20,total:2}}});
    if(url.pathname.endsWith('/status'))return route.fulfill({json:{cli:{available:true,version:'fixture',models:[]},runtime:{available:false}}});
    if(url.pathname.endsWith('/assisted-templates'))return route.fulfill({json:{items:[],counts:{total:0,core_verified:0,not_run:0}}});
    if(url.pathname.endsWith('/catalog')||url.pathname.endsWith('/batches')||url.pathname.endsWith('/artifacts'))return route.fulfill({json:[]});
    return route.fulfill({json:{}});
  });
  await page.goto('/factory?view=workflow');
  await expect(page.getByRole('tab',{name:'辅助生产进度'})).toHaveAttribute('aria-selected','true');
  await expect(page.getByRole('heading',{name:'任务管理',exact:true})).toBeVisible();
  for(const step of ['检查已有模板','确定场景','案例研究','生成模板','确定性检查','独立审阅','冻结入库','验证下载'])await expect(page.getByText(step,{exact:false}).first()).toBeVisible();
  await expect(page.getByText('复用已有模板，此叶子不会被显示为重新完成八步生产。')).toBeVisible();
  await expect(page.getByText('fixture/model',{exact:false}).first()).toBeVisible();
  await expect(page.getByText('已处理: 1',{exact:true})).toBeVisible();
  await expect(page.getByText('可用: 2',{exact:true})).toBeVisible();
  await expect(page.getByRole('link',{name:'打开制品 · artifact/abc'})).toHaveAttribute('href','/factory?view=artifacts&artifact_id=artifact%2Fabc');
  await page.getByLabel('状态筛选').selectOption('ready_not_run');
  await expect.poll(()=>requests.some(path=>path.includes('state=ready_not_run'))).toBe(true);
  expect(requests.some(path=>path.includes('plan%2Fdemo+one')||path.includes('plan%2Fdemo%20one'))).toBe(true);
});
