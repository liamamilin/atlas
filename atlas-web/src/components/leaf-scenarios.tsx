import { useState, type FormEvent } from "react";
import { Button } from "@/components/ui/button";
import { Link } from "react-router-dom";
import { useLang } from "@/lib/lang";
import { useAsync } from "@/components/loaders";
import { factoryRequest, type FactoryArtifact, type Scenario } from "@/lib/factory";

export function LeafScenarios({leaf}:{leaf:string}) {
  const {lang}=useLang();const zh=lang==="zh";
  const {data,error,loading}=useAsync(()=>factoryRequest<Scenario[]>(`catalog?leaf=${encodeURIComponent(leaf)}`),[leaf]);
  const templates=useAsync(()=>factoryRequest<FactoryArtifact[]>(`artifacts?leaf=${encodeURIComponent(leaf)}&published=1`),[leaf]);
  const scenarios=data?.filter(s=>s.status!=="archived")||[];
  return <section className="mt-6 rounded-xl border border-border p-5"><div className="flex flex-wrap items-center justify-between gap-3"><h2 className="font-serif text-xl font-medium">{zh?"应用场景与模板":"Scenarios and templates"}</h2><Link className="text-sm text-primary hover:underline" to={`/factory?leaf=${encodeURIComponent(leaf)}`}>{zh?"打开模板工厂":"Open template factory"} →</Link></div><p className="mt-2 text-sm leading-6 text-muted">{zh?"场景描述谁用这类软件完成什么事情；确认后的场景可以交给工厂生产模板。":"Scenarios describe who uses this software and why. Confirm a scenario to produce a reusable template."}</p>{loading?<p className="mt-3 text-xs text-subtle">{zh?"读取场景…":"Loading scenarios…"}</p>:error?<p className="mt-3 text-xs text-subtle">{zh?"场景服务暂不可用；请启动本地 API 后进入工厂重试。":"Scenarios are unavailable; start the local API and retry in the factory."}</p>:scenarios.length?<ul className="mt-3 space-y-2">{scenarios.map(s=><li key={s.id}><Link className="text-sm text-primary hover:underline" to={`/factory?leaf=${encodeURIComponent(leaf)}`}>{s.name}</Link><span className="ml-2 text-xs text-subtle">{s.status==="ready"?(zh?"已确认":"Confirmed"):(zh?"草案":"Draft")}</span><p className="mt-1 text-xs text-muted">{s.objective}</p></li>)}</ul>:<p className="mt-3 text-xs text-subtle">{zh?"还没有场景。可以在工厂添加，或通过 OpenCode 生成草案。":"No scenarios yet. Add one in the factory or generate proposals with OpenCode."}</p>}
    {templates.loading?<p className="mt-3 text-xs text-subtle">{zh?"读取已发布模板…":"Loading published templates…"}</p>:templates.error?<p className="mt-3 text-xs text-subtle">{zh?"已发布模板暂时无法读取，请稍后重试。":"Published templates are temporarily unavailable. Please retry later."}</p>:templates.data?.length?<div className="mt-5 space-y-3"><h3 className="font-medium">{zh?"已发布模板":"Published templates"}</h3>{templates.data.map(a=><PublishedTemplate key={a.id} artifact={a} zh={zh}/>)}</div>:<p className="mt-4 text-xs text-subtle">{zh?"此类型还没有已发布模板。生产完成后，可在工厂审阅并发布。":"No published templates for this type yet. Review and publish a candidate in the factory."}</p>}
    </section>;
}


function PublishedTemplate({artifact:a,zh}:{artifact:FactoryArtifact;zh:boolean}) {
  const meta=a as FactoryArtifact & {publication_status?:string;review_status?:string;runtime_reports?:Record<string,unknown>[]};
  const [name,setName]=useState("my-application");
  const [busy,setBusy]=useState(false);const [error,setError]=useState("");const [download,setDownload]=useState("");
  const runtime=a.acceptances?.filter(r=>r.method==="runtime-verification"||r.method==="blueprint-runtime")||[];
  const cognitive=a.artifact_type==="product-blueprint";
  async function submit(event:FormEvent) {
    event.preventDefault();setBusy(true);setError("");setDownload("");
    try {const result=await factoryRequest<{download_url:string}>(`artifacts/${a.id}/instantiate`,{project_name:name});setDownload(result.download_url);}
    catch(e){setError(String(e));}finally{setBusy(false);}
  }
  return <article className="rounded-lg bg-surface p-4"><h4 className="font-medium">{a.manifest.name}</h4><p className="mt-1 text-sm text-muted">{a.scenario_name} · {a.level}</p>
    {cognitive?<>
      <p className="mt-2 text-xs text-muted">{zh?"发布":"Publication"}: {meta.publication_status||a.state} · {zh?"认知审阅":"Cognitive review"}: {meta.review_status||"unknown"}</p>
      <p className="mt-2 text-xs text-muted">{zh?"开发交付按阶段导出；发布状态不代表目标应用已运行。":"Development is delivered as a selected phase package; publication does not mean the target application ran."}</p>
      <h5 className="mt-3 text-xs font-medium">{zh?"目标运行记录":"Target runtime reports"}</h5>
      {runtime.length?<ul className="mt-1 space-y-1 text-xs">{runtime.map((record,index)=><li key={record.id||index}>{record.scope} · {record.outcome} · {record.summary||record.error||""}</li>)}</ul>:<p className="mt-1 text-xs text-muted">{zh?"没有目标运行记录；未知状态会保持未知。":"No target runtime reports; an unknown status stays unknown."}</p>}
      {meta.runtime_reports?.length?<pre className="mt-2 max-h-40 overflow-auto whitespace-pre-wrap break-words text-[11px]">{JSON.stringify(meta.runtime_reports,null,2)}</pre>:null}
      <Link className="mt-3 inline-flex rounded-md border border-border px-3 py-2 text-xs text-primary hover:bg-bg-elevated" to={`/factory?view=artifacts&artifact_id=${encodeURIComponent(a.id)}`}>{zh?"查看认知包并选择阶段导出":"Open blueprint and choose a phase package"}</Link>
    </>:<>
      <p className="mt-2 text-xs text-muted">{runtime.some(record=>record.outcome==="passed")?(zh?"已通过运行验收；兼容范围请查看模板说明。":"Runtime acceptance passed; see the template documentation for supported environments."):(zh?"已通过 Harness 源码审阅，尚未通过运行验收。":"Harness source review passed; runtime acceptance has not passed.")}</p>
      <form className="mt-3 flex flex-wrap items-end gap-3" onSubmit={submit}><label className="text-xs">{zh?"应用名称":"Application name"}<input className="mt-1 block rounded-md border border-border bg-bg-elevated px-3 py-2 text-sm" aria-label={`${a.manifest.name} ${zh?"应用名称":"application name"}`} value={name} pattern="[a-z][a-z0-9-]{0,62}" required onChange={e=>{setName(e.target.value);setDownload("");}}/></label><Button type="submit" size="sm" disabled={busy}>{busy?(zh?"正在创建…":"Creating…"):(zh?"创建应用包":"Create application archive")}</Button></form>{error?<p className="mt-2 text-xs text-danger" role="alert">{error}</p>:null}{download?<p className="mt-3 text-xs" role="status"><a className="text-primary underline" href={download}>{zh?"下载应用包":"Download application"}</a> · {zh?"解压后按 README 启动，无需模型调用。":"Unzip and follow README; no model call needed."}</p>:null}
    </>}</article>;
}
