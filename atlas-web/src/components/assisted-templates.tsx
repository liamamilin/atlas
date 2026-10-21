import { useState } from "react";
import { Link } from "react-router-dom";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { useAsync } from "@/components/loaders";
import { Button } from "@/components/ui/button";
import { factoryRequest } from "@/lib/factory";
import { useLang } from "@/lib/lang";

export interface AssistedTemplate {
  artifact_id:string; digest:string; key:string; title:string; leaf:string;
  scenario:{id:string;revision:number;name:string;audience:string;objective:string;workflow:string[]};
  capabilities:string[]; limits:string[];
  production?:{mode:string;model:string;review_status:string;review_input_digest:string}|null;
  cases:{case_id:string;revision:number;digest:string;app_id:string;sources:{repository:string;commit_sha:string;license_files:string[]}[]}[];
  runtime:{status:"core_verified"|"not_run"|"evidence_unavailable";scope:string;recorded_date?:string;online_status:string;strict_acceptance:false};
  files:Record<string,{available:boolean;url?:string;sha256?:string;reason?:string}>;
}
export interface AssistedCatalog {items:AssistedTemplate[];unavailable:{artifact_id:string;reason:string}[];counts:{total:number;core_verified:number;not_run:number}}

export function codexStart(item:AssistedTemplate,zh:boolean) {
  return zh ? `使用 Atlas 辅助试用模板「${item.title}」。\n固定模板：${item.artifact_id}\n摘要：${item.digest}\n将标准开发包解压到新目录，先读 HANDOFF.md，再读 CURRENT_PHASE.json、ACCEPTANCE_CONTRACT.json、APP_DELIVERY.md 和 PROJECT_DECISIONS.json；按需查阅 KNOWLEDGE.md 与 blueprint/。\n先记录所消费包的摘要，再按当前阶段实现完整核心旅程，遵循包内数据与接口约定并运行验收。保留既有应用与数据。遇到会改变范围或破坏数据的决策先询问。\n已有示例只证明报告所列核心旅程曾验证，不等于严格 G1/T08 通过或本机服务在线；新实现仍需自己验证。交付启动命令、源码、实际结果与已知缺口。` : `Use the Atlas assisted trial template "${item.title}".\nPinned template: ${item.artifact_id}\nDigest: ${item.digest}\nUnzip the standard package into a new directory. Read HANDOFF.md first, then CURRENT_PHASE.json, ACCEPTANCE_CONTRACT.json, APP_DELIVERY.md and PROJECT_DECISIONS.json. Consult KNOWLEDGE.md and blueprint/ as needed.\nRecord the consumed package digest. Implement the complete core journey for the current phase, follow its data/API contracts and execute acceptance. Preserve existing apps and data; ask before changing scope or destructive decisions.\nHistorical examples cover only their reported journeys, not strict G1/T08 or current service availability. Validate the new implementation and deliver startup commands, source, actual results and gaps.`;
}

