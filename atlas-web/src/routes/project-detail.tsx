import { useEffect, useState, type FormEvent, type ReactNode } from "react";
import {
  AlertTriangle, ArrowLeft, Bot, CheckCircle2, Download, FileClock,
  FileText, FolderGit2, Lightbulb, Plus, RefreshCw, Scale, Save, Sparkles,
} from "lucide-react";
import { Link, useParams } from "react-router-dom";
import { ErrorBox, Loading, useAsync } from "@/components/loaders";
import { Prose } from "@/components/prose";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  addProjectDocumentVersion,
  applyProjectExecutionResult,
  applyProjectGenerationItem,
  captureWorkspaceBaseline,
  checkWorkspaceChanges,
  confirmProjectRequirement,
  continueProjectExecution,
  createProjectDecision,
  createProjectDocument,
  createProjectIteration,
  createProjectRequirement,
  createProjectTask,
  exportProject,
  getProjectExecution,
  getProjectDocumentDiff,
  getProjectDocumentVersions,
  getProjectGeneration,
  getProjectWorkspace,
  invalidateAtlasCache,
  listProjectGenerations,
  listWorkspaceBaselines,
  recordProjectTaskAcceptance,
  replyProjectExecutionPermission,
  replyProjectExecutionQuestion,
  startProjectExecution,
  startProjectGeneration,
  stopProjectExecution,
  updateProjectIterationStatus,
  updateProjectRequirement,
  type DocumentBasis,
  type ProjectDocument,
  type ProjectDocumentKind,
  type ProjectExport,
  type ProjectExecution,
  type ProjectGenerationRun,
  type ProjectReference,
  type ProjectRequirement,
  type ProjectScope,
  type ProjectTask,
  type ProjectWorkspace,
  type WorkspaceBaselineCheck,
  type WorkspaceBaselineSummary,
} from "@/lib/atlas";
import { useLang } from "@/lib/lang";
import { setCurrentProjectId } from "@/lib/project-selection";

const DOCUMENT_KINDS: { value: ProjectDocumentKind; zh: string; en: string }[] = [
  { value: "analysis", zh: "调研与分析", en: "Research & analysis" },
  { value: "value-analysis", zh: "价值分析", en: "Value analysis" },
  { value: "product-requirements", zh: "产品需求", en: "Product requirements" },
  { value: "interaction", zh: "交互与页面", en: "Interaction & screens" },
  { value: "technical-plan", zh: "技术方案", en: "Technical plan" },
  { value: "development-plan", zh: "开发规划", en: "Development plan" },
  { value: "acceptance-plan", zh: "验收方案", en: "Acceptance plan" },
  { value: "current-state", zh: "项目现状与变更", en: "Current state & changes" },
];
const DOCUMENT_BUNDLE_KINDS = DOCUMENT_KINDS.filter(
  (item) => item.value !== "current-state" && item.value !== "value-analysis");
const CORE_DOCUMENT_BUNDLE: ProjectDocumentKind[] = [
  "product-requirements", "technical-plan", "development-plan", "acceptance-plan",
];
const FULL_DOCUMENT_BUNDLE: ProjectDocumentKind[] = [
  "analysis", "product-requirements", "interaction", "technical-plan",
  "development-plan", "acceptance-plan",
];

export function ProjectDetail() {
  const { projectId = "" } = useParams<{ projectId: string }>();
  const { lang } = useLang();
  const [revision, setRevision] = useState(0);
  const [analysisRun, setAnalysisRun] = useState<ProjectGenerationRun | null>(null);
  const [hasBaseline, setHasBaseline] = useState<boolean | null>(null);
  const { data, error, loading } = useAsync(
    () => getProjectWorkspace(projectId), [projectId, revision]);

  useEffect(() => {
    if (data?.project.id) setCurrentProjectId(data.project.id);
  }, [data?.project.id]);

  useEffect(() => { setHasBaseline(null); }, [projectId]);

  const refresh = () => {
    invalidateAtlasCache();
    setRevision((value) => value + 1);
  };

  if (loading && !data) return <Loading />;
  if (error || !data) return <ErrorBox message={error || "project unavailable"} />;

  return (
    <main className="mx-auto max-w-6xl px-4 py-10">
      <Link to="/projects" className="inline-flex items-center gap-1.5 text-sm text-muted hover:text-fg">
        <ArrowLeft className="size-4" />{lang === "zh" ? "返回项目列表" : "Back to projects"}
      </Link>
      <div className="mt-5 flex flex-wrap items-start justify-between gap-4">
        <div>
          <p className="text-sm font-medium tracking-wide text-primary">{lang === "zh" ? "U17 · 项目工作台" : "U17 · Project workspace"}</p>
          <h1 className="mt-2 font-serif text-3xl font-medium">{data.project.name}</h1>
          <p className="mt-2 max-w-3xl text-sm leading-6 text-muted">{data.project.objective}</p>
        </div>
        <ExportButton projectId={projectId} lang={lang} />
      </div>

      <div className="mt-6 grid gap-3 sm:grid-cols-4">
        <Stat value={data.references.length} label={lang === "zh" ? "固定资料" : "Pinned sources"} />
        <Stat value={data.requirements.length} label={lang === "zh" ? "候选需求" : "Requirements"} />
        <Stat value={data.decisions.length} label={lang === "zh" ? "项目决定" : "Decisions"} />
        <Stat value={data.documents.length} label={lang === "zh" ? "关联文档" : "Documents"} />
      </div>

      <LifecycleOverview workspace={data} hasBaseline={hasBaseline} />

      <WorkspaceBaselinePanel projectId={projectId} onSaved={refresh}
        onBaselineChange={setHasBaseline} />

      <GenerationPanel projectId={projectId} workspace={data} onSaved={refresh}
        onAnalysis={setAnalysisRun} />

      <ConsistencyPanel workspace={data} analysisRun={analysisRun} />

      <section className="mt-8 grid gap-6 lg:grid-cols-[minmax(0,1fr)_22rem]">
        <div>
          <SectionTitle icon={Scale} title={lang === "zh" ? "范围与验收" : "Scope & acceptance"}
            description={lang === "zh" ? "分析建议和用户确认分别保存；修改需求内容会清除旧确认并提示关联文档复核。" : "Recommendations and user confirmations are stored separately. Meaningful edits clear old confirmation and flag linked documents."} />
          <div className="mt-4 space-y-3">
            {data.requirements.map((requirement) => (
              <RequirementCard key={`${requirement.id}:${requirement.updated_at}`} projectId={projectId}
                requirement={requirement} references={data.references} onSaved={refresh} />
            ))}
            {!data.requirements.length ? <Empty text={lang === "zh" ? "还没有候选需求。" : "No candidate requirements yet."} /> : null}
          </div>
        </div>
        <RequirementForm projectId={projectId} references={data.references} onSaved={refresh} />
      </section>

      <section className="mt-10 grid gap-6 lg:grid-cols-[minmax(0,1fr)_22rem]">
        <div>
          <SectionTitle icon={Lightbulb} title={lang === "zh" ? "已记录决定" : "Recorded decisions"}
            description={lang === "zh" ? "决定保存采用内容和理由，可引用固定资料。" : "Decisions retain the chosen direction, rationale, and pinned sources."} />
          <div className="mt-4 space-y-3">
            {data.decisions.map((decision) => (
              <article key={decision.id} className="rounded-xl bg-surface p-5 shadow-card">
                <div className="flex flex-wrap items-center gap-2">
                  <h3 className="font-medium">{decision.statement}</h3>
                  <span className="font-mono text-[11px] text-subtle">{decision.id}</span>
                </div>
                <p className="mt-2 text-sm leading-6 text-muted">{decision.rationale}</p>
                <IdLinks ids={decision.reference_ids} prefix={lang === "zh" ? "依据" : "Sources"} />
              </article>
            ))}
            {!data.decisions.length ? <Empty text={lang === "zh" ? "还没有项目决定。" : "No recorded decisions yet."} /> : null}
          </div>
        </div>
        <DecisionForm projectId={projectId} references={data.references} onSaved={refresh} />
      </section>

      <section className="mt-10">
        <SectionTitle icon={FileText} title={lang === "zh" ? "关联文档与版本" : "Linked documents & versions"}
          description={lang === "zh" ? "每次保存产生不可变版本，记录作者、修改说明和固定依据；旧版本可查看并比较。" : "Each save creates an immutable version with author, change summary, and pinned basis. Older versions remain viewable and comparable."} />
        <div className="mt-5 grid gap-6 lg:grid-cols-[minmax(0,1fr)_22rem]">
          <div className="space-y-4">
            {data.documents.map((document) => (
              <DocumentCard key={`${document.id}:${document.current_version}`} projectId={projectId}
                document={document} onSaved={refresh} />
            ))}
            {!data.documents.length ? <Empty text={lang === "zh" ? "还没有关联文档。" : "No linked documents yet."} /> : null}
          </div>
          <DocumentForm projectId={projectId} workspace={data} onSaved={refresh} />
        </div>
      </section>

      <ExecutionPanel projectId={projectId} workspace={data} hasBaseline={hasBaseline}
        onSaved={refresh} />
    </main>
  );
}

function LifecycleOverview({ workspace, hasBaseline }: {
  workspace: ProjectWorkspace; hasBaseline: boolean | null;
}) {
  const { lang } = useLang();
  const confirmed = workspace.requirements.some((item) => item.confirmed_scope === "current");
  const documentsReady = workspace.documents.some((item) => item.review.status === "current");
  const currentIteration = workspace.iterations.find((item) => item.status === "active")
    || workspace.iterations[0] || null;
  const currentTasks = currentIteration
    ? workspace.tasks.filter((item) => item.iteration_id === currentIteration.id) : [];
  const currentTaskIds = new Set(currentTasks.map((item) => item.id));
  const currentExecutions = workspace.executions.filter((item) => currentTaskIds.has(item.task_id));
  const latestExecution = (task: ProjectTask) =>
    currentExecutions.find((execution) => execution.task_id === task.id);
  const executed = currentTasks.length > 0 && currentTasks.every((task) =>
    task.execution_status === "completed");
  const applied = currentTasks.length > 0 && currentTasks.every((task) =>
    task.kind === "analysis" || latestExecution(task)?.application_status === "applied");
  const accepted = currentTasks.length > 0
    && currentTasks.every((item) => ["passed", "waived"].includes(item.acceptance_status));
  const steps = [
    { done: workspace.references.length > 0, zh: "收集资料", en: "Sources" },
    { done: confirmed, zh: "确认需求", en: "Scope" },
    { done: documentsReady, zh: "形成文档", en: "Documents" },
    { done: hasBaseline === true, zh: "确认工作区", en: "Workspace" },
    { done: Boolean(currentIteration), zh: "建立迭代", en: "Iteration" },
    { done: executed, zh: "执行改动", en: "Execution" },
    { done: applied, zh: "应用结果", en: "Apply" },
    { done: accepted, zh: "产品验收", en: "Acceptance" },
    { done: currentIteration?.status === "completed", zh: "完成迭代", en: "Complete" },
  ];
  const next = steps.find((item) => !item.done);
  return <section className="mt-5 rounded-xl border border-border bg-surface p-4 shadow-card">
    <div className="flex flex-wrap items-center justify-between gap-3">
      <div><p className="text-sm font-medium">{lang === "zh" ? "项目路径" : "Project path"}</p><p className="mt-1 text-xs text-subtle">{next ? (lang === "zh" ? `建议下一步：${next.zh}` : `Recommended next: ${next.en}`) : (lang === "zh" ? "当前迭代已完成。" : "The current iteration is complete.")}</p></div>
      <div className="flex flex-wrap gap-2">{steps.map((item, index) => <div key={item.en} className={`flex items-center gap-1.5 rounded-full px-2.5 py-1 text-[11px] ${item.done ? "bg-primary/10 text-primary" : item === next ? "bg-warn/10 text-warn" : "bg-bg-elevated text-subtle"}`}>
        {item.done ? <CheckCircle2 className="size-3.5" /> : <span>{index + 1}</span>}<span>{lang === "zh" ? item.zh : item.en}</span>
      </div>)}</div>
    </div>
  </section>;
}

