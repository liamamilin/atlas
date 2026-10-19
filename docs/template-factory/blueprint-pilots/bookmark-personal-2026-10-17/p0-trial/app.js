'use strict';

const DB_NAME='atlas-bookmarks';
const DB_VERSION=1;
const STORE_NAME='bookmarks';
const DEFAULT_CATEGORY='收件箱';

const form=document.getElementById('bookmark-form');
const titleInput=document.getElementById('title');
const urlInput=document.getElementById('url');
const categoryInput=document.getElementById('category');
const saveButton=document.getElementById('save-button');
const cancelButton=document.getElementById('cancel-edit');
const formHint=document.getElementById('form-hint');
const alertBox=document.getElementById('alert');
const statusBox=document.getElementById('status');
const searchInput=document.getElementById('search');
const filterSelect=document.getElementById('filter-category');
const categoryOptions=document.getElementById('category-options');
const list=document.getElementById('bookmark-list');
const emptyState=document.getElementById('empty-state');

let db=null;
let records=[];
let editingId=null;
let submitting=false;
let storageReady=false;

function appError(code,message,cause){
  const error=new Error(message||code);
  error.code=code;
  if(cause) error.cause=cause;
  return error;
}

function validationError(message,field){
  const error=appError('validation',message);
  if(field) error.field=field;
  return error;
}

function normalizeBookmarkUrl(value){
  if(typeof value!=='string') throw validationError('链接地址格式不正确。','url');
  let parsed;
  try{
    parsed=new URL(value.trim());
  }catch{
    throw validationError('请输入完整的 http:// 或 https:// 链接地址。','url');
  }
  if(!['http:','https:'].includes(parsed.protocol)||!parsed.hostname||parsed.username||parsed.password){
    throw validationError('只支持不含用户名和密码的 http:// 或 https:// 链接。','url');
  }
  return parsed.href;
}

function createId(){
  if(globalThis.crypto&&typeof globalThis.crypto.randomUUID==='function') return globalThis.crypto.randomUUID();
  const bytes=new Uint8Array(16);
  if(globalThis.crypto&&typeof globalThis.crypto.getRandomValues==='function') globalThis.crypto.getRandomValues(bytes);
  else for(let i=0;i<bytes.length;i+=1) bytes[i]=Math.floor(Math.random()*256);
  bytes[6]=(bytes[6]&15)|64;
  bytes[8]=(bytes[8]&63)|128;
  let hex='';
  for(const byte of bytes) hex+=byte.toString(16).padStart(2,'0');
  return hex.slice(0,8)+'-'+hex.slice(8,12)+'-'+hex.slice(12,16)+'-'+hex.slice(16,20)+'-'+hex.slice(20);
}

function openDatabase(){
  return new Promise((resolve,reject)=>{
    let request;
    try{
      request=indexedDB.open(DB_NAME,DB_VERSION);
    }catch(error){
      reject(appError('storage_unavailable','本地数据库打开失败。',error));
      return;
    }
    request.onupgradeneeded=()=>{
      const database=request.result;
      if(!database.objectStoreNames.contains(STORE_NAME)) database.createObjectStore(STORE_NAME,{keyPath:'id'});
    };
    request.onsuccess=()=>{
      const database=request.result;
      database.onversionchange=()=>database.close();
      resolve(database);
    };
    request.onerror=()=>reject(appError('storage_unavailable','本地数据库打开失败。',request.error));
    request.onblocked=()=>reject(appError('storage_unavailable','本地数据库被其他页面占用。'));
  });
}

function readAllRecords(){
  return new Promise((resolve,reject)=>{
    let tx;
    try{
      tx=db.transaction(STORE_NAME,'readonly');
    }catch(error){
      reject(appError('storage_unavailable','无法读取本地书签。',error));
      return;
    }
    let rows=[];
    let failed=false;
    tx.oncomplete=()=>{
      if(failed) reject(appError('storage_unavailable','读取本地书签失败。'));
      else resolve(rows);
    };
    tx.onabort=()=>reject(appError('storage_unavailable','读取本地书签的事务已中止。'));
    tx.onerror=()=>{ failed=true; };
    try{
      const request=tx.objectStore(STORE_NAME).getAll();
      request.onsuccess=()=>{ rows=Array.isArray(request.result)?request.result:[]; };
      request.onerror=()=>{ failed=true; };
    }catch(error){
      failed=true;
      reject(appError('storage_unavailable','无法读取本地书签。',error));
    }
  });
}

