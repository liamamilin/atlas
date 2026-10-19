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
    {templates.loading?<p className="mt-3 text-xs text-subtle">{zh?"读取已发布模板…":"Loading published templates…"}</p>:templates.error?<p className="mt-3 text-xs text-subtle">{zh?"已发布模板暂时无法读取，请稍后重试。":"Published templates are temporarily unavailable. Please retry later."}</p>:templates.data?.length?<div className="mt-5 space-y-3"><h3 className="font-medium">{zh?"从已发布模板创建应用":"Create from a published template"}</h3>{templates.data.map(a=><PublishedTemplate key={a.id} artifact={a} zh={zh}/>)}</div>:<p className="mt-4 text-xs text-subtle">{zh?"此类型还没有已发布模板。生产完成后，可在工厂审阅并发布。":"No published templates for this type yet. Review and publish a candidate in the factory."}</p>}
    </section>;
}


function PublishedTemplate({artifact:a,zh}:{artifact:FactoryArtifact;zh:boolean}) {
  const [name,setName]=useState("my-application");
  const [busy,setBusy]=useState(false);const [error,setError]=useState("");const [download,setDownload]=useState("");
  const runtime=a.acceptances?.some(r=>r.method==="runtime-verification"&&r.outcome==="passed");
  async function submit(event:FormEvent) {
    event.preventDefault();setBusy(true);setError("");setDownload("");
    try {const result=await factoryRequest<{download_url:string}>(`artifacts/${a.id}/instantiate`,{project_name:name});setDownload(result.download_url);}
    catch(e){setError(String(e));}finally{setBusy(false);}
  }
  return <article className="rounded-lg bg-surface p-4"><h4 className="font-medium">{a.manifest.name}</h4><p className="mt-1 text-sm text-muted">{a.scenario_name} · {a.level}</p><p className="mt-2 text-xs text-muted">{runtime?(zh?"已通过运行验收；兼容范围请查看模板说明。":"Runtime acceptance passed; see the template documentation for supported environments."):(zh?"已通过 Harness 源码审阅，尚未通过运行验收。":"Harness source review passed; runtime acceptance has not passed.")}</p><form className="mt-3 flex flex-wrap items-end gap-3" onSubmit={submit}><label className="text-xs">{zh?"应用名称":"Application name"}<input className="mt-1 block rounded-md border border-border bg-bg-elevated px-3 py-2 text-sm" aria-label={`${a.manifest.name} ${zh?"应用名称":"application name"}`} value={name} pattern="[a-z][a-z0-9-]{0,62}" required onChange={e=>{setName(e.target.value);setDownload("");}}/></label><Button type="submit" size="sm" disabled={busy}>{busy?(zh?"正在创建…":"Creating…"):(zh?"创建应用包":"Create application archive")}</Button></form>{error?<p className="mt-2 text-xs text-danger" role="alert">{error}</p>:null}{download?<p className="mt-3 text-xs" role="status"><a className="text-primary underline" href={download}>{zh?"下载应用包":"Download application"}</a> · {zh?"解压后按 README 启动，无需模型调用。":"Unzip and follow README; no model call needed."}</p>:null}</article>;
}
