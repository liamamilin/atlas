import { useEffect, useState, type FormEvent, type ReactNode } from "react";
import {
  AlertTriangle, ArrowLeft, Bot, CheckCircle2, Download, FileClock,
  FileText, Lightbulb, Plus, Scale, Save, Sparkles,
} from "lucide-react";
import { Link, useParams } from "react-router-dom";
import { ErrorBox, Loading, useAsync } from "@/components/loaders";
import { Prose } from "@/components/prose";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  addProjectDocumentVersion,
  applyProjectGenerationItem,
  confirmProjectRequirement,
  createProjectDecision,
  createProjectDocument,
  createProjectRequirement,
  exportProject,
  getProjectDocumentDiff,
  getProjectDocumentVersions,
  getProjectGeneration,
  getProjectWorkspace,
  invalidateAtlasCache,
  listProjectGenerations,
  startProjectGeneration,
  updateProjectRequirement,
  type DocumentBasis,
  type ProjectDocument,
  type ProjectDocumentKind,
  type ProjectExport,
  type ProjectGenerationRun,
  type ProjectReference,
  type ProjectRequirement,
  type ProjectScope,
  type ProjectWorkspace,
} from "@/lib/atlas";
import { useLang } from "@/lib/lang";
import { setCurrentProjectId } from "@/lib/project-selection";

const DOCUMENT_KINDS: { value: ProjectDocumentKind; zh: string; en: string }[] = [
  { value: "analysis", zh: "调研与分析", en: "Research & analysis" },
  { value: "product-requirements", zh: "产品需求", en: "Product requirements" },
  { value: "interaction", zh: "交互与页面", en: "Interaction & screens" },
  { value: "technical-plan", zh: "技术方案", en: "Technical plan" },
  { value: "development-plan", zh: "开发规划", en: "Development plan" },
  { value: "acceptance-plan", zh: "验收方案", en: "Acceptance plan" },
  { value: "current-state", zh: "项目现状与变更", en: "Current state & changes" },
];

export function ProjectDetail() {
  const { projectId = "" } = useParams<{ projectId: string }>();
  const { lang } = useLang();
  const [revision, setRevision] = useState(0);
  const [analysisRun, setAnalysisRun] = useState<ProjectGenerationRun | null>(null);
  const { data, error, loading } = useAsync(
    () => getProjectWorkspace(projectId), [projectId, revision]);

  useEffect(() => {
    if (data?.project.id) setCurrentProjectId(data.project.id);
  }, [data?.project.id]);

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
          <p className="text-sm font-medium tracking-wide text-primary">U17 · M2</p>
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
    </main>
  );
}

