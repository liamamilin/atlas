import {useState} from "react";
import type {Meta} from "@/lib/atlas";
import type {FactoryBatch, FactoryStatus, Scenario} from "@/lib/factory";
import {Button} from "@/components/ui/button";

const input="mt-1.5 w-full rounded-md border border-border bg-bg-elevated px-3 py-2 text-sm outline-none focus:ring-2 focus:ring-primary/35";

export function ScenarioGenerationPanel({meta,catalog,batches,zh,busy,loaded,model,setModel,status,concurrency,setConcurrency,timeout,setTimeoutSeconds,onGenerate}:{
  meta:Meta|null;catalog:Scenario[];batches:FactoryBatch[];zh:boolean;busy:boolean;loaded:boolean;
  model:string;setModel:(value:string)=>void;status:FactoryStatus|null;
  concurrency:number;setConcurrency:(value:number)=>void;timeout:number;setTimeoutSeconds:(value:number)=>void;
  onGenerate:(leaves:string[],skipGenerated:boolean)=>Promise<void>;
}) {
  const [search,setSearch]=useState("");
  const [coverage,setCoverage]=useState("new");
  const [selection,setSelection]=useState<string[]>([]);
  const [allowGenerated,setAllowGenerated]=useState(false);
  const counts=new Map<string,number>();
  catalog.forEach(s=>counts.set(s.leaf,(counts.get(s.leaf)||0)+1));
  const completed=new Set<string>();const active=new Set<string>();
  batches.forEach(b=>b.jobs.forEach(j=>{
    if(j.kind!=="scenarios")return;
    if(j.state==="completed")completed.add(j.snapshot.leaf.slug);
    if(b.state!=="cancelled"&&["queued","running"].includes(j.state))active.add(j.snapshot.leaf.slug);
  }));
  const generated=(slug:string)=>counts.has(slug)||completed.has(slug);
  const eligible=(slug:string)=>!active.has(slug)&&(allowGenerated||!generated(slug));
  const types=meta?.leafIndex||[];
  const matching=types.filter(l=>{
    const matches=`${l.name} ${l.name_zh||""} ${l.slug}`.toLowerCase().includes(search.trim().toLowerCase());
    return matches&&(coverage==="all"||(coverage==="new"?!generated(l.slug)&&!active.has(l.slug):coverage==="generated"?generated(l.slug):active.has(l.slug)));
  });
  const chosen=selection.filter(slug=>types.some(t=>t.slug===slug)&&eligible(slug));
  const stale=selection.length-chosen.length;
  const covered=types.filter(t=>generated(t.slug)).length;
  const pending=types.filter(t=>active.has(t.slug)).length;
  const missing=types.filter(t=>!generated(t.slug)&&!active.has(t.slug)).length;
  const ready=loaded&&!!meta;
  return <section aria-label={zh?"生成应用场景":"Generate application scenarios"} className="mt-6 rounded-xl bg-surface p-5 shadow-card">
    <div className="flex flex-wrap items-center justify-between gap-3"><h2 className="font-serif text-xl font-medium">{zh?"生成应用场景":"Generate application scenarios"}</h2><Button disabled={busy||!ready||!model||!chosen.length||!status?.cli.available} onClick={()=>onGenerate(chosen,!allowGenerated)}>{zh?`生成场景草案（${chosen.length} 类型）`:`Propose scenarios (${chosen.length} types)`}</Button></div>
    <p className="mt-2 text-sm leading-6 text-muted">{zh?"选择叶子 → 生成场景草案 → 自动独立审阅。建议每批 1–3 个叶子；审阅后由你确认。":"Select types → Generate drafts → Automatic independent review. Start with 1–3 types per batch; you confirm the results."}</p>
    <p className="mt-2 text-xs text-primary">{ready?(zh?`已覆盖 / 已调研 ${covered} · 未生成 ${missing} · 生成中 ${pending}`:`Covered / researched ${covered} · Not generated ${missing} · In progress ${pending}`):(zh?"正在加载叶子与生产记录…":"Loading types and production history…")}</p>
    <div className="mt-4 grid gap-3 sm:grid-cols-2">
      <label className="text-sm">{zh?"搜索生产叶子":"Search types to generate"}<input className={input} value={search} onChange={e=>setSearch(e.target.value)}/></label>
      <label className="text-sm">{zh?"场景生成状态":"Scenario generation status"}<select aria-label={zh?"场景生成状态":"Scenario generation status"} className={input} value={coverage} onChange={e=>setCoverage(e.target.value)}>
        <option value="new">{zh?"未生成（默认）":"Not generated (default)"}</option><option value="generated">{zh?"已有场景 / 已调研":"Has scenarios / Researched"}</option><option value="active">{zh?"生成中 / 排队中":"Generating / Queued"}</option><option value="all">{zh?"全部叶子":"All types"}</option>
      </select></label>
    </div>
    <label className="mt-3 flex items-start gap-2 text-xs leading-5 text-muted"><input type="checkbox" className="mt-1" checked={allowGenerated} onChange={e=>setAllowGenerated(e.target.checked)}/>{zh?"允许为已有场景或已调研叶子补充生成（会再次调用模型）":"Allow additional generation for covered or researched types (calls the model again)"}</label>
    <div className="mt-3 flex flex-wrap items-center gap-2">
      <Button size="sm" variant="outline" disabled={!ready||!matching.some(l=>eligible(l.slug))} onClick={()=>setSelection(v=>Array.from(new Set([...v,...matching.filter(l=>eligible(l.slug)).slice(0,3).map(l=>l.slug)])))}>{zh?"选择当前结果前 3 个可生产叶子":"Select first 3 eligible types"}</Button>
      <Button size="sm" variant="ghost" onClick={()=>setSelection([])}>{zh?"清空叶子选择":"Clear type selection"}</Button>
      <span className="text-xs text-muted">{zh?`${matching.length} 个匹配叶子`:`${matching.length} matching types`}</span>
    </div>
    <div className="mt-3 max-h-44 space-y-2 overflow-auto rounded-lg border border-border p-3" aria-label={zh?"生产叶子列表":"Production type list"}>
      {ready&&!matching.length?<p className="text-sm text-muted">{zh?"没有匹配叶子，试试其他关键词或生成状态。":"No matching types. Try a different search or generation status."}</p>:null}
      {matching.map(l=><label key={l.slug} className="flex items-start gap-2 text-sm">
        <input type="checkbox" className="mt-1" aria-label={`${zh?"选择叶子":"Select type"} ${zh?l.name_zh||l.name:l.name}`} disabled={!ready||!eligible(l.slug)} checked={selection.includes(l.slug)} onChange={e=>setSelection(v=>e.target.checked?Array.from(new Set([...v,l.slug])):v.filter(slug=>slug!==l.slug))}/>
        <span className="min-w-0 flex-1">{zh?l.name_zh||l.name:l.name}</span>
        <span className="shrink-0 text-xs text-muted">{active.has(l.slug)?(zh?"生成中 / 排队中":"Generating / Queued"):counts.has(l.slug)?(zh?`已有 ${counts.get(l.slug)} 个场景`:`${counts.get(l.slug)} scenarios`):completed.has(l.slug)?(zh?"已调研，暂无场景":"Researched, no scenarios"):(zh?"未生成":"Not generated")}</span>
      </label>)}
    </div>
    <p className="mt-3 break-words text-xs leading-5 text-primary">{zh?`本批已选 ${chosen.length} 个叶子`:`${chosen.length} types selected for this batch`}{chosen.length?`：${chosen.map(slug=>{const t=types.find(l=>l.slug===slug)!;return zh?t.name_zh||t.name:t.name;}).join(zh?"、":", ")}`:null}</p>
    {stale?<p className="mt-1 text-xs text-muted">{zh?`${stale} 个选择已有场景或正在生成，本次会跳过。`:`${stale} selected types are already covered or active and will be skipped.`}</p>:null}
    <label className="mt-3 block text-sm">{zh?"OpenCode 模型（provider/model）":"OpenCode model (provider/model)"}<input className={input} list="factory-models" placeholder="provider/model" value={model} onChange={e=>setModel(e.target.value)}/><datalist id="factory-models">{status?.cli.models.map(m=><option key={m} value={m}/>)}</datalist></label>
    <p className="mt-2 text-xs text-muted">{zh?"场景输出语言：中文（随当前界面语言）":"Scenario output language: English (follows the current interface)"}</p>
    <details className="mt-3 text-sm"><summary className="cursor-pointer text-primary">{zh?"并发与超时设置":"Concurrency and timeout"}</summary><div className="mt-2 grid grid-cols-2 gap-3">
      <label className="text-xs">{zh?"并发任务":"Concurrency"}<input className={input} type="number" min={1} max={8} value={concurrency} onChange={e=>setConcurrency(Number(e.target.value))}/></label>
      <label className="text-xs">{zh?"阶段超时（秒）":"Stage timeout (s)"}<input className={input} type="number" min={30} max={7200} value={timeout} onChange={e=>setTimeoutSeconds(Number(e.target.value))}/></label>
    </div></details>
    <div className="mt-4 text-xs text-muted"><span>{zh?"草案生成后自动独立审阅；模型调用可能计费。":"Drafts receive an independent review automatically; model calls may incur charges."}</span></div>
  </section>;
}