export function AssistedTemplateSummary({item,zh,detail=false}:{item:AssistedTemplate;zh:boolean;detail?:boolean}) {
  const [copy,setCopy]=useState("");const [guide,setGuide]=useState("");const [guideState,setGuideState]=useState("");
  const label=item.runtime.status==="core_verified"?(zh?"已有核心运行示例":"Core example verified"):item.runtime.status==="not_run"?(zh?"应用未运行":"Application not run"):(zh?"运行证据暂不可核对":"Runtime evidence unavailable");
  const files=item.files;
  async function readGuide(){
    setGuideState(zh?"读取中…":"Loading…");
    try {const r=await fetch(files.guide.url!);if(!r.ok)throw new Error(String(r.status));setGuide(await r.text());setGuideState("");}
    catch {setGuideState(zh?"说明暂不可用，请稍后重试。":"Guide unavailable; retry later.");}
  }
  return <section aria-label={`${zh?"辅助模板信息":"Assisted template information"} ${item.title}`} className="mt-3 rounded-lg border border-border bg-primary/5 p-4 text-sm">
    <div className="flex flex-wrap items-center gap-2"><span className="font-medium">{zh?"辅助试用模板":"Assisted trial template"}</span><span className="rounded-full bg-surface px-2 py-1 text-xs">{label}</span></div>
    {item.production?<p className="mt-2 text-xs">{zh?"生产模型":"Production model"}: {item.production.model} · {item.production.review_status==="passed"?(zh?"独立会话静态审阅通过；应用运行另行验证":"Separate-session static review passed; application runtime is verified separately"):(zh?"静态审阅待核对":"Static review pending verification")}</p>:null}
    {!detail?<h4 className="mt-2 font-medium"><Link className="text-primary underline" to={`/factory?view=artifacts&artifact_id=${item.artifact_id}`}>{item.title}</Link></h4>:null}
    <dl className="mt-3 space-y-2 text-xs leading-6"><div><dt className="font-medium">{zh?"适用用户":"For whom"}</dt><dd>{item.scenario.audience}</dd></div><div><dt className="font-medium">{zh?"解决的问题":"Problem solved"}</dt><dd>{item.scenario.objective}</dd></div></dl>
    <p className="mt-3 text-xs font-medium">{zh?"核心能力":"Core capabilities"}</p><ul className="mt-1 list-disc space-y-1 pl-5 text-xs">{item.capabilities.map(x=><li key={x}>{x}</li>)}</ul>
    <details className="mt-3 text-xs"><summary className="cursor-pointer font-medium">{zh?"适用范围与已知限制":"Scope and known limits"}</summary><ul className="mt-2 list-disc space-y-1 pl-5">{item.limits.map((x,i)=><li key={i}>{x}</li>)}</ul></details>
    <div className="mt-3 space-y-2 text-xs"><p className="font-medium">{zh?"固定案例来源":"Pinned case sources"}</p>{item.cases.map(c=><div key={`${c.case_id}:${c.revision}`} className="break-words"><Link className="text-primary underline" to={`/apps?app_id=${encodeURIComponent(c.app_id)}&case_id=${encodeURIComponent(c.case_id)}&case_revision=${c.revision}`}>{zh?"回查共享案例":"Read shared case"} · r{c.revision}</Link>{c.sources.map(s=><p key={s.repository+s.commit_sha}><a className="text-primary underline" href={`${s.repository}/tree/${s.commit_sha}`} target="_blank" rel="noreferrer">{s.repository.replace("https://github.com/","")} @ {s.commit_sha.slice(0,12)}</a>{s.license_files.map(path=><a key={path} className="ml-2 text-primary underline" href={`${s.repository}/blob/${s.commit_sha}/${path}`} target="_blank" rel="noreferrer">{path}</a>)}</p>)}</div>)}</div>
    <p className="mt-3 text-xs leading-6">{item.runtime.scope}{item.runtime.recorded_date?` · ${zh?"验证记录日期":"Recorded"} ${item.runtime.recorded_date}`:""}</p>
    <p className="mt-1 text-xs leading-6 text-muted">{zh?"辅助运行记录与严格工厂验收分别记录；不代表正式发布、严格 G1/T08 通过或本机服务此刻在线。":"Assisted runtime records are separate from strict factory acceptance. They do not imply formal publication, strict G1/T08 success or a currently running local service."}</p>
    <div className="mt-3 flex flex-wrap gap-3 text-xs">{files.development?.available?<a className="text-primary underline" href={files.development.url}>{zh?"下载标准开发包":"Download standard development package"}</a>:<span role="status">{zh?"标准包暂不可用，请勿使用摘要不符的文件":"Standard package unavailable; do not use mismatched files"}</span>}{files.source?.available?<a className="text-primary underline" href={files.source.url}>{zh?"下载示例源码":"Download example source"}</a>:null}{files.evidence?.available?<a className="text-primary underline" href={files.evidence.url}>{zh?"查看运行证据文件":"Read runtime evidence file"}</a>:null}{files.guide?.available?<button className="text-primary underline" onClick={()=>void readGuide()}>{zh?"阅读应用使用说明":"Read application guide"}</button>:null}</div>
    {guideState?<p role="status" className="mt-2 text-xs">{guideState}</p>:null}{guide?<details open className="mt-3"><summary className="cursor-pointer">{zh?"应用使用说明":"Application guide"}</summary><div className="prose mt-3 max-h-96 overflow-auto text-xs"><ReactMarkdown remarkPlugins={[remarkGfm]}>{guide}</ReactMarkdown></div></details>:null}
    {detail?<details className="mt-4 text-xs"><summary className="cursor-pointer font-medium">{zh?"让 Codex 从这里开始":"Start with Codex"}</summary><p className="mt-2 text-muted">{zh?"先下载标准开发包，将解压目录交给新的开发上下文，再复制以下说明。":"Download the standard package, give its extracted directory to a new development context, then copy this instruction."}</p><textarea aria-label={zh?"Codex 开始说明":"Codex start instruction"} readOnly value={codexStart(item,zh)} rows={9} className="mt-2 w-full rounded-md border border-border bg-surface p-3 leading-6"/><Button variant="outline" size="sm" onClick={async()=>{try {await navigator.clipboard.writeText(codexStart(item,zh));setCopy(zh?"已复制":"Copied");}catch {setCopy(zh?"请在上方文本框中手动复制":"Select and copy the text above");}}}>{zh?"复制 Codex 开始说明":"Copy Codex instruction"}</Button><p role="status" className="mt-1">{copy}</p></details>:null}
  </section>;
}

