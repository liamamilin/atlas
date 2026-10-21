import { useAsync } from "@/components/loaders";
import { type AssistedCatalog } from "@/components/assisted-templates";
import { useEffect, useState, type FormEvent } from "react";
import { Link, useSearchParams } from "react-router-dom";
import { CheckCircle2, ChevronDown, Download, Factory as FactoryIcon, Plus, RefreshCw } from "lucide-react";
import { getMeta, type Meta } from "@/lib/atlas";
import { factoryRequest, scenarioReviewState, type FactoryArtifact, type FactoryBatch, type FactoryJob, type FactoryStatus, type Scenario } from "@/lib/factory";
import { useLang } from "@/lib/lang";
import { Button } from "@/components/ui/button";
import { EmptyState, Loading } from "@/components/loaders";
import { ScenarioGenerationPanel } from "@/components/scenario-generation-panel";
import { BlueprintCard, BlueprintImportPanel } from "@/components/blueprint-artifacts";
import { ScenarioReviewPanel } from "@/components/scenario-review-panel";
import { FactoryV1 } from "@/components/factory-v1";

const input = "mt-1.5 w-full rounded-md border border-border bg-bg-elevated px-3 py-2 text-sm outline-none focus:ring-2 focus:ring-primary/35";
const names: Record<string, [string,string]> = {
  draft:["草案","Draft"],ready:["已确认","Confirmed"],archived:["已归档","Archived"],
  queued:["排队中","Queued"],running:["运行中","Running"],paused:["已暂停","Paused"],cancelled:["已取消","Cancelled"],
  completed:["已完成","Completed"],failed:["失败","Failed"],interrupted:["已中断","Interrupted"],needs_attention:["需要处理","Needs attention"],needs_review:["验收待处理","Acceptance needs attention"],
  discovery:["发现候选","Discovery"],source:["固定开源版本","Pin source"],plan:["固定验收计划","Plan"],baseline:["验证上游","Baseline"],
  scenarios:["提出场景","Propose scenarios"],freeze:["冻结制品","Freeze"],verify:["实例化验收","Verify"],repair:["修复","Repair"],package:["打包","Package"],
  acceptance:["独立验收","Independent acceptance"],"harness-review":["Harness 审阅","Harness review"],"runtime-verification":["运行验收","Runtime acceptance"],passed:["通过","Passed"],blocked:["发现阻断问题","Blocked"],uncertain:["待确认","Uncertain"],unavailable:["环境不可用","Unavailable"],
  published:["已发布","Published"],withdrawn:["已下架","Withdrawn"],
  "blueprint-production":["认知模板生产","Cognitive production"],"blueprint-research":["品类调研","Category research"],"blueprint-generate":["生成认知规范","Generate cognitive specification"],"cognitive-review":["独立认知审阅","Independent cognitive review"],"blueprint-runtime":["独立应用运行验收","Independent application acceptance"],
  "blueprint-import":["导入认知模板","Import cognitive template"],
  "scenario-review":["场景独立审阅","Scenario review"],needs_changes:["需要修改","Needs changes"],rejected:["不建议采用","Not recommended"],
};