function persistBookmark(input){
  if(!db) return Promise.reject(appError('storage_unavailable','本地数据库不可用。'));
  const title=typeof input.title==='string'?input.title.trim():'';
  if(!title) return Promise.reject(validationError('请填写标题后再保存。','title'));
  const url=normalizeBookmarkUrl(input.url);
  const category=typeof input.category==='string'&&input.category.trim()?input.category.trim():DEFAULT_CATEGORY;
  const now=new Date().toISOString();
  const id=typeof input.id==='string'&&input.id?input.id:null;
  return new Promise((resolve,reject)=>{
    let tx;
    try{
      tx=db.transaction(STORE_NAME,'readwrite');
    }catch(error){
      reject(appError('storage_write','无法启动本地写入事务。',error));
      return;
    }
    let outcome=null;
    tx.oncomplete=()=>{
      if(outcome&&outcome.error) reject(outcome.error);
      else if(outcome&&outcome.record) resolve(outcome.record);
      else reject(appError('storage_write','写入事务没有返回结果。'));
    };
    tx.onabort=()=>reject(outcome&&outcome.error?outcome.error:appError('storage_write','写入事务已中止，未保存任何内容。'));
    tx.onerror=()=>{};
    try{
      const store=tx.objectStore(STORE_NAME);
      if(id){
        const request=store.get(id);
        request.onsuccess=()=>{
          const existing=request.result;
          if(!existing){
            outcome={error:appError('not_found','要编辑的书签不存在。')};
            try{ tx.abort(); }catch{ }
            return;
          }
          const record={...existing,title,url,category,updatedAt:now};
          outcome={record};
          try{
            store.put(record);
          }catch(error){
            outcome={error:appError('storage_write','写入原记录失败。',error)};
            try{ tx.abort(); }catch{ }
          }
        };
        request.onerror=()=>{ outcome={error:appError('storage_write','读取原记录失败。')}; };
      }else{
        const record={id:createId(),title,url,category,createdAt:now,updatedAt:now,deletedAt:null};
        outcome={record};
        store.put(record);
      }
    }catch(error){
      outcome={error:appError('storage_write','写入本地书签失败。',error)};
      try{ tx.abort(); }catch{ }
    }
  });
}

function setAlert(message){
  alertBox.textContent=message||'';
}

function setStatus(message){
  statusBox.textContent=message||'';
}

function messageForError(error){
  const code=error&&error.code;
  if(code==='validation') return error.message||'输入内容不合法，请检查后重试。';
  if(code==='not_found') return '保存失败：要编辑的书签已经不存在，未写入任何内容。';
  if(code==='storage_unavailable') return '保存失败：本地数据库当前不可用，未写入任何内容。你的输入已保留，请刷新页面后重试。';
  return '保存失败：写入事务没有完成，未保存任何内容。你的输入和原有书签都已保留，请稍后重试。';
}

function optionNode(value,label){
  const node=document.createElement('option');
  node.value=value;
  node.textContent=label;
  return node;
}

function categoryNames(){
  return Array.from(new Set(records.map((record)=>record.category).filter((value)=>typeof value==='string'&&value)))
    .sort((a,b)=>a.localeCompare(b,'zh-Hans-CN'));
}

function refreshCategoryOptions(){
  const categories=categoryNames();
  const selected=filterSelect.value;
  const filterNodes=[optionNode('','全部分类')];
  for(const category of categories) filterNodes.push(optionNode(category,category));
  filterSelect.replaceChildren(...filterNodes);
  filterSelect.value=categories.includes(selected)?selected:'';
  const names=['收件箱',...categories.filter((category)=>category!=='收件箱')];
  categoryOptions.replaceChildren(...names.map((category)=>optionNode(category,category)));
}

function createArticle(record){
  const article=document.createElement('article');
  const heading=document.createElement('h2');
  heading.textContent=record.title;
  const category=document.createElement('p');
  category.className='bookmark-category';
  category.textContent='分类：'+record.category;
  const url=document.createElement('p');
  url.className='bookmark-url';
  url.textContent=record.url;
  const actions=document.createElement('div');
  actions.className='bookmark-actions';
  const link=document.createElement('a');
  link.href=record.url;
  link.target='_blank';
  link.rel='noopener noreferrer';
  link.textContent='打开原网页';
  const edit=document.createElement('button');
  edit.type='button';
  edit.className='secondary';
  edit.textContent='编辑';
  edit.addEventListener('click',()=>startEdit(record.id));
  actions.append(link,edit);
  article.append(heading,category,url,actions);
  return article;
}