export function AssistedTemplates({leaf,scenarioId,caseId,caseRevision}:{leaf?:string;scenarioId?:string;caseId?:string;caseRevision?:number}) {
  const {lang}=useLang();const zh=lang==="zh";
  const query=new URLSearchParams();if(leaf)query.set("leaf",leaf);if(scenarioId)query.set("scenario_id",scenarioId);if(caseId)query.set("case_id",caseId);if(caseRevision)query.set("case_revision",String(caseRevision));
  const result=useAsync(()=>factoryRequest<AssistedCatalog>(`assisted-templates?${query}`),[leaf,scenarioId,caseId,caseRevision]);
  return <section className="mt-6" aria-label={zh?"辅助试用模板目录":"Assisted trial catalog"}><h3 className="font-medium">{zh?"辅助试用模板":"Assisted trial templates"}</h3><p className="mt-2 text-xs leading-6 text-muted">{zh?"辅助生产，可阅读和导出使用；与正式发布区分开。":"Auxiliary production; available to read and export, separate from formal publication."}</p>{result.loading?<p className="mt-2 text-xs">{zh?"读取辅助模板…":"Loading assisted templates…"}</p>:result.error?<p role="status" className="mt-2 text-xs">{zh?"辅助目录暂不可用；正式发布区不受影响。":"Assisted catalog unavailable; formal publication is unaffected."}</p>:<>{result.data?.counts.total?<p className="mt-2 text-xs">{zh?`${result.data.counts.total} 份模板 · ${result.data.counts.core_verified} 份有核心运行示例 · ${result.data.counts.not_run} 份应用未运行`:`${result.data.counts.total} templates · ${result.data.counts.core_verified} core examples · ${result.data.counts.not_run} apps not run`}</p>:<p className="mt-2 text-xs text-muted">{zh?"此入口暂无辅助模板。":"No assisted templates for this entry."}</p>}{result.data?.items.map(item=><div key={item.artifact_id}><Link className="mt-3 inline-block text-xs text-primary underline" to={`/factory?view=artifacts&scenario_id=${item.scenario.id}`}>{zh?"查看此场景的模板":"Templates for this scenario"}: {item.scenario.name} · r{item.scenario.revision}</Link><AssistedTemplateSummary item={item} zh={zh}/></div>)}{result.data?.unavailable.length?<p role="status" className="mt-2 text-xs text-muted">{zh?"部分绑定版本暂不可读取；请恢复原制品后重试。":"Some pinned versions are unavailable; restore them before retrying."}</p>:null}</>}</section>;
}