export function Factory() {
  const {lang} = useLang();
  const zh = lang === "zh";
  const [params] = useSearchParams();
  const focusedArtifactId = params.get("artifact_id");
  const focusedRuntimeId = params.get("runtime_run_id");
  const scenarioFilterId=params.get("scenario_id");
  const requestedView=params.get("view");
  const assisted=useAsync(()=>factoryRequest<AssistedCatalog>("assisted-templates"),[]);
  const caseFilterId = params.get("case_id");
  const caseFilterRevision = Number(params.get("case_revision")) || undefined;
  const [view,setView] = useState<"catalog"|"batches"|"artifacts"|"v1">(() => params.get("view") === "artifacts" ? "artifacts" : params.get("view") === "v1" || params.has("scenario") || params.has("plan") ? "v1" : "catalog");
  const [leaf,setLeaf] = useState(params.get("leaf") || "");
  const [meta,setMeta] = useState<Meta|null>(null);
  const [catalog,setCatalog] = useState<Scenario[]>([]);
  const [batches,setBatches] = useState<FactoryBatch[]>([]);
  const [artifacts,setArtifacts] = useState<FactoryArtifact[]>([]);
  const [artifactSearch,setArtifactSearch] = useState("");
  const [runtimeFilter,setRuntimeFilter]=useState("all");
  useEffect(()=>{if(requestedView==="artifacts"){setView("artifacts");setArtifactSearch("");setRuntimeFilter("all");}},[requestedView,scenarioFilterId]);
  const [status,setStatus] = useState<FactoryStatus|null>(null);
  const [selected,setSelected] = useState<string[]>([]);
  const [filter,setFilter] = useState("");
  const [expandedGroups,setExpandedGroups] = useState<Record<string,boolean>>({});
  const [model,setModel] = useState("");
  const [concurrency,setConcurrency] = useState(1);
  const [timeout,setTimeoutSeconds] = useState(900);
  const [source,setSource] = useState("");
  const [cognitionGuidance,setCognitionGuidance] = useState("");
  const [error,setError] = useState("");
  const [refreshError,setRefreshError]=useState("");
  const [notice,setNotice] = useState("");
  const [busy,setBusy] = useState(false);
  const [loaded,setLoaded] = useState(false);
  const [editing,setEditing] = useState<Scenario|null>(null);
  const [job,setJob] = useState<FactoryJob|null>(null);
  const [evidence,setEvidence] = useState<unknown|null>(null);
  const reviewAction = (scenario:Scenario) => {
    const action=scenarioReviewState(scenario).action;
    const actions:Record<string,[string,string]>={first:["发起场景审阅","Review scenario"],again:["重新审阅场景","Review scenario again"],retry:["重试场景审阅","Retry scenario review"],queued:["等待审阅","Review queued"],running:["审阅中","Reviewing"]};
    return actions[action][zh?0:1];
  };
  const label = (value:string) => names[value]?.[zh?0:1] || (value.startsWith("blueprint-spec-review-")?(zh?"认知规范预审":"Specification design review"):"") || (value.startsWith("blueprint-generate-")?(zh?"生成认知规范":"Generate cognitive specification"):"") || (value.startsWith("blueprint-code-")?(zh?"生成验收与参考文件":"Generate acceptance and reference files"):"") || (value.startsWith("generate-") ? (zh?"生成模板":"Generate") : value);

  async function load(signal?:AbortSignal) {
    const [scenarios,production,templates] = await Promise.all([
      factoryRequest<Scenario[]>("catalog",undefined,signal),
      factoryRequest<FactoryBatch[]>("batches",undefined,signal),
      factoryRequest<FactoryArtifact[]>("artifacts",undefined,signal),
    ]);
    setCatalog(scenarios);setBatches(production);setArtifacts(templates);setLoaded(true);setRefreshError("");
  }
  useEffect(()=>{
    const abort = new AbortController();
    let active=true;
    load(abort.signal).catch(e=>{if(active)setRefreshError(String(e));});
    getMeta().then(v=>{if(active)setMeta(v);}).catch(()=>{});
    factoryRequest<FactoryStatus>("status",undefined,abort.signal).then(v=>{
      if(!active)return;setStatus(v);
      setModel(current=>current || ["opencode-go/deepseek-v4.1-flash","opencode-go/longcat-2.5-preview-free"].find(m=>v.cli.models.includes(m)) || v.cli.models.find(m=>m.toLowerCase().includes("deepseek")&&m.toLowerCase().includes("flash")) || "");
    }).catch(e=>{if(active)setError(String(e));});
    return ()=>{active=false;abort.abort();};
  },[]);
  useEffect(()=>{
    const abort=new AbortController();let active=true;
    const tick=async()=>{try {await load(abort.signal);if(job){const next=await factoryRequest<FactoryJob>(`jobs/${job.id}`,undefined,abort.signal);if(active)setJob(next);}}catch(e){if(active)setRefreshError(zh?`刷新失败，保留最后一次结果：${String(e)}`:`Refresh failed; showing last result: ${String(e)}`);}};
    const timer=window.setInterval(()=>void tick(),4000);
    return()=>{active=false;abort.abort();window.clearInterval(timer);};
  },[job?.id,zh]);
  async function act(action:()=>Promise<unknown>, message?:string) {
    setBusy(true);setError("");setNotice("");
    try {await action();await load();if(message)setNotice(message);}catch(e){const code=(e as {code?:string})?.code;setError(zh&&code==="invalid_blueprint_archive"?"认知包无法读取，请选择完整有效的 ZIP 文件。":zh&&code==="blueprint_operation_unavailable"?"该操作不适用于认知模板；请使用阅读、阶段导出、独立审阅或修订。符合固定案例证据与审阅要求的版本可在 V1 工厂管理发布。":zh&&code==="scenario_already_generated"?"所选叶子已有场景或已完成调研，请刷新目录；需要补充时勾选允许补充生成。":zh&&code==="scenario_generation_active"?"所选叶子正在排队或生成，请在任务批次查看进度，勿重复提交。":String(e));}finally{setBusy(false);}
  }
  async function createBatch(kind:"blueprint-production"|"production"|"scenarios"|"scenario-review", reviewIds?:string[],generation?:{leaves:string[];skip_generated:boolean}) {
    const leaves=generation?.leaves||[];
    await act(async()=>{
      await factoryRequest("batches", {kind,name:kind==="blueprint-production"?(zh?"认知模板生产批次":"Cognitive production"):kind==="scenario-review"?(zh?"场景独立审阅":"Scenario review"):zh?(kind==="production"?"模板生产批次":"应用场景调研"):kind==="production"?"Template production":"Scenario discovery",model,
        concurrency,timeout,language:lang,...(generation?{skip_generated:generation.skip_generated}:{}),scenario_ids:reviewIds||catalog.filter(s=>selected.includes(s.id)&&(["production","blueprint-production"].includes(kind)?s.status==="ready":s.status!=="archived")).map(s=>s.id),leaves,source_url:kind==="blueprint-production"?"":source,...(kind==="blueprint-production"?{cognition_guidance:cognitionGuidance,acceptance_protocol:"atlas.acceptance-runner.v1"}:{}),
        scenario_revisions:Object.fromEntries(catalog.map(s=>[s.id,s.revision]))});
      setView("batches");setSelected([]);
    },zh?"批次已创建；关闭页面后仍会继续执行。":"Batch created; work continues after this page closes.");
  }
  const visible = catalog.filter(s=>(!leaf||s.leaf===leaf)&&(!filter||`${s.name} ${s.leaf_name} ${s.objective}`.toLowerCase().includes(filter.toLowerCase())));
  const visibleArtifacts = artifacts.filter(artifact => {
    if (artifactSearch && !`${artifact.manifest.name} ${artifact.scenario_name} ${artifact.leaf}`.toLowerCase().includes(artifactSearch.toLowerCase())) return false;
    if (focusedArtifactId && artifact.id !== focusedArtifactId) return false;
    if(runtimeFilter!=="all"&&!assisted.data?.items.some(i=>i.artifact_id===artifact.id&&i.runtime.status===runtimeFilter))return false;
    if(scenarioFilterId&&artifact.scenario_id!==scenarioFilterId&&!assisted.data?.items.some(i=>i.artifact_id===artifact.id&&i.scenario.id===scenarioFilterId))return false;
    if (!caseFilterId) return true;
    const provenance = artifact.provenance as FactoryArtifact["provenance"] & {case_basis?:{case_refs?:{case_id:string;revision:number}[]}};
    return !![...(provenance.case_basis?.case_refs||[]),...(provenance.shared_case_refs||[])].some(ref => ref.case_id === caseFilterId && (!caseFilterRevision || ref.revision === caseFilterRevision));
  });
  const groups = Array.from(visible.reduce((result,scenario)=>{
    const group=result.get(scenario.leaf);
    if(group)group.push(scenario);else result.set(scenario.leaf,[scenario]);
    return result;
  },new Map<string,Scenario[]>())).map(([slug,scenarios])=>{
    const type=meta?.leafIndex.find(item=>item.slug===slug);
    const name=zh?(type?.name_zh||scenarios[0].leaf_name):(type?.name||scenarios[0].leaf_name);
    return {slug,name,scenarios};
  }).sort((a,b)=>a.name.localeCompare(b.name,zh?"zh":"en"));
  const groupOpen=(slug:string)=>expandedGroups[slug]??(!!leaf||!!filter.trim()||groups.length===1);
  const hiddenSelected=selected.filter(id=>catalog.some(s=>s.id===id)&&!visible.some(s=>s.id===id)).length;
  const selectedReady=catalog.filter(s=>selected.includes(s.id)&&s.status==="ready").length;
  const reviewable=catalog.filter(s=>selected.includes(s.id)&&s.status!=="archived");
  return <main className="mx-auto max-w-6xl px-4 py-10">
    <p className="flex items-center gap-2 text-sm font-medium text-primary"><FactoryIcon className="size-4"/>{zh?"模板工厂":"Template factory"}</p>
    <h1 className="mt-2 font-serif text-3xl font-medium">{zh?"从应用场景，生产可创建应用的模板":"Turn application scenarios into reusable templates"}</h1>
    <p className="mt-3 max-w-3xl text-sm leading-6 text-muted">{zh?"叶子 + 应用场景构成生产目录。认知模板交付产品判断、阶段计划与开发验收，可在制品页阅读并导出开发包。已确认场景可交给 OpenCode 调研并生成认知包，冻结后自动排入独立认知审阅。旧代码模板生产仍可使用。":"A type and scenario define a catalog entry. Cognitive templates provide product decisions, phased plans and acceptance programs to read and export from Artifacts. Confirmed scenarios can be researched and turned into cognitive packages by OpenCode, then frozen and queued for independent cognitive review. Code-template production remains available."}</p>
    <div className="mt-5 flex flex-wrap gap-3 text-xs text-muted">
      <span>{status?`OpenCode CLI · ${status.cli.available?status.cli.version:zh?"不可用":"Unavailable"}`:zh?"检查 CLI…":"Checking CLI…"}</span>
      <span>{status?`Docker · ${status.runtime.available?(zh?"已就绪":"Ready"):(zh?"运行验收未就绪（不影响生产）":"Runtime unavailable (production still available)")}`:zh?"检查运行环境…":"Checking runtime…"}</span>
      <Button size="sm" variant="ghost" disabled={busy} onClick={()=>act(async()=>{setStatus(await factoryRequest<FactoryStatus>("status"));})}><RefreshCw className="size-3.5"/>{zh?"重新检查":"Check again"}</Button>
    </div>
    {error||refreshError?<div role="alert" className="mt-4 rounded-lg bg-danger/10 p-4 text-sm text-danger"><p>{error||refreshError}</p><button className="mt-2 underline" onClick={()=>act(()=>load())}>{zh?"重试加载":"Retry loading"}</button></div>:null}
    {notice?<p role="status" className="mt-4 rounded-lg bg-primary/10 p-4 text-sm text-primary">{notice}</p>:null}
    <nav role="tablist" aria-label={zh?"工厂视图":"Factory views"} className="mt-6 flex flex-wrap gap-2 border-b border-border pb-3">
      {([['catalog',zh?'生产目录':'Catalog'],['batches',zh?'任务批次':'Batches'],['artifacts',zh?'模板制品':'Artifacts'],['v1',zh?'V1 计划与预算':'V1 plan and budget']] as const).map(([key,title])=><Button key={key} role="tab" aria-selected={view===key} variant={view===key?"default":"outline"} onClick={()=>setView(key)}>{title}</Button>)}
    </nav>
    {view==="catalog"?<>
      <ScenarioGenerationPanel meta={meta} catalog={catalog} batches={batches} zh={zh} busy={busy} loaded={loaded} model={model} setModel={setModel} status={status} concurrency={concurrency} setConcurrency={setConcurrency} timeout={timeout} setTimeoutSeconds={setTimeoutSeconds} onGenerate={(leaves,skip_generated)=>createBatch("scenarios",undefined,{leaves,skip_generated})}/>
      <section className="mt-6 rounded-xl bg-surface p-5 shadow-card">
        <h2 className="mb-4 font-medium">{zh?"查看已有场景":"Browse existing scenarios"}</h2>
        <div className="grid gap-4 md:grid-cols-2">
          <label className="text-sm">{zh?"叶子类型":"Application type"}<select aria-label={zh?"叶子类型":"Application type"} className={input} value={leaf} onChange={e=>{setLeaf(e.target.value);setEditing(null);setExpandedGroups({});}}><option value="">{zh?"所有类型":"All types"}</option>{meta?.leafIndex.map(l=><option key={l.slug} value={l.slug}>{zh?l.name_zh||l.name:l.name}{catalog.some(s=>s.leaf===l.slug)?(zh?` · 已有 ${catalog.filter(s=>s.leaf===l.slug).length} 个场景`:` · ${catalog.filter(s=>s.leaf===l.slug).length} scenarios`):""}</option>)}</select></label>
          <label className="text-sm">{zh?"搜索场景":"Search scenarios"}<input className={input} value={filter} onChange={e=>{setFilter(e.target.value);setExpandedGroups({});}}/></label>
        </div>

      </section>
      <div className="mt-6 grid gap-6 lg:grid-cols-[minmax(0,1fr)_22rem]">
        <section className="min-w-0 space-y-3">
          <div className="flex flex-wrap items-center justify-between gap-2">
            <h2 className="font-serif text-xl font-medium">{zh?"应用场景":"Scenarios"}</h2>
            <span className="text-sm text-muted">{zh?`${groups.length} 个叶子 · ${visible.length} 个场景`:`${groups.length} types · ${visible.length} scenarios`}</span>
          </div>
          <p className="text-xs leading-5 text-muted">{zh?"Agent 审阅结论与场景状态分开记录：审阅通过的草案仍需你人工确认，确认后才可生产模板。":"Agent review and scenario status are separate: a passed draft still needs your confirmation before template production."}</p>
          {groups.length?<div className="flex flex-wrap gap-2"><Button size="sm" variant="ghost" onClick={()=>setExpandedGroups(Object.fromEntries(groups.map(g=>[g.slug,true])))}>{zh?"全部展开":"Expand all"}</Button><Button size="sm" variant="ghost" onClick={()=>setExpandedGroups(Object.fromEntries(groups.map(g=>[g.slug,false])))}>{zh?"全部收起":"Collapse all"}</Button></div>:null}
          <div className="flex flex-wrap gap-2"><Button size="sm" variant="outline" onClick={()=>setSelected(v=>Array.from(new Set([...v,...visible.filter(s=>s.status==="ready").map(s=>s.id)])))}>{zh?"选择当前已确认场景":"Select confirmed scenarios"}</Button><Button size="sm" variant="outline" onClick={()=>setSelected(v=>Array.from(new Set([...v,...visible.filter(s=>s.status!=="archived").map(s=>s.id)])))}>{zh?"选择当前可审阅场景":"Select reviewable scenarios"}</Button><Button size="sm" variant="ghost" onClick={()=>setSelected([])}>{zh?"清空选择":"Clear selection"}</Button></div>
          {selected.length?<p role="status" className="text-xs text-primary">{zh?`已选择 ${selected.length} 个场景，收起分组后仍保留选择。`:`${selected.length} scenarios selected; collapsing groups keeps your selection.`}{hiddenSelected?(zh?`其中 ${hiddenSelected} 个不在当前筛选结果中。`:` ${hiddenSelected} are outside the current filter.`):null}</p>:null}
          {!loaded&&!error?<Loading/>:null}
          {loaded&&!visible.length?<EmptyState title={zh?"这个目录还没有应用场景":"No application scenarios yet"}>{zh?"添加一个具体用户场景，或让 OpenCode 提出草案。确认场景后才会进入模板生产。":"Add a concrete scenario or ask OpenCode for proposals. Confirm a scenario before production."}</EmptyState>:null}
          {groups.map(group=>{
            const open=groupOpen(group.slug);
            const groupSelected=group.scenarios.filter(s=>selected.includes(s.id)).length;
            const reviewCounts=group.scenarios.reduce((counts,s)=>{const key=scenarioReviewState(s).status;counts[key]=(counts[key]||0)+1;return counts;},{} as Record<string,number>);
            const eligible=group.scenarios.filter(s=>s.status!=="archived").map(s=>s.id);
            return <section key={group.slug} aria-label={zh?`${group.name}的场景`:`Scenarios for ${group.name}`} className="overflow-hidden rounded-xl border border-border bg-surface shadow-card">
              <div className="p-4">
                <h3><button type="button" aria-expanded={open} aria-controls={`scenarios-${group.slug}`} onClick={()=>setExpandedGroups(v=>({...v,[group.slug]:!open}))} className="flex w-full items-center gap-3 rounded-md text-left focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary/35">
                  <ChevronDown aria-hidden="true" className={`size-4 shrink-0 text-primary transition-transform ${open?"":"-rotate-90"}`}/>
                  <span className="min-w-0 flex-1 font-medium">{group.name}</span>
                  <span className="shrink-0 text-xs text-muted">{zh?`${group.scenarios.length} 个场景`:`${group.scenarios.length} scenarios`}</span>
                </button></h3>
                <div className="mt-3 flex flex-wrap gap-x-3 gap-y-1 pl-7 text-xs text-muted">
                  {(["ready","draft","archived"] as const).map(state=>{
                    const count=group.scenarios.filter(s=>s.status===state).length;
                    return count?<span key={state}>{label(state)} {count}</span>:null;
                  })}
                  {groupSelected?<span className="font-medium text-primary">{zh?`已选 ${groupSelected}`:`${groupSelected} selected`}</span>:null}
                </div>
                <div className="mt-2 flex flex-wrap gap-x-3 gap-y-1 pl-7 text-xs" aria-label={zh?"Agent 审阅汇总":"Agent review summary"}>
                  <span className="text-muted">{zh?"Agent 审阅：":"Agent review:"}</span>
                  {([['passed',zh?'通过':'Passed'],['needs_changes',zh?'需修改':'Needs changes'],['rejected',zh?'不建议采用':'Not recommended'],['queued',zh?'排队中':'Queued'],['running',zh?'审阅中':'Reviewing'],['failed',zh?'未完成':'Incomplete'],['outdated',zh?'已过期':'Outdated'],['unreviewed',zh?'未审阅':'Not reviewed']] as const).map(([key,title])=>reviewCounts[key]?<span key={key} className={key==="passed"?"font-medium text-primary":"text-muted"}>{title} {reviewCounts[key]}</span>:null)}
                </div>
                <div className="mt-3 flex flex-wrap items-center gap-2 pl-7">
                  <Button size="sm" variant="outline" disabled={!eligible.length} onClick={()=>setSelected(v=>Array.from(new Set([...v,...eligible])))}>{zh?"选择本组可审阅场景":"Select reviewable in group"}</Button>
                  {groupSelected?<Button size="sm" variant="ghost" onClick={()=>setSelected(v=>v.filter(id=>!group.scenarios.some(s=>s.id===id)))}>{zh?"清空本组选择":"Clear group selection"}</Button>:null}
                  <Link className="text-xs text-primary hover:underline" to={`/types/${group.slug}`}>{zh?"查看叶子类型":"View application type"}</Link>
                </div>
              </div>
              <div id={`scenarios-${group.slug}`} hidden={!open} className="space-y-3 border-t border-border bg-bg-elevated p-3">
          {group.scenarios.map(s=><article key={s.id} className="rounded-lg border border-border bg-surface p-4">
            <div className="flex items-start justify-between gap-3"><div className="flex min-w-0 items-start gap-3"><input type="checkbox" className="mt-1" aria-label={`${zh?"选择":"Select"} ${s.name}`} disabled={s.status==="archived"} checked={selected.includes(s.id)} onChange={e=>setSelected(v=>e.target.checked?[...v,s.id]:v.filter(x=>x!==s.id))}/><div><h4 className="font-medium break-words">{s.name}</h4></div></div><span className="shrink-0 rounded-full bg-chip px-2 py-1 text-xs">{s.status==="draft"&&scenarioReviewState(s).current?.outcome==="passed"?(zh?"待人工确认":"Awaiting confirmation"):label(s.status)} · r{s.revision}</span></div>
            <p className="mt-3 text-sm text-muted">{s.audience} · {s.objective}</p>
            <details className="mt-3 text-xs text-muted"><summary className="cursor-pointer">{zh?"流程与验收条件":"Workflow and acceptance"}</summary><p className="mt-2">{s.workflow.join(" → ")}</p><ul className="mt-2 list-inside list-disc">{s.acceptance.map((x,i)=><li key={i}>{x}</li>)}</ul></details>
            <Button variant="ghost" size="sm" className="mt-2" onClick={()=>{setEditing(s);setLeaf(s.leaf);}}>{zh?"编辑 / 确认场景":"Edit / confirm"}</Button>
            <Button variant="outline" size="sm" className="mt-2" disabled={busy||!model||!status?.cli.available||s.status==="archived"||s.review_jobs?.some(j=>j.current&&["queued","running"].includes(j.state))} onClick={()=>createBatch("scenario-review",[s.id])}>{reviewAction(s)}</Button>
            <Link className="mt-3 inline-block text-xs text-primary underline" to={`/factory?view=artifacts&scenario_id=${s.id}`}>{zh?"查看此场景的模板":"Templates for this scenario"}</Link>
            <ScenarioReviewPanel scenario={s} zh={zh}/>
          </article>)}
              </div>
            </section>;
          })}
          <section className="rounded-xl border border-border p-5">
            <h2 className="font-medium">{zh?"审阅与模板生产":"Review and template production"}</h2>
            <label className="mt-3 block text-sm">{zh?"代码模板仓库（可选，认知生产不使用此项）":"Code-template repository (optional; unused by cognitive production)"}<input className={input} placeholder="https://github.com/owner/repository" value={source} onChange={e=>setSource(e.target.value)}/></label>
            <p className="mt-3 text-xs leading-5 text-muted">{zh?"模型调用和搜索可能计费。生成与审阅会发送叶子正文及同类型现有场景；已有覆盖充分时，可以不新增场景并说明原因。新草案自动排入独立审阅，每个场景额外调用一次模型；审阅只给建议，由你确认场景。模板生产使用已确认版本，生产无需 Docker；模板验收在制品页另行发起。":"Model calls and searches may incur charges. Generation and review send leaf documents and existing same-type scenarios; sufficient existing coverage can yield no additions with a reason. New drafts get an independent review, one extra model call per scenario. You confirm scenarios. Production uses confirmed versions; Docker is optional and template acceptance is requested separately."}</p>
            <label className="mt-3 block text-sm">{zh?"认知模板补充要求（可选）":"Cognitive production guidance (optional)"}<textarea className={input} aria-label={zh?"认知模板补充要求（可选）":"Cognitive production guidance (optional)"} aria-describedby="cognition-guidance-hint" maxLength={12000} value={cognitionGuidance} onChange={e=>setCognitionGuidance(e.target.value)} placeholder={zh?"必须支持的用户流程、已有决定，或上次规范预审的修订意见":"Required user journeys, existing decisions, or corrections from the previous design review"}/><span id="cognition-guidance-hint" className="mt-1 block text-xs leading-5 text-muted">{zh?"先预审规范，再生成验收文件；预审有阻断时，在此补充修订意见后重新生产；待确认项会保留，不自动阻止产码。补充要求会随所选场景发送给模型。":"Specifications are reviewed before programs are authored. If blocked, add corrections here and start a new production. Uncertainty is retained without automatically blocking programs. This guidance is sent to the selected model with the scene."}</span></label><p className="mt-3 text-xs leading-5 text-muted">{zh?"认知生产：调研 → 规范 → 独立规范预审 → 验收文件 → 冻结 → 独立认知审阅。会将所选叶子正文、已确认场景、公开调研资料及生成内容发送给所选模型，可能计费；只冻结候选，不自动发布或执行包内程序。":"Cognitive production: research → specification → independent design review → acceptance programs → freeze → independent cognitive review. Selected leaf documents, confirmed scenes, public research and generated content are sent to the selected model and may incur charges. Candidates are not published and their programs are not executed automatically."}</p><div className="mt-4 flex flex-wrap gap-2"><Button variant="outline" disabled={busy||!model||!reviewable.length||!status?.cli.available||reviewable.some(s=>s.review_jobs?.some(j=>j.current&&["queued","running"].includes(j.state)))} onClick={()=>createBatch("scenario-review")}>{zh?`审阅所选场景（${reviewable.length}）`:`Review selected (${reviewable.length})`}</Button><Button disabled={busy||!model||!selectedReady||!status?.cli.available} onClick={()=>createBatch("blueprint-production")}>{zh?`生产认知模板（${selectedReady}）`:`Produce cognitive templates (${selectedReady})`}</Button><Button variant="outline" disabled={busy||!model||!selectedReady||!status?.cli.available} onClick={()=>createBatch("production")}>{zh?`生产代码模板（${selectedReady}）`:`Produce code templates (${selectedReady})`}</Button></div>
          </section>
        </section>
        <ScenarioForm key={editing?.id||leaf||"new"} leaf={leaf} scenario={editing} zh={zh} busy={busy} onCancel={()=>setEditing(null)} onSave={(body)=>act(async()=>{await factoryRequest(editing?`scenarios/${editing.id}`:"scenarios",body);setEditing(null);},zh?"场景已保存":"Scenario saved")}/>
      </div>
    </>:null}
    {view==="batches"?<section className="mt-6 space-y-4">{!batches.length?<EmptyState title={zh?"还没有任务批次":"No batches yet"}>{zh?"先在生产目录选择场景，再启动生产。":"Select scenarios in the catalog to start production."}</EmptyState>:null}{batches.map(b=><article key={b.id} className="rounded-xl bg-surface p-5 shadow-card"><div className="flex flex-wrap justify-between gap-3"><div><h2 className="font-medium">{["harness-review","runtime-verification"].includes(b.config.kind)?label(b.config.kind):zh&&b.config.name.startsWith("Repair: ")?`修订：${b.config.name.slice(8)}`:b.config.name}</h2><p className="mt-1 break-all text-xs text-muted">{label(b.state)} · {b.config.model} · {zh?"并发":"Concurrency"} {b.config.concurrency}</p></div><div className="flex gap-2">{b.state!=="cancelled"?<><Button size="sm" variant="outline" disabled={busy} onClick={()=>act(()=>factoryRequest(`batches/${b.id}/${b.state==="paused"?"resume":"pause"}`,{}))}>{b.state==="paused"?(zh?"继续":"Resume"):(zh?"暂停新任务":"Pause queue")}</Button><Button size="sm" variant="ghost" disabled={busy} onClick={()=>{if(window.confirm(zh?"取消此批次的排队与运行任务？已有制品和证据会保留。":"Cancel queued and running jobs? Existing artifacts and evidence are retained."))void act(()=>factoryRequest(`batches/${b.id}/cancel`,{}));}}>{zh?"取消批次":"Cancel batch"}</Button></>:null}</div></div><div className="mt-4 space-y-2">{b.jobs.map(j=><div key={j.id} className="rounded-lg border border-border p-3"><div className="flex flex-wrap items-center justify-between gap-2"><div><p className="text-sm font-medium">{j.snapshot.scenario?.name||j.snapshot.leaf.name_zh||j.snapshot.leaf.name}</p><p className="mt-1 text-xs text-muted">{label(j.state)} · {label(j.stage)} · {zh?"尝试":"Attempt"} {j.attempt}</p></div><div className="flex gap-2"><Button size="sm" variant="ghost" onClick={()=>act(async()=>{setJob(await factoryRequest(`jobs/${j.id}`));setEvidence(null);})}>{zh?"详情":"Details"}</Button>{["failed","interrupted","needs_review"].includes(j.state)&&b.state!=="cancelled"?<Button size="sm" variant="outline" disabled={busy} onClick={()=>act(()=>factoryRequest(`jobs/${j.id}/retry`,{}))}>{zh?"从检查点重试":"Retry checkpoints"}</Button>:null}</div></div><GenerationResult job={j} zh={zh}/>{j.error?<p className="mt-2 break-words text-xs text-danger">{j.error}</p>:null}</div>)}</div></article>)}
      {job?<section className="rounded-xl border border-border p-5"><h2 className="font-medium">{zh?"任务详情":"Job details"} · {label(job.stage)}</h2><p className="mt-1 text-xs text-subtle">{job.id}</p><GenerationResult job={job} zh={zh}/><DesignReviews reviews={job.design_reviews} zh={zh}/><Button size="sm" variant="outline" className="mt-3" onClick={()=>act(async()=>{setEvidence(await factoryRequest(`jobs/${job.id}/evidence`));})}>{zh?"查看计划与验证证据":"View plan and verification evidence"}</Button><ol className="mt-4 space-y-2 text-xs text-muted">{job.events?.map(e=><li key={e.seq}>{new Date(e.at).toLocaleTimeString()} · {label(e.stage)} · {e.message}</li>)}</ol>{evidence?<pre className="mt-4 max-h-96 overflow-auto whitespace-pre-wrap break-words rounded-lg bg-bg-elevated p-3 text-xs">{JSON.stringify(evidence,null,2)}</pre>:null}</section>:null}
    </section>:null}
    {view==="artifacts"?<section className="mt-6 space-y-4"><BlueprintImportPanel zh={zh} busy={busy} act={act}/><label className="block text-sm">{zh?"查找模板":"Find templates"}<input aria-label={zh?"查找模板":"Find templates"} className={input} value={artifactSearch} onChange={e=>setArtifactSearch(e.target.value)} placeholder={zh?"模板名称、场景或叶子":"Name, scenario or leaf"}/></label>{assisted.data?<label className="block text-sm">{zh?"按辅助运行记录筛选":"Filter assisted runtime records"}<select className={input} value={runtimeFilter} onChange={e=>setRuntimeFilter(e.target.value)}><option value="all">{zh?"全部制品":"All artifacts"}</option><option value="core_verified">{zh?"辅助：已有核心运行示例":"Assisted: core example verified"}</option><option value="not_run">{zh?"辅助：应用未运行":"Assisted: application not run"}</option></select></label>:null}{assisted.data?<p className="text-xs text-muted">{zh?`辅助目录：${assisted.data.counts.total} 条记录${assisted.data.counts.usable!==undefined?` · ${assisted.data.counts.usable} 份可用 · ${assisted.data.counts.needs_revision??0} 份待修订历史`:""} · ${assisted.data.counts.core_verified} 份有核心运行示例 · ${assisted.data.counts.not_run} 份应用未运行；不代表严格验收通过。`:`Assisted catalog: ${assisted.data.counts.total} templates · ${assisted.data.counts.core_verified} core examples · ${assisted.data.counts.not_run} apps not run; separate from strict acceptance.`}</p>:null}{assisted.error?<p role="status" className="text-xs text-muted">{zh?"辅助目录信息暂不可用；原制品仍可阅读和导出。":"Assisted catalog unavailable; existing artifacts remain readable and exportable."}</p>:null}{scenarioFilterId?<p className="text-xs text-primary">{zh?"当前场景":"Selected scenario"}: {assisted.data?.items.find(i=>i.scenario.id===scenarioFilterId)?.scenario.name||scenarioFilterId} · <Link className="underline" to="/factory?view=artifacts">{zh?"查看全部模板":"Show all templates"}</Link></p>:null}{focusedArtifactId||caseFilterId?<p className="rounded-md bg-primary/10 p-3 text-xs">{zh?"已按链接筛选制品":"Artifacts filtered from your link"}: {focusedArtifactId||`${caseFilterId}${caseFilterRevision?` · r${caseFilterRevision}`:""}`} · <Link className="underline" to="/factory?view=artifacts">{zh?"查看全部制品":"Show all artifacts"}</Link></p>:null}{!loaded||(!!scenarioFilterId&&assisted.loading)?<p role="status" className="text-sm text-muted">{zh?"正在读取模板…":"Loading templates…"}</p>:!visibleArtifacts.length?<EmptyState title={zh?(artifacts.length?"没有匹配的制品":"还没有候选模板"):(artifacts.length?"No matching artifact":"No candidate templates yet")}>{zh?"生产完成后，冻结候选模板会出现在这里。可先下载，再选择审阅或运行验收。":"Frozen candidates appear here after production. Download them or choose independent source or runtime acceptance."}</EmptyState>:null}{visibleArtifacts.map(a=><div key={a.id} id={`factory-artifact-${a.id}`}>{a.artifact_type==="product-blueprint"?<BlueprintCard artifact={a} zh={zh} busy={busy} act={act} model={model} timeout={timeout} runtimeRunId={focusedRuntimeId} assistedInfo={assisted.data?.items.find(i=>i.artifact_id===a.id)}/>:<ArtifactCard artifact={a} zh={zh} busy={busy} act={act} label={label} model={model} runtimeAvailable={!!status?.runtime.available} timeout={timeout}/>}</div>)}</section>:null}
    {view==="v1"?<FactoryV1/>:null}
  </main>;
}

