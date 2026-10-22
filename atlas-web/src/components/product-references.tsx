import { useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { useAsync } from "@/components/loaders";
import { Button } from "@/components/ui/button";
import { factoryRequest } from "@/lib/factory";

type Example = {key:string;name:string;counts:{pages:number;journeys:number;rules:number;acceptance_assertions:number}};
type Preview = {reference_digest:string;documents:Record<string,string>;scope_options:{id:string;name:string}[];selection:null|{action_ids:string[];deferred_action_ids:string[];journey_ids:string[]}};
type CatalogReference = {id:string;name:string;schema:string;package_sha256:string;reference_digest:string;pilot_id:string;leaf:string;revision_id:string;status:"static_review_passed";application_status:"application_not_run";publication_status:string;case_refs:{case_id:string;revision:number;digest:string;url:string}[]};
type CatalogDetail = CatalogReference & {document:string};

export function ProductReferences({zh}:{zh:boolean}) {
  const examples=useAsync(()=>factoryRequest<{items:Example[]}>("product-reference-examples"),[]);
  const catalog=useAsync(()=>factoryRequest<CatalogReference[]>("product-references"),[]);
  const [document,setDocument]=useState("");
  const [title,setTitle]=useState("");
  const [error,setError]=useState("");
  const [busy,setBusy]=useState(false);
  const [body,setBody]=useState<{reference:unknown;source_ids?:string[]}|null>(null);
  const [preview,setPreview]=useState<Preview|null>(null);
  const [scope,setScope]=useState("");
  const [notice,setNotice]=useState("");
  async function readExample(item:Example) {
    setBusy(true);setError("");setNotice("");
    try {const value=await factoryRequest<{markdown:string}>(`product-reference-examples?key=${encodeURIComponent(item.key)}`);setTitle(item.name);setDocument(value.markdown);setPreview(null);setBody(null);setScope("");}
    catch(e){setError(String(e));}finally{setBusy(false);}
  }
  async function readCatalogReference(item:CatalogReference) {
    setBusy(true);setError("");setNotice("");
    try {const value=await factoryRequest<CatalogDetail>(`product-references/${encodeURIComponent(item.id)}`);setTitle(value.name);setDocument(value.document);setPreview(null);setBody(null);setScope("");}
    catch(e){setError(String(e));}finally{setBusy(false);}
  }
  async function inspect(value:{reference:unknown;source_ids?:string[]},scopeId="") {
    const result=await factoryRequest<Preview>("product-references/preview",{...value,...(scopeId?{scope_id:scopeId}:{})});
    setBody(value);setPreview(result);setDocument(result.documents["PRODUCT_REFERENCE.md"]);setTitle(zh?"产品参考草案":"Product reference draft");setScope(scopeId);
  }
  async function upload(file?:File) {
    if(!file)return;
    setBusy(true);setError("");setNotice("");setPreview(null);setBody(null);setDocument("");setScope("");
    try {
      if(file.size>2*1024*1024)throw new Error(zh?"请选择小于 2 MiB 的 JSON 文件":"Select a JSON file smaller than 2 MiB");
      const value:unknown=JSON.parse(await file.text());
      const wrapped=typeof value==="object"&&value!==null&&"reference" in value;
      const uploaded=wrapped?value as {reference:unknown;source_ids?:string[]}:{reference:value};
      // Uploads may include an old scope_id. Only the explicit dropdown controls
      // selection; never carry unknown wrapper keys into preview or downloads.
      await inspect({reference:uploaded.reference,...(uploaded.source_ids?{source_ids:uploaded.source_ids}:{})});
    }catch(e){setError(String(e));}finally{setBusy(false);}
  }
  async function selectScope(id:string) {
    if(!body)return;
    setBusy(true);setError("");
    try {await inspect(body,id);}catch(e){setError(String(e));}finally{setBusy(false);}
  }
  async function download() {
    if(!body)return;
    setBusy(true);setError("");setNotice("");
    try {
      const result=await factoryRequest<{archive_base64:string;filename:string;sha256:string}>("product-references/export-preview",{...body,...(scope?{scope_id:scope}:{})});
      const bytes=Uint8Array.from(atob(result.archive_base64),char=>char.charCodeAt(0));
      const hash=Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256",bytes))).map(b=>b.toString(16).padStart(2,"0")).join("");
      if(hash!==result.sha256)throw new Error(zh?"下载摘要不匹配":"Download checksum mismatch");
      const url=URL.createObjectURL(new Blob([bytes],{type:"application/zip"}));
      const link=window.document.createElement("a");link.href=url;link.download=result.filename;link.click();
      window.setTimeout(()=>URL.revokeObjectURL(url),1000);
      setNotice(zh?"草案参考包已下载；它不是标准开发包，也没有审阅或运行通过记录。":"Draft reference downloaded; this is not a standard development package or a passed review/runtime record.");
    }catch(e){setError(String(e));}finally{setBusy(false);}
  }
  return <section className="mt-6 space-y-5" aria-label={zh?"产品参考规格":"Product reference specifications"}>
    <div className="rounded-xl bg-surface p-5 shadow-card">
      <h2 className="font-serif text-xl">{zh?"先看完整产品，再选择开发范围":"Understand the product, then choose a development slice"}</h2>
      <p className="mt-3 text-sm leading-6 text-muted">{zh?"完整参考规格描述角色、对象、入口、操作、旅程和共同规则。开发范围按旅程与依赖选择；同页的后期能力不会自动进入 P0。旧核心场景模板仍在模板制品页。":"References connect roles, objects, surfaces, actions, journeys and rules. Slices follow journeys and dependencies; sharing a page does not put later features into P0. Existing core templates remain in Artifacts."}</p>
      <p role="status" className="mt-3 text-sm text-primary">{catalog.loading? (zh?"正在确认正式参考目录状态…":"Checking the reviewed reference catalog…") : catalog.data?.length? (zh?"目录中的正式参考已完成独立静态审阅；应用运行仍未执行。下方样稿和草案预览仍不代表通过。":"Catalog references have passed independent static review; application runtime remains unrun. Examples and draft previews below are not passed references.") : (zh?"当前目录没有正式参考；下方为设计样稿与草案结构预览。":"No formal references are currently in the catalog; examples and structural draft previews follow.")}</p>
    </div>
    {catalog.loading?<p role="status">{zh?"读取正式参考目录…":"Loading reviewed reference catalog…"}</p>:catalog.error?<p role="alert">{zh?"正式参考目录暂不可读。":"Reviewed reference catalog is unavailable."}</p>:catalog.data?.length?<div className="space-y-3" aria-label={zh?"已审阅产品参考":"Reviewed product references"}><h3 className="font-medium">{zh?"已审阅产品参考":"Reviewed product references"}</h3><div className="grid gap-3 md:grid-cols-2">{catalog.data.map(item=><article key={item.id} className="rounded-xl border border-primary/30 bg-surface p-4"><h4 className="font-medium">{item.name}</h4><p className="mt-2 text-xs text-muted">{item.leaf} · {item.revision_id} · {zh?"独立静态审阅通过":"Independent static review passed"}</p><p className="mt-1 text-xs">{zh?"应用未运行 · 未发布":"Application not run · not published"}</p>{item.case_refs.length?<div className="mt-2 flex flex-wrap gap-2 text-xs">{item.case_refs.map(ref=><a key={`${ref.case_id}:${ref.revision}`} className="underline" href={ref.url}>{zh?`案例 ${ref.case_id} r${ref.revision}`:`Case ${ref.case_id} r${ref.revision}`}</a>)}</div>:null}<div className="mt-3 flex gap-2"><Button size="sm" variant="outline" disabled={busy} onClick={()=>void readCatalogReference(item)}>{zh?"阅读参考":"Read reference"}</Button><a className="inline-flex items-center rounded-md border border-border px-3 text-sm" href={`/api/factory/product-references/${encodeURIComponent(item.id)}/download`}>{zh?"下载 ZIP":"Download ZIP"}</a></div></article>)}</div></div>:null}
    <div className="grid gap-3 md:grid-cols-3">{examples.loading?<p>{zh?"读取参考样稿…":"Loading examples…"}</p>:examples.error?<p role="alert">{zh?"样稿暂不可读，请刷新重试。":"Examples unavailable; refresh to retry."}</p>:examples.data?.items.map(item=><article key={item.key} className="rounded-xl border border-border bg-surface p-4"><h3 className="font-medium">{item.name}</h3><p className="mt-2 text-xs text-muted">{zh?`${item.counts.pages} 个页面 · ${item.counts.journeys} 条旅程 · ${item.counts.rules} 条规则`:`${item.counts.pages} pages · ${item.counts.journeys} journeys · ${item.counts.rules} rules`}</p><p className="mt-2 text-xs">{zh?"设计参考样稿 · 未审阅 · 应用未运行":"Design example · not reviewed · app not run"}</p><Button className="mt-3" size="sm" variant="outline" disabled={busy} onClick={()=>void readExample(item)}>{zh?`阅读${item.name}`:`Read ${item.name}`}</Button></article>)}</div>
    <div className="rounded-xl border border-border bg-surface p-5">
      <label className="block text-sm font-medium">{zh?"预览产品参考 JSON 草案":"Preview a product reference JSON draft"}<input className="mt-3 block w-full text-sm" type="file" accept=".json,application/json" disabled={busy} onChange={e=>{void upload(e.target.files?.[0]);e.target.value="";}}/></label>
      <p className="mt-2 text-xs leading-6 text-muted">{zh?"选择 atlas.product-reference.v1 JSON；带来源的草案可用 {reference, source_ids} 包装。这里只检查结构和关联，所传来源 ID 不会被当作已核验案例，不修改目录或生产队列。":"Select atlas.product-reference.v1 JSON, optionally wrapped as {reference, source_ids}. Only structure and relationships are checked. Supplied source IDs are not verified evidence; the catalog and production queue are unchanged."}</p>
      {preview?<><p className="mt-3 break-all text-xs">SHA256: {preview.reference_digest}</p><label className="mt-3 block text-sm">{zh?"按旅程选择开发范围":"Choose scope by journeys"}<select className="ml-2 rounded border border-border bg-surface p-2" value={scope} disabled={busy} onChange={e=>void selectScope(e.target.value)}><option value="">{zh?"完整参考":"Full reference"}</option>{preview.scope_options.map(s=><option key={s.id} value={s.id}>{s.name}</option>)}</select></label>{preview.selection?<p className="mt-3 text-sm">{zh?`当前选择 ${preview.selection.journey_ids.length} 条旅程、${preview.selection.action_ids.length} 项操作；${preview.selection.deferred_action_ids.length} 项操作保留在完整参考中。`:`Selected ${preview.selection.journey_ids.length} journeys and ${preview.selection.action_ids.length} actions; ${preview.selection.deferred_action_ids.length} actions remain deferred in the full reference.`}</p>:null}<Button className="mt-3" variant="outline" size="sm" disabled={busy} onClick={()=>void download()}>{zh?"下载未审阅参考包":"Download unreviewed reference"}</Button></>:null}
    </div>
    {busy?<p role="status">{zh?"读取与检查中…":"Reading and checking…"}</p>:null}{error?<p role="alert" className="text-sm text-danger">{error}</p>:null}{notice?<p role="status" className="text-sm">{notice}</p>:null}
    {document?<article className="rounded-xl bg-surface p-6 shadow-card" aria-label={title}><h2 className="mb-4 font-serif text-xl">{title}</h2><div className="prose max-w-none overflow-x-auto text-sm"><ReactMarkdown remarkPlugins={[remarkGfm]} components={{h3:({children})=><h3 id={String(children).toLowerCase()}>{children}</h3>,img:()=>null}}>{document}</ReactMarkdown></div></article>:null}
  </section>;
}
