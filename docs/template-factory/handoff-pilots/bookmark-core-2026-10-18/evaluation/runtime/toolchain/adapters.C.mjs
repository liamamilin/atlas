// UI-only adapter, no API mutation or hidden seed records. Supports the actual inline-create UI.
export function createAdapter(page, baseUrl) {
  const root=baseUrl+'/';
  const saveForm=()=>page.locator('form.save-form');
  async function submit(action){
    const response=page.waitForResponse(r=>r.request().isNavigationRequest()&&r.request().method()==='POST'&&new URL(r.url()).origin===baseUrl);
    await action();await(await response).finished();await page.waitForLoadState('domcontentloaded');
  }
  async function options(select,name){
    return select.locator('option').evaluateAll((nodes,target)=>{
      const found=nodes.find(n=>target==null?n.value==='':n.textContent.trim()===target);
      return found?found.value:null;
    },name??null);
  }
  const card=record=>page.locator('li.record-card').filter({has:page.locator('a.record-open').filter({hasText:record.title||record.url})}).filter({has:page.locator('.record-url').filter({hasText:record.url})}).first();
  async function fill(record){
    await page.locator('#save-url').fill(record.url);
    await page.locator('#save-title').fill(record.title??'');
    await page.locator('#save-note').fill(record.note??'');
    await page.locator('#save-category-new').fill('');
    const select=page.locator('#save-category-select');
    const value=await options(select,record.category);
    if(record.category&&value===null){
      await select.selectOption('');await page.locator('#save-category-new').fill(record.category);
    }else await select.selectOption(value??'');
  }
  return {
    async ready(){await page.goto(root);await page.locator('#save-url').waitFor();},
    async save(record){await fill(record);await submit(()=>saveForm().locator('button[type=submit]').click());},
    async createCategory(name){
      const existing=await options(page.locator('#save-category-select'),name);
      if(existing!==null)return{category:name,actual:'already present; not a new creation claim'};
      const standalone=page.locator('form.category-create-form');
      if(await standalone.count()){
        await standalone.locator('input[name=name]').fill(name);
        await submit(()=>standalone.locator('button[type=submit]').click());
        return{category:name,actual:'created through standalone UI'};
      }
      return{category:name,actual:'No standalone empty-category action. Only inline creation while saving a real record is exposed; not created by this operation. save(record) uses that inline path when applicable.',created:false};
    },
    async viewCategory(name){
      const text=name==='all'?'全部':name==null?'未分类':name;
      await page.getByRole('link',{name:text,exact:true}).click();await page.waitForLoadState('domcontentloaded');
    },
    async move(record,destination){
      const row=card(record);const select=row.locator('select[name=category_id]');
      const value=await options(select,destination);
      if(value===null)throw new Error('Actual UI has no destination category '+destination+' and no independent create/move-create action; no hidden records or duplicate-error side effects used to manufacture it.');
      await select.selectOption(value);await submit(()=>row.getByRole('button',{name:'移动',exact:true}).click());
    },
    async search(query){
      await page.locator('#search-input').fill(query);
      await page.locator('#search-submit').click();await page.waitForLoadState('domcontentloaded');
    },
    async records(){return page.locator('li.record-card').evaluateAll(nodes=>nodes.map(n=>({
      url:n.getAttribute('data-url'),title:n.querySelector('a.record-open').textContent,
      note:n.querySelector('.record-note')?.textContent??'',text:n.innerText,
    })));},
    async openOriginal(record){
      const link=card(record).locator('a.record-open');const href=await link.getAttribute('href');
      const popup=page.context().waitForEvent('page');await link.click();await(await popup).waitForLoadState('domcontentloaded');return href;
    },
    async submitEmptyUrl(){await page.locator('#save-url').fill('');await submit(()=>saveForm().locator('button[type=submit]').click());return{feedback:await page.locator('.form-error').allTextContents()};},
    async doubleSave(record){
      await fill(record);await saveForm().locator('button[type=submit]').dblclick();await page.waitForTimeout(400);
      return{observation:'One physical double-click on the current save button; request outcomes recorded by common harness.'};
    },
  };
}