function DesignReviews({reviews,zh}:{reviews:FactoryJob["design_reviews"];zh:boolean}) {
  if(!reviews?.length)return null;
  return <section className="mt-4 space-y-2" aria-label={zh?"规范预审记录":"Specification design reviews"}><h3 className="text-sm font-medium">{zh?"规范预审：先检查用户流程与契约":"Design review: user journeys and contracts first"}</h3><p className="text-xs text-muted">{zh?"仅审阅规范草案；不代表验收程序或应用已运行。有阻断时请把意见补充到生产目录，再重新生产；待确认项会保留。":"Draft specification review only; no program or runtime acceptance. Add corrections in the catalog and produce again if blocked."}</p>{reviews.map(review=><details key={review.stage} className="rounded-lg border border-border p-3"><summary className="cursor-pointer text-sm">{review.outcome==="passed"?(zh?"预审通过":"Design passed"):review.outcome==="blocked"?(zh?"需要修订规范":"Specification needs revision"):(zh?"规范待确认":"Specification uncertain")}</summary><p className="mt-2 whitespace-pre-wrap text-sm">{review.summary}</p>{review.checks.map(check=><p key={check.dimension} className="mt-2 whitespace-pre-wrap text-xs text-muted">{check.reason}</p>)}{review.suggestions.length?<ul className="mt-2 list-disc space-y-1 pl-5 text-xs">{review.suggestions.map((suggestion,i)=><li key={i}>{suggestion}</li>)}</ul>:null}</details>)}</section>;
}

