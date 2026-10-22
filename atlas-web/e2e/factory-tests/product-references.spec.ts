import {test,expect} from '@playwright/test';

test('product references distinguish design examples and unreviewed scoped drafts',async({page})=>{
  const writes:string[]=[];
  await page.route('**/api/**',async route=>{
    const url=new URL(route.request().url());
    if(route.request().method()==='POST')writes.push(url.pathname);
    if(url.pathname.endsWith('/product-reference-examples'))return route.fulfill({json:url.searchParams.has('key')?{markdown:'# 个人收藏夹\n\n设计参考样稿。没有应用运行。\n\n![untrusted](https://example.invalid/tracker.png)'}:{items:[{key:'01-personal-bookmarks',name:'个人收藏夹',counts:{pages:8,journeys:8,rules:10}}]}});
    if(url.pathname.endsWith('/product-references/preview')){
      const body=route.request().postDataJSON();
      if(body.reference?.schema==='broken')return route.fulfill({status:400,json:{code:'invalid_product_reference',error:'missing action reference'}});
      return route.fulfill({json:{reference_digest:'a'.repeat(64),documents:{'PRODUCT_REFERENCE.md':'# 参考草案\n\n### save\n\n[save](#save)'},scope_options:[{id:'p0',name:'P0'}],selection:body.scope_id?{action_ids:['save'],journey_ids:['save-flow'],deferred_action_ids:['bulk']}:null}});
    }
    if(url.pathname.endsWith('/status'))return route.fulfill({json:{cli:{available:true,version:'fixture',models:[]},runtime:{available:false}}});
    if(url.pathname.endsWith('/assisted-templates'))return route.fulfill({json:{items:[],counts:{total:0,core_verified:0,not_run:0}}});
    if(['/catalog','/batches','/artifacts'].some(p=>url.pathname.endsWith(p)))return route.fulfill({json:[]});
    return route.fulfill({json:{}});
  });
  await page.goto('/factory?view=references');
  await expect(page.getByRole('tab',{name:'产品参考',exact:true})).toHaveAttribute('aria-selected','true');
  await page.getByRole('button',{name:'阅读个人收藏夹'}).click();
  await expect(page.getByRole('article',{name:'个人收藏夹'})).toContainText('没有应用运行');
  await expect(page.getByRole('article',{name:'个人收藏夹'}).locator('img')).toHaveCount(0);
  await page.getByLabel('预览产品参考 JSON 草案').setInputFiles({name:'reference.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify({reference:{schema:'atlas.product-reference.v1'},scope_id:'p0'}))});
  await expect(page.getByLabel('按旅程选择开发范围')).toHaveValue('');
  await expect(page.getByText('当前选择 1 条旅程、1 项操作；1 项操作保留在完整参考中。')).toHaveCount(0);
  await page.getByLabel('按旅程选择开发范围').selectOption('p0');
  await expect(page.getByText('当前选择 1 条旅程、1 项操作；1 项操作保留在完整参考中。')).toBeVisible();
  await expect(page.getByRole('button',{name:'下载未审阅参考包'})).toBeVisible();
  await expect(page.getByRole('link',{name:'save',exact:true})).toHaveAttribute('href','#save');
  await expect(page.locator('h3#save')).toHaveText('save');
  await page.getByLabel('预览产品参考 JSON 草案').setInputFiles({name:'bad.json',mimeType:'application/json',buffer:Buffer.from('{"schema":"broken"}')});
  await expect(page.getByRole('alert')).toContainText('missing action reference');
  await expect(page.getByRole('button',{name:'下载未审阅参考包'})).toHaveCount(0);
  expect(writes.every(p=>p==='/api/factory/product-references/preview')).toBe(true);
});

test('reviewed references are catalog entries with explicit non-runtime status and shared case links',async({page})=>{
  await page.addInitScript(()=>localStorage.setItem('atlas-lang','en'));
  const item={id:'ref_'+'a'.repeat(32),name:'个人收藏夹',schema:'atlas.product-reference.v1',package_sha256:'b'.repeat(64),reference_digest:'c'.repeat(64),pilot_id:'pilot-fixture',leaf:'bookmark-manager',revision_id:'r2',status:'static_review_passed',application_status:'application_not_run',publication_status:'not_published',case_refs:[{case_id:'case:bookmark',revision:2,digest:'d'.repeat(64),url:'/api/factory/v1/cases/case:bookmark/revisions/2'}]};
  await page.route('**/api/**',async route=>{
    const url=new URL(route.request().url());
    if(url.pathname.endsWith('/product-references/'+item.id+'/download'))return route.fulfill({status:200,body:'fixture zip'});
    if(url.pathname.endsWith('/product-references/'+item.id))return route.fulfill({json:{...item,document:'# 个人收藏夹\n\nReviewed reference.'}});
    if(url.pathname.endsWith('/product-references'))return route.fulfill({json:[item]});
    if(url.pathname.endsWith('/product-reference-examples'))return route.fulfill({json:{items:[]}});
    if(url.pathname.endsWith('/status'))return route.fulfill({json:{cli:{available:true,version:'fixture',models:[]},runtime:{available:false}}});
    if(url.pathname.endsWith('/assisted-templates'))return route.fulfill({json:{items:[],counts:{total:0,core_verified:0,not_run:0}}});
    if(['/catalog','/batches','/artifacts'].some(p=>url.pathname.endsWith(p)))return route.fulfill({json:[]});
    return route.fulfill({json:{}});
  });
  await page.goto('/factory?view=references');
  await expect(page.getByRole('status').filter({hasText:'Catalog references have passed independent static review'})).toBeVisible();
  const card=page.getByRole('article').filter({hasText:'r2'});
  await expect(card).toContainText('Application not run');
  await expect(card.getByRole('link',{name:'Case case:bookmark r2'})).toHaveAttribute('href',item.case_refs[0].url);
  await card.getByRole('button',{name:'Read reference'}).click();
  await expect(page.getByRole('article',{name:'个人收藏夹'})).toContainText('Reviewed reference.');
  expect(page.locator('input[type=file]')).toHaveCount(1);
});