function render(){
  if(!storageReady) return;
  const query=searchInput.value.trim().toLowerCase();
  const selectedCategory=filterSelect.value;
  const visible=records
    .filter((record)=>!record.deletedAt)
    .filter((record)=>!selectedCategory||record.category===selectedCategory)
    .filter((record)=>{
      if(!query) return true;
      return [record.title,record.url,record.category].some((value)=>String(value||'').toLowerCase().includes(query));
    })
    .sort((a,b)=>String(b.createdAt||'').localeCompare(String(a.createdAt||'')));
  list.replaceChildren(...visible.map(createArticle));
  emptyState.hidden=visible.length>0;
}

function startEdit(id){
  const record=records.find((item)=>item.id===id);
  if(!record){
    setAlert('要编辑的书签已经不存在，未做任何修改。');
    return;
  }
  editingId=id;
  titleInput.value=record.title;
  urlInput.value=record.url;
  categoryInput.value=record.category;
  cancelButton.hidden=false;
  formHint.textContent='正在编辑「'+record.title+'」；保存后将更新这条原记录。';
  formHint.hidden=false;
  setAlert('');
  setStatus('');
  titleInput.focus();
}

function resetForm(){
  form.reset();
  editingId=null;
  cancelButton.hidden=true;
  formHint.hidden=true;
  formHint.textContent='';
}

async function handleSubmit(event){
  event.preventDefault();
  if(submitting||!storageReady) return;
  submitting=true;
  saveButton.disabled=true;
  setStatus('');
  setAlert('');
  titleInput.removeAttribute('aria-invalid');
  urlInput.removeAttribute('aria-invalid');
  const wasEditing=Boolean(editingId);
  try{
    let saved;
    try{
      saved=await persistBookmark({
        id:editingId||undefined,
        title:titleInput.value,
        url:urlInput.value,
        category:categoryInput.value
      });
    }catch(error){
      if(error&&error.field==='title'){
        titleInput.setAttribute('aria-invalid','true');
        titleInput.focus();
      }else if(error&&error.field==='url'){
        urlInput.setAttribute('aria-invalid','true');
        urlInput.focus();
      }
      setAlert(messageForError(error));
      return;
    }
    try{
      if(wasEditing){
        const index=records.findIndex((record)=>record.id===saved.id);
        if(index>=0) records[index]=saved;
        else records.push(saved);
      }else if(!records.some((record)=>record.id===saved.id)){
        records.push(saved);
      }
      resetForm();
      refreshCategoryOptions();
      render();
      setStatus((wasEditing?'已更新：':'已保存：')+saved.title);
    }catch(uiError){
      setAlert('书签已保存，但界面刷新失败，请刷新页面查看。');
    }
  }finally{
    submitting=false;
    saveButton.disabled=!storageReady;
  }
}

async function init(){
  try{
    db=await openDatabase();
    records=await readAllRecords();
    storageReady=true;
    refreshCategoryOptions();
    render();
    saveButton.disabled=false;
    setAlert('');
  }catch(error){
    if(db){
      try{ db.close(); }catch{ }
    }
    db=null;
    records=[];
    storageReady=false;
    saveButton.disabled=true;
    list.replaceChildren();
    emptyState.hidden=true;
    setStatus('');
    setAlert('本地数据库不可用，暂时无法读取或保存书签。请确认浏览器允许本站使用 IndexedDB，然后刷新页面重试。');
  }
}

form.addEventListener('submit',handleSubmit);
searchInput.addEventListener('input',render);
filterSelect.addEventListener('change',render);
cancelButton.addEventListener('click',()=>{
  resetForm();
  setAlert('');
  setStatus('');
  titleInput.focus();
});
titleInput.addEventListener('input',()=>titleInput.removeAttribute('aria-invalid'));
urlInput.addEventListener('input',()=>urlInput.removeAttribute('aria-invalid'));

init().catch(()=>{
  storageReady=false;
  saveButton.disabled=true;
  setAlert('应用启动失败：本地数据库不可用，请刷新页面重试。');
});