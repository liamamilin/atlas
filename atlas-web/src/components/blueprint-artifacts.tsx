import {useState} from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import {Download, BookOpen} from "lucide-react";
import {Button} from "@/components/ui/button";
import {factoryRequest, type FactoryArtifact} from "@/lib/factory";

const input="mt-1.5 w-full rounded-md border border-border bg-bg-elevated px-3 py-2 text-sm outline-none focus:ring-2 focus:ring-primary/35";
type Act=(action:()=>Promise<unknown>,message?:string)=>Promise<void>;
interface BlueprintDetails {
  digest:string;
  runtime_acceptance?:FactoryArtifact["runtime_acceptance"];
  documents:Record<string,string>;
  spec:{
    phases:{id:string;title:string;goal:string;features:string[];acceptance:string[]}[];
    decisions:{id:string;question:string;default:string;when_to_ask:string;impact:string}[];
    features:{id:string;name:string;phase:string|null;applicability:string;reason:string}[];
    sources:{id:string;name:string;url:string;version:string;license:string;reuse:string}[];
    evidence:{kind:string;path:string;scope:string}[];
  };
}

export function BlueprintImportPanel({zh,busy,act}:{zh:boolean;busy:boolean;act:Act}) {
  const [file,setFile]=useState<File|null>(null);
  const [error,setError]=useState("");
  async function importFile(){
    setError("");
    if(!file||file.size>1024*1024){setError(zh?"请选择不超过 1 MiB 的认知模板 ZIP。":"Choose a cognitive ZIP up to 1 MiB.");return;}
    await act(async()=>{
      const data=await new Promise<string>((resolve,reject)=>{
        const reader=new FileReader();
        reader.onerror=()=>reject(new Error(zh?"无法读取文件，请重新选择。":"Unable to read file; choose it again."));
        reader.onload=()=>resolve(String(reader.result).split(",")[1]);reader.readAsDataURL(file);
      });
      await factoryRequest("blueprints/import",{archive_base64:data});
    },zh?"认知包已校验并冻结；重复导入会复用同一制品。":"Cognitive package checked and frozen; duplicate imports reuse the same artifact.");
  }
  return <section aria-label={zh?"认知模板入口":"Cognitive template entry"} className="rounded-xl border border-border bg-surface p-5 shadow-card">
    <h2 className="font-medium">{zh?"认知模板：先把产品想清楚，再交给开发 agent":"Cognitive templates: define the product before development"}</h2>
    <p className="mt-2 max-w-3xl text-sm leading-6 text-muted">{zh?"包含品类认知、产品定义、架构决策、阶段路线图、验收程序与 Agent 指令。先查看已验证的书签样板，或导入同一协议的认知包；自动生产请在生产目录选择已确认场景。":"Includes category research, product definition, architecture, roadmap, acceptance programs and agent instructions. Start with the bookmark sample or import a compatible package. For automatic production, select confirmed scenarios in Catalog."}</p>
    <Button className="mt-3" size="sm" variant="outline" disabled={busy} onClick={()=>act(()=>factoryRequest("blueprints/sample",{}),zh?"书签认知样板已加入制品；没有调用模型或执行包内代码。":"Bookmark cognition sample added; no model calls or package code executed.")}>{zh?"载入书签认知样板":"Load bookmark cognition sample"}</Button>
    <details className="mt-4 text-sm"><summary className="cursor-pointer text-primary">{zh?"导入其他认知包":"Import another cognitive package"}</summary>
      <label className="mt-3 block">{zh?"认知模板 ZIP":"Cognitive template ZIP"}<input type="file" accept=".zip,application/zip" className={input} disabled={busy} onChange={e=>{setFile(e.target.files?.[0]||null);setError("");}}/></label>
      <p className="mt-2 text-xs leading-5 text-muted">{zh?"支持 atlas.product-blueprint.v0，ZIP 根目录需有 template.json 与 integrity.json。压缩包上限 1 MiB，展开上限 8 MiB；导入只检查结构、引用和摘要，不执行脚本，也不将包内报告认定为工厂验收。":"Supports atlas.product-blueprint.v0 with template.json and integrity.json at ZIP root. Limits: 1 MiB compressed, 8 MiB expanded. Import checks structure, references and hashes; scripts do not run and bundled reports are not factory acceptance."}</p>
      <Button className="mt-3" size="sm" disabled={busy||!file} onClick={()=>void importFile()}>{zh?"校验并导入":"Validate and import"}</Button>
      {error?<p role="alert" className="mt-2 text-sm text-danger">{error}</p>:null}
    </details>
  </section>;
}

