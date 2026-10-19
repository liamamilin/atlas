import { useEffect, useState, type FormEvent, type ReactNode } from "react";
import {
  ArrowLeft, Bot, CheckCircle2, Download,
  FileText, Lightbulb, Plus, Scale, Save, Sparkles,
} from "lucide-react";
import { Link, useParams } from "react-router-dom";
import { ErrorBox, Loading, useAsync } from "@/components/loaders";
import { GenerationPanel } from "@/components/project-generation-panel";
import { DocumentCard, DocumentForm } from "@/components/project-document-panel";
import { WorkspaceBaselinePanel } from "@/components/project-workspace-baseline-panel";
import {
  actionError,
  ChangePaths,
  documentKind,
  generationMode,
  inputClass,
  lines,
  scopeLabel,
  TechnicalError,
  TechnicalMeta,
  TextArea,
} from "@/components/project-detail-shared";
import { Prose } from "@/components/prose";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  applyProjectExecutionResult,
  backfillLegacyAcceptance,
  cleanupProjectExecution,
  confirmProjectRequirement,
  continueProjectExecution,
  createProjectDecision,
  createProjectIteration,
  createProjectRequirement,
  createProjectTask,
  exportProject,
  reconcileProjectExecution,
  recoverProjectExecutionApply,
  getProjectHarnessPreflight,
  getProjectWorkspace,
  getLegacyAcceptanceMigration,
  invalidateAtlasCache,
  recordProjectTaskAcceptance,
  rebaseProjectIteration,
  replyProjectExecutionPermission,
  replyProjectExecutionQuestion,
  resolveProjectOpenItem,
  startProjectExecution,
  stopProjectExecution,
  updateProjectIterationStatus,
  updateProjectRequirement,
  type ProjectDocument,
  type ProjectExport,
  type ProjectExecution,
  type ProjectGenerationRun,
  type HarnessPreflight,
  type ProjectOpenItem,
  type ProjectReference,
  type ProjectRequirement,
  type ProjectScope,
  type ProjectTask,
  type AcceptanceConditionResult,
  type AcceptanceEvidence,
  type ProjectRequirementSnapshot,
  type ProjectWorkspace,
} from "@/lib/atlas";
import { useLang } from "@/lib/lang";
import { setCurrentProjectId } from "@/lib/project-selection";
import {
  projectBlockingCounts,
  projectLifecycleSteps,
  type ProjectLifecycleStep,
} from "@/lib/project-status";

function Expandable({
  initialOpen,
  summary,
  className,
  children,
}: {
  initialOpen: boolean;
  summary: ReactNode;
  className?: string;
  children: ReactNode;
}) {
  const [open, setOpen] = useState(initialOpen);
  useEffect(() => setOpen(initialOpen), [initialOpen]);
  return (
    <details className={className} open={open} onToggle={(event) => setOpen(event.currentTarget.open)}>
      <summary className="cursor-pointer">{summary}</summary>
      {children}
    </details>
  );
}

export function ProjectDetail() {
  const { projectId = "" } = useParams<{ projectId: string }>();
  const { lang } = useLang();
  const [revision, setRevision] = useState(0);
  const [analysisRun, setAnalysisRun] = useState<ProjectGenerationRun | null>(null);
  const [hasBaseline, setHasBaseline] = useState<boolean | null>(null);
  const [latestBaselineId, setLatestBaselineId] = useState<string | null>(null);
  const [harnessPreflight, setHarnessPreflight] = useState<HarnessPreflight | null>(null);
  const { data, error, loading } = useAsync(
    () => getProjectWorkspace(projectId), [projectId, revision]);

  useEffect(() => {
    if (data && data.project.id === projectId) setCurrentProjectId(data.project.id);
  }, [data, projectId]);

  useEffect(() => {
    setHasBaseline(null);
    setAnalysisRun(null);
    setLatestBaselineId(null);
    setHarnessPreflight(null);
  }, [projectId]);

  useEffect(() => {
    if (!projectId) return;
    let alive = true;
    getProjectHarnessPreflight(projectId).then((value) => {
      if (alive) setHarnessPreflight(value);
    }).catch(() => {
      if (alive) setHarnessPreflight({ status: "failed", code: "request_failed", message: lang === "zh" ? "无法读取 OpenCode 启动前检查。" : "Could not read the OpenCode preflight." });
    });
    return () => { alive = false; };
  }, [projectId, revision, lang]);

  const refresh = () => {
    invalidateAtlasCache();
    setRevision((value) => value + 1);
  };

  if (loading && !data) return <Loading />;
  if (error || !data) return <ErrorBox message={error || "project unavailable"} />;
  if (data.project.id !== projectId) return <Loading />;
  const activeIteration = data.iterations.find((item) => item.status === "active") || null;

  return (
    <main key={projectId} className="mx-auto max-w-6xl px-4 py-10">
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

      <ProjectStatusHeader workspace={data} activeIteration={activeIteration} hasBaseline={hasBaseline}
        nextStep={projectLifecycleSteps(data, hasBaseline).find((item) => !item.done) || null} />
      {!data.iterations.length ? <FirstWorkspaceHint lang={lang} /> : null}
      {activeIteration ? <ExecutionReadiness lang={lang} preflight={harnessPreflight} /> : null}

      <StageSection stage={STAGES[0]}>
        <LifecycleOverview workspace={data} hasBaseline={hasBaseline} />

        <WorkspaceBaselinePanel projectId={projectId} onSaved={refresh}
          onBaselineChange={(value, latestId) => { setHasBaseline(value); setLatestBaselineId(latestId); }} />

        <GenerationPanel projectId={projectId} workspace={data} onSaved={refresh}
          onAnalysis={setAnalysisRun} />
      </StageSection>

      <StageSection stage={STAGES[1]}>
        <OpenItemsPanel projectId={projectId} workspace={data} onSaved={refresh} />

        <ConsistencyPanel workspace={data} analysisRun={analysisRun} />

        <AcceptanceMigrationPanel projectId={projectId} onSaved={refresh} />

        <section className="mt-8 grid gap-6 lg:grid-cols-[minmax(0,1fr)_22rem]">
          <div>
            <SectionTitle icon={Scale} title={lang === "zh" ? "范围与验收" : "Scope & acceptance"}
              description={lang === "zh" ? "分析建议和用户确认分别保存；修改需求内容会清除旧确认并生成新的修订号。" : "Recommendations and user confirmations are stored separately. Meaningful edits clear old confirmation and create a new revision."} />
            <Expandable className="mt-4 rounded-xl border border-border bg-bg-elevated p-3" initialOpen={data.requirements.length <= 3 || data.requirements.some((item) => !item.confirmed_scope)}
              summary={<span className="block px-2 py-1 text-sm font-medium text-primary">{lang === "zh" ? `查看候选需求（${data.requirements.length}）` : `View candidate requirements (${data.requirements.length})`}</span>}>
              <div className="mt-3 space-y-3">
                {data.requirements.map((requirement) => (
                  <RequirementCard key={`${requirement.id}:${requirement.updated_at}`} projectId={projectId}
                    requirement={requirement} references={data.references} onSaved={refresh} />
                ))}
                {!data.requirements.length ? <Empty text={lang === "zh" ? "还没有候选需求。" : "No candidate requirements yet."} /> : null}
              </div>
            </Expandable>
          </div>
          <RequirementForm projectId={projectId} references={data.references} onSaved={refresh} />
        </section>

        <section className="mt-10 grid gap-6 lg:grid-cols-[minmax(0,1fr)_22rem]">
          <div>
            <SectionTitle icon={Lightbulb} title={lang === "zh" ? "已记录决定" : "Recorded decisions"}
              description={lang === "zh" ? "决定保存采用内容和理由，可引用固定资料。" : "Decisions retain the chosen direction, rationale, and pinned sources."} />
            <Expandable className="mt-4 rounded-xl border border-border bg-bg-elevated p-3" initialOpen={data.decisions.length <= 3}
              summary={<span className="block px-2 py-1 text-sm font-medium text-primary">{lang === "zh" ? `查看已记录决定（${data.decisions.length}）` : `View recorded decisions (${data.decisions.length})`}</span>}>
              <div className="mt-3 space-y-3">
                {data.decisions.map((decision) => (
                  <article key={decision.id} className="rounded-xl bg-surface p-5 shadow-card">
                    <div className="flex flex-wrap items-center gap-2">
                      <h3 className="font-medium">{decision.statement}</h3>
                      <TechnicalMeta label={lang === "zh" ? "技术信息" : "Technical details"} value={decision.id} inline />
                    </div>
                    <p className="mt-2 text-sm leading-6 text-muted">{decision.rationale}</p>
                    <IdLinks ids={decision.reference_ids} prefix={lang === "zh" ? "依据" : "Sources"} />
                  </article>
                ))}
                {!data.decisions.length ? <Empty text={lang === "zh" ? "还没有项目决定。" : "No recorded decisions yet."} /> : null}
              </div>
            </Expandable>
          </div>
          <DecisionForm projectId={projectId} references={data.references} onSaved={refresh} />
        </section>
      </StageSection>

      <StageSection stage={STAGES[2]}>
        <section className="mt-8">
          <SectionTitle icon={FileText} title={lang === "zh" ? "关联文档与版本" : "Linked documents & versions"}
            description={lang === "zh" ? "每次保存产生不可变版本并记录固定依据。依赖新鲜度与人工审阅分别记录；只有已批准且依据为当前的版本才能固定为迭代输入。" : "Each save creates an immutable version with pinned basis. Dependency freshness and human review are tracked separately; only approved, current-basis versions can be pinned into an iteration."} />
          <div className="mt-5 grid gap-6 lg:grid-cols-[minmax(0,1fr)_22rem]">
            <Expandable className="space-y-4" initialOpen={data.documents.length <= 3 || data.documents.some((item) => item.review.status === "needs_review" || (item.review.approval || "pending") !== "approved")}
              summary={<span className="block rounded-xl border border-border bg-bg-elevated p-3 text-sm font-medium text-primary">{lang === "zh" ? `查看关联文档（${data.documents.length}）` : `View linked documents (${data.documents.length})`}</span>}>
              <div className="mt-4 space-y-4">
                {data.documents.map((document) => (
                  <DocumentCard key={`${document.id}:${document.current_version}`} projectId={projectId}
                    document={document} onSaved={refresh} />
                ))}
                {!data.documents.length ? <Empty text={lang === "zh" ? "还没有关联文档。" : "No linked documents yet."} /> : null}
              </div>
            </Expandable>
            <DocumentForm projectId={projectId} workspace={data} onSaved={refresh} />
          </div>
        </section>

        {activeIteration ? <p className="mt-6 rounded-lg bg-bg-elevated p-4 text-xs leading-5 text-muted">{lang === "zh" ? `活动迭代 #${activeIteration.sequence}《${activeIteration.title}》已建立并固定输入；执行、应用与验收在阶段四。` : `Active iteration #${activeIteration.sequence} "${activeIteration.title}" is active with frozen inputs; execute, apply, and accept in stage 4.`} <a className="text-primary" href="#stage-execute">{lang === "zh" ? "前往执行与验收" : "Go to Execute & accept"}</a></p> : <section className="mt-8">
          <SectionTitle icon={Bot} title={lang === "zh" ? "建立活动迭代" : "Create active iteration"}
            description={lang === "zh" ? "冻结已批准文档版本、已确认需求修订与当前已接受基线；建立后进入执行阶段。" : "Freeze approved document versions, confirmed requirement revisions, and the current accepted baseline. Execution follows."} />
          <div className="mt-5"><IterationForm projectId={projectId} workspace={data} hasBaseline={hasBaseline} onSaved={refresh} /></div>
        </section>}
      </StageSection>

      <StageSection stage={STAGES[3]}>
        <ExecutionPanel projectId={projectId} workspace={data}
          latestBaselineId={latestBaselineId} harnessPreflight={harnessPreflight} onSaved={refresh} />
      </StageSection>
    </main>
  );
}

type StageId = "understand" | "scope" | "plan" | "execute";

const STAGES: { id: StageId; zh: string; en: string; descriptionZh: string; descriptionEn: string }[] = [
  {
    id: "understand", zh: "理解项目", en: "Understand",
    descriptionZh: "固定资料、检查工作区现状，并运行分析或价值评估。",
    descriptionEn: "Pin sources, review the workspace state, and run analysis or value assessment.",
  },
  {
    id: "scope", zh: "确定范围", en: "Scope",
    descriptionZh: "处理开放问题、冲突与建议；确认需求范围并记录决定。",
    descriptionEn: "Resolve open questions, conflicts, and suggestions; confirm requirement scope and record decisions.",
  },
  {
    id: "plan", zh: "冻结计划", en: "Plan",
    descriptionZh: "审阅并批准文档；冻结需求修订、文档版本与工作区基线，建立迭代。",
    descriptionEn: "Review and approve documents; freeze requirement revisions, document versions, and the workspace baseline, then create the iteration.",
  },
  {
    id: "execute", zh: "执行与验收", en: "Execute & accept",
    descriptionZh: "任务执行、结果应用与产品验收；历史记录保持只读。",
    descriptionEn: "Execute tasks, apply results, and record product acceptance; history stays read-only.",
  },
];