function ExecutionPanel({ projectId, workspace, hasBaseline, onSaved }: {
  projectId: string; workspace: ProjectWorkspace; hasBaseline: boolean | null;
  onSaved: () => void;
}) {
  const { lang } = useLang();
  const active = workspace.iterations.find((item) => item.status === "active") || null;
  const tasks = active ? workspace.tasks.filter((item) => item.iteration_id === active.id) : [];
  const [busy, setBusy] = useState("");
  const [error, setError] = useState("");
  const changeIteration = async (status: "completed" | "abandoned") => {
    if (!active) return;
    setBusy(status); setError("");
    try { await updateProjectIterationStatus(projectId, active.id, status); onSaved(); }
    catch (cause) { setError(String(cause)); } finally { setBusy(""); }
  };
  return <section className="mt-10">
    <SectionTitle icon={Bot} title={lang === "zh" ? "迭代与开发执行" : "Iterations & development execution"}
      description={lang === "zh" ? "把已确认需求、固定文档版本和已接受代码基线绑定为任务；OpenCode 负责执行，Atlas 独立记录状态、权限、文件变化和产品验收。" : "Bind confirmed requirements, fixed document versions, and an accepted code baseline into tasks. OpenCode executes while Atlas independently records state, permissions, file changes, and product acceptance."} />
    <div className="mt-5 space-y-5">
      {!active ? <IterationForm projectId={projectId} workspace={workspace}
        hasBaseline={hasBaseline} onSaved={onSaved} /> : <>
        <article className="rounded-xl bg-surface p-5 shadow-card">
          <div className="flex flex-wrap items-start justify-between gap-4">
            <div><div className="flex flex-wrap items-center gap-2"><Badge tone="ok">{lang === "zh" ? `活动迭代 ${active.sequence}` : `Active iteration ${active.sequence}`}</Badge><span className="font-mono text-[11px] text-subtle">{active.id}</span></div><h3 className="mt-2 font-medium">{active.title}</h3><p className="mt-1 text-sm leading-6 text-muted">{active.objective}</p></div>
            <div className="flex gap-2"><Button size="sm" variant="outline" disabled={Boolean(busy)} onClick={() => changeIteration("abandoned")}>{lang === "zh" ? "放弃迭代" : "Abandon"}</Button><Button size="sm" disabled={Boolean(busy) || !tasks.length} onClick={() => changeIteration("completed")}><CheckCircle2 className="size-4" />{lang === "zh" ? "完成迭代" : "Complete iteration"}</Button></div>
          </div>
          <IdLinks ids={active.input_document_versions} prefix={lang === "zh" ? "固定文档版本" : "Fixed document versions"} />
          <IdLinks ids={active.requirement_ids} prefix={lang === "zh" ? "本版需求" : "Current requirements"} />
          {error ? <p className="mt-3 text-xs text-danger">{error}</p> : null}
        </article>
        <div className="grid gap-6 lg:grid-cols-[minmax(0,1fr)_22rem]">
          <div className="space-y-4">
            {tasks.map((task) => <ExecutionTaskCard key={`${task.id}:${task.updated_at}`} projectId={projectId} task={task} executions={workspace.executions.filter((item) => item.task_id === task.id)} onSaved={onSaved} />)}
            {!tasks.length ? <Empty text={lang === "zh" ? "本迭代还没有执行任务。" : "This iteration has no execution tasks yet."} /> : null}
          </div>
          <TaskForm projectId={projectId} workspace={workspace} iteration={active} onSaved={onSaved} />
        </div>
      </>}
      {workspace.iterations.filter((item) => item.status !== "active").length ? <details className="rounded-xl bg-surface p-5 shadow-card"><summary className="cursor-pointer text-sm text-primary">{lang === "zh" ? "历史迭代" : "Iteration history"}</summary><div className="mt-3 space-y-3">{workspace.iterations.filter((item) => item.status !== "active").map((item) => { const historicalTasks = workspace.tasks.filter((task) => task.iteration_id === item.id); return <details key={item.id} className="rounded-md bg-bg-elevated p-3"><summary className="cursor-pointer text-sm"><span className="font-medium">#{item.sequence} · {item.title}</span><span className="ml-2 text-xs text-subtle">{item.status} · {historicalTasks.length} {lang === "zh" ? "个任务" : "task(s)"}</span></summary><div className="mt-3 space-y-3">{historicalTasks.map((task) => <ExecutionTaskCard key={`${task.id}:${task.updated_at}`} projectId={projectId} task={task} executions={workspace.executions.filter((execution) => execution.task_id === task.id)} onSaved={onSaved} />)}{!historicalTasks.length ? <p className="text-xs text-subtle">{lang === "zh" ? "没有任务记录。" : "No task records."}</p> : null}</div></details>; })}</div></details> : null}
    </div>
  </section>;
}

function IterationForm({ projectId, workspace, hasBaseline, onSaved }: {
  projectId: string; workspace: ProjectWorkspace; hasBaseline: boolean | null;
  onSaved: () => void;
}) {
  const { lang } = useLang();
  const current = workspace.requirements.filter((item) => item.confirmed_scope === "current");
  const currentDocuments = workspace.documents.filter((item) => item.review.status === "current");
  const [title, setTitle] = useState(""); const [objective, setObjective] = useState("");
  const [documents, setDocuments] = useState<string[]>(currentDocuments.map((item) => item.version_id));
  const [requirements, setRequirements] = useState<string[]>(current.map((item) => item.id));
  const documentOptionsKey = currentDocuments.map((item) => item.version_id).join("\0");
  const requirementOptionsKey = current.map((item) => item.id).join("\0");
  useEffect(() => {
    setDocuments(currentDocuments.map((item) => item.version_id));
  }, [documentOptionsKey]);
  useEffect(() => {
    setRequirements(current.map((item) => item.id));
  }, [requirementOptionsKey]);
  const [saving, setSaving] = useState(false); const [error, setError] = useState("");
  const missing: string[] = [];
  if (hasBaseline === false) missing.push(lang === "zh" ? "已接受的工作区基线" : "an accepted workspace baseline");
  if (!currentDocuments.length) missing.push(lang === "zh" ? "至少一份当前文档" : "at least one current document");
  if (!current.length) missing.push(lang === "zh" ? "至少一条已确认本版需求" : "at least one confirmed current requirement");
  const submit = async (event: FormEvent) => { event.preventDefault(); setSaving(true); setError(""); try {
    await createProjectIteration(projectId, { title, objective, input_document_versions: documents, requirement_ids: requirements }); onSaved();
  } catch (cause) { setError(String(cause)); } finally { setSaving(false); } };
  return <article className="rounded-xl bg-surface p-5 shadow-card"><form onSubmit={submit}>
    <div className="grid gap-5 lg:grid-cols-2"><div className="space-y-4"><h3 className="font-medium">{lang === "zh" ? "建立活动迭代" : "Create active iteration"}</h3><Field label={lang === "zh" ? "迭代标题" : "Iteration title"} value={title} onChange={setTitle} required /><TextArea label={lang === "zh" ? "本轮目标" : "Iteration objective"} value={objective} onChange={setObjective} required /></div><div className="grid gap-4 sm:grid-cols-2"><Picker label={lang === "zh" ? "固定已复核文档版本" : "Pin reviewed document versions"} options={currentDocuments.map((item) => ({ key: item.version_id, label: `${item.title} · v${item.current_version}` }))} selected={documents} onChange={setDocuments} /><Picker label={lang === "zh" ? "固定已确认本版需求" : "Pin confirmed current requirements"} options={current.map((item) => ({ key: item.id, label: item.content }))} selected={requirements} onChange={setRequirements} /></div></div>
    {missing.length ? <p className="mt-4 rounded-md bg-warn/10 p-3 text-xs leading-5 text-warn">{lang === "zh" ? `开始迭代前还需要：${missing.join("、")}。` : `Before starting an iteration, add ${missing.join(", ")}.`}</p> : null}
    {error ? <p className="mt-3 text-xs text-danger">{error}</p> : null}<Button className="mt-5" disabled={saving || hasBaseline !== true || !documents.length || !requirements.length || !title.trim() || !objective.trim()}><Plus className="size-4" />{lang === "zh" ? "创建并启动迭代" : "Create and activate iteration"}</Button>
  </form></article>;
}

function TaskForm({ projectId, workspace, iteration, onSaved }: {
  projectId: string; workspace: ProjectWorkspace; iteration: ProjectWorkspace["iterations"][number]; onSaved: () => void;
}) {
  const { lang } = useLang();
  const docs = workspace.documents.filter((item) => iteration.input_document_versions.includes(item.version_id));
  const requirements = workspace.requirements.filter((item) => iteration.requirement_ids.includes(item.id));
  const [kind, setKind] = useState<ProjectTask["kind"]>("code"); const [title, setTitle] = useState("");
  const [objective, setObjective] = useState(""); const [writePaths, setWritePaths] = useState("");
  const [commands, setCommands] = useState(""); const [documentIds, setDocumentIds] = useState(docs.map((item) => item.version_id));
  const [requirementIds, setRequirementIds] = useState(requirements.map((item) => item.id));
  const [saving, setSaving] = useState(false); const [error, setError] = useState("");
  const submit = async (event: FormEvent) => { event.preventDefault(); setSaving(true); setError(""); try {
    await createProjectTask(projectId, { iteration_id: iteration.id, kind, title, objective, input_document_versions: documentIds, requirement_ids: requirementIds, write_paths: kind === "analysis" ? [] : lines(writePaths), verification_commands: lines(commands) }); setTitle(""); setObjective(""); setWritePaths(""); setCommands(""); onSaved();
  } catch (cause) { setError(String(cause)); } finally { setSaving(false); } };
  return <SideForm title={lang === "zh" ? "添加执行任务" : "Add execution task"} icon={Plus}><form className="space-y-4" onSubmit={submit}>
    <label className="block text-sm"><span className="text-muted">{lang === "zh" ? "任务类型" : "Task kind"}</span><select value={kind} onChange={(event) => setKind(event.target.value as ProjectTask["kind"])} className={inputClass}><option value="code">{lang === "zh" ? "代码修改" : "Code change"}</option><option value="document">{lang === "zh" ? "项目文档" : "Project document"}</option><option value="analysis">{lang === "zh" ? "只读分析" : "Read-only analysis"}</option></select></label>
    <Field label={lang === "zh" ? "任务标题" : "Task title"} value={title} onChange={setTitle} required /><TextArea label={lang === "zh" ? "明确目标" : "Concrete objective"} value={objective} onChange={setObjective} required />
    {kind !== "analysis" ? <TextArea label={lang === "zh" ? "允许写入路径（每行一个）" : "Allowed write paths (one per line)"} value={writePaths} onChange={setWritePaths} required /> : null}
    <TextArea label={lang === "zh" ? "固定验证命令（每行一个）" : "Fixed verification commands (one per line)"} value={commands} onChange={setCommands} />
    <Picker label={lang === "zh" ? "任务文档" : "Task documents"} options={docs.map((item) => ({ key: item.version_id, label: `${item.title} v${item.current_version}` }))} selected={documentIds} onChange={setDocumentIds} /><Picker label={lang === "zh" ? "任务需求" : "Task requirements"} options={requirements.map((item) => ({ key: item.id, label: item.content }))} selected={requirementIds} onChange={setRequirementIds} />
    {error ? <p className="text-xs text-danger">{error}</p> : null}<Button className="w-full" disabled={saving || !title.trim() || !objective.trim() || (kind !== "analysis" && !lines(writePaths).length)}>{lang === "zh" ? "保存任务" : "Save task"}</Button>
  </form></SideForm>;
}

function ExecutionTaskCard({ projectId, task, executions, onSaved }: {
  projectId: string; task: ProjectTask; executions: ProjectExecution[]; onSaved: () => void;
}) {
  const { lang } = useLang();
  const [execution, setExecution] = useState<ProjectExecution | null>(executions[0] || null);
  const [working, setWorking] = useState(""); const [error, setError] = useState("");
  const active = execution && ["queued", "running", "waiting_permission", "waiting_input"].includes(execution.status);
  const unavailable = execution?.status === "unknown";
  useEffect(() => { setExecution(executions[0] || null); }, [executions[0]?.id]);
  useEffect(() => {
    if (!active || !execution) return;
    let alive = true;
    const timer = window.setInterval(() => getProjectExecution(projectId, execution.id).then((next) => { if (!alive) return; setExecution(next); if (["completed", "failed", "stopped", "unknown"].includes(next.status)) onSaved(); }, (cause) => { if (alive) setError(String(cause)); }), 1500);
    return () => { alive = false; window.clearInterval(timer); };
  }, [active, execution?.id, projectId]);
  const start = async () => { setWorking("start"); setError(""); try { setExecution(await startProjectExecution(projectId, task.id)); onSaved(); } catch (cause) { setError(String(cause)); } finally { setWorking(""); } };
  const stop = async () => { if (!execution) return; setWorking("stop"); setError(""); try { setExecution(await stopProjectExecution(projectId, execution.id)); onSaved(); } catch (cause) { setError(String(cause)); } finally { setWorking(""); } };
  const filesystem = execution?.raw_state.evidence?.filesystem;
  const verification = execution?.raw_state.evidence?.verification;
  const completionReport = execution?.raw_state.evidence?.completion_report;
  const commandEvidence = execution?.raw_state.evidence?.tool_calls?.commands || [];
  const displayStatus = execution?.status || task.execution_status;
  const acceptanceOpen = ["pending", "failed"].includes(task.acceptance_status);
  return <article className="rounded-xl bg-surface p-5 shadow-card">
    <div className="flex flex-wrap items-start justify-between gap-3"><div><div className="flex flex-wrap items-center gap-2"><Badge tone={displayStatus === "completed" ? "ok" : displayStatus === "failed" || displayStatus === "unknown" ? "danger" : active ? "warn" : "default"}>{executionStatus(displayStatus, lang)}</Badge>{execution && task.kind !== "analysis" ? <Badge tone={execution.application_status === "applied" ? "ok" : execution.application_status === "conflict" || execution.application_status === "failed" ? "danger" : execution.application_status === "superseded" ? "default" : "warn"}>{lang === "zh" ? `结果 ${execution.application_status}` : `Result ${execution.application_status}`}</Badge> : null}<Badge tone={task.acceptance_status === "passed" ? "ok" : task.acceptance_status === "failed" ? "danger" : "default"}>{lang === "zh" ? `验收 ${task.acceptance_status}` : `Acceptance ${task.acceptance_status}`}</Badge><span className="font-mono text-[11px] text-subtle">{task.id}</span></div><h3 className="mt-2 font-medium">{task.title}</h3><p className="mt-1 text-sm leading-6 text-muted">{task.objective}</p></div><div className="flex gap-2">{!active && !unavailable && acceptanceOpen && (task.acceptance_status === "failed" || execution?.application_status !== "applied") ? <Button size="sm" onClick={start} disabled={Boolean(working)}><Bot className="size-4" />{execution ? (lang === "zh" ? "新建重试执行" : "Start retry") : (lang === "zh" ? "启动 OpenCode" : "Start OpenCode")}</Button> : null}{active || unavailable ? <Button size="sm" variant="outline" onClick={stop} disabled={Boolean(working)}>{unavailable ? (lang === "zh" ? "关闭不可用执行" : "Close unavailable run") : (lang === "zh" ? "停止" : "Stop")}</Button> : null}</div></div>
    <div className="mt-3 grid gap-2 text-xs sm:grid-cols-3"><div className="rounded bg-bg-elevated p-3"><span className="text-subtle">{lang === "zh" ? "类型" : "Kind"}</span><p className="mt-1">{task.kind}</p></div><div className="rounded bg-bg-elevated p-3"><span className="text-subtle">{lang === "zh" ? "写入范围" : "Write scope"}</span><p className="mt-1 break-all">{task.write_paths.join(" · ") || (lang === "zh" ? "只读" : "Read only")}</p></div><div className="rounded bg-bg-elevated p-3"><span className="text-subtle">{lang === "zh" ? "验证命令" : "Verification"}</span><p className="mt-1">{task.verification_commands.length}</p></div></div>
    {execution ? <ExecutionResult projectId={projectId} task={task} execution={execution} onChange={setExecution} onSaved={onSaved} /> : null}
    {verification ? <div className={`mt-4 rounded-md p-4 ${verification.all_planned_passed ? "bg-ok/10" : "bg-warn/10"}`}><p className={`text-sm font-medium ${verification.all_planned_passed ? "text-ok" : "text-warn"}`}>{verification.all_planned_passed ? (lang === "zh" ? "所有固定验证命令已通过" : "All fixed verification commands passed") : (lang === "zh" ? "验证未完整通过或证据不足" : "Verification is incomplete or did not pass")}</p>{commandEvidence.map((item, index) => <details key={`${item.command}:${index}`} className="mt-2"><summary className="cursor-pointer font-mono text-xs">{item.exit === 0 ? "✓" : "!"} {item.command}</summary><pre className="mt-2 max-h-48 overflow-auto whitespace-pre-wrap rounded bg-surface p-3 font-mono text-[11px] text-muted">{item.output || (lang === "zh" ? "没有记录输出" : "No output recorded")}</pre></details>)}</div> : null}
    {completionReport && execution && ["completed", "failed", "stopped"].includes(execution.status) ? <div className={`mt-4 rounded-md p-4 ${completionReport.valid ? "bg-bg-elevated" : "bg-warn/10"}`}><p className={`text-sm font-medium ${completionReport.valid ? "text-fg" : "text-warn"}`}>{completionReport.valid ? (lang === "zh" ? "Agent 结构化完成报告" : "Structured agent completion report") : (lang === "zh" ? "Agent 完成报告缺失或无效" : "Agent completion report is missing or invalid")}</p><p className="mt-1 text-xs text-subtle">{lang === "zh" ? "此报告经过格式与需求 ID 校验，但仍是 agent 提供的信息，不等于 Atlas 验证或产品验收。" : "Its shape and requirement IDs are validated, but it remains agent-supplied information rather than Atlas verification or product acceptance."}</p>{completionReport.valid ? <div className="mt-3 space-y-2 text-xs">{completionReport.requirements.map((item) => <div key={item.id} className="rounded bg-surface p-3"><p><span className="font-mono">{item.id}</span> · <strong>{item.status}</strong></p>{item.evidence.map((value) => <p key={value} className="mt-1 text-muted">{value}</p>)}</div>)}<ChangePaths title={lang === "zh" ? "未完成项" : "Unfinished"} paths={completionReport.unfinished} /><ChangePaths title={lang === "zh" ? "方案偏离" : "Deviations"} paths={completionReport.deviations} /></div> : <p className="mt-2 font-mono text-xs text-warn">{completionReport.error}</p>}</div> : null}
    {filesystem ? <div className={`mt-4 rounded-md p-4 ${filesystem.scope_compliant ? "bg-ok/10" : "bg-danger/10"}`}><p className={`text-sm font-medium ${filesystem.scope_compliant ? "text-ok" : "text-danger"}`}>{filesystem.scope_compliant ? (lang === "zh" ? "文件变化位于声明范围内" : "File changes stayed within scope") : (lang === "zh" ? "发现超出声明范围的文件变化" : "File changes exceeded the declared scope")}</p><ChangePaths title={lang === "zh" ? "新增" : "Added"} paths={filesystem.added} /><ChangePaths title={lang === "zh" ? "修改" : "Modified"} paths={filesystem.modified} /><ChangePaths title={lang === "zh" ? "删除" : "Removed"} paths={filesystem.removed} />{filesystem.out_of_scope_changes.length ? <ChangePaths title={lang === "zh" ? "越界变化" : "Out-of-scope changes"} paths={filesystem.out_of_scope_changes} /> : null}</div> : null}
    {execution?.raw_state.evidence?.assistant_text ? <details className="mt-4"><summary className="cursor-pointer text-sm text-primary">{lang === "zh" ? "查看引擎结果" : "View engine result"}</summary><div className="mt-3 rounded-md bg-bg-elevated p-4"><Prose md={execution.raw_state.evidence.assistant_text} /></div></details> : null}
    {error ? <p className="mt-3 text-xs text-danger">{error}</p> : null}
  </article>;
}

function ExecutionResult({ projectId, task, execution, onChange, onSaved }: {
  projectId: string; task: ProjectTask; execution: ProjectExecution; onChange: (value: ProjectExecution) => void; onSaved: () => void;
}) {
  const { lang } = useLang(); const [working, setWorking] = useState(""); const [error, setError] = useState(""); const [evidence, setEvidence] = useState(""); const [followUp, setFollowUp] = useState("");
  const acceptanceOpen = ["pending", "failed"].includes(task.acceptance_status);
  const interaction = execution.raw_state.interaction;
  useEffect(() => { setEvidence(""); setFollowUp(""); setError(""); }, [execution.id]);
  useEffect(() => {
    const verification = execution.raw_state.evidence?.verification;
    if (!evidence && verification?.all_planned_passed) setEvidence(
      lang === "zh" ? `Atlas 已记录 ${verification.successful_commands.length} 条固定验证命令通过：${verification.successful_commands.join("；")}` : `Atlas recorded ${verification.successful_commands.length} fixed verification command(s) passing: ${verification.successful_commands.join("; ")}`);
  }, [execution.updated_at]);
  const permission = async (reply: "once" | "always" | "reject") => { if (!interaction?.request.id) return; setWorking(reply); setError(""); try { onChange(await replyProjectExecutionPermission(projectId, execution.id, { request_id: interaction.request.id, reply })); } catch (cause) { setError(String(cause)); } finally { setWorking(""); } };
  const applyResult = async () => { setWorking("apply"); setError(""); try { onChange(await applyProjectExecutionResult(projectId, execution.id)); onSaved(); } catch (cause) { setError(String(cause)); onSaved(); } finally { setWorking(""); } };
  const continueRun = async () => { setWorking("continue"); setError(""); try { onChange(await continueProjectExecution(projectId, execution.id, followUp)); setFollowUp(""); onSaved(); } catch (cause) { setError(String(cause)); onSaved(); } finally { setWorking(""); } };
  const accept = async (status: "passed" | "failed" | "waived") => { setWorking(status); setError(""); try { await recordProjectTaskAcceptance(projectId, task.id, { status, evidence: status === "waived" ? [] : [{ kind: "review", summary: evidence }] }); onSaved(); } catch (cause) { setError(String(cause)); } finally { setWorking(""); } };
  return <div className="mt-4 border-t border-border pt-4">
    <div className="flex flex-wrap items-center gap-2 text-xs"><span className="font-mono text-subtle">{execution.id}</span><span className="text-muted">OpenCode · {execution.input_state.model || "unknown model"}</span><span className="text-subtle">{execution.raw_state.engine_status || execution.status}</span></div>
    {interaction?.type === "permission" ? <div className="mt-3 rounded-md bg-warn/10 p-4"><p className="text-sm font-medium text-warn">{lang === "zh" ? "OpenCode 等待工具权限" : "OpenCode is waiting for tool permission"}</p><p className="mt-2 break-all font-mono text-xs text-muted">{interaction.request.permission || "tool"} · {(interaction.request.patterns || []).join(" · ")}</p><div className="mt-3 flex flex-wrap gap-2"><Button size="sm" disabled={Boolean(working)} onClick={() => permission("once")}>{lang === "zh" ? "仅本次允许" : "Allow once"}</Button><Button size="sm" variant="outline" disabled={Boolean(working)} onClick={() => permission("always")}>{lang === "zh" ? "后续同类允许" : "Always allow"}</Button><Button size="sm" variant="outline" disabled={Boolean(working)} onClick={() => permission("reject")}>{lang === "zh" ? "拒绝" : "Reject"}</Button></div></div> : null}
    {interaction?.type === "question" ? <ExecutionQuestionForm projectId={projectId} execution={execution} onChange={onChange} /> : null}
    {["completed", "failed", "stopped"].includes(execution.status) && acceptanceOpen && (task.kind === "analysis" || ["pending", "conflict", "failed"].includes(execution.application_status)) ? <div className="mt-4 rounded-md border border-border p-4"><p className="text-sm font-medium">{lang === "zh" ? "在当前 OpenCode 会话中继续" : "Continue in this OpenCode session"}</p><p className="mt-1 text-xs leading-5 text-muted">{lang === "zh" ? "后续指令会沿用当前隔离副本和会话上下文，同时建立一条新的执行记录与快照边界。" : "The follow-up keeps the isolated work copy and session context while creating a new execution record and snapshot boundary."}</p><TextArea label={lang === "zh" ? "后续修改或核查要求" : "Follow-up change or review instruction"} value={followUp} onChange={setFollowUp} /><Button className="mt-3" size="sm" variant="outline" disabled={Boolean(working) || !followUp.trim()} onClick={continueRun}>{lang === "zh" ? "继续当前会话" : "Continue session"}</Button></div> : null}
    {execution.status === "completed" && task.kind !== "analysis" && execution.application_status !== "applied" && execution.application_status !== "superseded" ? <div className={`mt-4 rounded-md p-4 ${execution.application_status === "conflict" || execution.application_status === "failed" ? "bg-danger/10" : "bg-primary/10"}`}><p className="text-sm font-medium">{lang === "zh" ? "结果仍在隔离工作副本中" : "The result is still in the isolated work copy"}</p><p className="mt-2 text-xs leading-5 text-muted">{lang === "zh" ? "应用前 Atlas 会再次核对源工作区和已接受基线；有冲突时不会覆盖现有文件。应用成功后，准确写回的状态会成为新的已接受项目基线。" : "Before applying, Atlas rechecks the source workspace and accepted baseline. Conflicts do not overwrite current files. A successful exact write-back becomes the new accepted project baseline."}</p>{execution.application_state.error ? <p className="mt-2 text-xs text-danger">{execution.application_state.error}</p> : null}<Button className="mt-3" size="sm" disabled={Boolean(working) || !execution.raw_state.evidence?.filesystem?.scope_compliant} onClick={applyResult}><Save className="size-4" />{lang === "zh" ? "应用并更新项目基线" : "Apply and update baseline"}</Button></div> : null}
    {["completed", "failed", "stopped"].includes(execution.status) && acceptanceOpen && (task.kind === "analysis" || execution.application_status === "applied") ? <div className="mt-4 rounded-md border border-border p-4"><p className="text-sm font-medium">{task.acceptance_status === "failed" ? (lang === "zh" ? "上次验收失败，可补充证据后重新确认" : "The last acceptance failed; review the result and decide again") : (lang === "zh" ? "产品验收仍待独立确认" : "Product acceptance still needs a separate decision")}</p><TextArea label={lang === "zh" ? "验收证据或失败原因" : "Acceptance evidence or failure reason"} value={evidence} onChange={setEvidence} /><div className="mt-3 flex flex-wrap gap-2"><Button size="sm" disabled={Boolean(working) || !evidence.trim()} onClick={() => accept("passed")}>{lang === "zh" ? "验收通过" : "Pass"}</Button><Button size="sm" variant="outline" disabled={Boolean(working) || !evidence.trim()} onClick={() => accept("failed")}>{lang === "zh" ? "验收失败" : "Fail"}</Button><Button size="sm" variant="outline" disabled={Boolean(working)} onClick={() => accept("waived")}>{lang === "zh" ? "明确免验" : "Waive"}</Button></div></div> : null}
    {error ? <p className="mt-3 text-xs text-danger">{error}</p> : null}
  </div>;
}

function ExecutionQuestionForm({ projectId, execution, onChange }: {
  projectId: string; execution: ProjectExecution; onChange: (value: ProjectExecution) => void;
}) {
  const { lang } = useLang(); const questions = execution.raw_state.interaction?.request.questions || [];
  const [answers, setAnswers] = useState<string[]>(questions.map(() => "")); const [working, setWorking] = useState(false); const [error, setError] = useState("");
  const submit = async () => { const requestId = execution.raw_state.interaction?.request.id; if (!requestId) return; setWorking(true); setError(""); try { onChange(await replyProjectExecutionQuestion(projectId, execution.id, { request_id: requestId, answers: answers.map((value) => value.split(",").map((item) => item.trim()).filter(Boolean)) })); } catch (cause) { setError(String(cause)); } finally { setWorking(false); } };
  const reject = async () => { const requestId = execution.raw_state.interaction?.request.id; if (!requestId) return; setWorking(true); setError(""); try { onChange(await replyProjectExecutionQuestion(projectId, execution.id, { request_id: requestId, reject: true })); } catch (cause) { setError(String(cause)); } finally { setWorking(false); } };
  return <div className="mt-3 rounded-md bg-warn/10 p-4"><p className="text-sm font-medium text-warn">{lang === "zh" ? "OpenCode 需要你的输入" : "OpenCode needs your input"}</p><div className="mt-3 space-y-3">{questions.map((question, index) => <div key={`${question.header}:${index}`}><p className="text-sm">{question.question}</p>{question.options.length ? <p className="mt-1 text-xs leading-5 text-muted">{question.options.map((item) => `${item.label}：${item.description}`).join(" · ")}</p> : null}<Field label={question.multiple ? (lang === "zh" ? "答案（多选用逗号分隔）" : "Answer (comma-separated for multiple)") : (lang === "zh" ? "答案" : "Answer")} value={answers[index] || ""} onChange={(value) => setAnswers((items) => items.map((item, offset) => offset === index ? value : item))} required /></div>)}</div><div className="mt-3 flex gap-2"><Button size="sm" disabled={working || answers.some((value) => !value.trim())} onClick={submit}>{lang === "zh" ? "提交答案" : "Submit answers"}</Button><Button size="sm" variant="outline" disabled={working} onClick={reject}>{lang === "zh" ? "拒绝回答" : "Reject question"}</Button></div>{error ? <p className="mt-2 text-xs text-danger">{error}</p> : null}</div>;
}

function executionStatus(status: ProjectTask["execution_status"], lang: "zh" | "en") {
  const zh: Record<ProjectTask["execution_status"], string> = { planned: "待执行", queued: "排队中", running: "执行中", waiting_permission: "等待权限", waiting_input: "等待输入", completed: "执行完成", failed: "执行失败", stopped: "已停止", unknown: "待核对" };
  return lang === "zh" ? zh[status] : status.replaceAll("_", " ");
}

function WorkspaceBaselinePanel({ projectId, onSaved, onBaselineChange }: {
  projectId: string; onSaved: () => void;
  onBaselineChange: (value: boolean) => void;
}) {
  const { lang } = useLang();
  const [baselines, setBaselines] = useState<WorkspaceBaselineSummary[]>([]);
  const [check, setCheck] = useState<WorkspaceBaselineCheck | null>(null);
  const [focus, setFocus] = useState("");
  const [loading, setLoading] = useState(true);
  const [working, setWorking] = useState<"capture" | "check" | "">("");
  const [error, setError] = useState("");
  const latest = baselines[0] || null;

  useEffect(() => {
    let alive = true;
    setLoading(true); setError(""); setCheck(null);
    listWorkspaceBaselines(projectId).then(
      (items) => {
        if (!alive) return;
        setBaselines(items);
        onBaselineChange(items.length > 0);
        setFocus(items[0]?.coverage.focus_paths.join("\n") || "");
      },
      (cause) => { if (alive) setError(String(cause)); },
    ).finally(() => { if (alive) setLoading(false); });
    return () => { alive = false; };
  }, [projectId]);

  const capture = async () => {
    if (latest && !check) {
      setError(lang === "zh" ? "请先检查当前工作区变化。" : "Check the current workspace before adoption.");
      return;
    }
    setWorking("capture"); setError("");
    try {
      const created = await captureWorkspaceBaseline(projectId, {
        focus_paths: lines(focus),
        ...(latest && check ? {
          expected_baseline_id: latest.id,
          expected_content_fingerprint: check.current.content_fingerprint,
        } : {}),
      });
      setBaselines((items) => [created, ...items]);
      onBaselineChange(true);
      setFocus(created.coverage.focus_paths.join("\n"));
      setCheck(null);
      onSaved();
    } catch (cause) { setError(String(cause)); } finally { setWorking(""); }
  };

  const inspect = async () => {
    setWorking("check"); setError("");
    try { setCheck(await checkWorkspaceChanges(projectId)); }
    catch (cause) { setError(String(cause)); } finally { setWorking(""); }
  };

  const changes = check?.changes;
  const focusChanged = Boolean(latest && lines(focus).join("\n") !== latest.coverage.focus_paths.join("\n"));
  const mayAdopt = Boolean(changes && (
    changes.changed || changes.git_state_changed || changes.comparison_limited_by_errors || focusChanged));
  return <section className="mt-8 rounded-xl bg-surface p-5 shadow-card">
    <div className="flex flex-wrap items-start justify-between gap-4">
      <div className="flex max-w-2xl items-start gap-3">
        <FolderGit2 className="mt-0.5 size-5 shrink-0 text-primary" />
        <div><h2 className="font-serif text-xl font-medium">{lang === "zh" ? "项目工作区基线" : "Project workspace baseline"}</h2>
          <p className="mt-1 text-xs leading-5 text-subtle">{lang === "zh" ? "记录文件指纹、Git 状态、已读取证据和未检查范围。检查变化不会修改已接受基线；确认后才采用当前状态。" : "Record file fingerprints, Git state, read evidence, and unchecked scope. Change checks do not mutate the accepted baseline; the current state is adopted only after review."}</p></div>
      </div>
      <div className="flex flex-wrap gap-2">
        {latest ? <Button size="sm" variant="outline" disabled={Boolean(working)} onClick={inspect}><RefreshCw className={`size-4 ${working === "check" ? "animate-spin" : ""}`} />{lang === "zh" ? "检查外部变化" : "Check external changes"}</Button> : null}
        {!latest ? <Button size="sm" disabled={Boolean(working) || loading} onClick={capture}><FolderGit2 className="size-4" />{lang === "zh" ? "建立项目基线" : "Create baseline"}</Button> : null}
      </div>
    </div>

    <div className="mt-5 grid gap-5 lg:grid-cols-[minmax(0,1fr)_20rem]">
      <div>
        {loading ? <p className="text-sm text-subtle">{lang === "zh" ? "正在读取基线…" : "Loading baselines…"}</p> : null}
        {!loading && !latest ? <div className="rounded-lg bg-bg-elevated p-4 text-sm leading-6 text-muted">{lang === "zh" ? "还没有已接受基线。首次建立会扫描工作区全部文件的元数据和内容指纹，并读取入口文档、工程清单及重点路径中的文本。" : "There is no accepted baseline yet. The first capture fingerprints all workspace files and reads entry documents, manifests, and text under the focus paths."}</div> : null}
        {latest ? <div className="rounded-lg bg-bg-elevated p-4">
          <div className="flex flex-wrap items-center gap-2"><Badge tone="ok">{lang === "zh" ? "已接受基线" : "Accepted baseline"}</Badge><span className="font-mono text-[11px] text-subtle">{latest.id}</span></div>
          <div className="mt-3 grid gap-2 text-xs text-muted sm:grid-cols-2 lg:grid-cols-4">
            <div><span className="text-subtle">{lang === "zh" ? "文件" : "Files"}</span><p className="mt-1 font-medium text-fg">{latest.inventory.file_count}</p></div>
            <div><span className="text-subtle">{lang === "zh" ? "读取正文" : "Read content"}</span><p className="mt-1 font-medium text-fg">{latest.coverage.read_paths.length}</p></div>
            <div><span className="text-subtle">Git</span><p className="mt-1 truncate font-medium text-fg">{latest.git.repository ? (latest.git.branch || "detached") : (lang === "zh" ? "非仓库" : "Not a repo")}</p></div>
            <div><span className="text-subtle">{lang === "zh" ? "记录时间" : "Captured"}</span><p className="mt-1 font-medium text-fg">{new Date(latest.created_at).toLocaleString(lang === "zh" ? "zh-CN" : "en")}</p></div>
          </div>
          <p className="mt-3 break-all font-mono text-[10px] text-subtle">content {latest.content_fingerprint.slice(0, 16)} · record {latest.fingerprint.slice(0, 16)}</p>
          <details className="mt-4 border-t border-border pt-3"><summary className="cursor-pointer text-sm text-primary">{lang === "zh" ? "查看现状证据报告" : "View evidence report"}</summary><div className="mt-4"><Prose md={latest.report_markdown} /></div></details>
        </div> : null}

        {changes ? <div className="mt-4 rounded-lg border border-border p-4">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <div className="flex flex-wrap items-center gap-2"><Badge tone={changes.requires_focused_review ? "warn" : "ok"}>{changes.requires_focused_review ? (lang === "zh" ? "重点范围需要复核" : "Focus review required") : (lang === "zh" ? "重点范围未变化" : "Focus scope unchanged")}</Badge><span className="text-xs text-subtle">+{changes.added.length} · ~{changes.modified.length} · −{changes.removed.length}</span></div>
            {mayAdopt ? <Button size="sm" disabled={Boolean(working)} onClick={capture}>{lang === "zh" ? "采用当前状态为新基线" : "Adopt current state"}</Button> : null}
          </div>
          {changes.git_revision_changed ? <p className="mt-3 flex gap-2 text-xs leading-5 text-warn"><AlertTriangle className="mt-0.5 size-4 shrink-0" />{lang === "zh" ? "Git 分支、提交或仓库边界已变化，需要复核重点范围。" : "The Git branch, revision, or repository boundary changed and requires focus review."}</p> : null}
          <ChangePaths title={lang === "zh" ? "已读取或重点范围内" : "Read or focused scope"} paths={changes.reviewed_scope_changes} />
          <ChangePaths title={lang === "zh" ? "当前审阅范围外" : "Outside current review scope"} paths={changes.outside_review_scope_changes} />
          {changes.has_unread_changes ? <p className="mt-3 text-xs leading-5 text-subtle">{lang === "zh" ? "范围外变化只表示本次没有读取其正文；系统不会据此断言它无关，也不会强制重做整份分析。" : "Outside-scope changes mean their content was not read in this review. They are not declared irrelevant and do not force a full reanalysis."}</p> : null}
          {focusChanged ? <p className="mt-3 text-xs leading-5 text-primary">{lang === "zh" ? "重点读取路径已编辑；采用后会按新范围建立报告。" : "The focus paths were edited. Adoption will create a report with the new scope."}</p> : null}
          {!changes.changed && !changes.git_state_changed && !changes.comparison_limited_by_errors ? <p className="mt-3 text-sm text-ok">{lang === "zh" ? "工作区与已接受基线一致。" : "The workspace matches the accepted baseline."}</p> : null}
          {changes.comparison_limited_by_errors ? <p className="mt-3 text-xs text-danger">{lang === "zh" ? "部分路径读取失败，比较结论受限。" : "Some paths could not be read, so the comparison is limited."}</p> : null}
        </div> : null}
        {error ? <p className="mt-4 rounded-md bg-danger/10 p-3 text-xs leading-5 text-danger">{error}</p> : null}
      </div>

      <div className="rounded-lg border border-border p-4">
        <TextArea label={lang === "zh" ? "重点读取路径（每行一个相对路径）" : "Focus paths (one relative path per line)"} value={focus} onChange={setFocus} rows={6} />
        <p className="mt-2 text-[11px] leading-5 text-subtle">{lang === "zh" ? "留空时仍读取 README、docs 文档和工程清单。修改此列表会在采用下一份基线时生效。" : "README files, docs, and manifests are still read when empty. Changes take effect when the next baseline is adopted."}</p>
        {latest ? <div className="mt-4 border-t border-border pt-4 text-xs leading-5 text-muted"><p>{lang === "zh" ? `共 ${baselines.length} 份不可变基线` : `${baselines.length} immutable baseline(s)`}</p><p className="mt-1 break-all font-mono text-[10px] text-subtle">{latest.root}</p>{latest.git.head ? <p className="mt-1 font-mono text-[10px] text-subtle">HEAD {latest.git.head.slice(0, 12)}{latest.git.dirty ? " · dirty" : ""}</p> : null}</div> : null}
      </div>
    </div>
  </section>;
}

function ChangePaths({ title, paths }: { title: string; paths: string[] }) {
  return <div className="mt-3"><p className="text-xs font-medium">{title} · {paths.length}</p>{paths.length ? <div className="mt-1 max-h-28 overflow-auto rounded bg-bg-elevated px-3 py-2 font-mono text-[11px] leading-5 text-muted">{paths.map((path) => <div key={path}>{path}</div>)}</div> : <p className="mt-1 text-xs text-subtle">—</p>}</div>;
}

function GenerationPanel({ projectId, workspace, onSaved, onAnalysis }: {
  projectId: string; workspace: ProjectWorkspace; onSaved: () => void;
  onAnalysis: (run: ProjectGenerationRun | null) => void;
}) {
  const { lang } = useLang();
  const [runs, setRuns] = useState<ProjectGenerationRun[]>([]);
  const [selectedRunId, setSelectedRunId] = useState("");
  const [selectedKinds, setSelectedKinds] = useState<ProjectDocumentKind[]>(CORE_DOCUMENT_BUNDLE);
  const [compact, setCompact] = useState(true);
  const [improvementGoal, setImprovementGoal] = useState("");
  const [error, setError] = useState("");
  const [starting, setStarting] = useState(false);
  const [applying, setApplying] = useState("");
  const run = runs.find((item) => item.id === selectedRunId) || null;
  const hasConfirmedScope = workspace.requirements.some((item) => item.confirmed_scope === "current");
  const active = run?.status === "queued" || run?.status === "running";
  const hasActiveRun = runs.some((item) => item.status === "queued" || item.status === "running");

  useEffect(() => {
    let alive = true;
    listProjectGenerations(projectId).then(
      (items) => {
        if (!alive) return;
        setRuns(items);
        setSelectedRunId(items[0]?.id || "");
        onAnalysis(items.find((item) =>
          (item.mode === "analysis" || item.mode === "improvement")
          && item.status === "completed") || null);
      },
      (cause) => { if (alive) setError(String(cause)); },
    );
    return () => { alive = false; };
  }, [projectId]);

  useEffect(() => {
    if (!hasActiveRun) return;
    let alive = true;
    const timer = window.setInterval(() => {
      listProjectGenerations(projectId).then(
        (items) => {
          if (!alive) return;
          setRuns(items);
          const latestAnalysis = items.find((item) =>
            (item.mode === "analysis" || item.mode === "improvement")
            && item.status === "completed");
          if (latestAnalysis) onAnalysis(latestAnalysis);
        },
        (cause) => { if (alive) setError(String(cause)); },
      );
    }, 1500);
    return () => { alive = false; window.clearInterval(timer); };
  }, [hasActiveRun, projectId]);

  const start = async (mode: "analysis" | "value" | "documents" | "improvement") => {
    setStarting(true); setError("");
    try {
      const created = await startProjectGeneration(projectId, {
        mode, ...(mode === "documents" ? { document_kinds: selectedKinds } : {}),
        ...(mode === "improvement" ? { improvement_goal: improvementGoal.trim() } : {}),
      });
      setRuns((items) => [created, ...items.filter((item) => item.id !== created.id)]);
      setSelectedRunId(created.id);
    } catch (cause) { setError(String(cause)); } finally { setStarting(false); }
  };
  const apply = async (itemKind: "requirement" | "document", index: number) => {
    if (!run) return;
    const key = `${itemKind}:${index}`; setApplying(key); setError("");
    try {
      const result = await applyProjectGenerationItem(
        projectId, run.id, { item_kind: itemKind, index });
      setRuns((items) => items.map((item) => item.id === result.run.id ? result.run : item));
      if (result.run.mode === "analysis" || result.run.mode === "improvement") {
        onAnalysis(result.run);
      }
      onSaved();
    } catch (cause) { setError(String(cause)); } finally { setApplying(""); }
  };
  const result = run?.result;
  const choosePreset = (value: ProjectDocumentKind[]) => setSelectedKinds([...value]);
  const toggleKind = (kind: ProjectDocumentKind) => setSelectedKinds((items) =>
    items.includes(kind) ? items.filter((item) => item !== kind)
      : DOCUMENT_BUNDLE_KINDS.map((item) => item.value).filter(
        (item) => [...items, kind].includes(item)));
  return <section className="mt-8 rounded-xl bg-surface p-5 shadow-card">
    <div className="flex flex-wrap items-start justify-between gap-4">
      <div className="flex max-w-2xl items-start gap-3"><Bot className="mt-0.5 size-5 text-primary" /><div>
        <h2 className="font-serif text-xl font-medium">{lang === "zh" ? "资料分析与文档草案" : "Source analysis & document drafts"}</h2>
        <p className="mt-1 text-xs leading-5 text-subtle">{lang === "zh" ? "OpenCode 只读取本项目已固定的依据。输出先作为 AI 建议供审阅，需求不会自动获得用户确认，文档也不会自动覆盖现有版本。" : "OpenCode reads only this project's pinned input. Results remain reviewable AI proposals; requirements are never user-confirmed automatically and documents never overwrite a newer version."}</p>
      </div></div>
      <div className="flex flex-wrap items-end gap-2">
        <Button size="sm" variant="outline" disabled={starting || hasActiveRun} onClick={() => start("analysis")}><Sparkles className="size-4" />{lang === "zh" ? "分析固定资料" : "Analyze pinned sources"}</Button>
      </div>
    </div>
    <div className="mt-4 flex flex-wrap items-center justify-between gap-3 rounded-lg border border-primary/20 bg-primary/[0.04] p-4">
      <div className="max-w-2xl"><p className="text-sm font-medium">{lang === "zh" ? "可选价值分析" : "Optional value analysis"}</p><p className="mt-1 text-[11px] leading-5 text-subtle">{lang === "zh" ? "整理有依据的观察、未知、替代方案、差异化假设、成本风险和小型验证实验。结果只供判断和取舍，不评分、不通过或否决想法，也不改变需求范围或阻止后续工作。" : "Organizes evidence-backed observations, unknowns, alternatives, differentiation hypotheses, cost and risk signals, and small validation experiments. It offers advice only: no score, approval, rejection, scope change, or development block."}</p></div>
      <Button size="sm" variant="outline" disabled={starting || hasActiveRun || !workspace.references.length} onClick={() => start("value")}><Sparkles className="size-4" />{lang === "zh" ? "评估想法价值（仅建议）" : "Analyze value (advice only)"}</Button>
    </div>
    <div className="mt-4 rounded-lg border border-border p-4">
      <div className="flex flex-wrap items-center justify-between gap-3"><div><p className="text-sm font-medium">{lang === "zh" ? "按依赖生成文档集合" : "Generate a dependency-aware document set"}</p><p className="mt-1 text-[11px] leading-5 text-subtle">{lang === "zh" ? "Atlas 固定生成顺序；保存下游草案时会引用本轮已保存上游的不可变版本。" : "Atlas fixes generation order and links saved downstream drafts to immutable upstream versions from this run."}</p></div><div className="flex gap-2">
        <Button size="sm" variant={sameKinds(selectedKinds, CORE_DOCUMENT_BUNDLE) ? "default" : "outline"} onClick={() => choosePreset(CORE_DOCUMENT_BUNDLE)}>{lang === "zh" ? "核心 4 份" : "Core 4"}</Button>
        <Button size="sm" variant={sameKinds(selectedKinds, FULL_DOCUMENT_BUNDLE) ? "default" : "outline"} onClick={() => choosePreset(FULL_DOCUMENT_BUNDLE)}>{lang === "zh" ? "完整 6 份" : "Full 6"}</Button>
      </div></div>
      <fieldset className="mt-3"><legend className="sr-only">{lang === "zh" ? "选择文档类型" : "Choose document kinds"}</legend><div className="grid gap-2 sm:grid-cols-2 lg:grid-cols-3">{DOCUMENT_BUNDLE_KINDS.map((item) => <label key={item.value} className="flex items-center gap-2 rounded-md bg-bg-elevated px-3 py-2 text-xs text-muted"><input type="checkbox" checked={selectedKinds.includes(item.value)} onChange={() => toggleKind(item.value)} /><span>{lang === "zh" ? item.zh : item.en}</span></label>)}</div></fieldset>
      <div className="mt-3 flex flex-wrap items-center justify-between gap-3"><p className="text-[11px] text-subtle">{lang === "zh" ? `已选 ${selectedKinds.length} 份；可逐份审阅，必须按依赖顺序保存。` : `${selectedKinds.length} selected; review individually and save in dependency order.`}</p><Button size="sm" disabled={starting || hasActiveRun || !hasConfirmedScope || !selectedKinds.length} onClick={() => start("documents")}><FileText className="size-4" />{lang === "zh" ? `生成 ${selectedKinds.length} 份草案` : `Generate ${selectedKinds.length} drafts`}</Button></div>
    </div>
    <div className="mt-4 grid gap-3 rounded-lg border border-border p-4 md:grid-cols-[minmax(0,1fr)_auto] md:items-end">
      <TextArea label={lang === "zh" ? "本轮局部改进目标" : "Improvement goal for this iteration"} value={improvementGoal} onChange={setImprovementGoal} rows={2} />
      <Button size="sm" disabled={starting || hasActiveRun || !improvementGoal.trim() || !workspace.references.length} onClick={() => start("improvement")}><FolderGit2 className="size-4" />{lang === "zh" ? "生成项目改进方案" : "Generate improvement plan"}</Button>
      <p className="text-[11px] leading-5 text-subtle md:col-span-2">{lang === "zh" ? "使用已接受工作区基线和已固定 Atlas 资料，输出当前/期望行为、影响范围、任务依赖与回归条件。工作区有未采用变化时会拒绝启动。" : "Uses the accepted workspace baseline and pinned Atlas sources to produce current/expected behavior, impact, task dependencies, and regression conditions. A changed workspace must be reviewed and adopted first."}</p>
    </div>
    {!workspace.references.length ? <p className="mt-3 text-xs text-warn">{lang === "zh" ? "改进方案需要至少一份已固定的类型或应用资料。" : "An improvement plan requires at least one pinned type or application source."}</p> : null}
    {!hasConfirmedScope ? <p className="mt-3 text-xs text-warn">{lang === "zh" ? "生成产品与开发文档前，至少确认一条本版需求。资料分析可以先运行。" : "Confirm at least one current requirement before generating product or development documents. Source analysis can run first."}</p> : null}
    {runs.length ? <div className="mt-4 flex flex-wrap items-end justify-between gap-3 border-t border-border pt-4"><label className="text-xs text-muted"><span className="block">{lang === "zh" ? "生成历史" : "Generation history"}</span><select value={selectedRunId} onChange={(event) => setSelectedRunId(event.target.value)} className={`${inputClass} mt-1 h-9 min-w-72`}>{runs.map((item) => <option key={item.id} value={item.id}>{new Date(item.created_at).toLocaleString(lang === "zh" ? "zh-CN" : "en")} · {item.mode} · {item.status}</option>)}</select></label><div className="flex gap-2"><Button size="sm" variant={compact ? "default" : "outline"} onClick={() => setCompact(true)}>{lang === "zh" ? "简要" : "Compact"}</Button><Button size="sm" variant={!compact ? "default" : "outline"} onClick={() => setCompact(false)}>{lang === "zh" ? "完整" : "Full"}</Button></div></div> : null}
    {run ? <div className="mt-3 flex flex-wrap items-center gap-2 text-xs text-subtle">
      <Badge tone={run.status === "completed" ? "ok" : run.status === "failed" ? "warn" : "default"}>{run.status}</Badge>
      <span className="font-mono">{run.id}</span><span>{run.mode} · {run.engine}{run.model ? ` · ${run.model}` : ""}</span>
      <span className="font-mono">input {run.input_fingerprint.slice(0, 12)}</span>
      {run.engine_session_id ? <span className="font-mono">{run.engine_session_id}</span> : null}
      {run.mode === "value" ? <span className="rounded bg-primary/10 px-2 py-1 text-primary">{lang === "zh" ? "仅供参考，不改变范围" : "Advisory only; scope unchanged"}</span> : null}
    </div> : null}
    {active ? <p className="mt-4 text-sm text-muted">{lang === "zh" ? (run?.status === "queued" ? "等待文档执行器…" : "正在分析固定输入…") : (run?.status === "queued" ? "Waiting for the document runner…" : "Analyzing fixed input…")}</p> : null}
    {run?.status === "failed" ? <p className="mt-4 rounded-md bg-danger/10 p-3 text-xs text-danger">{run.error}</p> : null}
    {error ? <p className="mt-4 text-xs text-danger">{error}</p> : null}
    {result ? <div className="mt-5 grid gap-5 border-t border-border pt-5 lg:grid-cols-2">
      <div className="space-y-4">
        <ProposalList title={lang === "zh" ? "需要用户回答" : "Questions for the user"} items={result.questions.map((item) => ({ title: item.question, text: item.why }))} empty={lang === "zh" ? "没有生成新的关键问题。" : "No new critical questions."} />
        <ProposalList title={lang === "zh" ? "明确冲突" : "Explicit conflicts"} items={result.conflicts.map((item) => ({ title: item.summary, text: item.impact || "" }))} empty={lang === "zh" ? "生成结果没有报告有依据的明确冲突。" : "The result reports no evidence-backed explicit conflicts."} />
        <ProposalList title={lang === "zh" ? "参考建议" : "Suggestions"} items={result.suggestions.map((item) => ({ title: item.summary, text: item.reason || "" }))} empty={lang === "zh" ? "没有额外参考建议。" : "No additional suggestions."} />
      </div>
      <div className="space-y-4">
        {result.requirements.map((item, index) => {
          const applied = run.applied.requirements[String(index)];
          return <article key={item.key} className="rounded-lg bg-bg-elevated p-4"><div className="flex items-start justify-between gap-3"><div><p className="text-[11px] text-primary">{lang === "zh" ? "AI 候选需求" : "AI candidate requirement"} · {scopeLabel(item.recommended_scope, lang)}</p><h3 className="mt-1 text-sm font-medium leading-6">{item.content}</h3></div><Button size="sm" variant="outline" disabled={Boolean(applied) || applying === `requirement:${index}`} onClick={() => apply("requirement", index)}>{applied ? (lang === "zh" ? "已加入" : "Added") : (lang === "zh" ? "加入候选" : "Add candidate")}</Button></div><p className="mt-2 text-xs leading-5 text-muted">{item.recommendation_reason}</p></article>;
        })}
        {result.documents.map((item, index) => {
          const applied = run.applied.documents[String(index)];
          const dependencies = item.depends_on || [];
          const unmet = dependencies.filter((dependency) => {
            const dependencyIndex = result.documents.findIndex((candidate) => candidate.kind === dependency);
            return dependencyIndex < 0 || !run.applied.documents[String(dependencyIndex)];
          });
          const content = <div className="mt-3 max-h-80 overflow-auto rounded-md bg-surface p-3"><Prose md={item.content} /></div>;
          return <article key={`${item.kind}:${index}`} className="rounded-lg bg-bg-elevated p-4"><div className="flex items-start justify-between gap-3"><div><p className="text-[11px] text-primary">{lang === "zh" ? `第 ${index + 1}/${result.documents.length} 份` : `${index + 1} of ${result.documents.length}`} · {documentKind(item.kind, lang)}</p><h3 className="mt-1 text-sm font-medium">{item.title}</h3>{dependencies.length ? <p className="mt-1 text-[11px] text-subtle">{lang === "zh" ? "依赖" : "Depends on"}: {dependencies.map((value) => documentKind(value, lang)).join(" · ")}</p> : null}{unmet.length ? <p className="mt-1 text-[11px] text-warn">{lang === "zh" ? "请先保存" : "Save first"}: {unmet.map((value) => documentKind(value, lang)).join(" · ")}</p> : null}</div><Button size="sm" variant="outline" disabled={Boolean(applied) || Boolean(unmet.length) || applying === `document:${index}`} onClick={() => apply("document", index)}>{applied ? (lang === "zh" ? "已保存" : "Saved") : item.document_id ? (lang === "zh" ? "保存为新版本" : "Save new version") : (lang === "zh" ? "创建关联文档" : "Create document")}</Button></div>{compact ? <details className="mt-3"><summary className="cursor-pointer text-xs text-primary">{lang === "zh" ? "查看完整草案" : "View full draft"}</summary>{content}</details> : content}</article>;
        })}
      </div>
    </div> : null}
  </section>;
}

function ProposalList({ title, items, empty }: { title: string; items: { title: string; text: string }[]; empty: string }) {
  return <div><h3 className="text-sm font-medium">{title}</h3><div className="mt-2 space-y-2">{items.map((item, index) => <div key={`${item.title}:${index}`} className="rounded-md bg-bg-elevated p-3"><p className="text-sm">{item.title}</p>{item.text ? <p className="mt-1 text-xs leading-5 text-muted">{item.text}</p> : null}</div>)}{!items.length ? <p className="text-xs text-subtle">{empty}</p> : null}</div></div>;
}

function ConsistencyPanel({ workspace, analysisRun }: {
  workspace: ProjectWorkspace; analysisRun: ProjectGenerationRun | null;
}) {
  const { lang } = useLang();
  const pending = workspace.requirements.filter((item) => !item.confirmed_scope);
  const review = workspace.documents.filter((item) => item.review.status === "needs_review");
  const recommended = workspace.requirements.filter((item) => item.recommended_scope && !item.confirmed_scope);
  const analysis = analysisRun?.result;
  const openCandidates = analysis?.requirements.filter(
    (_item, index) => !analysisRun?.applied.requirements[String(index)]) || [];
  const decisions = pending.length + (analysis?.questions.length || 0);
  const suggestions = recommended.length + openCandidates.length + (analysis?.suggestions.length || 0);
  return (
    <section className="mt-6 rounded-xl bg-primary/[0.06] p-5 ring-1 ring-primary/15">
      <h2 className="font-medium">{lang === "zh" ? "一致性信号" : "Consistency signals"}</h2>
      <div className="mt-4 grid gap-3 md:grid-cols-2 xl:grid-cols-4">
        <Signal title={lang === "zh" ? "明确冲突" : "Explicit conflicts"}
          count={analysis ? analysis.conflicts.length : (lang === "zh" ? "未检查" : "Not checked")}
          text={analysis
            ? (analysis.conflicts.length
              ? (lang === "zh" ? "最近一次固定输入分析发现了可定位的明确冲突。" : "The latest fixed-input analysis found evidence-backed explicit conflicts.")
              : (lang === "zh" ? "最近一次固定输入分析未报告明确冲突；这不代表未来输入也没有冲突。" : "The latest fixed-input analysis reported no explicit conflict; future input may differ."))
            : (lang === "zh" ? "尚未完成固定输入分析，不能推断为“没有冲突”。" : "No fixed-input analysis has completed, so absence of conflict cannot be inferred.")}
          muted={!analysis} />
        <Signal title={lang === "zh" ? "需要决定" : "Needs a decision"} count={decisions}
          text={decisions
            ? (lang === "zh" ? `${pending.length} 条需求待确认，${analysis?.questions.length || 0} 个分析问题待回答。` : `${pending.length} requirements await confirmation and ${analysis?.questions.length || 0} analysis questions await answers.`)
            : (lang === "zh" ? "当前没有待确认需求或分析问题。" : "No requirements or analysis questions await a decision.")} />
        <Signal title={lang === "zh" ? "参考建议" : "Suggestions"} count={suggestions}
          text={suggestions
            ? (lang === "zh" ? `${recommended.length} 条已保存范围建议，${openCandidates.length} 条未加入候选，${analysis?.suggestions.length || 0} 条分析建议。` : `${recommended.length} saved scope recommendations, ${openCandidates.length} unapplied candidates, and ${analysis?.suggestions.length || 0} analysis suggestions.`)
            : (lang === "zh" ? "当前没有未处理的参考建议。" : "There are no pending suggestions.")} />
        <Signal title={lang === "zh" ? "关联复核" : "Linked reviews"} count={review.length}
          text={review.length
            ? (lang === "zh" ? `${review.length} 份文档因依据变化待复核。` : `${review.length} documents need review after basis changes.`)
            : (lang === "zh" ? "关联文档的固定依据均为当前版本。" : "All linked documents use current pinned basis versions.")} />
      </div>
    </section>
  );
}

function RequirementForm({ projectId, references, onSaved }: {
  projectId: string; references: ProjectReference[]; onSaved: () => void;
}) {
  const { lang } = useLang();
  const [content, setContent] = useState("");
  const [recommended, setRecommended] = useState<"" | ProjectScope>("");
  const [reason, setReason] = useState("");
  const [acceptance, setAcceptance] = useState("");
  const [referenceIds, setReferenceIds] = useState<string[]>([]);
  const [error, setError] = useState("");
  const [saving, setSaving] = useState(false);
  const submit = async (event: FormEvent) => {
    event.preventDefault(); setSaving(true); setError("");
    try {
      await createProjectRequirement(projectId, {
        content, ...(recommended ? { recommended_scope: recommended } : {}),
        recommendation_reason: reason,
        acceptance_conditions: lines(acceptance), reference_ids: referenceIds,
      });
      setContent(""); setRecommended(""); setReason(""); setAcceptance(""); setReferenceIds([]);
      onSaved();
    } catch (cause) { setError(String(cause)); } finally { setSaving(false); }
  };
  return (
    <SideForm title={lang === "zh" ? "添加候选需求" : "Add candidate requirement"} icon={Plus}>
      <form className="space-y-4" onSubmit={submit}>
        <TextArea label={lang === "zh" ? "需求内容" : "Requirement"} value={content} onChange={setContent} required />
        <label className="block text-sm"><span className="text-muted">{lang === "zh" ? "分析建议（不是用户确认）" : "Analysis recommendation (not confirmation)"}</span>
          <select value={recommended} onChange={(event) => setRecommended(event.target.value as "" | ProjectScope)} className={inputClass}>
            <option value="">{lang === "zh" ? "暂不建议" : "No recommendation"}</option>
            <option value="current">{lang === "zh" ? "建议本版" : "Recommend current"}</option>
            <option value="later">{lang === "zh" ? "建议以后" : "Recommend later"}</option>
            <option value="excluded">{lang === "zh" ? "建议不做" : "Recommend exclude"}</option>
          </select>
        </label>
        <TextArea label={lang === "zh" ? "建议理由" : "Recommendation reason"} value={reason} onChange={setReason} />
        <TextArea label={lang === "zh" ? "验收条件（每行一条）" : "Acceptance conditions (one per line)"} value={acceptance} onChange={setAcceptance} />
        <ReferencePicker references={references} selected={referenceIds} onChange={setReferenceIds} />
        {error ? <p className="text-xs text-danger">{error}</p> : null}
        <Button className="w-full" disabled={saving}>{saving ? (lang === "zh" ? "保存中…" : "Saving…") : (lang === "zh" ? "保存候选需求" : "Save candidate")}</Button>
      </form>
    </SideForm>
  );
}

function RequirementCard({ projectId, requirement, references, onSaved }: {
  projectId: string; requirement: ProjectRequirement; references: ProjectReference[]; onSaved: () => void;
}) {
  const { lang } = useLang();
  const [scope, setScope] = useState<ProjectScope>(requirement.confirmed_scope || requirement.recommended_scope || "current");
  const [reason, setReason] = useState(requirement.confirmation_reason);
  const [content, setContent] = useState(requirement.content);
  const [acceptance, setAcceptance] = useState(requirement.acceptance_conditions.join("\n"));
  const [referenceIds, setReferenceIds] = useState(requirement.reference_ids);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");
  const confirm = async () => {
    setSaving(true); setError("");
    try { await confirmProjectRequirement(projectId, requirement.id, { scope, reason }); onSaved(); }
    catch (cause) { setError(String(cause)); } finally { setSaving(false); }
  };
  const edit = async () => {
    setSaving(true); setError("");
    try {
      await updateProjectRequirement(projectId, requirement.id, {
        content, acceptance_conditions: lines(acceptance), reference_ids: referenceIds,
      });
      onSaved();
    } catch (cause) { setError(String(cause)); } finally { setSaving(false); }
  };
  return (
    <article className="rounded-xl bg-surface p-5 shadow-card">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div className="min-w-0 flex-1">
          <div className="flex flex-wrap items-center gap-2">
            <span className="font-mono text-[11px] text-subtle">{requirement.id}</span>
            <Badge tone={requirement.confirmed_scope ? "ok" : "warn"}>
              {requirement.confirmed_scope ? (lang === "zh" ? "用户已确认" : "User confirmed") : (lang === "zh" ? "待决定" : "Pending decision")}
            </Badge>
          </div>
          <h3 className="mt-2 font-medium leading-6">{requirement.content}</h3>
        </div>
      </div>
      <div className="mt-3 grid gap-3 text-xs sm:grid-cols-2">
        <div className="rounded-md bg-bg-elevated p-3"><span className="text-subtle">{lang === "zh" ? "分析建议" : "Recommendation"}</span>
          <p className="mt-1 text-muted">{scopeLabel(requirement.recommended_scope, lang)} · {requirement.recommendation_reason || (lang === "zh" ? "无理由" : "No reason")}</p></div>
        <div className="rounded-md bg-bg-elevated p-3"><span className="text-subtle">{lang === "zh" ? "用户确认" : "User confirmation"}</span>
          <p className="mt-1 text-muted">{scopeLabel(requirement.confirmed_scope, lang)} · {requirement.confirmation_reason || (lang === "zh" ? "尚未确认" : "Pending")}</p></div>
      </div>
      {requirement.acceptance_conditions.length ? <ul className="mt-3 list-disc space-y-1 pl-5 text-sm text-muted">{requirement.acceptance_conditions.map((item) => <li key={item}>{item}</li>)}</ul> : null}
      <IdLinks ids={requirement.reference_ids} prefix={lang === "zh" ? "来源" : "Sources"} />
      <details className="mt-4 border-t border-border pt-3">
        <summary className="cursor-pointer text-sm text-primary">{lang === "zh" ? "确认范围或编辑需求" : "Confirm scope or edit requirement"}</summary>
        <div className="mt-4 grid gap-5 md:grid-cols-2">
          <div className="space-y-3">
            <h4 className="text-sm font-medium">{lang === "zh" ? "用户确认" : "User confirmation"}</h4>
            <select value={scope} onChange={(event) => setScope(event.target.value as ProjectScope)} className={inputClass}>
              <option value="current">{lang === "zh" ? "本版做" : "Current"}</option><option value="later">{lang === "zh" ? "以后做" : "Later"}</option><option value="excluded">{lang === "zh" ? "不做" : "Excluded"}</option>
            </select>
            <TextArea label={lang === "zh" ? "确认理由" : "Confirmation reason"} value={reason} onChange={setReason} required />
            <Button size="sm" onClick={confirm} disabled={saving || !reason.trim()}><CheckCircle2 className="size-4" />{lang === "zh" ? "保存用户确认" : "Save confirmation"}</Button>
          </div>
          <div className="space-y-3">
            <h4 className="text-sm font-medium">{lang === "zh" ? "修改需求内容" : "Edit requirement meaning"}</h4>
            <TextArea label={lang === "zh" ? "需求" : "Requirement"} value={content} onChange={setContent} required />
            <TextArea label={lang === "zh" ? "验收条件（每行一条）" : "Acceptance (one per line)"} value={acceptance} onChange={setAcceptance} />
            <ReferencePicker references={references} selected={referenceIds} onChange={setReferenceIds} />
            <p className="text-[11px] leading-5 text-warn">{lang === "zh" ? "内容、验收或来源发生变化时，旧的用户确认会被清除。" : "Changing meaning, acceptance, or sources clears the old confirmation."}</p>
            <Button size="sm" variant="outline" onClick={edit} disabled={saving}><Save className="size-4" />{lang === "zh" ? "保存需求修订" : "Save revision"}</Button>
          </div>
        </div>
        {error ? <p className="mt-3 text-xs text-danger">{error}</p> : null}
      </details>
    </article>
  );
}

function DecisionForm({ projectId, references, onSaved }: { projectId: string; references: ProjectReference[]; onSaved: () => void }) {
  const { lang } = useLang(); const [statement, setStatement] = useState(""); const [rationale, setRationale] = useState("");
  const [ids, setIds] = useState<string[]>([]); const [saving, setSaving] = useState(false); const [error, setError] = useState("");
  const submit = async (event: FormEvent) => { event.preventDefault(); setSaving(true); setError(""); try {
    await createProjectDecision(projectId, { statement, rationale, reference_ids: ids }); setStatement(""); setRationale(""); setIds([]); onSaved();
  } catch (cause) { setError(String(cause)); } finally { setSaving(false); } };
  return <SideForm title={lang === "zh" ? "记录决定" : "Record decision"} icon={Plus}><form className="space-y-4" onSubmit={submit}>
    <TextArea label={lang === "zh" ? "决定" : "Decision"} value={statement} onChange={setStatement} required />
    <TextArea label={lang === "zh" ? "理由" : "Rationale"} value={rationale} onChange={setRationale} required />
    <ReferencePicker references={references} selected={ids} onChange={setIds} />
    {error ? <p className="text-xs text-danger">{error}</p> : null}<Button className="w-full" disabled={saving}>{lang === "zh" ? "保存决定" : "Save decision"}</Button>
  </form></SideForm>;
}

function DocumentForm({ projectId, workspace, onSaved }: { projectId: string; workspace: ProjectWorkspace; onSaved: () => void }) {
  const { lang } = useLang(); const [kind, setKind] = useState<ProjectDocumentKind>("analysis");
  const [title, setTitle] = useState(""); const [content, setContent] = useState(""); const [keys, setKeys] = useState<string[]>([]);
  const [saving, setSaving] = useState(false); const [error, setError] = useState("");
  const submit = async (event: FormEvent) => { event.preventDefault(); setSaving(true); setError(""); try {
    await createProjectDocument(projectId, { kind, title, content, basis: basisFromKeys(keys), author: "human", change_summary: lang === "zh" ? "创建人工初稿" : "Created manual draft" });
    setTitle(""); setContent(""); setKeys([]); onSaved();
  } catch (cause) { setError(String(cause)); } finally { setSaving(false); } };
  return <SideForm title={lang === "zh" ? "新建关联文档" : "Create linked document"} icon={Plus}><form className="space-y-4" onSubmit={submit}>
    <label className="block text-sm"><span className="text-muted">{lang === "zh" ? "文档类型" : "Document kind"}</span><select value={kind} onChange={(event) => setKind(event.target.value as ProjectDocumentKind)} className={inputClass}>{DOCUMENT_KINDS.map((item) => <option key={item.value} value={item.value}>{lang === "zh" ? item.zh : item.en}</option>)}</select></label>
    <Field label={lang === "zh" ? "标题" : "Title"} value={title} onChange={setTitle} required />
    <TextArea label="Markdown" value={content} onChange={setContent} required rows={9} />
    <BasisPicker workspace={workspace} selected={keys} onChange={setKeys} />
    {error ? <p className="text-xs text-danger">{error}</p> : null}<Button className="w-full" disabled={saving}>{lang === "zh" ? "创建文档 v1" : "Create document v1"}</Button>
  </form></SideForm>;
}

function DocumentCard({ projectId, document, onSaved }: { projectId: string; document: ProjectDocument; onSaved: () => void }) {
  const { lang } = useLang(); const [content, setContent] = useState(document.content); const [summary, setSummary] = useState("");
  const [saving, setSaving] = useState(false); const [error, setError] = useState(""); const [diff, setDiff] = useState<string | null>(null);
  const headings = markdownHeadings(document.content);
  const [sectionHeading, setSectionHeading] = useState(headings[0] || "");
  const [revisionInstruction, setRevisionInstruction] = useState("");
  const [revisionRun, setRevisionRun] = useState<ProjectGenerationRun | null>(null);
  const [revisionBusy, setRevisionBusy] = useState("");
  const [revisionError, setRevisionError] = useState("");
  const versions = useAsync(() => getProjectDocumentVersions(projectId, document.id), [projectId, document.id, document.current_version]);
  const revisionActive = revisionRun?.status === "queued" || revisionRun?.status === "running";
  useEffect(() => {
    if (!revisionActive || !revisionRun) return;
    let alive = true;
    const timer = window.setInterval(() => getProjectGeneration(projectId, revisionRun.id).then(
      (next) => { if (alive) setRevisionRun(next); },
      (cause) => { if (alive) setRevisionError(String(cause)); },
    ), 1200);
    return () => { alive = false; window.clearInterval(timer); };
  }, [projectId, revisionActive, revisionRun?.id]);
  const save = async () => { setSaving(true); setError(""); try {
    await addProjectDocumentVersion(projectId, document.id, { content, basis: document.basis, expected_current_version: document.current_version, author: "human", change_summary: summary }); onSaved();
  } catch (cause) { setError(String(cause)); } finally { setSaving(false); } };
  const compare = async () => { setError(""); try { setDiff((await getProjectDocumentDiff(projectId, document.id)).diff || (lang === "zh" ? "两个版本正文相同。" : "The two versions have identical content.")); } catch (cause) { setError(String(cause)); } };
  const startRevision = async () => {
    setRevisionBusy("start"); setRevisionError("");
    try {
      setRevisionRun(await startProjectGeneration(projectId, {
        mode: "revision", document_id: document.id, section_heading: sectionHeading,
        revision_instruction: revisionInstruction.trim(),
      }));
    } catch (cause) { setRevisionError(String(cause)); } finally { setRevisionBusy(""); }
  };
  const applyRevision = async () => {
    if (!revisionRun) return;
    setRevisionBusy("apply"); setRevisionError("");
    try {
      const result = await applyProjectGenerationItem(
        projectId, revisionRun.id, { item_kind: "document", index: 0 });
      setRevisionRun(result.run); onSaved();
    } catch (cause) { setRevisionError(String(cause)); } finally { setRevisionBusy(""); }
  };
  const revisionCandidate = revisionRun?.result?.documents[0];
  return <article className={`rounded-xl bg-surface p-5 shadow-card ${document.review.status === "needs_review" ? "ring-2 ring-warn/25" : ""}`}>
    <div className="flex flex-wrap items-start justify-between gap-3"><div><div className="flex flex-wrap items-center gap-2"><h3 className="font-medium">{document.title}</h3><Badge tone={document.review.status === "current" ? "ok" : "warn"}>{document.review.status === "current" ? (lang === "zh" ? "依据为当前" : "Current") : (lang === "zh" ? "需要复核" : "Needs review")}</Badge></div>
      <p className="mt-1 text-xs text-subtle">{documentKind(document.kind, lang)} · v{document.current_version} · {document.author} · {document.version_id}</p></div></div>
    {document.review.status === "needs_review" ? <p className="mt-3 flex gap-2 rounded-md bg-warn/10 p-3 text-xs leading-5 text-warn"><AlertTriangle className="mt-0.5 size-4 shrink-0" />{lang === "zh" ? "关联需求、上游文档或工作区基线已有变化。正文未被自动改写，请比较后保存新版本。" : "A linked requirement, upstream document, or workspace baseline changed. The content was preserved; review it before saving a new version."}</p> : null}
    <details className="mt-4"><summary className="cursor-pointer text-sm text-primary">{lang === "zh" ? "查看正文、编辑和版本" : "View, edit, and versions"}</summary>
      <div className="mt-4 rounded-md border border-border bg-bg-elevated p-4"><Prose md={document.content} /></div>
      <div className="mt-5 grid gap-4 lg:grid-cols-2"><div><TextArea label={lang === "zh" ? "编辑完整 Markdown（从当前版开始）" : "Edit full Markdown (starts from current)"} value={content} onChange={setContent} required rows={12} /><Field label={lang === "zh" ? "修改说明" : "Change summary"} value={summary} onChange={setSummary} required /><Button className="mt-3" size="sm" onClick={save} disabled={saving || !summary.trim()}><Save className="size-4" />{lang === "zh" ? "保存新版本" : "Save new version"}</Button></div>
        <div><h4 className="text-sm font-medium">{lang === "zh" ? "版本历史" : "Version history"}</h4>{versions.loading ? <p className="mt-2 text-xs text-subtle">…</p> : versions.data?.map((version) => <div key={version.version_id} className="mt-2 rounded-md bg-chip p-3 text-xs"><div>v{version.version} · {version.author} · {version.change_summary || (lang === "zh" ? "无说明" : "No summary")}</div><div className="mt-1 font-mono text-[10px] text-subtle">{version.content_sha256.slice(0, 12)}</div></div>)}
          <Button className="mt-3" size="sm" variant="outline" disabled={document.current_version < 2} onClick={compare}><FileClock className="size-4" />{lang === "zh" ? "比较最近两版" : "Compare latest two"}</Button></div></div>
      {diff ? <pre className="mt-4 max-h-96 overflow-auto whitespace-pre-wrap rounded-md bg-fg p-4 font-mono text-xs text-bg">{diff}</pre> : null}{error ? <p className="mt-3 text-xs text-danger">{error}</p> : null}
      <div className="mt-5 border-t border-border pt-5"><h4 className="text-sm font-medium">{lang === "zh" ? "用自然语言修改一个章节" : "Revise one section in natural language"}</h4><p className="mt-1 text-[11px] leading-5 text-subtle">{lang === "zh" ? "Atlas 固定当前版本；AI 只能改所选章节正文，章节标题与其它人工内容必须逐字保持。结果先显示差异，确认后才保存。" : "Atlas pins the current version. AI may change only the selected section body; the heading and all other content must remain byte-for-byte identical. Review the diff before saving."}</p>
        {headings.length ? <div className="mt-3 grid gap-3 lg:grid-cols-[minmax(0,16rem)_minmax(0,1fr)_auto] lg:items-end"><label className="block text-sm"><span className="text-muted">{lang === "zh" ? "目标章节" : "Target section"}</span><select value={sectionHeading} onChange={(event) => setSectionHeading(event.target.value)} className={inputClass}>{headings.map((heading) => <option key={heading} value={heading}>{heading}</option>)}</select></label><TextArea label={lang === "zh" ? "修改要求" : "Revision instruction"} value={revisionInstruction} onChange={setRevisionInstruction} rows={2} /><Button size="sm" variant="outline" disabled={Boolean(revisionBusy) || revisionActive || !revisionInstruction.trim()} onClick={startRevision}><Sparkles className="size-4" />{lang === "zh" ? "生成修改候选" : "Generate revision"}</Button></div> : <p className="mt-3 text-xs text-warn">{lang === "zh" ? "正文没有 Markdown 标题，请先用完整编辑加入章节结构。" : "This document has no Markdown headings. Add section structure with the full editor first."}</p>}
        {revisionActive ? <p className="mt-3 text-xs text-muted">{lang === "zh" ? "正在生成章节修改候选…" : "Generating a section revision…"}</p> : null}
        {revisionRun?.status === "failed" ? <p className="mt-3 rounded-md bg-danger/10 p-3 text-xs text-danger">{revisionRun.error}</p> : null}
        {revisionCandidate ? <div className="mt-4 rounded-md border border-border p-4"><div className="flex flex-wrap items-start justify-between gap-3"><div><Badge tone="ok">{lang === "zh" ? "修改候选" : "Revision candidate"}</Badge><p className="mt-2 text-xs text-muted">{revisionRun?.revision?.section_heading}</p></div><Button size="sm" disabled={Boolean(revisionRun?.applied.documents["0"]) || revisionBusy === "apply"} onClick={applyRevision}>{revisionRun?.applied.documents["0"] ? (lang === "zh" ? "已保存" : "Saved") : (lang === "zh" ? "保存为新版本" : "Save as new version")}</Button></div>{revisionCandidate.diff ? <pre className="mt-3 max-h-80 overflow-auto whitespace-pre-wrap rounded-md bg-fg p-4 font-mono text-xs text-bg">{revisionCandidate.diff}</pre> : null}<details className="mt-3"><summary className="cursor-pointer text-xs text-primary">{lang === "zh" ? "查看候选全文" : "View full candidate"}</summary><div className="mt-3 max-h-80 overflow-auto rounded-md bg-bg-elevated p-3"><Prose md={revisionCandidate.content} /></div></details></div> : null}
        {revisionError ? <p className="mt-3 text-xs text-danger">{revisionError}</p> : null}
      </div>
    </details>
  </article>;
}

function ExportButton({ projectId, lang }: { projectId: string; lang: "zh" | "en" }) {
  const [result, setResult] = useState<ProjectExport | null>(null); const [error, setError] = useState(""); const [saving, setSaving] = useState(false);
  const run = async () => { setSaving(true); setError(""); try { setResult(await exportProject(projectId)); } catch (cause) { setError(String(cause)); } finally { setSaving(false); } };
  return <div className="max-w-md text-right"><Button onClick={run} disabled={saving}><Download className="size-4" />{saving ? (lang === "zh" ? "导出中…" : "Exporting…") : (lang === "zh" ? "导出 Markdown 包" : "Export Markdown bundle")}</Button>{result ? <div className="mt-2 break-all text-left font-mono text-[11px] leading-5 text-subtle"><div>{result.archive}</div><div>sha256 {result.archive_sha256.slice(0, 16)}…</div></div> : null}{error ? <p className="mt-2 text-xs text-danger">{error}</p> : null}</div>;
}

function BasisPicker({ workspace, selected, onChange }: { workspace: ProjectWorkspace; selected: string[]; onChange: (value: string[]) => void }) {
  const { lang } = useLang();
  const options = [
    ...workspace.references.map((item) => ({ key: `reference:${item.id}`, label: `${lang === "zh" ? "资料" : "Source"} · ${item.source_ref}${item.locator ? `#${item.locator}` : ""}` })),
    ...workspace.requirements.map((item) => ({ key: `requirement:${item.id}`, label: `${lang === "zh" ? "需求" : "Requirement"} · ${item.id} · ${item.content}` })),
    ...workspace.decisions.map((item) => ({ key: `decision:${item.id}`, label: `${lang === "zh" ? "决定" : "Decision"} · ${item.statement}` })),
    ...workspace.documents.map((item) => ({ key: `document_version:${item.version_id}`, label: `${lang === "zh" ? "上游文档" : "Upstream document"} · ${item.title} v${item.current_version}` })),
  ];
  return <Picker label={lang === "zh" ? "固定依据" : "Pinned basis"} options={options} selected={selected} onChange={onChange} />;
}

function ReferencePicker({ references, selected, onChange }: { references: ProjectReference[]; selected: string[]; onChange: (value: string[]) => void }) {
  const { lang } = useLang(); return <Picker label={lang === "zh" ? "关联固定资料" : "Linked pinned sources"} options={references.map((item) => ({ key: item.id, label: `${item.source_ref}${item.locator ? `#${item.locator}` : ""}` }))} selected={selected} onChange={onChange} />;
}

function Picker({ label, options, selected, onChange }: { label: string; options: { key: string; label: string }[]; selected: string[]; onChange: (value: string[]) => void }) {
  return <fieldset><legend className="text-sm text-muted">{label}</legend><div className="mt-2 max-h-40 space-y-2 overflow-y-auto">{options.map((item) => <label key={item.key} className="flex items-start gap-2 text-xs leading-5 text-muted"><input type="checkbox" className="mt-1" checked={selected.includes(item.key)} onChange={(event) => onChange(event.target.checked ? [...selected, item.key] : selected.filter((value) => value !== item.key))} /><span>{item.label}</span></label>)}{!options.length ? <p className="text-xs text-subtle">—</p> : null}</div></fieldset>;
}

function basisFromKeys(keys: string[]): DocumentBasis[] { return keys.map((key) => { const [kind, id] = key.split(":", 2); return { kind: kind as NonNullable<DocumentBasis["kind"]>, id }; }); }
function sameKinds(left: ProjectDocumentKind[], right: ProjectDocumentKind[]) { return left.length === right.length && left.every((item) => right.includes(item)); }
function markdownHeadings(content: string) { const values = Array.from(content.matchAll(/^(#{1,6})[ \t]+(.+?)[ \t]*$/gm), (match) => match[0].trim()); return values.filter((value, index) => values.indexOf(value) === index && values.lastIndexOf(value) === index); }
function lines(value: string) { return value.split("\n").map((item) => item.trim()).filter(Boolean); }
function scopeLabel(scope: ProjectScope | null, lang: "zh" | "en") { if (!scope) return lang === "zh" ? "无" : "None"; const labels = { current: { zh: "本版", en: "Current" }, later: { zh: "以后", en: "Later" }, excluded: { zh: "不做", en: "Excluded" } }; return labels[scope][lang]; }
function documentKind(kind: ProjectDocumentKind, lang: "zh" | "en") { const item = DOCUMENT_KINDS.find((candidate) => candidate.value === kind); return item ? (lang === "zh" ? item.zh : item.en) : kind; }
function IdLinks({ ids, prefix }: { ids: string[]; prefix: string }) { return ids.length ? <p className="mt-3 font-mono text-[11px] text-subtle">{prefix}: {ids.join(" · ")}</p> : null; }
function Stat({ value, label }: { value: number; label: string }) { return <div className="rounded-xl bg-surface p-4 shadow-card"><div className="font-serif text-2xl">{value}</div><div className="mt-1 text-xs text-muted">{label}</div></div>; }
function Empty({ text }: { text: string }) { return <div className="rounded-xl bg-surface p-6 text-sm text-muted shadow-card">{text}</div>; }
function Signal({ title, count, text, muted }: { title: string; count: number | string; text: string; muted?: boolean }) { return <div className="rounded-lg bg-surface p-4 shadow-card"><div className="flex items-center justify-between gap-2"><h3 className="text-sm font-medium">{title}</h3><span className={`text-xs ${muted ? "text-subtle" : "text-primary"}`}>{count}</span></div><p className="mt-2 text-xs leading-5 text-muted">{text}</p></div>; }
function SectionTitle({ icon: Icon, title, description }: { icon: typeof FileText; title: string; description: string }) { return <div className="flex items-start gap-3"><Icon className="mt-0.5 size-5 text-primary" /><div><h2 className="font-serif text-xl font-medium">{title}</h2><p className="mt-1 text-xs leading-5 text-subtle">{description}</p></div></div>; }
function SideForm({ title, icon: Icon, children }: { title: string; icon: typeof Plus; children: ReactNode }) { return <aside className="h-fit rounded-xl bg-surface p-5 shadow-card"><h3 className="mb-5 flex items-center gap-2 font-medium"><Icon className="size-4" />{title}</h3>{children}</aside>; }
function Field({ label, value, onChange, required }: { label: string; value: string; onChange: (value: string) => void; required?: boolean }) { return <label className="block text-sm"><span className="text-muted">{label}</span><input required={required} value={value} onChange={(event) => onChange(event.target.value)} className={inputClass} /></label>; }
function TextArea({ label, value, onChange, required, rows = 3 }: { label: string; value: string; onChange: (value: string) => void; required?: boolean; rows?: number }) { return <label className="block text-sm"><span className="text-muted">{label}</span><textarea required={required} rows={rows} value={value} onChange={(event) => onChange(event.target.value)} className={`${inputClass} h-auto py-2.5`} /></label>; }
const inputClass = "mt-1.5 h-11 w-full rounded-md border border-border bg-bg-elevated px-3 outline-none focus:ring-2 focus:ring-primary/35";