function GenerationPanel({ projectId, workspace, onSaved, onAnalysis }: {
  projectId: string; workspace: ProjectWorkspace; onSaved: () => void;
  onAnalysis: (run: ProjectGenerationRun | null) => void;
}) {
  const { lang } = useLang();
  const [run, setRun] = useState<ProjectGenerationRun | null>(null);
  const [kind, setKind] = useState<ProjectDocumentKind>("product-requirements");
  const [error, setError] = useState("");
  const [starting, setStarting] = useState(false);
  const [applying, setApplying] = useState("");
  const hasConfirmedScope = workspace.requirements.some((item) => item.confirmed_scope === "current");
  const active = run?.status === "queued" || run?.status === "running";

  useEffect(() => {
    let alive = true;
    listProjectGenerations(projectId).then(
      (items) => {
        if (!alive) return;
        if (items[0]) setRun(items[0]);
        onAnalysis(items.find((item) => item.mode === "analysis" && item.status === "completed") || null);
      },
      (cause) => { if (alive) setError(String(cause)); },
    );
    return () => { alive = false; };
  }, [projectId]);

  useEffect(() => {
    if (!active || !run) return;
    let alive = true;
    const timer = window.setInterval(() => {
      getProjectGeneration(projectId, run.id).then(
        (next) => {
          if (!alive) return;
          setRun(next);
          if (next.mode === "analysis" && next.status === "completed") onAnalysis(next);
        },
        (cause) => { if (alive) setError(String(cause)); },
      );
    }, 1500);
    return () => { alive = false; window.clearInterval(timer); };
  }, [active, projectId, run?.id]);

  const start = async (mode: "analysis" | "documents") => {
    setStarting(true); setError("");
    try {
      setRun(await startProjectGeneration(projectId, {
        mode, ...(mode === "documents" ? { document_kinds: [kind] } : {}),
      }));
    } catch (cause) { setError(String(cause)); } finally { setStarting(false); }
  };
  const apply = async (itemKind: "requirement" | "document", index: number) => {
    if (!run) return;
    const key = `${itemKind}:${index}`; setApplying(key); setError("");
    try {
      const result = await applyProjectGenerationItem(
        projectId, run.id, { item_kind: itemKind, index });
      setRun(result.run); onSaved();
    } catch (cause) { setError(String(cause)); } finally { setApplying(""); }
  };
  const result = run?.result;
  return <section className="mt-8 rounded-xl bg-surface p-5 shadow-card">
    <div className="flex flex-wrap items-start justify-between gap-4">
      <div className="flex max-w-2xl items-start gap-3"><Bot className="mt-0.5 size-5 text-primary" /><div>
        <h2 className="font-serif text-xl font-medium">{lang === "zh" ? "资料分析与文档草案" : "Source analysis & document drafts"}</h2>
        <p className="mt-1 text-xs leading-5 text-subtle">{lang === "zh" ? "OpenCode 只读取本项目已固定的依据。输出先作为 AI 建议供审阅，需求不会自动获得用户确认，文档也不会自动覆盖现有版本。" : "OpenCode reads only this project's pinned input. Results remain reviewable AI proposals; requirements are never user-confirmed automatically and documents never overwrite a newer version."}</p>
      </div></div>
      <div className="flex flex-wrap items-end gap-2">
        <Button size="sm" variant="outline" disabled={starting || active} onClick={() => start("analysis")}><Sparkles className="size-4" />{lang === "zh" ? "分析固定资料" : "Analyze pinned sources"}</Button>
        <label className="text-xs text-muted"><span className="block">{lang === "zh" ? "文档类型" : "Document kind"}</span><select value={kind} onChange={(event) => setKind(event.target.value as ProjectDocumentKind)} className={`${inputClass} mt-1 h-9 min-w-40`}>
          {DOCUMENT_KINDS.map((item) => <option key={item.value} value={item.value}>{lang === "zh" ? item.zh : item.en}</option>)}
        </select></label>
        <Button size="sm" disabled={starting || active || !hasConfirmedScope} onClick={() => start("documents")}><FileText className="size-4" />{lang === "zh" ? "生成文档草案" : "Generate document draft"}</Button>
      </div>
    </div>
    {!hasConfirmedScope ? <p className="mt-3 text-xs text-warn">{lang === "zh" ? "生成产品与开发文档前，至少确认一条本版需求。资料分析可以先运行。" : "Confirm at least one current requirement before generating product or development documents. Source analysis can run first."}</p> : null}
    {run ? <div className="mt-4 flex flex-wrap items-center gap-2 border-t border-border pt-4 text-xs text-subtle">
      <Badge tone={run.status === "completed" ? "ok" : run.status === "failed" ? "warn" : "default"}>{run.status}</Badge>
      <span className="font-mono">{run.id}</span><span>{run.engine}{run.model ? ` · ${run.model}` : ""}</span>
      <span className="font-mono">input {run.input_fingerprint.slice(0, 12)}</span>
      {run.engine_session_id ? <span className="font-mono">{run.engine_session_id}</span> : null}
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
          return <article key={`${item.kind}:${index}`} className="rounded-lg bg-bg-elevated p-4"><div className="flex items-start justify-between gap-3"><div><p className="text-[11px] text-primary">{lang === "zh" ? "AI 文档草案" : "AI document draft"} · {documentKind(item.kind, lang)}</p><h3 className="mt-1 text-sm font-medium">{item.title}</h3></div><Button size="sm" variant="outline" disabled={Boolean(applied) || applying === `document:${index}`} onClick={() => apply("document", index)}>{applied ? (lang === "zh" ? "已保存" : "Saved") : item.document_id ? (lang === "zh" ? "保存为新版本" : "Save new version") : (lang === "zh" ? "创建关联文档" : "Create document")}</Button></div><div className="mt-3 max-h-80 overflow-auto rounded-md bg-surface p-3"><Prose md={item.content} /></div></article>;
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
            ? (lang === "zh" ? `${review.length} 份文档因上游变化待复核。` : `${review.length} documents need review after upstream changes.`)
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
  const versions = useAsync(() => getProjectDocumentVersions(projectId, document.id), [projectId, document.id, document.current_version]);
  const save = async () => { setSaving(true); setError(""); try {
    await addProjectDocumentVersion(projectId, document.id, { content, basis: document.basis, expected_current_version: document.current_version, author: "human", change_summary: summary }); onSaved();
  } catch (cause) { setError(String(cause)); } finally { setSaving(false); } };
  const compare = async () => { setError(""); try { setDiff((await getProjectDocumentDiff(projectId, document.id)).diff || (lang === "zh" ? "两个版本正文相同。" : "The two versions have identical content.")); } catch (cause) { setError(String(cause)); } };
  return <article className={`rounded-xl bg-surface p-5 shadow-card ${document.review.status === "needs_review" ? "ring-2 ring-warn/25" : ""}`}>
    <div className="flex flex-wrap items-start justify-between gap-3"><div><div className="flex flex-wrap items-center gap-2"><h3 className="font-medium">{document.title}</h3><Badge tone={document.review.status === "current" ? "ok" : "warn"}>{document.review.status === "current" ? (lang === "zh" ? "依据为当前" : "Current") : (lang === "zh" ? "需要复核" : "Needs review")}</Badge></div>
      <p className="mt-1 text-xs text-subtle">{documentKind(document.kind, lang)} · v{document.current_version} · {document.author} · {document.version_id}</p></div></div>
    {document.review.status === "needs_review" ? <p className="mt-3 flex gap-2 rounded-md bg-warn/10 p-3 text-xs leading-5 text-warn"><AlertTriangle className="mt-0.5 size-4 shrink-0" />{lang === "zh" ? "关联需求或上游文档已有变化。正文未被自动改写，请比较后保存新版本。" : "A linked requirement or upstream document changed. The content was preserved; review it before saving a new version."}</p> : null}
    <details className="mt-4"><summary className="cursor-pointer text-sm text-primary">{lang === "zh" ? "查看正文、编辑和版本" : "View, edit, and versions"}</summary>
      <div className="mt-4 rounded-md border border-border bg-bg-elevated p-4"><Prose md={document.content} /></div>
      <div className="mt-5 grid gap-4 lg:grid-cols-2"><div><TextArea label={lang === "zh" ? "编辑完整 Markdown（从当前版开始）" : "Edit full Markdown (starts from current)"} value={content} onChange={setContent} required rows={12} /><Field label={lang === "zh" ? "修改说明" : "Change summary"} value={summary} onChange={setSummary} required /><Button className="mt-3" size="sm" onClick={save} disabled={saving || !summary.trim()}><Save className="size-4" />{lang === "zh" ? "保存新版本" : "Save new version"}</Button></div>
        <div><h4 className="text-sm font-medium">{lang === "zh" ? "版本历史" : "Version history"}</h4>{versions.loading ? <p className="mt-2 text-xs text-subtle">…</p> : versions.data?.map((version) => <div key={version.version_id} className="mt-2 rounded-md bg-chip p-3 text-xs"><div>v{version.version} · {version.author} · {version.change_summary || (lang === "zh" ? "无说明" : "No summary")}</div><div className="mt-1 font-mono text-[10px] text-subtle">{version.content_sha256.slice(0, 12)}</div></div>)}
          <Button className="mt-3" size="sm" variant="outline" disabled={document.current_version < 2} onClick={compare}><FileClock className="size-4" />{lang === "zh" ? "比较最近两版" : "Compare latest two"}</Button></div></div>
      {diff ? <pre className="mt-4 max-h-96 overflow-auto whitespace-pre-wrap rounded-md bg-fg p-4 font-mono text-xs text-bg">{diff}</pre> : null}{error ? <p className="mt-3 text-xs text-danger">{error}</p> : null}
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