function StageSection({ stage, children }: { stage: (typeof STAGES)[number]; children: ReactNode }) {
  const { lang } = useLang();
  return <section id={`stage-${stage.id}`} className="mt-12 scroll-mt-6">
    <div className="flex items-start gap-3 border-b border-border pb-3">
      <span className="flex size-7 shrink-0 items-center justify-center rounded-full bg-primary/10 text-sm font-medium text-primary">{STAGES.indexOf(stage) + 1}</span>
      <div><h2 className="font-serif text-2xl font-medium">{lang === "zh" ? stage.zh : stage.en}</h2><p className="mt-1 text-xs leading-5 text-subtle">{lang === "zh" ? stage.descriptionZh : stage.descriptionEn}</p></div>
    </div>
    {children}
  </section>;
}

function MiniStat({ value, label, warn }: { value: number; label: string; warn: boolean }) {
  return <div className={`rounded-lg p-3 ${warn ? "bg-warn/10" : "bg-bg-elevated"}`}><div className={`text-lg font-medium ${warn ? "text-warn" : "text-fg"}`}>{value}</div><div className="mt-0.5 text-[11px] leading-4 text-muted">{label}</div></div>;
}

function ProjectStatusHeader({ workspace, activeIteration, hasBaseline, nextStep }: {
  workspace: ProjectWorkspace;
  activeIteration: ProjectWorkspace["iterations"][number] | null;
  hasBaseline: boolean | null;
  nextStep: ProjectLifecycleStep | null;
}) {
  const { lang } = useLang();
  const checkingBaseline = hasBaseline === null;
  const latestIteration = workspace.iterations.slice().sort((a, b) => b.sequence - a.sequence)[0] || null;
  const openItems = (workspace.open_items || []).filter((item) => item.current && item.status === "open");
  const blockingCounts = projectBlockingCounts(workspace, activeIteration, hasBaseline);
  const optionalCounts = [
    { value: openItems.filter((item) => item.kind === "suggestion").length, zh: "参考建议", en: "Suggestions" },
    { value: workspace.documents.filter((item) => item.review.status === "needs_review").length, zh: "待复核文档", en: "Documents to review" },
    { value: workspace.documents.filter((item) => (item.review.approval || "pending") !== "approved").length, zh: "未批准文档", en: "Unapproved documents" },
  ];
  const stageIndex = checkingBaseline ? 0 : nextStep ? STAGES.findIndex((stage) => stage.id === nextStep.stage) : STAGES.length - 1;
  const visibleBlockingCounts = blockingCounts.filter((item) => item.value > 0);
  const visibleOptionalCounts = optionalCounts.filter((item) => item.value > 0);
  return <section className="mt-6 rounded-xl border border-border bg-surface p-5 shadow-card">
    <div className="grid gap-5 lg:grid-cols-[minmax(0,1fr)_minmax(0,1.1fr)]">
      <div>
        <div className="flex flex-wrap items-center gap-2">
          <p className="text-xs font-medium tracking-wide text-primary">{lang === "zh" ? "当前状态" : "Current status"}</p>
          <span className="rounded-full bg-chip px-2 py-0.5 text-[11px] text-muted">
            {checkingBaseline ? (lang === "zh" ? "检查中" : "Checking") : lang === "zh" ? `第 ${stageIndex + 1} / ${STAGES.length} 阶段` : `Stage ${stageIndex + 1} of ${STAGES.length}`}
          </span>
        </div>
        <p className="mt-2 font-serif text-xl font-medium">{checkingBaseline ? (lang === "zh" ? "正在检查工作区" : "Checking the workspace") : lang === "zh" ? STAGES[stageIndex].zh : STAGES[stageIndex].en}</p>
        <p className="mt-2 text-sm">{activeIteration
          ? (lang === "zh" ? `活动迭代 #${activeIteration.sequence}《${activeIteration.title}》` : `Active iteration #${activeIteration.sequence} "${activeIteration.title}"`)
          : latestIteration?.status === "completed"
            ? (lang === "zh" ? `最近迭代 #${latestIteration.sequence}《${latestIteration.title}》已完成` : `Latest iteration #${latestIteration.sequence} "${latestIteration.title}" is complete`)
            : (lang === "zh" ? "活动迭代：尚未建立" : "Active iteration: not created yet")}</p>
        <p className="mt-1 text-sm text-warn">{checkingBaseline ? (lang === "zh" ? "正在读取工作区状态，稍后会显示下一步。" : "Reading the workspace state; the next step will appear shortly.") : nextStep ? (lang === "zh" ? <>下一项：<a className="underline" href={`#stage-${nextStep.stage}`}>{nextStep.zh}</a></> : <>Next: <a className="underline" href={`#stage-${nextStep.stage}`}>{nextStep.en}</a></>) : (lang === "zh" ? "当前迭代已完成；可以开始新一轮迭代。" : "The current iteration is complete; start the next round.")}</p>
        <p className="mt-2 text-xs text-subtle">{lang === "zh" ? `${workspace.references.length} 条固定资料 · ${workspace.requirements.length} 条候选需求 · ${workspace.decisions.length} 项决定 · ${workspace.documents.length} 份文档` : `${workspace.references.length} sources · ${workspace.requirements.length} requirements · ${workspace.decisions.length} decisions · ${workspace.documents.length} documents`}</p>
        {nextStep && !checkingBaseline ? <Button asChild size="sm" className="mt-4"><a href={`#stage-${nextStep.stage}`}>{lang === "zh" ? `开始：${nextStep.zh}` : `Start: ${nextStep.en}`}</a></Button> : null}
      </div>
      <div>
        <p className="text-xs font-medium text-muted">{activeIteration
          ? (lang === "zh" ? "当前迭代" : "Current iteration")
          : (lang === "zh" ? "下一步准备" : "Next-step readiness")}</p>
        {visibleBlockingCounts.length ? (
          <div className="mt-2 grid grid-cols-2 gap-2 sm:grid-cols-3">{visibleBlockingCounts.map((item) => <MiniStat key={item.en} value={item.value} label={lang === "zh" ? item.zh : item.en} warn />)}</div>
        ) : (
          <div className="mt-2 rounded-lg bg-primary/10 p-4 text-sm text-primary">
            <CheckCircle2 className="mb-1 size-4" />
            {activeIteration
              ? (lang === "zh" ? "当前没有阻塞项。" : "There are no blockers for the current iteration.")
              : latestIteration?.status === "completed"
                ? (lang === "zh" ? "最近迭代已完成；当前没有活动迭代。" : "The latest iteration is complete; there is no active iteration.")
                : (lang === "zh" ? "建立迭代的前置条件已满足。" : "The prerequisites for creating an iteration are satisfied.")}
          </div>
        )}
        {visibleOptionalCounts.length ? <div className="mt-3 rounded-lg bg-bg-elevated p-3"><p className="text-xs font-medium text-muted">{lang === "zh" ? "可选建议与后续处理" : "Optional suggestions and follow-ups"}</p><div className="mt-2 grid grid-cols-2 gap-2 sm:grid-cols-3">{visibleOptionalCounts.map((item) => <MiniStat key={item.en} value={item.value} label={lang === "zh" ? item.zh : item.en} warn={false} />)}</div></div> : null}
      </div>
    </div>
    <nav className="mt-4 flex flex-wrap gap-2 border-t border-border pt-3">{STAGES.map((stage, index) => <a key={stage.id} href={`#stage-${stage.id}`} className="rounded-full bg-bg-elevated px-3 py-1 text-xs text-muted hover:text-fg">{index + 1} · {lang === "zh" ? stage.zh : stage.en}</a>)}</nav>
  </section>;
}

function FirstWorkspaceHint({ lang }: { lang: "zh" | "en" }) {
  return <section className="mt-4 rounded-xl border border-primary/20 bg-primary/[0.06] p-4">
    <div className="flex items-start gap-3">
      <Sparkles className="mt-0.5 size-4 shrink-0 text-primary" />
      <div className="min-w-0">
        <p className="text-sm font-medium">{lang === "zh" ? "第一次使用？按这三步开始" : "First time here? Start with these three steps"}</p>
        <p className="mt-1 text-xs leading-5 text-muted">{lang === "zh" ? "先确认依据，再确认范围，最后冻结计划。完成前不会修改你的本地项目。" : "Confirm the evidence, define the scope, then freeze a plan. Nothing changes in your local project before you review it."}</p>
        <div className="mt-3 flex flex-wrap gap-2 text-xs">
          <a className="rounded-full bg-surface px-3 py-1.5 text-primary shadow-card hover:underline" href="#stage-understand">{lang === "zh" ? "1 · 固定资料" : "1 · Pin evidence"}</a>
          <a className="rounded-full bg-surface px-3 py-1.5 text-primary shadow-card hover:underline" href="#stage-scope">{lang === "zh" ? "2 · 确认范围" : "2 · Define scope"}</a>
          <a className="rounded-full bg-surface px-3 py-1.5 text-primary shadow-card hover:underline" href="#stage-plan">{lang === "zh" ? "3 · 冻结计划" : "3 · Freeze plan"}</a>
          <Link className="px-2 py-1.5 text-muted hover:text-fg" to="/tutorial">{lang === "zh" ? "查看完整教程" : "Read the full tutorial"}</Link>
        </div>
      </div>
    </div>
  </section>;
}

function ExecutionReadiness({ lang, preflight }: { lang: "zh" | "en"; preflight: HarnessPreflight | null }) {
  const status = preflight?.status || "checking";
  const tone = status === "passed" ? "bg-primary/10 text-primary" : status === "failed" ? "bg-danger/10 text-danger" : "bg-warn/10 text-warn";
  return <section className={`mt-4 rounded-xl p-4 text-sm ${tone}`}>
    <div className="flex flex-wrap items-start justify-between gap-3">
      <div>
        <p className="font-medium">{lang === "zh" ? "执行准备" : "Execution readiness"}</p>
        <p className="mt-1 text-xs leading-5">
          {status === "checking"
            ? (lang === "zh" ? "正在检查 OpenCode 和 provider，稍后会显示是否可以启动任务。" : "Checking OpenCode and its provider; readiness will appear shortly.")
            : status === "passed"
              ? (lang === "zh" ? `已准备好：${preflight?.version || "OpenCode"} · provider 检查通过。` : `Ready: ${preflight?.version || "OpenCode"} · provider check passed.`)
              : status === "not_configured"
                ? (lang === "zh" ? "尚未配置 OpenCode；完成配置后才能启动隔离执行。" : "OpenCode is not configured; configure it before starting an isolated run.")
                : (lang === "zh" ? "检查未通过；修复环境后回到这里重新检查。" : "The check failed; fix the environment and return here to check again.")}
        </p>
      </div>
      <div className="flex flex-wrap gap-2 text-xs">
        <a className="rounded-full bg-surface px-3 py-1.5 text-primary shadow-card hover:underline" href="#stage-execute">{lang === "zh" ? "查看执行区" : "View execution"}</a>
        {status === "not_configured" || status === "failed" ? <Link className="px-2 py-1.5 text-muted hover:text-fg" to="/tutorial">{lang === "zh" ? "查看配置说明" : "Read setup guide"}</Link> : null}
      </div>
    </div>
  </section>;
}

function LifecycleOverview({ workspace, hasBaseline }: {
  workspace: ProjectWorkspace; hasBaseline: boolean | null;
}) {
  const { lang } = useLang();
  const steps = projectLifecycleSteps(workspace, hasBaseline);
  const checkingBaseline = hasBaseline === null;
  const next = steps.find((item) => !item.done);
  const completed = steps.filter((item) => item.done).length;
  return <section className="mt-5 rounded-xl border border-border bg-surface p-4 shadow-card">
    <div className="flex flex-wrap items-center justify-between gap-3">
      <div><p className="text-sm font-medium">{lang === "zh" ? "项目路径" : "Project path"}</p><p className="mt-1 text-xs text-subtle">{checkingBaseline ? (lang === "zh" ? "正在检查工作区状态。" : "Checking the workspace state.") : next ? (lang === "zh" ? `建议下一步：${next.zh}` : `Recommended next: ${next.en}`) : (lang === "zh" ? "当前迭代已完成。" : "The current iteration is complete.")} {!checkingBaseline && <>· {lang === "zh" ? `${completed}/${steps.length} 项已完成` : `${completed} of ${steps.length} complete`}</>}</p></div>
      <div className="flex flex-wrap gap-2">{steps.map((item, index) => <a key={item.en} href={`#stage-${item.stage}`} className={`flex items-center gap-1.5 rounded-full px-2.5 py-1 text-[11px] hover:opacity-80 ${item.done ? "bg-primary/10 text-primary" : item === next ? "bg-warn/10 text-warn" : "bg-bg-elevated text-subtle"}`}>
        {item.done ? <CheckCircle2 className="size-3.5" /> : <span>{index + 1}</span>}<span>{lang === "zh" ? item.zh : item.en}</span>
      </a>)}</div>
    </div>
  </section>;
}