function GenerationResult({job,zh}:{job:FactoryJob;zh:boolean}) {
  const result=job.generation_result;
  if(!result)return null;
  return <div className="mt-2 rounded-md bg-primary/5 p-3 text-xs leading-5 text-muted">
    {job.snapshot.config.language?<p>{zh?"本批场景输出语言：":"Pinned output language: "}{job.snapshot.config.language==="zh"?(zh?"中文":"Chinese"):(zh?"英文":"English")}</p>:null}
    <p className="font-medium text-fg">{result.count===0?(zh?"未新增场景（已有覆盖或没有合适的独立场景）":"No new scenarios (existing coverage or no suitable distinct addition)"):(zh?`新增 ${result.count} 个草案，已排入独立审阅`:`${result.count} new drafts queued for independent review`)}</p>
    {result.reason?<p className="mt-1 whitespace-pre-wrap break-words">{result.reason}</p>:null}
  </div>;
}

function ScenarioForm({leaf,scenario,zh,busy,onCancel,onSave}:{leaf:string;scenario:Scenario|null;zh:boolean;busy:boolean;onCancel:()=>void;onSave:(body:unknown)=>Promise<void>}) {
  const [name,setName]=useState(scenario?.name||"");const [audience,setAudience]=useState(scenario?.audience||"");
  const [objective,setObjective]=useState(scenario?.objective||"");const [workflow,setWorkflow]=useState(scenario?.workflow.join("\n")||"");
  const [acceptance,setAcceptance]=useState(scenario?.acceptance.join("\n")||"");const [state,setState]=useState(scenario?.status||"draft");
  const submit=(e:FormEvent)=>{e.preventDefault();return onSave({leaf,name,audience,objective,workflow:workflow.split("\n").map(s=>s.trim()).filter(Boolean),acceptance:acceptance.split("\n").map(s=>s.trim()).filter(Boolean),status:state,expected_revision:scenario?.revision});};
  return <form className="h-fit rounded-xl bg-surface p-5 shadow-card" onSubmit={submit}><h2 className="flex items-center gap-2 font-medium"><Plus className="size-4"/>{scenario?(zh?"编辑应用场景":"Edit scenario"):(zh?"添加应用场景":"Add scenario")}</h2><p className="mt-2 text-xs leading-5 text-muted">{leaf?(zh?"描述谁在什么情况下完成什么事情，确认后成为生产目录项。":"Describe who does what and why; confirm it to enable production."):(zh?"先选择一个叶子类型。":"Select an application type first.")}</p>{([[zh?"场景名称":"Scenario name",name,setName],[zh?"目标用户":"Audience",audience,setAudience]] as const).map(([title,value,setter])=><label key={title} className="mt-4 block text-sm">{title}<input className={input} value={value} onChange={e=>setter(e.target.value)} required/></label>)}<label className="mt-4 block text-sm">{zh?"用户目标":"User objective"}<textarea className={input} value={objective} onChange={e=>setObjective(e.target.value)} required/></label><label className="mt-4 block text-sm">{zh?"核心流程（每行一步）":"Workflow (one step per line)"}<textarea className={input} value={workflow} onChange={e=>setWorkflow(e.target.value)} required/></label><label className="mt-4 block text-sm">{zh?"验收条件（每行一条）":"Acceptance (one criterion per line)"}<textarea className={input} value={acceptance} onChange={e=>setAcceptance(e.target.value)} required/></label><label className="mt-4 block text-sm">{zh?"场景状态":"Scenario status"}<select aria-label={zh?"场景状态":"Scenario status"} className={input} value={state} onChange={e=>setState(e.target.value as Scenario["status"])}><option value="draft">{zh?"草案，待人工确认":"Draft, awaiting confirmation"}</option><option value="ready">{zh?"已确认，可以生产":"Confirmed, ready to produce"}</option><option value="archived">{zh?"归档":"Archived"}</option></select></label><div className="mt-4 flex gap-2"><Button disabled={busy||!leaf} type="submit"><CheckCircle2 className="size-4"/>{zh?"保存场景":"Save scenario"}</Button>{scenario?<Button type="button" variant="ghost" onClick={onCancel}>{zh?"取消编辑":"Cancel editing"}</Button>:null}</div></form>;
}