export function BlueprintCard({artifact:a,zh,busy,act,model,timeout,runtimeRunId}:{artifact:FactoryArtifact;zh:boolean;busy:boolean;act:Act;model:string;timeout:number;runtimeRunId?:string|null}) {
  const [details,setDetails]=useState<BlueprintDetails|null>(null);
  const [project,setProject]=useState("my-application");
  const [phase,setPhase]=useState(a.manifest.phases?.[0]?.id||"");
  const [download,setDownload]=useState("");
  const [repair,setRepair]=useState("");
  const [runtimeFile,setRuntimeFile]=useState<File|null>(null);
  const [runtimeConsent,setRuntimeConsent]=useState(false);
  const reviewJob=a.acceptance_jobs?.find(j=>j.kind==="cognitive-review"&&["queued","running"].includes(j.state));
  const review=a.acceptances?.find(r=>r.method==="cognitive-review");
  const reviewLabels:Record<string,[string,string]>={queued:["排队中","Queued"],running:["审阅中","Reviewing"],passed:["范围内通过","Passed within scope"],blocked:["需修改","Needs changes"],uncertain:["待确认","Uncertain"],unavailable:["未完成","Incomplete"]};
  const lastReviewJob=a.acceptance_jobs?.find(j=>j.kind==="cognitive-review");
  const runtimeJob=a.acceptance_jobs?.find(j=>j.kind==="blueprint-runtime"&&["queued","running"].includes(j.state));
  const runtimeResults=a.acceptances?.filter(r=>r.method==="blueprint-runtime")||[];
  const runtimeLabels:Record<string,[string,string]>={passed:["通过","Passed"],failed:["失败","Failed"],blocked:["阻断","Blocked"],unavailable:["不可用","Unavailable"],not_run:["未运行","Not run"],aborted:["已中止","Aborted"],unverified:["未核实","Unverified"],queued:["排队中","Queued"],running:["运行中","Running"]};
  const runtimeStatus=(value:string)=>runtimeLabels[value]?.[zh?0:1]||value;
  const incomplete=review?.outcome==="unavailable"||(lastReviewJob&&["failed","interrupted","cancelled"].includes(lastReviewJob.state)&&lastReviewJob.id!==review?.job_id);
  const reviewState=reviewJob?.state||(incomplete?"unavailable":review?.outcome);
  const dimensions:Record<string,[string,string]>={category_evidence:["品类依据","Category evidence"],scenario_scope:["场景范围","Scenario scope"],product_completeness:["产品完整性","Product completeness"],architecture_contract:["架构与契约","Architecture and contracts"],phase_acceptance:["阶段与验收","Phases and acceptance"],decisions_defaults:["决策与默认值","Decisions and defaults"],agent_handoff:["开发交接","Agent handoff"],evidence_honesty:["验证声明","Evidence claims"]};
  const [document,setDocument]=useState("PRODUCT.md");
  const names:Record<string,[string,string]>={"README.md":["开始使用","Getting started"],"CATEGORY.md":["品类认知","Category research"],"PRODUCT.md":["产品定义","Product definition"],"ARCHITECTURE.md":["架构与契约","Architecture and contracts"],"DECISIONS.md":["默认决策","Default decisions"],"ROADMAP.md":["阶段路线图","Roadmap"],"AGENT.md":["Agent 指令","Agent instructions"],"VALIDATION.md":["包内验证说明（声明）","Bundled validation claims"]};
  const validName=/^[a-z][a-z0-9-]{0,62}$/.test(project);
  const publicationLabel=a.state==="published"?(zh?"正式目录已发布":"Published in catalog"):a.state==="withdrawn"?(zh?"已撤回目录":"Withdrawn from catalog"):(zh?"已冻结候选":"Frozen candidate");
  return <article aria-label={`${zh?"认知模板":"Cognitive template"} ${a.manifest.name}`} className="rounded-xl bg-surface p-5 shadow-card">
    <div className="flex flex-wrap justify-between gap-3"><div><p className="text-xs font-medium text-primary">{zh?`认知模板 · ${publicationLabel}`:`Cognitive template · ${publicationLabel}`} · v{a.manifest.version}</p><h2 className="mt-1 font-serif text-xl font-medium">{a.manifest.name}</h2><p className="mt-1 text-xs text-muted">{a.scenario_name} · r{a.scenario_revision}</p></div><Button asChild size="sm" variant="outline"><a href={`/api/factory/artifacts/${a.id}/download`}><Download className="size-4"/>{zh?"下载冻结包":"Download frozen bundle"}</a></Button></div>
    <p className="mt-3 text-sm text-muted">{a.manifest.description}</p>
    <p className="mt-3 text-sm">{zh?`${a.manifest.feature_count} 项能力 · ${a.manifest.decision_count} 个决策 · ${a.manifest.phase_count} 个阶段 · ${a.manifest.acceptance_count} 个验收用例`:`${a.manifest.feature_count} capabilities · ${a.manifest.decision_count} decisions · ${a.manifest.phase_count} phases · ${a.manifest.acceptance_count} acceptance cases`}</p>
    <p className="mt-3 rounded-lg bg-primary/5 p-3 text-xs leading-5 text-muted">{zh?"冻结检查覆盖结构、引用、阶段映射与文件摘要，本身不执行包内程序。包内报告作为来源声明保留，不等于工厂重新验收；工厂独立审阅和每个下游目标的运行结果分别记录。符合当前审阅与固定案例证据要求的模板，可在 V1 工厂中管理目录发布。":"Freezing checks structure, references, phase mappings and hashes without running package programs. Bundled reports remain source claims, not fresh factory acceptance; independent review and each downstream runtime target are recorded separately. Templates that meet current review and fixed case-evidence requirements can be published through the V1 factory."}</p>
    <section aria-label={zh?"完整认知库":"Full knowledge"} className="mt-4 rounded-lg border border-border p-4 text-sm">
      <h3 className="font-medium">{zh?"1. 完整认知库":"1. Full knowledge"}</h3>
      <p className="mt-2 text-xs leading-5 text-muted">{zh?"查看已冻结章节，或下载包含完整 blueprint/ 来源文件的原始冻结包。":"Read the frozen chapters or download the raw frozen bundle with the complete blueprint/ source tree."}</p>
    </section>
    <section aria-label={zh?"工厂认知审阅":"Factory cognitive review"} className="mt-4 rounded-lg border border-border p-4 text-sm">
      <p>{zh?"独立认知审阅：":"Independent cognitive review: "}{reviewState?reviewLabels[reviewState]?.[zh?0:1]||reviewState:(zh?"未发起":"Not requested")}</p>
      <Button className="mt-3" size="sm" disabled={busy||!model||!!reviewJob} onClick={()=>act(()=>factoryRequest(`artifacts/${a.id}/accept`,{method:"cognitive-review",expected_digest:a.digest,model,timeout,language:zh?"zh":"en"}),zh?"独立认知审阅已排队；不执行包内程序。":"Cognitive review queued; package programs are not executed.")}>{reviewJob?(zh?"等待认知审阅":"Cognitive review pending"):incomplete?(zh?"重试认知审阅":"Retry cognitive review"):review?(zh?"重新认知审阅":"Review cognition again"):(zh?"发起认知审阅":"Request cognitive review")}</Button>
      <p className="mt-2 text-xs leading-5 text-muted">{zh?"会向所选模型发送冻结认知包与对应叶子、场景，可能计费；这是静态审阅，不证明下游应用运行成功。":"The frozen package, leaf and scenario are sent to the selected model and may incur charges. This static review does not prove downstream runtime success."}</p>
      {a.acceptances?.filter(r=>r.method==="cognitive-review").map(r=><details className="mt-3" key={r.id}><summary className="cursor-pointer text-primary">{reviewLabels[r.outcome]?.[zh?0:1]||r.outcome} · {new Date(r.created_at).toLocaleString()}</summary><p className="mt-2 text-xs">{r.summary||r.scope}</p>{r.error?<p className="mt-2 text-xs text-danger">{r.error}</p>:null}{r.protocol_note?<p className="mt-2 text-xs text-muted">{r.protocol_note}</p>:null}{r.checks?.map(c=><div key={c.dimension} className="mt-2 text-xs"><p className="font-medium">{dimensions[c.dimension]?.[zh?0:1]||c.dimension} · {reviewLabels[c.outcome]?.[zh?0:1]||c.outcome}</p><p>{c.reason}</p><p className="text-muted">{c.files.join(", ")}</p></div>)}{r.suggestions?.length?<ul className="mt-3 list-inside list-disc text-xs">{r.suggestions.map((s,i)=><li key={i}>{s}</li>)}</ul>:null}</details>)}
      <details className="mt-4"><summary className="cursor-pointer text-primary">{zh?"按冻结场景生产认知修订版":"Produce a cognitive revision of the pinned scenario"}</summary><label className="mt-3 block">{zh?"认知修订要求":"Cognitive revision instructions"}<textarea className={input} value={repair} onChange={e=>setRepair(e.target.value)}/></label><p className="mt-2 text-xs text-muted">{zh?"复用原调研和场景，连同原包、审阅意见发给所选模型；创建新候选并再次独立审阅，保留原版本。可能计费。":"Reuses pinned research and scenario, sending the prior package and review to the selected model. A new candidate is created and reviewed independently; the original stays intact. Calls may incur charges."}</p><Button className="mt-3" size="sm" disabled={busy||!model||!repair.trim()} onClick={()=>act(()=>factoryRequest(`artifacts/${a.id}/repair`,{expected_digest:a.digest,note:repair,model,timeout,language:zh?"zh":"en"}),zh?"认知修订已排队，原候选保留。":"Cognitive revision queued; original candidate retained.")}>{zh?"生产认知修订版":"Produce cognitive revision"}</Button></details>
    </section>
    <Button className="mt-3" size="sm" variant="outline" disabled={busy} onClick={()=>act(async()=>{setDetails(await factoryRequest<BlueprintDetails>(`artifacts/${a.id}/blueprint`));})}><BookOpen className="size-4"/>{zh?"查看认知内容":"Read cognitive content"}</Button>
    {details?<section className="mt-4 space-y-4" aria-label={zh?"认知内容":"Cognitive content"}>
      <div className="grid gap-3 md:grid-cols-3">{details.spec.phases.map(p=><div key={p.id} className="rounded-lg border border-border p-3"><h3 className="font-medium">{p.id} · {p.title}</h3><p className="mt-2 text-xs leading-5 text-muted">{p.goal}</p><p className="mt-2 text-xs">{zh?`${p.features.length} 项能力 / ${p.acceptance.length} 项验收`:`${p.features.length} capabilities / ${p.acceptance.length} cases`}</p></div>)}</div>
      <label className="block text-sm">{zh?"阅读章节":"Read chapter"}<select aria-label={zh?"阅读章节":"Read chapter"} className={input} value={document} onChange={e=>setDocument(e.target.value)}>{Object.keys(details.documents).map(name=><option key={name} value={name}>{names[name]?.[zh?0:1]||name}</option>)}</select></label>
      <section aria-label={zh?"章节正文":"Chapter content"} className="max-h-[32rem] min-w-0 overflow-auto rounded-lg border border-border bg-bg-elevated p-4">
        <div className="prose prose-sm max-w-none break-words [&_table]:text-xs [&_pre]:overflow-auto [&_pre]:whitespace-pre-wrap [&_pre]:break-words">
          <ReactMarkdown remarkPlugins={[remarkGfm]} skipHtml components={{
            img:({alt})=><span className="text-muted">{alt|| (zh?"图片未自动加载":"Image not loaded automatically")}</span>,
            a:({href,children})=>href&&/^https?:\/\//i.test(href)?<a href={href} target="_blank" rel="noopener noreferrer">{children}</a>:<span>{children}</span>,
          }}>{details.documents[document]}</ReactMarkdown>
        </div>
      </section>
      <details className="text-sm"><summary className="cursor-pointer text-primary">{zh?"能力地图与适用性":"Capability map and applicability"}</summary><ul className="mt-3 space-y-3">{details.spec.features.map(f=><li key={f.id}><p className="font-medium">{f.id} · {f.name} · {f.phase|| (zh?"当前阶段外":"Outside current phases")}</p><p className="mt-1 text-xs text-muted">{f.applicability} · {f.reason}</p></li>)}</ul></details>
      <details className="text-sm"><summary className="cursor-pointer text-primary">{zh?"人工决策与默认值":"Human decisions and defaults"}</summary><ul className="mt-3 space-y-3">{details.spec.decisions.map(d=><li key={d.id}><h3 className="font-medium">{d.id} · {d.question}</h3><p className="mt-1 text-xs">{d.default}</p><p className="mt-1 text-xs text-muted">{d.when_to_ask}</p></li>)}</ul></details>
      <details className="text-sm"><summary className="cursor-pointer text-primary">{zh?"来源与许可证记录":"Sources and license records"}</summary><ul className="mt-3 space-y-3">{details.spec.sources.map(s=><li key={s.id}><p>{s.id} · {s.name}</p><p className="mt-1 break-all text-xs text-muted">{s.url} · {s.version} · {s.license}</p><p className="mt-1 text-xs text-muted">{s.reuse}</p></li>)}</ul></details>
    </section>:null}
    <section className="mt-5 border-t border-border pt-4" aria-label={zh?"创建认知开发包":"Create cognitive development package"}>
      <h3 className="font-medium">{zh?"2. 当前阶段执行包":"2. Current phase execution package"}</h3><p className="mt-2 text-xs leading-5 text-muted">{zh?"按阶段导出，从 HANDOFF.md 开始，再按需加载完整认知和契约；无需一开始预加载全部材料。旧包阶段可能未覆盖完整场景，应对照已确认场景核实范围；不能静默更改冻结承诺或视为已完成。导出不会运行验收。":"Export the selected phase. Start with HANDOFF.md, then load the full knowledge and contracts when needed without preloading everything. Legacy phases may not cover the full scenario: verify scope against the confirmed scenario, never silently change frozen commitments or claim they are complete. Export runs no acceptance."}</p>
      <div className="mt-3 grid gap-3 md:grid-cols-2"><label className="text-sm">{zh?"开发项目名称":"Development project name"}<input className={input} value={project} onChange={e=>{setProject(e.target.value);setDownload("");}}/></label><label className="text-sm">{zh?"本次开发阶段":"Development phase"}<select aria-label={zh?"本次开发阶段":"Development phase"} className={input} value={phase} onChange={e=>{setPhase(e.target.value);setDownload("");}}>{a.manifest.phases?.map(p=><option key={p.id} value={p.id}>{p.id} · {p.title}</option>)}</select></label></div>
      {!validName?<p className="mt-2 text-xs text-muted">{zh?"名称须以小写字母开头，仅含小写字母、数字和连字符，最多 63 字符。":"Use up to 63 lowercase letters, digits or hyphens, starting with a letter."}</p>:null}
      <Button className="mt-3" size="sm" disabled={busy||!validName||!phase} onClick={()=>act(async()=>{const result=await factoryRequest<{download_url:string}>(`artifacts/${a.id}/development-package`,{expected_digest:a.digest,project_name:project,phase});setDownload(result.download_url);},zh?"开发包已创建；未调用模型、安装依赖或运行应用。":"Development package created; no model calls, installation or application execution.")}>{zh?"创建开发包":"Create development package"}</Button>
      {download?<a className="ml-3 text-sm text-primary underline" href={download}>{zh?"下载开发包":"Download development package"}</a>:null}
    </section>
    <section aria-label={zh?"独立运行验收":"Independent runtime acceptance"} className="mt-4 rounded-lg border border-border p-4 text-sm">
      <h3 className="font-medium">{zh?"3. 独立验收：运行冻结用例":"3. Independent acceptance: run frozen cases"}</h3>
      <p className="mt-2 text-xs leading-5 text-muted">{zh?"与静态认知审阅分开记录。仅在冻结包声明支持适配器时可提交；容器运行时是否可用由提交结果确认。不会调用模型。":"Recorded separately from static cognition review. Submission is available only when the frozen blueprint declares a runner adapter; container readiness is determined by the result. No model is called."}</p>
      {!details?<p className="mt-2 text-xs text-muted">{zh?"先读取冻结包能力以确认是否有运行适配器。":"Load frozen package capabilities to check for a runtime adapter."}</p>:null}
      {details?.runtime_acceptance?.supported?<>
        <p className="mt-2 text-xs">{zh?"适配器支持；实际容器可用性尚未确认。网络策略：none。":"Adapter supported; container availability is not yet confirmed. Network policy: none."}</p>
        <details className="mt-3 rounded-md bg-bg-elevated p-3"><summary className="cursor-pointer text-primary">{zh?"delivery.json 与打包说明":"delivery.json and archive instructions"}</summary>
          <p className="mt-2 text-xs leading-5 text-muted">{zh?"ZIP 根目录放 delivery.json 和应用源文件。files 必须精确列出 ZIP 中全部源文件（不含 delivery.json）；也可统一放在 app/ 并设置 root 为 app。runtime 使用受支持的 profile、命令及端口；readiness_path 可选。不要放真实凭据。压缩 ZIP 不超过 1 MiB，展开后不超过 8 MiB。":"Put delivery.json and app source files at ZIP root. files must list every source file in the ZIP (excluding delivery.json); alternatively place them all under app/ and set root to app. runtime declares a supported profile, commands and port; readiness_path is optional. Do not include real credentials. ZIP limit is 1 MiB compressed and 8 MiB expanded."}</p>
          <pre className="mt-2 overflow-auto whitespace-pre-wrap break-words text-[11px]">{`{
  "schema": "atlas.application-delivery.v1",
  "root": ".",
  "files": ["app.py"],
  "runtime": {
    "profile": "python-web",
    "install": [],
    "build": [],
    "start": ["python", "app.py"],
    "port": 8000,
    "readiness_path": "/"
  }
}`}</pre>
          <p className="mt-2 text-xs text-muted">{zh?"本地制作：新建目录 → 放入源文件和 delivery.json → 从该目录内容创建 ZIP（不要多套一层目录）。":"To prepare locally: create a folder, add source files and delivery.json, then ZIP the folder contents without an extra enclosing folder."}</p>
        </details>
        <label className="mt-3 block">{zh?"应用源代码 ZIP":"Application source ZIP"}<input aria-label={zh?"应用源代码 ZIP":"Application source ZIP"} type="file" accept=".zip,application/zip" className={input} disabled={busy||!!runtimeJob} onChange={e=>setRuntimeFile(e.target.files?.[0]||null)}/></label>
        {runtimeFile?<p className="mt-1 text-xs text-muted">{runtimeFile.name} · {(runtimeFile.size/1024).toFixed(1)} KiB</p>:null}
        <label className="mt-3 flex items-start gap-2 text-xs leading-5"><input type="checkbox" className="mt-1" checked={runtimeConsent} disabled={busy||!!runtimeJob} onChange={e=>setRuntimeConsent(e.target.checked)}/><span>{zh?"我确认：上传的应用代码和冻结验收程序将在离线托管容器中执行。":"I acknowledge that uploaded application code and frozen acceptance programs will execute in managed offline containers."}</span></label>
        <Button className="mt-3" size="sm" disabled={busy||!!runtimeJob||!runtimeFile||runtimeFile.size>1024*1024||!runtimeConsent||!phase} onClick={()=>act(async()=>{
          if(!runtimeFile) return;
          const source_archive_base64=await new Promise<string>((resolve,reject)=>{const reader=new FileReader();reader.onerror=()=>reject(new Error("Unable to read ZIP"));reader.onload=()=>resolve(String(reader.result).split(",")[1]);reader.readAsDataURL(runtimeFile);});
          await factoryRequest(`artifacts/${a.id}/accept`,{method:"blueprint-runtime",expected_digest:a.digest,phase,source_archive_base64,timeout,language:zh?"zh":"en",execution_confirmed:true});
        },zh?"独立运行验收已排队。":"Independent runtime acceptance queued.")}>{runtimeJob?(zh?"运行验收排队中":"Runtime acceptance pending"):(zh?"提交并运行冻结验收":"Submit and run frozen acceptance")}</Button>
        {runtimeFile&&runtimeFile.size>1024*1024?<p role="alert" className="mt-2 text-xs text-danger">{zh?"ZIP 超过 1 MiB。":"ZIP exceeds 1 MiB."}</p>:null}
      </>:details?<p className="mt-2 text-xs text-muted">{details.runtime_acceptance?.reason|| (zh?"冻结包未声明受支持的运行适配器；无法猜测运行命令。":"No supported runtime adapter is declared by this frozen blueprint; commands cannot be guessed.")}</p>:null}
      {runtimeJob?<p role="status" className="mt-2 text-xs">{runtimeStatus(runtimeJob.state)}</p>:null}
      {runtimeResults.map(r=><details key={r.id} id={`factory-runtime-${r.id}`} open={r.id===runtimeRunId} className="mt-3"><summary className="cursor-pointer text-primary">{runtimeStatus(r.outcome)} · {new Date(r.created_at).toLocaleString()}</summary><p className="mt-2 text-xs">{r.scope}</p>
        {r.startup?<div className="mt-2 text-xs"><p>{zh?"启动":"Startup"}: {runtimeStatus(r.startup.status)}{r.startup.reason?` · ${r.startup.reason}`:""}{r.startup.error?` · ${r.startup.error}`:""}</p>
          {r.startup.captured_output||r.startup.readiness?.output||r.startup.output||r.failure?<details className="mt-2 rounded-md bg-bg-elevated p-2"><summary className="cursor-pointer text-primary">{zh?"启动诊断":"Startup diagnostics"}</summary>
            {r.failure?<p className="mt-2 text-danger">{zh?"失败":"Failure"}: {r.failure}</p>:null}
            {r.startup.captured_output?.stdout?<><p className="mt-2 font-medium">stdout</p><pre className="max-h-40 overflow-auto whitespace-pre-wrap break-words">{r.startup.captured_output.stdout}</pre></>:null}
            {r.startup.captured_output?.stderr?<><p className="mt-2 font-medium">stderr</p><pre className="max-h-40 overflow-auto whitespace-pre-wrap break-words text-danger">{r.startup.captured_output.stderr}</pre></>:null}
            {r.startup.readiness?<><p className="mt-2 font-medium">{zh?"就绪检查":"Readiness check"}: {r.startup.readiness.status|| (r.startup.readiness.passed?"passed":"failed")}</p>{r.startup.readiness.error?<p className="text-danger">{r.startup.readiness.error}</p>:null}{r.startup.readiness.output?<pre className="max-h-40 overflow-auto whitespace-pre-wrap break-words">{r.startup.readiness.output}</pre>:null}</>:null}
            {r.startup.output?<pre className="mt-2 max-h-40 overflow-auto whitespace-pre-wrap break-words">{r.startup.output}</pre>:null}
          </details>:null}
        </div>:r.failure?<p className="mt-2 text-xs text-danger">{zh?"失败":"Failure"}: {r.failure}</p>:null}
        {r.case_results?.map((c,i)=>{
          const caseId=c.id||c.case_id||`case-${i+1}`;
          const assertions=c.assertions||[];
          return <details key={`${caseId}-${i}`} className="mt-2 rounded-md bg-bg-elevated p-2"><summary className="cursor-pointer text-xs">{caseId} · {runtimeStatus(c.status)}{c.reason?` · ${c.reason}`:""}{c.error?` · ${c.error}`:""}</summary>{c.output?<pre className="mt-2 max-h-48 overflow-auto whitespace-pre-wrap break-words text-[11px]">{c.output}</pre>:null}{assertions.length?<ul className="mt-2 space-y-1 text-xs">{assertions.map((assertion,j)=><li key={`${assertion.id}-${j}`}><span className={assertion.passed?"text-primary":"text-danger"}>{assertion.passed?"✓":"✗"} {assertion.id}</span>{assertion.detail?` · ${assertion.detail}`:""}</li>)}</ul>:null}</details>;
        })}
        {r.cleanup?<div className="mt-2 text-xs"><p>{zh?"清理":"Cleanup"}: {runtimeStatus(r.cleanup.status)}{r.cleanup.reason?` · ${r.cleanup.reason}`:""}{r.cleanup.error?` · ${r.cleanup.error}`:""}</p>{r.cleanup.errors?.length?<details className="mt-1"><summary className="cursor-pointer text-primary">{zh?`清理错误（${r.cleanup.errors.length}）`:`Cleanup errors (${r.cleanup.errors.length})`}</summary><ul className="mt-1 list-disc space-y-1 pl-5 text-danger">{r.cleanup.errors.map((error,i)=><li key={i}>{error}</li>)}</ul></details>:null}</div>:null}
        {r.error?<p className="mt-2 text-xs text-danger">{r.error}</p>:null}</details>)}
    </section>
  </article>;
}