function ExecutionPanel({ projectId, workspace, latestBaselineId, harnessPreflight, onSaved }: {
  projectId: string; workspace: ProjectWorkspace;
  latestBaselineId: string | null; harnessPreflight: HarnessPreflight | null;
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
    catch (cause) { setError(actionError(cause, lang)); } finally { setBusy(""); }
  };
  const rebase = async () => {
    if (!active) return;
    setBusy("rebase"); setError("");
    try {
      await rebaseProjectIteration(projectId, active.id, { note: "ui: rebase to latest accepted baseline" });
      onSaved();
    } catch (cause) { setError(actionError(cause, lang)); } finally { setBusy(""); }
  };
  const baselineBehind = Boolean(active?.baseline_id && latestBaselineId
    && active.baseline_id !== latestBaselineId);
  return <section className="mt-10">
    <SectionTitle icon={Bot} title={lang === "zh" ? "迭代与开发执行" : "Iterations & development execution"}
      description={lang === "zh" ? "把已确认需求、固定文档版本和已接受代码基线绑定为任务；OpenCode 负责执行，Atlas 独立记录状态、权限、文件变化和产品验收。" : "Bind confirmed requirements, fixed document versions, and an accepted code baseline into tasks. OpenCode executes while Atlas independently records state, permissions, file changes, and product acceptance."} />
    <div className="mt-5 space-y-5">
      {harnessPreflight && harnessPreflight.status !== "not_configured" ? <div className={`rounded-xl p-4 text-sm ${harnessPreflight.status === "passed" ? "bg-primary/10 text-primary" : "bg-danger/10 text-danger"}`}>
        <p className="font-medium">{lang === "zh" ? "OpenCode 启动前检查" : "OpenCode preflight"}</p>
        {harnessPreflight.status === "passed" ? <p className="mt-1 text-xs leading-5">{lang === "zh" ? `已通过：${harnessPreflight.version || "未知版本"} · ${harnessPreflight.executable || "CLI"} · provider 检查通过。` : `Passed: ${harnessPreflight.version || "unknown version"} · ${harnessPreflight.executable || "CLI"} · provider check passed.`}</p> : <p className="mt-1 text-xs leading-5">{harnessPreflight.message || (lang === "zh" ? "检查未通过；修复环境后再启动任务。" : "Preflight failed; fix the environment before starting a task.")}</p>}
      </div> : null}
      {!active ? <div className="rounded-xl bg-surface p-5 text-sm text-muted shadow-card">{lang === "zh" ? "当前没有活动迭代。请到" : "There is no active iteration. Create one in "}<a className="text-primary" href="#stage-plan">{lang === "zh" ? "阶段三「冻结计划」" : "stage 3 Plan"}</a>{lang === "zh" ? "固定输入并建立迭代。" : " by freezing the inputs."}</div> : <>
        <article className="rounded-xl bg-surface p-5 shadow-card">
          <div className="flex flex-wrap items-start justify-between gap-4">
            <div><div className="flex flex-wrap items-center gap-2"><Badge tone="ok">{lang === "zh" ? `活动迭代 ${active.sequence}` : `Active iteration ${active.sequence}`}</Badge><span className="font-mono text-[11px] text-subtle">{active.id}</span></div><h3 className="mt-2 font-medium">{active.title}</h3><p className="mt-1 text-sm leading-6 text-muted">{active.objective}</p></div>
            <div className="flex gap-2"><Button size="sm" variant="outline" disabled={Boolean(busy)} onClick={() => changeIteration("abandoned")}>{lang === "zh" ? "放弃迭代" : "Abandon"}</Button><Button size="sm" disabled={Boolean(busy) || !tasks.length} onClick={() => changeIteration("completed")}><CheckCircle2 className="size-4" />{lang === "zh" ? "完成迭代" : "Complete iteration"}</Button></div>
          </div>
          <IdLinks ids={active.input_document_versions} prefix={lang === "zh" ? "固定文档版本" : "Fixed document versions"} />
          <IdLinks ids={active.requirement_ids.map((id) => { const pin = (active.requirement_revisions || []).find((item) => item.requirement_id === id); return pin ? `${id} · r${pin.revision}` : id; })} prefix={lang === "zh" ? "本版需求（固定修订）" : "Current requirements (pinned revisions)"} />
          <IdLinks ids={active.baseline_id ? [active.baseline_id] : []} prefix={lang === "zh" ? "固定工作区基线" : "Pinned workspace baseline"} />
          {baselineBehind ? <div className="mt-3 rounded-md bg-warn/10 p-3"><p className="text-xs leading-5 text-warn">{lang === "zh" ? "已应用的结果推进了项目基线；开始新的执行前需要把本迭代显式重新对齐到最新基线。已完成的执行与验收记录不受影响。" : "An applied result advanced the project baseline. Rebase this iteration explicitly before starting more executions; finished records are unchanged."}</p><Button className="mt-2" size="sm" disabled={Boolean(busy)} onClick={rebase}>{lang === "zh" ? "重新对齐迭代基线" : "Rebase iteration baseline"}</Button></div> : null}
          {active.baseline_history?.length ? <details className="mt-2"><summary className="cursor-pointer text-xs text-primary">{lang === "zh" ? `基线调整记录 · ${active.baseline_history.length}` : `Baseline rebases · ${active.baseline_history.length}`}</summary><div className="mt-2 space-y-1 font-mono text-[10px] text-subtle">{active.baseline_history.map((item, index) => <p key={`${item.rebased_at}:${index}`}>{new Date(item.rebased_at).toLocaleString(lang === "zh" ? "zh-CN" : "en")} · {item.baseline_id || "none"} → {item.note || ""}</p>)}</div></details> : null}
          {error ? <p className="mt-3 text-xs text-danger">{error}</p> : null}
        </article>
        <div className="grid gap-6 lg:grid-cols-[minmax(0,1fr)_22rem]">
          <div className="space-y-4">
            {tasks.map((task) => <ExecutionTaskCard key={`${task.id}:${task.updated_at}`} projectId={projectId} task={task} executions={workspace.executions.filter((item) => item.task_id === task.id)} requirements={workspace.requirements} documents={workspace.documents} readOnly={false} harnessReady={!harnessPreflight || harnessPreflight.status === "passed" || harnessPreflight.status === "not_configured"} onSaved={onSaved} />)}
            {!tasks.length ? <Empty text={lang === "zh" ? "本迭代还没有执行任务。" : "This iteration has no execution tasks yet."} /> : null}
          </div>
          <TaskForm projectId={projectId} workspace={workspace} iteration={active} onSaved={onSaved} />
        </div>
      </>}
      {workspace.iterations.filter((item) => item.status !== "active").length ? <details className="rounded-xl bg-surface p-5 shadow-card"><summary className="cursor-pointer text-sm text-primary">{lang === "zh" ? "历史迭代" : "Iteration history"}</summary><div className="mt-3 space-y-3">{workspace.iterations.filter((item) => item.status !== "active").map((item) => { const historicalTasks = workspace.tasks.filter((task) => task.iteration_id === item.id); return <details key={item.id} className="rounded-md bg-bg-elevated p-3"><summary className="cursor-pointer text-sm"><span className="font-medium">#{item.sequence} · {item.title}</span><span className="ml-2 text-xs text-subtle">{iterationStatus(item.status, lang)} · {historicalTasks.length} {lang === "zh" ? "个任务" : "task(s)"}</span></summary><div className="mt-3 space-y-3">{historicalTasks.map((task) => <ExecutionTaskCard key={`${task.id}:${task.updated_at}`} projectId={projectId} task={task} executions={workspace.executions.filter((execution) => execution.task_id === task.id)} requirements={workspace.requirements} documents={workspace.documents} readOnly onSaved={onSaved} />)}{!historicalTasks.length ? <p className="text-xs text-subtle">{lang === "zh" ? "没有任务记录。" : "No task records."}</p> : null}</div></details>; })}</div></details> : null}
    </div>
  </section>;
}

function IterationForm({ projectId, workspace, hasBaseline, onSaved }: {
  projectId: string; workspace: ProjectWorkspace; hasBaseline: boolean | null;
  onSaved: () => void;
}) {
  const { lang } = useLang();
  const current = workspace.requirements.filter((item) => item.confirmed_scope === "current");
  const currentDocuments = workspace.documents.filter((item) =>
    item.review.status === "current" && (item.review.approval || "pending") === "approved");
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
  if (!currentDocuments.length) missing.push(lang === "zh" ? "至少一份已批准且依据为当前的文档" : "at least one approved document with current basis");
  if (!current.length) missing.push(lang === "zh" ? "至少一条已确认本版需求" : "at least one confirmed current requirement");
  const submit = async (event: FormEvent) => { event.preventDefault(); setSaving(true); setError(""); try {
    await createProjectIteration(projectId, { title, objective, input_document_versions: documents, requirement_ids: requirements }); onSaved();
  } catch (cause) { setError(actionError(cause, lang)); } finally { setSaving(false); } };
  return <article className="rounded-xl bg-surface p-5 shadow-card"><form onSubmit={submit}>
    <div className="grid gap-5 lg:grid-cols-2"><div className="space-y-4"><h3 className="font-medium">{lang === "zh" ? "建立活动迭代" : "Create active iteration"}</h3><Field label={lang === "zh" ? "迭代标题" : "Iteration title"} value={title} onChange={setTitle} required /><TextArea label={lang === "zh" ? "本轮目标" : "Iteration objective"} value={objective} onChange={setObjective} required /></div><div className="grid gap-4 sm:grid-cols-2"><Picker label={lang === "zh" ? "固定已批准文档版本" : "Pin approved document versions"} options={currentDocuments.map((item) => ({ key: item.version_id, label: `${item.title} · v${item.current_version}` }))} selected={documents} onChange={setDocuments} /><Picker label={lang === "zh" ? "固定已确认本版需求" : "Pin confirmed current requirements"} options={current.map((item) => ({ key: item.id, label: item.content }))} selected={requirements} onChange={setRequirements} /></div></div>
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
  const [commands, setCommands] = useState(""); const [timeoutSeconds, setTimeoutSeconds] = useState(""); const [documentIds, setDocumentIds] = useState(docs.map((item) => item.version_id));
  const [requirementIds, setRequirementIds] = useState(requirements.map((item) => item.id));
  const documentOptionsKey = docs.map((item) => item.version_id).join("\0");
  const requirementOptionsKey = requirements.map((item) => item.id).join("\0");
  useEffect(() => {
    setDocumentIds(docs.map((item) => item.version_id));
  }, [documentOptionsKey]);
  useEffect(() => {
    setRequirementIds(requirements.map((item) => item.id));
  }, [requirementOptionsKey]);
  const [saving, setSaving] = useState(false); const [error, setError] = useState("");
  const inputsMissing = !documentIds.length || !requirementIds.length;
  const submit = async (event: FormEvent) => { event.preventDefault(); setSaving(true); setError(""); try {
    const parsedTimeout = timeoutSeconds.trim() ? Number(timeoutSeconds) : undefined;
    if (parsedTimeout !== undefined && (!Number.isInteger(parsedTimeout) || parsedTimeout < 30 || parsedTimeout > 1800)) { setError(lang === "zh" ? "任务超时必须是 30–1800 秒的整数。" : "Task timeout must be an integer from 30 to 1800 seconds."); setSaving(false); return; }
    await createProjectTask(projectId, { iteration_id: iteration.id, kind, title, objective, input_document_versions: documentIds, requirement_ids: requirementIds, write_paths: kind === "analysis" ? [] : lines(writePaths), verification_commands: lines(commands), timeout_seconds: parsedTimeout }); setTitle(""); setObjective(""); setWritePaths(""); setCommands(""); setTimeoutSeconds(""); onSaved();
  } catch (cause) { setError(actionError(cause, lang)); } finally { setSaving(false); } };
  return <SideForm title={lang === "zh" ? "添加执行任务" : "Add execution task"} icon={Plus}><form className="space-y-4" onSubmit={submit}>
    <label className="block text-sm"><span className="text-muted">{lang === "zh" ? "任务类型" : "Task kind"}</span><select value={kind} onChange={(event) => setKind(event.target.value as ProjectTask["kind"])} className={inputClass}><option value="code">{lang === "zh" ? "代码修改" : "Code change"}</option><option value="document">{lang === "zh" ? "项目文档" : "Project document"}</option><option value="analysis">{lang === "zh" ? "只读分析" : "Read-only analysis"}</option></select></label>
    <Field label={lang === "zh" ? "任务标题" : "Task title"} value={title} onChange={setTitle} required /><TextArea label={lang === "zh" ? "明确目标" : "Concrete objective"} value={objective} onChange={setObjective} required />
    {kind !== "analysis" ? <TextArea label={lang === "zh" ? "允许写入路径（每行一个）" : "Allowed write paths (one per line)"} value={writePaths} onChange={setWritePaths} required /> : null}
    <TextArea label={lang === "zh" ? "固定验证命令（每行一个；仅注册验证器，不支持 shell、内联代码或绝对路径）" : "Fixed verification commands (one per line; registered verifiers only, no shell, inline code, or absolute paths)"} value={commands} onChange={setCommands} />
    <label className="block text-sm"><span className="text-muted">{lang === "zh" ? "任务验证超时（秒，可选）" : "Task verification timeout (seconds, optional)"}</span><input type="number" min={30} max={1800} step={1} placeholder={lang === "zh" ? "留空使用项目默认值" : "Leave blank for project default"} value={timeoutSeconds} onChange={(event) => setTimeoutSeconds(event.target.value)} className={inputClass} /><span className="mt-1 block text-[11px] leading-5 text-subtle">{lang === "zh" ? "范围 30–1800 秒；只限制固定验证命令，不改变 OpenCode 会话超时。" : "30–1800 seconds; applies to fixed verification commands, not the OpenCode session."}</span></label>
    <Picker label={lang === "zh" ? "任务文档" : "Task documents"} options={docs.map((item) => ({ key: item.version_id, label: `${item.title} v${item.current_version}` }))} selected={documentIds} onChange={setDocumentIds} /><Picker label={lang === "zh" ? "任务需求" : "Task requirements"} options={requirements.map((item) => ({ key: item.id, label: item.content }))} selected={requirementIds} onChange={setRequirementIds} />
    {inputsMissing ? <p className="rounded-md bg-warn/10 p-3 text-xs leading-5 text-warn" role="status">{lang === "zh" ? "任务必须至少固定一份文档版本和一条已确认需求。" : "A task must pin at least one document version and one confirmed requirement."}</p> : null}
    {error ? <p className="text-xs text-danger" role="alert">{error}</p> : null}<Button className="w-full" disabled={saving || inputsMissing || !title.trim() || !objective.trim() || (kind !== "analysis" && !lines(writePaths).length)}>{lang === "zh" ? "保存任务" : "Save task"}</Button>
  </form></SideForm>;
}

function ExecutionTaskCard({ projectId, task, executions, requirements, documents, readOnly, harnessReady = true, onSaved }: {
  projectId: string; task: ProjectTask; executions: ProjectExecution[];
  requirements: ProjectRequirement[]; documents: ProjectDocument[];
  readOnly: boolean; harnessReady?: boolean; onSaved: () => void;
}) {
  const { lang } = useLang();
  const [live, setLive] = useState<ProjectExecution | null>(executions[0] || null);
  const [viewId, setViewId] = useState(executions[0]?.id || "");
  const [transport, setTransport] = useState<"http" | "cli">("http");
  const [working, setWorking] = useState(""); const [error, setError] = useState("");
  useEffect(() => { setLive(executions[0] || null); setViewId(executions[0]?.id || ""); }, [executions[0]?.id, task.id]);
  const execution = viewId && viewId !== live?.id
    ? executions.find((item) => item.id === viewId) || live
    : live;
  // A planned task has no execution record yet. Treat that empty state as
  // the latest attempt so the first-run action remains discoverable.
  const isLatest = !live || execution?.id === live?.id;
  const active = execution && ["queued", "running", "waiting_permission", "waiting_input"].includes(execution.status);
  const unavailable = execution?.status === "unknown";
  useEffect(() => {
    if (!active || !execution || !isLatest) return;
    let alive = true;
    const timer = window.setInterval(() => reconcileProjectExecution(projectId, execution.id).then((next) => { if (!alive) return; setLive(next); if (["completed", "failed", "stopped", "unknown"].includes(next.status)) onSaved(); }, (cause) => { if (alive) setError(actionError(cause, lang)); }), 1500);
    return () => { alive = false; window.clearInterval(timer); };
  }, [active, execution?.id, projectId, isLatest]);
  const start = async () => { setWorking("start"); setError(""); try { const created = await startProjectExecution(projectId, task.id, { transport }); setLive(created); setViewId(created.id); onSaved(); } catch (cause) { setError(actionError(cause, lang)); } finally { setWorking(""); } };
  const stop = async () => { if (!execution) return; setWorking("stop"); setError(""); try { setLive(await stopProjectExecution(projectId, execution.id)); onSaved(); } catch (cause) { setError(actionError(cause, lang)); } finally { setWorking(""); } };
  const filesystem = execution?.raw_state.evidence?.filesystem;
  const verification = execution?.raw_state.evidence?.verification;
  const verificationSource = execution?.raw_state.evidence?.verification_source;
  const atlasVerified = verificationSource === "atlas_fixed";
  const runSummary = execution?.raw_state.evidence?.run_summary;
  const cliRun = execution?.raw_state.evidence?.cli_run;
  const completionReport = execution?.raw_state.evidence?.completion_report;
  const commandEvidence = execution?.raw_state.evidence?.tool_calls?.commands || [];
  const displayStatus = execution?.status || task.execution_status;
  const acceptanceOpen = ["pending", "failed"].includes(task.acceptance_status);
  const baselineAdoptionError = execution?.application_state.baseline_adoption_error;
  const fullyApplied = execution?.application_status === "applied" && !baselineAdoptionError;
  const taskRequirements = requirements.filter((item) => task.requirement_ids.includes(item.id));
  const pinnedRevisions = new Map((task.requirement_revisions || []).map(
    (item) => [item.requirement_id, item.revision]));
  const taskDocuments = documents.filter((item) => task.input_document_versions.includes(item.version_id));
  return <article className="rounded-xl bg-surface p-5 shadow-card">
    <div className="flex flex-wrap items-start justify-between gap-3"><div><div className="flex flex-wrap items-center gap-2"><Badge tone={displayStatus === "completed" ? "ok" : displayStatus === "failed" || displayStatus === "unknown" ? "danger" : active ? "warn" : "default"}>{executionStatus(displayStatus, lang)}</Badge>{execution && task.kind !== "analysis" ? <Badge tone={execution.application_status === "applied" ? (baselineAdoptionError ? "danger" : "ok") : execution.application_status === "conflict" || execution.application_status === "failed" ? "danger" : execution.application_status === "superseded" ? "default" : "warn"}>{lang === "zh" ? `结果 ${applicationStatus(execution.application_status, lang)}${baselineAdoptionError ? "（基线未采用）" : ""}` : `Result ${applicationStatus(execution.application_status, lang)}${baselineAdoptionError ? " (baseline not adopted)" : ""}`}</Badge> : null}<Badge tone={task.acceptance_status === "passed" ? "ok" : task.acceptance_status === "failed" ? "danger" : "default"}>{lang === "zh" ? `验收 ${acceptanceStatus(task.acceptance_status, lang)}` : `Acceptance ${acceptanceStatus(task.acceptance_status, lang)}`}</Badge><TechnicalMeta label={lang === "zh" ? "任务技术信息" : "Task details"} value={task.id} inline /></div><h3 className="mt-2 font-medium">{task.title}</h3><p className="mt-1 text-sm leading-6 text-muted">{task.objective}</p>{!readOnly && !harnessReady && task.execution_status === "planned" ? <p className="mt-2 text-xs text-danger">{lang === "zh" ? "OpenCode 启动前检查未通过，修复环境后才能创建隔离执行。" : "OpenCode preflight must pass before an isolated run can be created."}</p> : null}</div><div className="flex flex-wrap items-center gap-2">{readOnly ? <Badge tone="default">{lang === "zh" ? "只读记录" : "Read-only"}</Badge> : !isLatest ? <Badge tone="default">{lang === "zh" ? "旧尝试只读" : "Older attempt"}</Badge> : null}{!readOnly && harnessReady && isLatest && !active && !unavailable && acceptanceOpen && (task.acceptance_status === "failed" || !fullyApplied) ? <><select aria-label={lang === "zh" ? "执行方式" : "Execution transport"} value={transport} onChange={(event) => setTransport(event.target.value as "http" | "cli")} className={`${inputClass} w-auto py-1.5 text-xs`}><option value="http">{lang === "zh" ? "OpenCode 会话" : "OpenCode session"}</option><option value="cli">OpenCode CLI</option></select><Button size="sm" onClick={start} disabled={Boolean(working)}><Bot className="size-4" />{execution ? (lang === "zh" ? "新建重试执行" : "Start retry") : (lang === "zh" ? "启动 OpenCode" : "Start OpenCode")}</Button></> : null}{!readOnly && isLatest && (active || unavailable) ? <Button size="sm" variant="outline" onClick={stop} disabled={Boolean(working)}>{unavailable ? (lang === "zh" ? "关闭不可用执行" : "Close unavailable run") : (lang === "zh" ? "停止" : "Stop")}</Button> : null}</div></div>
    {executions.length > 1 ? <div className="mt-3 flex flex-wrap items-center gap-2"><span className="text-xs text-subtle">{lang === "zh" ? "执行尝试" : "Attempts"}:</span>{executions.map((item, index) => <button key={item.id} type="button" onClick={() => setViewId(item.id)} className={`rounded-full px-2.5 py-1 font-mono text-[10px] ${item.id === execution?.id ? "bg-primary/10 text-primary" : "bg-bg-elevated text-subtle"}`}>{executions.length - index} · {executionStatus(item.status, lang)}</button>)}</div> : null}
    <div className="mt-3 grid gap-2 text-xs sm:grid-cols-4"><div className="rounded bg-bg-elevated p-3"><span className="text-subtle">{lang === "zh" ? "类型" : "Kind"}</span><p className="mt-1">{taskKind(task.kind, lang)}</p></div><div className="rounded bg-bg-elevated p-3"><span className="text-subtle">{lang === "zh" ? "写入范围" : "Write scope"}</span><p className="mt-1 break-all">{task.write_paths.join(" · ") || (lang === "zh" ? "只读" : "Read only")}</p></div><div className="rounded bg-bg-elevated p-3"><span className="text-subtle">{lang === "zh" ? "验证命令" : "Verification"}</span><p className="mt-1">{task.verification_commands.length}</p></div><div className="rounded bg-bg-elevated p-3"><span className="text-subtle">{lang === "zh" ? "验证超时" : "Timeout"}</span><p className="mt-1">{task.timeout_seconds ? `${task.timeout_seconds}s` : (lang === "zh" ? "项目默认" : "Project default")}</p></div></div>
    <div className="mt-3 grid gap-3 text-xs sm:grid-cols-2">
      <div className="rounded bg-bg-elevated p-3"><span className="text-subtle">{lang === "zh" ? "关联需求与验收条件" : "Linked requirements & acceptance"}</span>{taskRequirements.map((item) => <div key={item.id} className="mt-2"><p className="leading-5">{item.content}{pinnedRevisions.has(item.id) ? <span className="ml-1 font-mono text-[10px] text-subtle">r{pinnedRevisions.get(item.id)}</span> : null}</p>{item.acceptance_conditions.length ? <ul className="mt-1 list-disc space-y-0.5 pl-4 text-muted">{item.acceptance_conditions.map((value) => <li key={value}>{value}</li>)}</ul> : null}</div>)}{!taskRequirements.length ? <p className="mt-1 text-warn">{lang === "zh" ? "该任务未关联需求。" : "This task links no requirement."}</p> : null}</div>
      <div className="rounded bg-bg-elevated p-3"><span className="text-subtle">{lang === "zh" ? "固定文档版本" : "Pinned document versions"}</span>{taskDocuments.map((item) => <p key={item.version_id} className="mt-1">{item.title} · v{item.current_version}</p>)}{!taskDocuments.length ? <p className="mt-1 text-subtle">—</p> : null}</div>
    </div>
    {execution ? <ExecutionResult projectId={projectId} task={task} execution={execution} requirements={taskRequirements} readOnly={readOnly || !isLatest} onChange={(value) => { setLive(value); setViewId(value.id); }} onSaved={onSaved} /> : null}
    {verification ? <div className={`mt-4 rounded-md p-4 ${atlasVerified && verification.all_planned_passed ? "bg-ok/10" : "bg-warn/10"}`}><p className={`text-sm font-medium ${atlasVerified && verification.all_planned_passed ? "text-ok" : "text-warn"}`}>{atlasVerified && verification.all_planned_passed ? (lang === "zh" ? "Atlas 固定验证命令已通过" : "Atlas fixed verification commands passed") : verification.all_planned_passed ? (lang === "zh" ? "Agent 报告验证通过，但尚未由 Atlas 独立重跑" : "Agent-reported verification passed; Atlas has not rerun it") : (lang === "zh" ? "验证未完整通过或证据不足" : "Verification is incomplete or did not pass")}</p>{commandEvidence.map((item, index) => <details key={`${item.command}:${index}`} className="mt-2"><summary className="cursor-pointer font-mono text-xs">{item.exit === 0 ? "✓" : "!"} {item.command}{item.durationMs !== undefined ? ` · ${item.durationMs}ms` : ""}{item.timedOut ? (lang === "zh" ? " · 超时" : " · timed out") : ""}</summary><pre className="mt-2 max-h-48 overflow-auto whitespace-pre-wrap rounded bg-surface p-3 font-mono text-[11px] text-muted">{item.output || (lang === "zh" ? "没有记录输出" : "No output recorded")}</pre></details>)}</div> : null}
    {runSummary ? <div className={`mt-4 rounded-md p-4 ${runSummary.status === "completed" && (!verification || (atlasVerified && verification.all_planned_passed)) ? "bg-ok/10" : "bg-warn/10"}`}><p className="text-sm font-medium">{lang === "zh" ? "运行摘要" : "Run summary"}</p><div className="mt-2 grid gap-2 text-xs sm:grid-cols-4"><div><span className="text-subtle">{lang === "zh" ? "状态" : "Status"}</span><p className="mt-1">{runSummary.status || "—"}</p></div><div><span className="text-subtle">{lang === "zh" ? "退出码" : "Exit code"}</span><p className="mt-1">{runSummary.exitCode ?? "—"}</p></div><div><span className="text-subtle">{lang === "zh" ? "超时" : "Timed out"}</span><p className="mt-1">{runSummary.timedOut ? (lang === "zh" ? "是" : "Yes") : (lang === "zh" ? "否" : "No")}</p></div><div><span className="text-subtle">{lang === "zh" ? "执行方式" : "Transport"}</span><p className="mt-1">{execution.input_state.transport === "cli" ? "OpenCode CLI" : "OpenCode session"}</p></div></div>{cliRun?.summary?.eventTypes?.length ? <p className="mt-2 text-xs text-muted">{lang === "zh" ? "CLI 事件" : "CLI events"}：{cliRun.summary.eventTypes.join(" · ")}</p> : null}{cliRun?.directory ? <p className="mt-2 break-all font-mono text-[10px] text-subtle">{lang === "zh" ? "证据目录" : "Evidence directory"}：{cliRun.directory}</p> : null}</div> : null}
    {completionReport && execution && ["completed", "failed", "stopped"].includes(execution.status) ? <div className={`mt-4 rounded-md p-4 ${completionReport.valid ? "bg-bg-elevated" : "bg-warn/10"}`}><p className={`text-sm font-medium ${completionReport.valid ? "text-fg" : "text-warn"}`}>{completionReport.valid ? (lang === "zh" ? "Agent 结构化完成报告" : "Structured agent completion report") : (lang === "zh" ? "Agent 完成报告缺失或无效" : "Agent completion report is missing or invalid")}</p><p className="mt-1 text-xs text-subtle">{lang === "zh" ? "此报告经过格式与需求 ID 校验，但仍是 agent 提供的信息，不等于 Atlas 验证或产品验收。" : "Its shape and requirement IDs are validated, but it remains agent-supplied information rather than Atlas verification or product acceptance."}</p>{completionReport.valid ? <div className="mt-3 space-y-2 text-xs">{completionReport.requirements.map((item) => <div key={item.id} className="rounded bg-surface p-3"><p><strong>{acceptanceStatus(item.status, lang)}</strong><TechnicalMeta label={lang === "zh" ? "需求技术信息" : "Requirement details"} value={item.id} inline /></p>{item.evidence.map((value) => <p key={value} className="mt-1 text-muted">{value}</p>)}</div>)}<ChangePaths title={lang === "zh" ? "未完成项" : "Unfinished"} paths={completionReport.unfinished} /><ChangePaths title={lang === "zh" ? "方案偏离" : "Deviations"} paths={completionReport.deviations} /></div> : <TechnicalError message={completionReport.error} lang={lang} />}</div> : null}
    {filesystem ? <div className={`mt-4 rounded-md p-4 ${filesystem.scope_compliant ? "bg-ok/10" : "bg-danger/10"}`}><p className={`text-sm font-medium ${filesystem.scope_compliant ? "text-ok" : "text-danger"}`}>{filesystem.scope_compliant ? (lang === "zh" ? "文件变化位于声明范围内" : "File changes stayed within scope") : (lang === "zh" ? "发现超出声明范围的文件变化" : "File changes exceeded the declared scope")}</p><ChangePaths title={lang === "zh" ? "新增" : "Added"} paths={filesystem.added} /><ChangePaths title={lang === "zh" ? "修改" : "Modified"} paths={filesystem.modified} /><ChangePaths title={lang === "zh" ? "删除" : "Removed"} paths={filesystem.removed} />{filesystem.out_of_scope_changes.length ? <ChangePaths title={lang === "zh" ? "越界变化" : "Out-of-scope changes"} paths={filesystem.out_of_scope_changes} /> : null}</div> : null}
    {execution?.raw_state.evidence?.assistant_text ? <details className="mt-4"><summary className="cursor-pointer text-sm text-primary">{lang === "zh" ? "查看引擎结果" : "View engine result"}</summary><div className="mt-3 rounded-md bg-bg-elevated p-4"><Prose md={execution.raw_state.evidence.assistant_text} /></div></details> : null}
    {task.acceptance_evidence.length ? <details className="mt-4"><summary className="cursor-pointer text-sm text-primary">{lang === "zh" ? "验收记录" : "Acceptance record"} · {acceptanceStatus(task.acceptance_status, lang)}</summary><div className="mt-2 space-y-2">{task.acceptance_evidence.map((item, index) => <AcceptanceEvidenceItem key={`${item.kind}:${index}`} item={item} lang={lang} />)}</div></details> : null}
    {error ? <p className="mt-3 text-xs text-danger">{error}</p> : null}
  </article>;
}

function AcceptanceEvidenceItem({ item, lang }: {
  item: AcceptanceEvidence;
  lang: "zh" | "en";
}) {
  if (item.kind !== "acceptance_binding") {
    return <div className="rounded-md bg-bg-elevated p-3 text-xs"><span className="font-mono text-subtle">{item.kind}</span><p className="mt-1 leading-5 text-muted">{item.summary}</p></div>;
  }
  const binding = item as typeof item & {
    execution_id?: string | null;
    baseline_id?: string | null;
    document_version_ids?: string[];
    requirement_bindings?: Array<{ requirement_id?: string; revision?: number; acceptance_conditions?: string[] }>;
    condition_results?: AcceptanceConditionResult[];
  };
  const requirements = Array.isArray(binding.requirement_bindings) ? binding.requirement_bindings : [];
  const documents = Array.isArray(binding.document_version_ids) ? binding.document_version_ids : [];
  const conditionCount = requirements.reduce((total, requirement) =>
    total + (requirement.acceptance_conditions?.length || 0), 0);
  const conditionResults = Array.isArray(binding.condition_results)
    ? binding.condition_results : null;
  return <div className="rounded-md border border-primary/20 bg-bg-elevated p-3 text-xs">
    <div className="flex flex-wrap items-center gap-2"><span className="font-mono text-primary">{item.kind}</span><code className="font-mono text-subtle">{binding.execution_id || (lang === "zh" ? "无 execution" : "no execution")}</code></div>
    <p className="mt-1 leading-5 text-muted">{item.summary}</p>
    <div className="mt-2 grid gap-1 text-[11px] text-subtle sm:grid-cols-2">
      <span>{lang === "zh" ? "基线" : "Baseline"}: <code>{binding.baseline_id || "—"}</code></span>
      <span>{lang === "zh" ? "文档版本" : "Document versions"}: <code>{documents.length}</code></span>
    </div>
    {requirements.length ? <div className="mt-2"><p className="font-medium text-muted">{lang === "zh" ? "需求条件快照" : "Requirement condition snapshot"}</p>{requirements.map((requirement) => <div key={requirement.requirement_id || "unknown"} className="mt-1"><span className="font-mono text-subtle">{requirement.requirement_id || "unknown"}</span>{requirement.revision ? <span className="ml-1 text-subtle">r{requirement.revision}</span> : null}{requirement.acceptance_conditions?.length ? <ul className="ml-4 list-disc text-muted">{requirement.acceptance_conditions.map((condition) => <li key={condition}>{condition}</li>)}</ul> : null}</div>)}</div> : null}
    {conditionCount ? <div className="mt-2 border-t border-border pt-2"><p className="font-medium text-muted">{lang === "zh" ? "逐条件人工结果" : "Per-condition human results"}</p>{conditionResults && conditionResults.length === conditionCount ? <ul className="mt-1 space-y-1">{conditionResults.map((result) => <li key={`${result.requirement_id}:${result.revision}:${result.condition}`}><span className="font-mono text-subtle">{result.requirement_id} · r{result.revision}</span><span className="ml-2">{acceptanceStatus(result.result, lang)}</span><span className="ml-2 text-muted">{result.condition}</span>{result.note ? <span className="ml-2 text-subtle">— {result.note}</span> : null}</li>)}</ul> : <p className="mt-1 text-warn">{lang === "zh" ? "旧记录未回填逐条件结果；不会据此推断通过或失败。" : "This legacy record has no backfilled per-condition results; no pass/fail conclusion is inferred."}</p>}</div> : null}
  </div>;
}

type AcceptanceConditionDraft = Omit<AcceptanceConditionResult, "result"> & {
  result: AcceptanceConditionResult["result"] | "pending";
};

type AcceptanceConditionRow = {
  key: string;
  requirement_id: string;
  revision: number;
  condition: string;
};

function taskConditionRows(task: ProjectTask, requirements: ProjectRequirement[]): AcceptanceConditionRow[] {
  const snapshots: ProjectRequirementSnapshot[] = task.requirement_snapshots?.length
    ? task.requirement_snapshots
    : requirements.map((item) => ({
        requirement_id: item.id,
        revision: item.revision ?? 1,
        content: item.content,
        acceptance_conditions: item.acceptance_conditions,
        reference_ids: item.reference_ids,
      }));
  return snapshots.flatMap((snapshot) => snapshot.acceptance_conditions.map((condition, index) => ({
    key: `${snapshot.requirement_id}:${snapshot.revision}:${index}`,
    requirement_id: snapshot.requirement_id,
    revision: snapshot.revision,
    condition,
  })));
}

function ExecutionResult({ projectId, task, execution, requirements, readOnly, onChange, onSaved }: {
  projectId: string; task: ProjectTask; execution: ProjectExecution; requirements: ProjectRequirement[]; readOnly: boolean;
  onChange: (value: ProjectExecution) => void; onSaved: () => void;
}) {
  const { lang } = useLang(); const [working, setWorking] = useState(""); const [error, setError] = useState(""); const [evidence, setEvidence] = useState(""); const [followUp, setFollowUp] = useState("");
  const conditionRows = taskConditionRows(task, requirements);
  const conditionRowsKey = conditionRows.map((row) => row.key).join("\0");
  const [conditionResults, setConditionResults] = useState<Record<string, AcceptanceConditionDraft>>({});
  useEffect(() => {
    const next: Record<string, AcceptanceConditionDraft> = {};
    for (const row of conditionRows) next[row.key] = { ...row, result: "pending" };
    setConditionResults(next);
  }, [conditionRowsKey, task.id]);
  const acceptanceOpen = ["pending", "failed"].includes(task.acceptance_status);
  const baselineAdoptionError = execution.application_state.baseline_adoption_error;
  const fullyApplied = execution.application_status === "applied" && !baselineAdoptionError;
  const interaction = execution.raw_state.interaction;
  const canCleanup = ["completed", "failed", "stopped", "unknown"].includes(execution.status)
    && (task.kind === "analysis" || execution.status !== "completed"
      || ["applied", "not_applicable", "superseded"].includes(execution.application_status));
  useEffect(() => { setEvidence(""); setFollowUp(""); setError(""); }, [execution.id]);
  useEffect(() => {
    const verification = execution.raw_state.evidence?.verification;
    const verificationSource = execution.raw_state.evidence?.verification_source;
    if (!evidence && verification?.all_planned_passed && verificationSource === "atlas_fixed") setEvidence(
      lang === "zh" ? `Atlas 已记录 ${verification.successful_commands.length} 条固定验证命令通过：${verification.successful_commands.join("；")}` : `Atlas recorded ${verification.successful_commands.length} fixed verification command(s) passing: ${verification.successful_commands.join("; ")}`);
  }, [execution.updated_at]);
  const permission = async (reply: "once" | "reject") => { if (!interaction?.request.id) return; setWorking(reply); setError(""); try { onChange(await replyProjectExecutionPermission(projectId, execution.id, { request_id: interaction.request.id, reply })); } catch (cause) { setError(actionError(cause, lang)); } finally { setWorking(""); } };
  const applyResult = async () => { setWorking("apply"); setError(""); try { onChange(await applyProjectExecutionResult(projectId, execution.id)); onSaved(); } catch (cause) { setError(actionError(cause, lang)); onSaved(); } finally { setWorking(""); } };
  const recoverApply = async () => {
    if (!window.confirm(lang === "zh" ? "这会明确恢复 apply 前的文件状态，不会自动重放结果。继续吗？" : "This explicitly restores the pre-apply files and will not replay the result. Continue?")) return;
    setWorking("recover-apply"); setError("");
    try { onChange(await recoverProjectExecutionApply(projectId, execution.id)); onSaved(); }
    catch (cause) { setError(actionError(cause, lang)); }
    finally { setWorking(""); }
  };
  const cleanup = async () => { setWorking("cleanup"); setError(""); try { onChange(await cleanupProjectExecution(projectId, execution.id)); onSaved(); } catch (cause) { setError(actionError(cause, lang)); } finally { setWorking(""); } };
  const continueRun = async () => { setWorking("continue"); setError(""); try { onChange(await continueProjectExecution(projectId, execution.id, followUp)); setFollowUp(""); onSaved(); } catch (cause) { setError(actionError(cause, lang)); onSaved(); } finally { setWorking(""); } };
  const accept = async (status: "passed" | "failed" | "waived") => {
    const results = conditionRows.map((row) => {
      const draft = conditionResults[row.key];
      if (!draft || draft.result === "pending") return null;
      return {
        requirement_id: row.requirement_id,
        revision: row.revision,
        condition: row.condition,
        result: draft.result,
        ...(draft.note?.trim() ? { note: draft.note } : {}),
      } as AcceptanceConditionResult;
    }).filter((value): value is AcceptanceConditionResult => value !== null);
    if (results.length !== conditionRows.length) {
      setError(lang === "zh" ? "请先为每条验收条件选择明确结果。" : "Choose an explicit result for every acceptance condition first.");
      return;
    }
    if (status === "passed" && results.some((item) => item.result !== "passed")) {
      setError(lang === "zh" ? "验收通过要求每条条件都已通过。" : "Passing acceptance requires every condition to pass.");
      return;
    }
    if (status === "waived" && results.some((item) => item.result !== "waived")) {
      setError(lang === "zh" ? "明确免验要求每条条件都标记为免验。" : "Waiving requires every condition to be marked waived.");
      return;
    }
    if (status === "failed" && !results.some((item) => item.result === "failed")) {
      setError(lang === "zh" ? "验收失败至少需要一条条件标记为未通过。" : "A failed acceptance needs at least one failed condition.");
      return;
    }
    setWorking(status); setError("");
    try {
      await recordProjectTaskAcceptance(projectId, task.id, {
        status, evidence: [{ kind: "review", summary: evidence }], condition_results: results,
      });
      onSaved();
    } catch (cause) { setError(actionError(cause, lang)); } finally { setWorking(""); }
  };
  const conditionsIncomplete = conditionRows.some((row) =>
    !conditionResults[row.key] || conditionResults[row.key].result === "pending");
  return <div className="mt-4 border-t border-border pt-4">
    <div className="flex flex-wrap items-center gap-2 text-xs"><TechnicalMeta label={lang === "zh" ? "执行技术信息" : "Execution details"} value={execution.id} inline /><span className="text-muted">OpenCode · {execution.input_state.model || (lang === "zh" ? "未记录模型" : "unknown model")}</span><span className="text-subtle">{execution.raw_state.engine_status || executionStatus(execution.status, lang)}</span></div>
    {readOnly ? <p className="mt-2 text-[11px] leading-5 text-subtle">{lang === "zh" ? "只读：历史尝试和已结束迭代不能继续操作；请切换到最新尝试或建立新迭代。" : "Read-only: historical attempts and finished iterations cannot be operated. Use the latest attempt or start a new iteration."}</p> : null}
    {!readOnly && interaction?.type === "permission" ? <div className="mt-3 rounded-md bg-warn/10 p-4"><p className="text-sm font-medium text-warn">{lang === "zh" ? "OpenCode 等待工具权限" : "OpenCode is waiting for tool permission"}</p><p className="mt-2 break-all font-mono text-xs text-muted">{interaction.request.permission || "tool"} · {(interaction.request.patterns || []).join(" · ")}</p><div className="mt-3 flex flex-wrap gap-2"><Button size="sm" disabled={Boolean(working)} onClick={() => permission("once")}>{lang === "zh" ? "仅本次允许" : "Allow once"}</Button><Button size="sm" variant="outline" disabled={Boolean(working)} onClick={() => permission("reject")}>{lang === "zh" ? "拒绝" : "Reject"}</Button></div></div> : null}
    {!readOnly && interaction?.type === "question" ? <ExecutionQuestionForm projectId={projectId} execution={execution} onChange={onChange} /> : null}
    {!readOnly && execution.engine !== "opencode-cli" && ["completed", "failed", "stopped"].includes(execution.status) && acceptanceOpen && (task.kind === "analysis" || ["pending", "conflict", "failed"].includes(execution.application_status)) ? <div className="mt-4 rounded-md border border-border p-4"><p className="text-sm font-medium">{lang === "zh" ? "在当前 OpenCode 会话中继续" : "Continue in this OpenCode session"}</p><p className="mt-1 text-xs leading-5 text-muted">{lang === "zh" ? "后续指令会沿用当前隔离副本和会话上下文，同时建立一条新的执行记录与快照边界。" : "The follow-up keeps the isolated work copy and session context while creating a new execution record and snapshot boundary."}</p><TextArea label={lang === "zh" ? "后续修改或核查要求" : "Follow-up change or review instruction"} value={followUp} onChange={setFollowUp} /><Button className="mt-3" size="sm" variant="outline" disabled={Boolean(working) || !followUp.trim()} onClick={continueRun}>{lang === "zh" ? "继续当前会话" : "Continue session"}</Button></div> : null}
    {!readOnly && execution.application_state.recovery?.action === "explicit_apply_recovery_required" ? <div className="mt-4 rounded-md border border-danger/40 bg-danger/10 p-4"><p className="text-sm font-medium text-danger">{lang === "zh" ? "检测到未完成的文件应用" : "An interrupted file apply needs review"}</p><p className="mt-2 text-xs leading-5 text-muted">{lang === "zh" ? "Atlas 保留了 apply journal，但不会自动重放或覆盖文件。只有在你明确确认后，才会尝试恢复 apply 前的文件状态。" : "Atlas kept the apply journal, but will not replay or overwrite files automatically. Only explicitly confirm to attempt restoring the pre-apply state."}</p><Button className="mt-3" size="sm" variant="outline" disabled={Boolean(working)} onClick={recoverApply}>{lang === "zh" ? "明确恢复 apply 前文件" : "Restore pre-apply files"}</Button></div> : null}
    {!readOnly && execution.status === "completed" && task.kind !== "analysis" && execution.application_status !== "applied" && execution.application_status !== "superseded" && execution.application_state.recovery?.action !== "explicit_apply_recovery_required" ? <div className={`mt-4 rounded-md p-4 ${execution.application_status === "conflict" || execution.application_status === "failed" ? "bg-danger/10" : "bg-primary/10"}`}><p className="text-sm font-medium">{lang === "zh" ? "结果仍在隔离工作副本中" : "The result is still in the isolated work copy"}</p><p className="mt-2 text-xs leading-5 text-muted">{lang === "zh" ? "应用前 Atlas 会再次核对源工作区和已接受基线；有冲突时不会覆盖现有文件。应用成功后，准确写回的状态会成为新的已接受项目基线。" : "Before applying, Atlas rechecks the source workspace and accepted baseline. Conflicts do not overwrite current files. A successful exact write-back becomes the new accepted project baseline."}</p>{execution.application_state.error ? <TechnicalError message={execution.application_state.error} lang={lang} /> : null}<Button className="mt-3" size="sm" disabled={Boolean(working) || !execution.raw_state.evidence?.filesystem?.scope_compliant} onClick={applyResult}><Save className="size-4" />{lang === "zh" ? "应用并更新项目基线" : "Apply and update baseline"}</Button></div> : null}
    {!readOnly && canCleanup ? <div className="mt-4 rounded-md border border-border p-4"><p className="text-sm font-medium">{lang === "zh" ? "工作副本清理" : "Work copy cleanup"}</p><p className="mt-1 text-xs leading-5 text-muted">{execution.status === "failed" || execution.status === "stopped" ? (lang === "zh" ? "本次执行未进入应用阶段；清理会删除隔离副本，但保留失败/停止证据。" : "This run did not enter the apply stage; cleanup removes the isolated copy while preserving failure/stop evidence.") : (lang === "zh" ? "清理只删除本次隔离工作副本，保留执行记录和证据目录。" : "This removes only the isolated work copy and preserves the execution record and evidence directory.")}</p><Button className="mt-3" size="sm" variant="outline" disabled={Boolean(working)} onClick={cleanup}>{lang === "zh" ? "清理工作副本" : "Clean work copy"}</Button></div> : null}
    {baselineAdoptionError ? <div className="mt-4 rounded-md bg-danger/10 p-4"><p className="text-sm font-medium text-danger">{lang === "zh" ? "文件已写回，但新项目基线未采用" : "Files were written back, but the new project baseline was not adopted"}</p><TechnicalError message={baselineAdoptionError} lang={lang} /><p className="mt-2 text-xs leading-5 text-muted">{lang === "zh" ? "Atlas 已把执行结果写回工作区，但采用新基线失败；在此之前结果不应视为完整应用，也不能通过验收。请在「项目工作区基线」中检查外部变化并采用当前状态，然后新建重试执行或重新验收。" : "Atlas wrote the result back, but adopting the new baseline failed; the result is not fully applied and cannot pass acceptance. Check external changes and adopt the current state in the workspace baseline panel, then retry or accept again."}</p></div> : null}
    {!readOnly && ["completed", "failed", "stopped"].includes(execution.status) && acceptanceOpen && (task.kind === "analysis" || fullyApplied) ? <div className="mt-4 rounded-md border border-border p-4"><p className="text-sm font-medium">{task.acceptance_status === "failed" ? (lang === "zh" ? "上次验收失败，可补充证据后重新确认" : "The last acceptance failed; review the result and decide again") : (lang === "zh" ? "产品验收仍待独立确认" : "Product acceptance still needs a separate decision")}</p>{execution.status !== "completed" ? <p className="mt-1 text-xs leading-5 text-warn">{lang === "zh" ? `本次执行${execution.status === "stopped" ? "已停止" : "失败"}，不能验收通过；请新建重试执行，或填写理由后明确免验。` : `This execution ${execution.status === "stopped" ? "was stopped" : "failed"} and cannot pass acceptance. Start a retry, or waive it with an explicit reason.`}</p> : null}{conditionRows.length ? <fieldset className="mt-4 rounded-md border border-border p-3"><legend className="px-1 text-xs font-medium">{lang === "zh" ? "逐条验收条件（必填）" : "Per-condition acceptance (required)"}</legend><div className="space-y-3">{conditionRows.map((row) => { const draft = conditionResults[row.key]; return <div key={row.key} className="rounded-md bg-bg-elevated p-3"><div className="flex flex-wrap items-center gap-2"><span className="min-w-0 flex-1 text-xs leading-5">{row.condition}</span><select aria-label={`${lang === "zh" ? "验收条件结果" : "Acceptance condition result"}: ${row.condition}`} value={draft?.result || "pending"} onChange={(event) => setConditionResults((current) => ({ ...current, [row.key]: { requirement_id: row.requirement_id, revision: row.revision, condition: row.condition, result: event.target.value as AcceptanceConditionDraft["result"], note: current[row.key]?.note || "" } }))} className={`${inputClass} mt-0 h-9 w-auto min-w-32`}><option value="pending">{lang === "zh" ? "请选择" : "Choose"}</option><option value="passed">{lang === "zh" ? "通过" : "Passed"}</option><option value="failed">{lang === "zh" ? "未通过" : "Failed"}</option><option value="waived">{lang === "zh" ? "免验" : "Waived"}</option></select></div><input aria-label={`${lang === "zh" ? "验收条件说明" : "Acceptance condition note"}: ${row.condition}`} value={draft?.note || ""} onChange={(event) => setConditionResults((current) => ({ ...current, [row.key]: { requirement_id: row.requirement_id, revision: row.revision, condition: row.condition, result: current[row.key]?.result || "pending", note: event.target.value } }))} placeholder={lang === "zh" ? "可选说明" : "Optional note"} className={`${inputClass} mt-2 h-9`} /></div>; })}</div><p className="mt-2 text-[11px] leading-5 text-subtle">{lang === "zh" ? "每条条件都必须明确选择结果；通过要求全部通过，免验要求全部免验。" : "Every condition needs an explicit result; passing requires all passed, and waiving requires all waived."}</p></fieldset> : null}<TextArea label={lang === "zh" ? "验收证据或失败原因" : "Acceptance evidence or failure reason"} value={evidence} onChange={setEvidence} /><div className="mt-3 flex flex-wrap gap-2">{execution.status === "completed" ? <><Button size="sm" disabled={Boolean(working) || !evidence.trim() || conditionsIncomplete} onClick={() => accept("passed")}>{lang === "zh" ? "验收通过" : "Pass"}</Button><Button size="sm" variant="outline" disabled={Boolean(working) || !evidence.trim() || conditionsIncomplete} onClick={() => accept("failed")}>{lang === "zh" ? "验收失败" : "Fail"}</Button></> : null}<Button size="sm" variant="outline" disabled={Boolean(working) || !evidence.trim() || conditionsIncomplete} onClick={() => accept("waived")}>{execution.status === "completed" ? (lang === "zh" ? "明确免验" : "Waive") : (lang === "zh" ? "填写理由并免验" : "Waive with reason")}</Button></div></div> : null}
    {error ? <p className="mt-3 text-xs text-danger">{error}</p> : null}
  </div>;
}

function ExecutionQuestionForm({ projectId, execution, onChange }: {
  projectId: string; execution: ProjectExecution; onChange: (value: ProjectExecution) => void;
}) {
  const { lang } = useLang(); const questions = execution.raw_state.interaction?.request.questions || [];
  const [answers, setAnswers] = useState<string[]>(questions.map(() => "")); const [working, setWorking] = useState(false); const [error, setError] = useState("");
  const submit = async () => { const requestId = execution.raw_state.interaction?.request.id; if (!requestId) return; setWorking(true); setError(""); try { onChange(await replyProjectExecutionQuestion(projectId, execution.id, { request_id: requestId, answers: answers.map((value) => value.split(",").map((item) => item.trim()).filter(Boolean)) })); } catch (cause) { setError(actionError(cause, lang)); } finally { setWorking(false); } };
  const reject = async () => { const requestId = execution.raw_state.interaction?.request.id; if (!requestId) return; setWorking(true); setError(""); try { onChange(await replyProjectExecutionQuestion(projectId, execution.id, { request_id: requestId, reject: true })); } catch (cause) { setError(actionError(cause, lang)); } finally { setWorking(false); } };
  return <div className="mt-3 rounded-md bg-warn/10 p-4"><p className="text-sm font-medium text-warn">{lang === "zh" ? "OpenCode 需要你的输入" : "OpenCode needs your input"}</p><div className="mt-3 space-y-3">{questions.map((question, index) => <div key={`${question.header}:${index}`}><p className="text-sm">{question.question}</p>{question.options.length ? <p className="mt-1 text-xs leading-5 text-muted">{question.options.map((item) => `${item.label}：${item.description}`).join(" · ")}</p> : null}<Field label={question.multiple ? (lang === "zh" ? "答案（多选用逗号分隔）" : "Answer (comma-separated for multiple)") : (lang === "zh" ? "答案" : "Answer")} value={answers[index] || ""} onChange={(value) => setAnswers((items) => items.map((item, offset) => offset === index ? value : item))} required /></div>)}</div><div className="mt-3 flex gap-2"><Button size="sm" disabled={working || answers.some((value) => !value.trim())} onClick={submit}>{lang === "zh" ? "提交答案" : "Submit answers"}</Button><Button size="sm" variant="outline" disabled={working} onClick={reject}>{lang === "zh" ? "拒绝回答" : "Reject question"}</Button></div>{error ? <p className="mt-2 text-xs text-danger">{error}</p> : null}</div>;
}

function executionStatus(status: ProjectTask["execution_status"], lang: "zh" | "en") {
  const zh: Record<ProjectTask["execution_status"], string> = { planned: "待执行", queued: "排队中", running: "执行中", waiting_permission: "等待权限", waiting_input: "等待输入", completed: "执行完成", failed: "执行失败", stopped: "已停止", unknown: "待核对" };
  return lang === "zh" ? zh[status] : status.replaceAll("_", " ");
}

function iterationStatus(status: string, lang: "zh" | "en") {
  const labels: Record<string, { zh: string; en: string }> = {
    active: { zh: "进行中", en: "Active" }, completed: { zh: "已完成", en: "Completed" }, abandoned: { zh: "已放弃", en: "Abandoned" },
  };
  return labels[status]?.[lang] || status.replaceAll("_", " ");
}

function taskKind(kind: string, lang: "zh" | "en") {
  const labels: Record<string, { zh: string; en: string }> = {
    code: { zh: "代码修改", en: "Code change" }, document: { zh: "项目文档", en: "Project document" }, analysis: { zh: "只读分析", en: "Read-only analysis" },
  };
  return labels[kind]?.[lang] || kind;
}

function applicationStatus(status: string, lang: "zh" | "en") {
  const labels: Record<string, { zh: string; en: string }> = {
    pending: { zh: "待应用", en: "Pending" }, applied: { zh: "已应用", en: "Applied" }, conflict: { zh: "有冲突", en: "Conflict" }, failed: { zh: "应用失败", en: "Failed" }, superseded: { zh: "已被替代", en: "Superseded" },
  };
  return labels[status]?.[lang] || status.replaceAll("_", " ");
}

function acceptanceStatus(status: string, lang: "zh" | "en") {
  const labels: Record<string, { zh: string; en: string }> = {
    pending: { zh: "待验收", en: "Pending" }, passed: { zh: "已通过", en: "Passed" }, failed: { zh: "未通过", en: "Failed" }, waived: { zh: "已免验", en: "Waived" },
  };
  return labels[status]?.[lang] || status.replaceAll("_", " ");
}

function OpenItemsPanel({ projectId, workspace, onSaved }: {
  projectId: string; workspace: ProjectWorkspace; onSaved: () => void;
}) {
  const { lang } = useLang();
  const items = workspace.open_items || [];
  const openItems = items.filter((item) => item.status === "open");
  const handled = items.filter((item) => item.status !== "open");
  const [activeId, setActiveId] = useState("");
  const [note, setNote] = useState("");
  const [working, setWorking] = useState("");
  const [error, setError] = useState("");
  const [showHandled, setShowHandled] = useState(false);
  const resolve = async (item: ProjectOpenItem, status: "answered" | "resolved" | "accepted" | "deferred" | "dismissed", convert?: "decision" | "requirement") => {
    setWorking(`${item.id}:${status}`); setError("");
    try {
      await resolveProjectOpenItem(projectId, {
        run_id: item.run_id, item_kind: item.kind, item_index: item.index,
        item_key: item.key, status, note: note.trim(), ...(convert ? { convert } : {}),
      });
      setActiveId(""); setNote(""); onSaved();
    } catch (cause) { setError(actionError(cause, lang)); } finally { setWorking(""); }
  };
  return <section className="mt-6 rounded-xl bg-surface p-5 shadow-card">
    <div className="flex flex-wrap items-start justify-between gap-3">
      <div className="flex max-w-2xl items-start gap-3"><Lightbulb className="mt-0.5 size-5 text-primary" /><div>
        <h2 className="font-serif text-xl font-medium">{lang === "zh" ? "待处理事项" : "Open items"}</h2>
        <p className="mt-1 text-xs leading-5 text-subtle">{lang === "zh" ? "来自最近一次完成的分析、改进或价值运行的问题、冲突和建议。处理结果会持久保存；回答问题可同时记录为项目决定，建议可转为候选需求。" : "Questions, conflicts, and suggestions from the latest completed analysis, improvement, or value run. Dispositions are persisted; answers can become decisions and suggestions can become candidate requirements."}</p>
      </div></div>
      <span className={`text-xs ${openItems.length ? "text-warn" : "text-subtle"}`}>{lang === "zh" ? `${openItems.length} 项待处理` : `${openItems.length} open`}</span>
    </div>
    {!items.length ? <p className="mt-4 text-sm text-subtle">{lang === "zh" ? "还没有可处理的分析结果。先运行「分析固定资料」。" : "No analysis output to process yet. Run \"Analyze pinned sources\" first."}</p> : null}
    {error ? <p className="mt-3 rounded-md bg-danger/10 p-3 text-xs text-danger">{error}</p> : null}
    <div className="mt-4 space-y-3">
      {openItems.map((item) => <article key={item.id} className="rounded-lg bg-bg-elevated p-4">
        <div className="flex flex-wrap items-center gap-2">
          <Badge tone={item.kind === "conflict" ? "warn" : "default"}>{openItemKind(item.kind, lang)}</Badge>
          <Badge tone="default">{generationMode(item.mode, lang)}</Badge>
          {!item.current ? <Badge tone="default">{lang === "zh" ? "仅供参考" : "Advisory"}</Badge> : null}
          <TechnicalMeta label={lang === "zh" ? "技术信息" : "Technical details"} value={item.key} />
        </div>
        <p className="mt-2 text-sm leading-6">{item.title}</p>
        {item.detail ? <p className="mt-1 text-xs leading-5 text-muted">{item.detail}</p> : null}
        {item.affects.length ? <p className="mt-2 flex flex-wrap gap-1.5">{item.affects.map((value) => <span key={value} className="rounded bg-chip px-1.5 py-0.5 text-[10px] text-muted">{documentKind(value, lang)}</span>)}</p> : null}
        {activeId === item.id ? <div className="mt-3 border-t border-border pt-3">
          <TextArea label={openItemNoteLabel(item.kind, lang)} value={note} onChange={setNote} />
          <div className="mt-3 flex flex-wrap gap-2">
            {item.kind === "question" ? <Button size="sm" disabled={Boolean(working) || !note.trim()} onClick={() => resolve(item, "answered", "decision")}>{lang === "zh" ? "保存回答并记录决定" : "Answer and record decision"}</Button> : null}
            {item.kind === "conflict" ? <><Button size="sm" disabled={Boolean(working) || !note.trim()} onClick={() => resolve(item, "resolved")}>{lang === "zh" ? "标记已解决" : "Mark resolved"}</Button><Button size="sm" variant="outline" disabled={Boolean(working) || !note.trim()} onClick={() => resolve(item, "resolved", "decision")}>{lang === "zh" ? "转为决定" : "Record decision"}</Button></> : null}
            {item.kind === "suggestion" ? <><Button size="sm" disabled={Boolean(working) || !note.trim()} onClick={() => resolve(item, "accepted", "requirement")}>{lang === "zh" ? "转为候选需求" : "To candidate requirement"}</Button><Button size="sm" variant="outline" disabled={Boolean(working) || !note.trim()} onClick={() => resolve(item, "accepted", "decision")}>{lang === "zh" ? "转为决定" : "Record decision"}</Button></> : null}
            <Button size="sm" variant="outline" disabled={Boolean(working)} onClick={() => resolve(item, "deferred")}>{lang === "zh" ? "暂缓" : "Defer"}</Button>
            <Button size="sm" variant="outline" disabled={Boolean(working)} onClick={() => resolve(item, "dismissed")}>{item.kind === "conflict" ? (lang === "zh" ? "说明不冲突" : "Not a conflict") : (lang === "zh" ? "忽略" : "Dismiss")}</Button>
            <Button size="sm" variant="outline" disabled={Boolean(working)} onClick={() => { setActiveId(""); setNote(""); }}>{lang === "zh" ? "取消" : "Cancel"}</Button>
          </div>
        </div> : <div className="mt-3 flex flex-wrap gap-2">
          <Button size="sm" variant="outline" onClick={() => { setActiveId(item.id); setNote(""); }}>{lang === "zh" ? "处理" : "Resolve"}</Button>
        </div>}
      </article>)}
      {!openItems.length && items.length ? <p className="text-sm text-muted">{lang === "zh" ? "所有开放项都已处理。" : "All open items have been handled."}</p> : null}
    </div>
    {handled.length ? <div className="mt-4 border-t border-border pt-3">
      <button type="button" className="text-xs text-primary" onClick={() => setShowHandled((value) => !value)}>{lang === "zh" ? `已处理 ${handled.length} 项` : `${handled.length} handled`} {showHandled ? "▾" : "▸"}</button>
      {showHandled ? <div className="mt-2 space-y-2">{handled.map((item) => <div key={item.id} className="rounded-md bg-bg-elevated p-3"><div className="flex flex-wrap items-center gap-2"><Badge tone="ok">{openItemStatus(item.status, lang)}</Badge><span className="text-xs text-muted">{item.title}</span></div>{item.note ? <p className="mt-1 text-xs leading-5 text-muted">{item.note}</p> : null}{item.decision_id || item.requirement_id ? <TechnicalMeta label={lang === "zh" ? "处理结果技术信息" : "Disposition details"} value={[item.decision_id ? `decision ${item.decision_id}` : "", item.requirement_id ? `requirement ${item.requirement_id}` : ""].filter(Boolean).join(" · ")} /> : null}</div>)}</div> : null}
    </div> : null}
  </section>;
}

function openItemKind(kind: ProjectOpenItem["kind"], lang: "zh" | "en") {
  const labels = {
    question: { zh: "开放问题", en: "Open question" },
    conflict: { zh: "明确冲突", en: "Explicit conflict" },
    suggestion: { zh: "参考建议", en: "Suggestion" },
  };
  return labels[kind][lang];
}

function openItemStatus(status: ProjectOpenItem["status"], lang: "zh" | "en") {
  const labels: Record<ProjectOpenItem["status"], { zh: string; en: string }> = {
    open: { zh: "待处理", en: "Open" },
    answered: { zh: "已回答", en: "Answered" },
    resolved: { zh: "已解决", en: "Resolved" },
    accepted: { zh: "已采纳", en: "Accepted" },
    deferred: { zh: "已暂缓", en: "Deferred" },
    dismissed: { zh: "已忽略", en: "Dismissed" },
  };
  return labels[status][lang];
}

function openItemNoteLabel(kind: ProjectOpenItem["kind"], lang: "zh" | "en") {
  if (kind === "question") return lang === "zh" ? "回答（会作为决定内容保存）" : "Answer (saved as the decision statement)";
  if (kind === "suggestion") return lang === "zh" ? "采纳理由或决定内容" : "Adoption reason or decision statement";
  return lang === "zh" ? "处理说明或决定内容" : "Resolution note or decision statement";
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
  const currentItems = (workspace.open_items || []).filter((item) => item.current);
  const openItems = currentItems.filter((item) => item.status === "open");
  const openQuestions = openItems.filter((item) => item.kind === "question");
  const openConflicts = openItems.filter((item) => item.kind === "conflict");
  const openSuggestions = openItems.filter((item) => item.kind === "suggestion");
  const handledConflicts = currentItems.filter(
    (item) => item.kind === "conflict" && item.status !== "open");
  const decisions = pending.length + openQuestions.length;
  const suggestions = recommended.length + openCandidates.length + openSuggestions.length;
  return (
    <section className="mt-6 rounded-xl bg-primary/[0.06] p-5 ring-1 ring-primary/15">
      <h2 className="font-medium">{lang === "zh" ? "一致性信号" : "Consistency signals"}</h2>
      <p className="mt-1 text-[11px] leading-5 text-subtle">{analysisRun
        ? (lang === "zh"
          ? <>统计来源：最近一次完成的固定输入分析（{generationMode(analysisRun.mode, lang)} · {new Date(analysisRun.created_at).toLocaleString("zh-CN")}）。价值分析与当前选中的其它生成运行不计入。 <TechnicalMeta label="运行技术信息" value={analysisRun.id} inline /></>
          : <>Counted from the latest completed fixed-input analysis ({generationMode(analysisRun.mode, lang)} · {new Date(analysisRun.created_at).toLocaleString("en")}). Value analysis and any other selected run are not counted. <TechnicalMeta label="Run details" value={analysisRun.id} inline /></>)
        : (lang === "zh"
          ? "统计来源：尚无已完成的固定输入分析；分析类数字显示为“未检查”。"
          : "Source: no completed fixed-input analysis yet; analysis-based counts show as not checked.")}</p>
      <div className="mt-4 grid gap-3 md:grid-cols-2 xl:grid-cols-4">
        <Signal title={lang === "zh" ? "明确冲突" : "Explicit conflicts"}
          count={analysis ? openConflicts.length : (lang === "zh" ? "未检查" : "Not checked")}
          text={analysis
            ? (openConflicts.length
              ? (lang === "zh" ? `可在「待处理事项」中处理${handledConflicts.length ? `；另有 ${handledConflicts.length} 项已处理` : ""}。` : `Resolve them in Open items${handledConflicts.length ? `; ${handledConflicts.length} already handled` : ""}.`)
              : (handledConflicts.length
                ? (lang === "zh" ? `全部 ${handledConflicts.length} 项冲突已处理，没有未处理冲突。` : `All ${handledConflicts.length} conflicts are handled; none remain open.`)
                : (lang === "zh" ? "最近一次固定输入分析未报告明确冲突；这不代表未来输入也没有冲突。" : "The latest fixed-input analysis reported no explicit conflict; future input may differ.")))
            : (lang === "zh" ? "尚未完成固定输入分析，不能推断为“没有冲突”。" : "No fixed-input analysis has completed, so absence of conflict cannot be inferred.")}
          muted={!analysis} />
        <Signal title={lang === "zh" ? "需要决定" : "Needs a decision"} count={decisions}
          text={decisions
            ? (lang === "zh" ? `${pending.length} 条需求待确认，${openQuestions.length} 个开放问题未处理（来自该运行）。` : `${pending.length} requirements await confirmation and ${openQuestions.length} open questions await answers (from that run).`)
            : (lang === "zh" ? "当前没有待确认需求或开放问题。" : "No requirements or open questions await a decision.")} />
        <Signal title={lang === "zh" ? "参考建议" : "Suggestions"} count={suggestions}
          text={suggestions
            ? (lang === "zh" ? `${recommended.length} 条已保存范围建议，${openCandidates.length} 条未加入候选，${openSuggestions.length} 条分析建议未处理。` : `${recommended.length} saved scope recommendations, ${openCandidates.length} unapplied candidates, and ${openSuggestions.length} unhandled analysis suggestions.`)
            : (lang === "zh" ? "当前没有未处理的参考建议。" : "There are no pending suggestions.")} />
        <Signal title={lang === "zh" ? "关联复核" : "Linked reviews"} count={review.length}
          text={review.length
            ? (lang === "zh" ? `${review.length} 份文档因依据变化待复核。` : `${review.length} documents need review after basis changes.`)
            : (lang === "zh" ? "关联文档的固定依据均为当前版本。" : "All linked documents use current pinned basis versions.")} />
      </div>
    </section>
  );
}

function AcceptanceMigrationPanel({ projectId, onSaved }: {
  projectId: string; onSaved: () => void;
}) {
  const { lang } = useLang();
  const [revision, setRevision] = useState(0);
  const [busy, setBusy] = useState(false);
  const [notice, setNotice] = useState("");
  const [error, setError] = useState("");
  const { data, error: reportError, loading } = useAsync(
    () => getLegacyAcceptanceMigration(projectId), [projectId, revision]);
  const summary = data?.summary;
  const refresh = () => {
    invalidateAtlasCache();
    setRevision((value) => value + 1);
    setError("");
  };
  const backfill = async () => {
    if (busy || !summary?.not_backfilled) return;
    const message = lang === "zh"
      ? "为旧验收记录补充“未回填”元数据？\n\n这不会推断任何通过/失败结果，也不会改变历史验收状态。"
      : "Add “not backfilled” metadata to legacy acceptance records?\n\nThis does not infer pass/fail results or change historical acceptance status.";
    if (!window.confirm(message)) return;
    setBusy(true);
    setError("");
    setNotice("");
    try {
      const result = await backfillLegacyAcceptance(projectId);
      setNotice(lang === "zh"
        ? `已标记 ${result.backfilled_task_ids?.length || 0} 条旧记录；历史人工结论仍保持未知。`
        : `Marked ${result.backfilled_task_ids?.length || 0} legacy records; historical human conclusions remain unknown.`);
      onSaved();
      refresh();
    } catch (cause) {
      setError(cause instanceof Error ? cause.message
        : (lang === "zh" ? "旧验收记录迁移失败。" : "Legacy acceptance migration failed."));
    } finally {
      setBusy(false);
    }
  };
  return <section className="mt-6 rounded-xl border border-border bg-surface p-5 shadow-card">
    <div className="flex flex-wrap items-start justify-between gap-3">
      <div>
        <h2 className="font-serif text-xl font-medium">{lang === "zh" ? "旧验收记录" : "Legacy acceptance records"}</h2>
        <p className="mt-1 text-xs leading-5 text-subtle">
          {lang === "zh"
            ? "只读扫描历史 acceptance binding；缺少逐条件人工结果时只标记为未回填，不会从总体状态推断结论。"
            : "Read-only scan of historical acceptance bindings; missing per-condition human results are marked not backfilled and never inferred from overall status."}
        </p>
      </div>
      <Button size="sm" variant="ghost" disabled={busy} onClick={refresh}>
        {lang === "zh" ? "重新扫描" : "Rescan"}
      </Button>
    </div>
    {loading ? <Loading /> : null}
    {reportError || error ? <p className="mt-3 text-sm text-danger" role="alert">{error || String(reportError)}</p> : null}
    {notice ? <p className="mt-3 rounded-md bg-primary/10 p-3 text-sm text-primary" role="status">{notice}</p> : null}
    {summary ? <>
      <div className="mt-4 grid grid-cols-2 gap-2 text-xs sm:grid-cols-4">
        <MiniStat value={summary.total_bindings} label={lang === "zh" ? "绑定总数" : "Bindings"} warn={false} />
        <MiniStat value={summary.not_backfilled} label={lang === "zh" ? "待标记" : "Not backfilled"} warn={summary.not_backfilled > 0} />
        <MiniStat value={summary.backfilled} label={lang === "zh" ? "已标记" : "Backfilled"} warn={false} />
        <MiniStat value={summary.needs_review} label={lang === "zh" ? "需人工复核" : "Needs review"} warn={summary.needs_review > 0} />
      </div>
      {data?.records.some((item) => item.status === "not_backfilled" || item.status === "needs_review") ? (
        <details className="mt-4 rounded-lg bg-bg-elevated p-3 text-xs">
          <summary className="cursor-pointer text-primary">{lang === "zh" ? "查看待处理记录" : "View records needing attention"}</summary>
          <div className="mt-2 space-y-2">
            {data.records.filter((item) => item.status === "not_backfilled" || item.status === "needs_review").map((item) => (
              <div key={item.task_id} className="flex flex-wrap items-center justify-between gap-2 border-t border-border pt-2">
                <span className="font-mono">{item.task_id}</span>
                <span className="text-muted">{item.status} · {item.missing_conditions.length} {lang === "zh" ? "条缺失条件" : "missing conditions"}</span>
              </div>
            ))}
          </div>
        </details>
      ) : null}
      <div className="mt-4 flex flex-wrap items-center gap-2">
        <Button size="sm" disabled={busy || !summary.not_backfilled} onClick={backfill}>
          {lang === "zh" ? "标记旧记录为未回填" : "Mark legacy records not backfilled"}
        </Button>
        <span className="text-[11px] text-subtle">{lang === "zh" ? "只补充迁移元数据，不改历史结论。" : "Adds migration metadata only; historical conclusions stay unchanged."}</span>
      </div>
    </> : null}
  </section>;
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
    } catch (cause) { setError(actionError(cause, lang)); } finally { setSaving(false); }
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
    try { await confirmProjectRequirement(projectId, requirement.id, { scope, reason, expected_revision: requirement.revision ?? 1 }); onSaved(); }
    catch (cause) { setError(actionError(cause, lang)); } finally { setSaving(false); }
  };
  const edit = async () => {
    setSaving(true); setError("");
    try {
      await updateProjectRequirement(projectId, requirement.id, {
        content, acceptance_conditions: lines(acceptance), reference_ids: referenceIds,
      });
      onSaved();
    } catch (cause) { setError(actionError(cause, lang)); } finally { setSaving(false); }
  };
  return (
    <article className="rounded-xl bg-surface p-5 shadow-card">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div className="min-w-0 flex-1">
          <div className="flex flex-wrap items-center gap-2">
            <span className="font-mono text-[11px] text-subtle">{requirement.id}</span>
            <Badge tone="default">r{requirement.revision ?? 1}</Badge>
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
  } catch (cause) { setError(actionError(cause, lang)); } finally { setSaving(false); } };
  return <SideForm title={lang === "zh" ? "记录决定" : "Record decision"} icon={Plus}><form className="space-y-4" onSubmit={submit}>
    <TextArea label={lang === "zh" ? "决定" : "Decision"} value={statement} onChange={setStatement} required />
    <TextArea label={lang === "zh" ? "理由" : "Rationale"} value={rationale} onChange={setRationale} required />
    <ReferencePicker references={references} selected={ids} onChange={setIds} />
    {error ? <p className="text-xs text-danger">{error}</p> : null}<Button className="w-full" disabled={saving}>{lang === "zh" ? "保存决定" : "Save decision"}</Button>
  </form></SideForm>;
}

function ExportButton({ projectId, lang }: { projectId: string; lang: "zh" | "en" }) {
  const [result, setResult] = useState<ProjectExport | null>(null); const [error, setError] = useState(""); const [saving, setSaving] = useState(false);
  const run = async () => { setSaving(true); setError(""); try { setResult(await exportProject(projectId)); } catch { setError(lang === "zh" ? "项目资料导出失败，请稍后重试。" : "Project export failed. Please try again."); } finally { setSaving(false); } };
  return <div className="max-w-md text-right"><Button onClick={run} disabled={saving}><Download className="size-4" />{saving ? (lang === "zh" ? "导出中…" : "Exporting…") : (lang === "zh" ? "导出 Markdown 包" : "Export Markdown bundle")}</Button><p className="mt-2 text-left text-[11px] leading-5 text-subtle">{lang === "zh" ? "只读导出当前项目的资料、需求、决定、文档和验收记录，不会修改本地工作区或源代码。" : "Exports the current project sources, requirements, decisions, documents, and acceptance records without changing the local workspace or source code."}</p>{result ? <details className="mt-2 text-left text-[11px] text-subtle"><summary className="cursor-pointer">{lang === "zh" ? "导出已完成" : "Export completed"}</summary><div className="mt-1 break-all font-mono"><div>{result.archive}</div><div>sha256 {result.archive_sha256.slice(0, 16)}…</div></div></details> : null}{error ? <p className="mt-2 text-xs text-danger">{error}</p> : null}</div>;
}

function ReferencePicker({ references, selected, onChange }: { references: ProjectReference[]; selected: string[]; onChange: (value: string[]) => void }) {
  const { lang } = useLang(); return <Picker label={lang === "zh" ? "关联固定资料" : "Linked pinned sources"} options={references.map((item) => ({ key: item.id, label: `${item.source_ref}${item.locator ? `#${item.locator}` : ""}` }))} selected={selected} onChange={onChange} />;
}

function Picker({ label, options, selected, onChange }: { label: string; options: { key: string; label: string }[]; selected: string[]; onChange: (value: string[]) => void }) {
  return <fieldset><legend className="text-sm text-muted">{label}</legend><div className="mt-2 max-h-40 space-y-2 overflow-y-auto">{options.map((item) => <label key={item.key} className="flex items-start gap-2 text-xs leading-5 text-muted"><input type="checkbox" className="mt-1" checked={selected.includes(item.key)} onChange={(event) => onChange(event.target.checked ? [...selected, item.key] : selected.filter((value) => value !== item.key))} /><span>{item.label}</span></label>)}{!options.length ? <p className="text-xs text-subtle">—</p> : null}</div></fieldset>;
}

function IdLinks({ ids, prefix }: { ids: string[]; prefix: string }) {
  return ids.length
    ? <details className="mt-3 text-[11px] text-subtle"><summary className="cursor-pointer">{prefix} · {ids.length}</summary><code className="mt-1 block break-all rounded bg-chip px-1.5 py-0.5 font-mono">{ids.join(" · ")}</code></details>
    : null;
}
function Empty({ text }: { text: string }) { return <div className="rounded-xl bg-surface p-6 text-sm text-muted shadow-card">{text}</div>; }
function Signal({ title, count, text, muted }: { title: string; count: number | string; text: string; muted?: boolean }) { return <div className="rounded-lg bg-surface p-4 shadow-card"><div className="flex items-center justify-between gap-2"><h3 className="text-sm font-medium">{title}</h3><span className={`text-xs ${muted ? "text-subtle" : "text-primary"}`}>{count}</span></div><p className="mt-2 text-xs leading-5 text-muted">{text}</p></div>; }
function SectionTitle({ icon: Icon, title, description }: { icon: typeof FileText; title: string; description: string }) { return <div className="flex items-start gap-3"><Icon className="mt-0.5 size-5 text-primary" /><div><h2 className="font-serif text-xl font-medium">{title}</h2><p className="mt-1 text-xs leading-5 text-subtle">{description}</p></div></div>; }
function SideForm({ title, icon: Icon, children }: { title: string; icon: typeof Plus; children: ReactNode }) { return <aside className="h-fit rounded-xl bg-surface p-5 shadow-card"><h3 className="mb-5 flex items-center gap-2 font-medium"><Icon className="size-4" />{title}</h3>{children}</aside>; }
function Field({ label, value, onChange, required }: { label: string; value: string; onChange: (value: string) => void; required?: boolean }) { return <label className="block text-sm"><span className="text-muted">{label}</span><input required={required} value={value} onChange={(event) => onChange(event.target.value)} className={inputClass} /></label>; }