function ArtifactCard({artifact:a,zh,busy,act,label,model,runtimeAvailable,timeout}:{artifact:FactoryArtifact;zh:boolean;busy:boolean;act:(action:()=>Promise<unknown>,message?:string)=>Promise<void>;label:(s:string)=>string;model:string;runtimeAvailable:boolean;timeout:number}) {
  const [name,setName]=useState("my-application");
  const [review,setReview]=useState("");
  const [level,setLevel]=useState(a.level === "L0" ? "L1" : a.level);
  const [download,setDownload]=useState("");
  const [repair,setRepair]=useState("");
  const [replan,setReplan]=useState(false);
  const acceptances=a.acceptances || [];
  const latest=(method:string)=>acceptances.find(r=>r.method===method);
  const pending=(method:string)=>a.acceptance_jobs?.find(j=>j.kind===method&&["queued","running"].includes(j.state));
  const acceptanceStatus=(method:string)=>pending(method)?label(pending(method)!.state):latest(method)?label(latest(method)!.outcome):(zh?"未执行":"Not requested");
  const canPublish=acceptances.some(r=>r.outcome==="passed");
  return <article className="rounded-xl bg-surface p-5 shadow-card">
    <div className="flex flex-wrap justify-between gap-3">
      <div><h2 className="font-serif text-xl font-medium">{a.manifest.name}</h2><p className="mt-1 text-xs text-muted">{a.level} · {label(a.state)} · {a.scenario_name} · r{a.scenario_revision}</p></div>
      <Button asChild variant="outline" size="sm"><a href={`/api/factory/artifacts/${a.id}/download`}><Download className="size-4"/>{zh?"下载模板":"Download template"}</a></Button>
    </div>
    <p className="mt-3 text-sm text-muted">{a.manifest.description}</p>
    <p className="mt-2 break-words text-xs text-subtle"><a href={a.provenance.repository} target="_blank" rel="noreferrer" className="text-primary underline">{a.provenance.repository}</a> · {a.provenance.commit?.slice(0,12)} · {a.provenance.license}</p>
    <div className="mt-4 rounded-lg border border-border p-4 text-sm">
      <p>{zh?"形式检查：结构与两组名称渲染通过（未运行应用）":"Formal checks: structure and two rendered names passed (application not executed)"}</p>
      <p className="mt-2">{zh?"Harness 审阅":"Harness review"}: {acceptanceStatus("harness-review")}</p>
      <p className="mt-2">{zh?"运行验收":"Runtime acceptance"}: {acceptanceStatus("runtime-verification")}</p>
      <p className="mt-2 text-xs leading-5 text-muted">{zh?"Harness 审阅只读取代码并给出范围内的结论。运行验收会在 Linux 容器中安装、启动并操作应用。两者独立排队，不影响生产。":"Harness review reads code and reports scoped findings. Runtime acceptance installs, starts and exercises the application in Linux containers. Both use a queue independent of production."}</p>
      <div className="mt-3 flex flex-wrap gap-2">
        <Button size="sm" disabled={busy||!model||!!pending("harness-review")} onClick={()=>act(()=>factoryRequest(`artifacts/${a.id}/accept`,{method:"harness-review",model,timeout,expected_digest:a.digest}),zh?"Harness 审阅已排队，可在任务批次查看。":"Harness review queued; view it in Batches.")}>{zh?"发起 Harness 审阅":"Request harness review"}</Button>
        <Button size="sm" variant="outline" disabled={busy||!runtimeAvailable||!!pending("runtime-verification")} onClick={()=>act(()=>factoryRequest(`artifacts/${a.id}/accept`,{method:"runtime-verification",timeout,expected_digest:a.digest}),zh?"运行验收已排队，可在任务批次查看。":"Runtime acceptance queued; view it in Batches.")}>{zh?"发起运行验收":"Request runtime acceptance"}</Button>
      </div>
      {!runtimeAvailable?<p className="mt-2 text-xs text-muted">{zh?"运行验收需要 Docker Desktop；模板生产、下载和 Harness 审阅可继续使用。":"Runtime acceptance needs Docker Desktop. Production, downloads and harness review remain available."}</p>:null}
      {acceptances.map(r=><details key={r.id} className="mt-3 text-xs"><summary className="cursor-pointer text-primary">{label(r.method)} · {label(r.outcome)} · {new Date(r.created_at).toLocaleString()}</summary><p className="mt-2">{r.scope}</p><pre className="mt-2 max-h-72 overflow-auto whitespace-pre-wrap break-words text-muted">{JSON.stringify(r,null,2)}</pre></details>)}
    </div>
    <details className="mt-3"><summary className="cursor-pointer text-xs text-primary">{zh?"冻结摘要与来源":"Frozen digest and provenance"}</summary><pre className="mt-2 max-h-80 overflow-auto whitespace-pre-wrap break-words text-xs text-muted">{JSON.stringify({digest:a.digest,provenance:a.provenance,formal_checks:a.formal_checks,review:a.review},null,2)}</pre></details>
    <div className="mt-5 grid gap-5 md:grid-cols-2">
      <section>
        <label className="text-sm">{zh?"创建应用名称":"New application name"}<input className={input} value={name} pattern="[a-z][a-z0-9-]{0,62}" onChange={e=>{setName(e.target.value);setDownload("");}}/></label>
        <Button className="mt-3" size="sm" disabled={busy||!name} onClick={()=>act(async()=>{const value=await factoryRequest<{download_url:string}>(`artifacts/${a.id}/instantiate`,{project_name:name});setDownload(value.download_url);},zh?"应用包已创建，无需模型调用；下载后按 README 启动。":"Application created without a model call; follow README after downloading.")}>{zh?"创建应用包":"Create application archive"}</Button>
        {download?<a className="ml-3 text-sm text-primary underline" href={download}>{zh?"下载应用":"Download application"}</a>:null}
        <p className="mt-2 text-xs text-muted">{zh?"L0 是冻结候选，尚未通过独立验收；试用时请核对当前验收记录。":"L0 is a frozen candidate awaiting independent acceptance. Check the recorded evidence before using it."}</p>
      </section>
      <section>
        <label className="text-sm">{zh?"审阅说明":"Review note"}<textarea className={input} value={review} onChange={e=>setReview(e.target.value)} placeholder={zh?"核对场景覆盖、来源与验收范围":"Review scenario coverage, provenance and acceptance scope"}/></label>
        <label className="mt-2 block text-xs">{zh?"发布等级":"Publication level"}<select aria-label={zh?"发布等级":"Publication level"} className={input} value={level} onChange={e=>setLevel(e.target.value)}><option value="L1">L1 · {zh?"可行，已通过至少一种独立验收":"Viable, one acceptance method passed"}</option><option value="L2">L2 · {zh?"标准，已人工复核完整性":"Standard, completeness manually reviewed"}</option></select></label>
        <div className="mt-3 flex gap-2"><Button size="sm" disabled={busy||!review.trim()||!canPublish} onClick={()=>act(()=>factoryRequest(`artifacts/${a.id}/review`,{action:"publish",review,level,expected_digest:a.digest}))}>{zh?"审阅并发布":"Review and publish"}</Button>{a.state==="published"?<Button size="sm" variant="outline" disabled={busy||!review.trim()} onClick={()=>act(()=>factoryRequest(`artifacts/${a.id}/review`,{action:"withdraw",review,expected_digest:a.digest}))}>{zh?"下架":"Withdraw"}</Button>:null}</div>
        {!canPublish?<p className="mt-2 text-xs text-muted">{zh?"发布前需 Harness 审阅或运行验收通过；不强制运行验收。":"Publication requires a passed harness review or runtime acceptance; runtime acceptance is optional."}</p>:null}
      </section>
    </div>
    <details className="mt-5 border-t border-border pt-4"><summary className="cursor-pointer text-sm text-primary">{zh?"根据问题生产修订版":"Produce a revision"}</summary><label className="mt-3 block text-sm">{zh?"修复要求":"Repair instructions"}<textarea className={input} value={repair} onChange={e=>setRepair(e.target.value)}/></label><label className="mt-3 flex items-start gap-2 text-sm"><input type="checkbox" checked={replan} onChange={e=>setReplan(e.target.checked)}/>{zh?"同时修订运行验收计划（仅用于计划或运行环境有误）":"Also revise the runtime acceptance plan (for plan or environment errors)"}</label><p className="mt-2 text-xs text-muted">{zh?"默认沿用冻结计划修复源码；勾选后重新生成技术检查，业务场景与验收条件保持原版本。":"Source repairs keep the frozen plan by default. Selecting this regenerates technical checks while retaining the original scenario and acceptance criteria."}</p><p className="mt-2 text-xs text-muted">{zh?"保留当前冻结版本与验收证据，创建新的生产任务和候选模板，再单独送验。":"Keep this frozen version and its evidence. A new production job creates a revised candidate for separate acceptance."}</p><Button className="mt-3" size="sm" variant="outline" disabled={busy||!repair.trim()} onClick={()=>act(()=>factoryRequest(`artifacts/${a.id}/repair`,{expected_digest:a.digest,note:repair,replan}),zh?"修订生产已排队，原制品保留。":"Revision queued; original artifact retained.")}>{zh?"生产修订版":"Produce revision"}</Button></details>
  </article>;
}
