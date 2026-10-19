import { useEffect, useState } from "react";
import { Bot, FileText, FolderGit2, Sparkles } from "lucide-react";
import { Prose } from "@/components/prose";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  applyProjectGenerationItem,
  listProjectGenerations,
  startProjectGeneration,
  type ProjectDocumentKind,
  type ProjectGenerationRun,
  type ProjectWorkspace,
} from "@/lib/atlas";
import { useLang } from "@/lib/lang";
import {
  actionError,
  CORE_DOCUMENT_BUNDLE,
  DOCUMENT_BUNDLE_KINDS,
  documentKind,
  FULL_DOCUMENT_BUNDLE,
  generationMode,
  inputClass,
  runStatus,
  sameKinds,
  scopeLabel,
  TechnicalError,
  TechnicalMeta,
  TextArea,
} from "@/components/project-detail-shared";

export function GenerationPanel({ projectId, workspace, onSaved, onAnalysis }: {
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
  const [staleConfirmed, setStaleConfirmed] = useState(false);
  const run = runs.find((item) => item.id === selectedRunId) || null;
  const staleBlocked = Boolean(run && (run.stale || run.stale_known === false)) && !staleConfirmed;
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
      (cause) => { if (alive) setError(actionError(cause, lang)); },
    );
    return () => { alive = false; };
  }, [projectId]);

  useEffect(() => { setStaleConfirmed(false); }, [selectedRunId]);

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
        (cause) => { if (alive) setError(actionError(cause, lang)); },
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
    } catch (cause) { setError(actionError(cause, lang)); } finally { setStarting(false); }
  };
  const apply = async (itemKind: "requirement" | "document", index: number) => {
    if (!run) return;
    const key = `${itemKind}:${index}`; setApplying(key); setError("");
    try {
      const result = await applyProjectGenerationItem(
        projectId, run.id, { item_kind: itemKind, index, confirm_stale: staleConfirmed });
      setRuns((items) => items.map((item) => item.id === result.run.id ? result.run : item));
      if (result.run.mode === "analysis" || result.run.mode === "improvement") {
        onAnalysis(result.run);
      }
      onSaved();
    } catch (cause) { setError(actionError(cause, lang)); } finally { setApplying(""); }
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
    {runs.length ? <div className="mt-4 flex flex-wrap items-end justify-between gap-3 border-t border-border pt-4"><label className="text-xs text-muted"><span className="block">{lang === "zh" ? "生成历史" : "Generation history"}</span><select value={selectedRunId} onChange={(event) => setSelectedRunId(event.target.value)} className={`${inputClass} mt-1 h-9 min-w-72`}>{runs.map((item) => <option key={item.id} value={item.id}>{new Date(item.created_at).toLocaleString(lang === "zh" ? "zh-CN" : "en")} · {generationMode(item.mode, lang)} · {runStatus(item.status, lang)}</option>)}</select></label><div className="flex gap-2"><Button size="sm" variant={compact ? "default" : "outline"} onClick={() => setCompact(true)}>{lang === "zh" ? "简要" : "Compact"}</Button><Button size="sm" variant={!compact ? "default" : "outline"} onClick={() => setCompact(false)}>{lang === "zh" ? "完整" : "Full"}</Button></div></div> : null}
    {run ? <div className="mt-3 flex flex-wrap items-center gap-2 text-xs text-subtle">
      <Badge tone={run.status === "completed" ? "ok" : run.status === "failed" ? "warn" : "default"}>{runStatus(run.status, lang)}</Badge>
      <span>{generationMode(run.mode, lang)} · {run.engine === "opencode" ? "OpenCode" : run.engine}</span>
      <TechnicalMeta label={lang === "zh" ? "技术信息" : "Technical details"} value={[`run ${run.id}`, `${lang === "zh" ? "输入指纹" : "input fingerprint"} ${run.input_fingerprint}`, run.model ? `model ${run.model}` : "", run.engine_session_id ? `session ${run.engine_session_id}` : ""].filter(Boolean).join(" · ")} />
      {run.mode === "value" ? <span className="rounded bg-primary/10 px-2 py-1 text-primary">{lang === "zh" ? "仅供参考，不改变范围" : "Advisory only; scope unchanged"}</span> : null}
    </div> : null}
    {run && (run.stale || run.stale_known === false) ? <div className="mt-3 rounded-md bg-warn/10 p-4"><p className="text-sm font-medium text-warn">{run.stale_known === false ? (lang === "zh" ? "无法验证该结果的固定输入" : "The result input cannot be verified") : (lang === "zh" ? "该结果的固定输入已过期" : "This result is stale against the current inputs")}</p><p className="mt-1 text-xs leading-5 text-muted">{run.stale_known === false ? (lang === "zh" ? "该运行没有可验证的依据指纹，不能自动应用；请重新生成或显式确认后再处理。" : "This run has no verifiable basis fingerprint and cannot be applied automatically; regenerate or explicitly review it first.") : (lang === "zh" ? "生成之后至少有资料、需求或决定发生了变化。应用前请复核差异；确认后仍可按原结果应用。" : "Sources, requirements, or decisions changed after this run. Review the difference before applying; you may still apply the original result explicitly.")}</p>{!staleConfirmed ? <Button className="mt-2" size="sm" variant="outline" onClick={() => setStaleConfirmed(true)}>{lang === "zh" ? "确认仍要应用过期结果" : "Confirm applying the stale result"}</Button> : <p className="mt-2 text-xs text-warn">{lang === "zh" ? "已确认，可以应用。" : "Confirmed; applying is enabled."}</p>}</div> : null}
    {active ? <p className="mt-4 text-sm text-muted">{lang === "zh" ? (run?.status === "queued" ? "等待文档执行器…" : "正在分析固定输入…") : (run?.status === "queued" ? "Waiting for the document runner…" : "Analyzing fixed input…")}</p> : null}
    {run?.status === "failed" ? <div className="mt-4 rounded-md bg-danger/10 p-3"><p className="text-xs text-danger">{lang === "zh" ? "本次生成失败，请检查固定资料和当前项目状态后重试。" : "This generation failed. Review the pinned sources and project state, then try again."}</p><TechnicalError message={run.error} lang={lang} /></div> : null}
    {error ? <p className="mt-4 text-xs text-danger">{error}</p> : null}
    {result ? <div className="mt-5 grid gap-5 border-t border-border pt-5 lg:grid-cols-2">
      <div className="space-y-4">
        <ProposalList title={lang === "zh" ? "分析提出的开放问题" : "Open questions from the analysis"}
          note={lang === "zh" ? "这里保留当轮生成原文；请在下方「待处理事项」中回答、暂缓或忽略。只有每个模式最新完成运行的项目才会进入待处理事项。" : "This keeps the original run output. Answer, defer, or dismiss items in the Open items panel below; only the latest completed run per mode feeds that panel."}
          items={result.questions.map((item) => ({ title: item.question, text: item.why, meta: item.affects.map((value) => documentKind(value, lang)) }))} empty={lang === "zh" ? "没有生成新的关键问题。" : "No new critical questions."} />
        <ProposalList title={lang === "zh" ? "明确冲突" : "Explicit conflicts"} items={result.conflicts.map((item) => ({ title: item.summary, text: item.impact || "", meta: item.evidence.map((value) => value.id) }))} empty={lang === "zh" ? "生成结果没有报告有依据的明确冲突。" : "The result reports no evidence-backed explicit conflicts."} collapseMeta />
        <ProposalList title={lang === "zh" ? "参考建议" : "Suggestions"} items={result.suggestions.map((item) => ({ title: item.summary, text: item.reason || "", meta: item.evidence.map((value) => value.id) }))} empty={lang === "zh" ? "没有额外参考建议。" : "No additional suggestions."} collapseMeta />
      </div>
      <div className="space-y-4">
        {result.requirements.map((item, index) => {
          const applied = run.applied.requirements[String(index)];
          return <article key={item.key} className="rounded-lg bg-bg-elevated p-4"><div className="flex items-start justify-between gap-3"><div><p className="text-[11px] text-primary">{lang === "zh" ? "AI 候选需求" : "AI candidate requirement"} · {scopeLabel(item.recommended_scope, lang)}</p><h3 className="mt-1 text-sm font-medium leading-6">{item.content}</h3></div><Button size="sm" variant="outline" disabled={Boolean(applied) || staleBlocked || applying === `requirement:${index}`} onClick={() => apply("requirement", index)}>{applied ? (lang === "zh" ? "已加入" : "Added") : (lang === "zh" ? "加入候选" : "Add candidate")}</Button></div><p className="mt-2 text-xs leading-5 text-muted">{item.recommendation_reason}</p></article>;
        })}
        {result.documents.map((item, index) => {
          const applied = run.applied.documents[String(index)];
          const dependencies = item.depends_on || [];
          const unmet = dependencies.filter((dependency) => {
            const dependencyIndex = result.documents.findIndex((candidate) => candidate.kind === dependency);
            return dependencyIndex < 0 || !run.applied.documents[String(dependencyIndex)];
          });
          const content = <div className="mt-3 max-h-80 overflow-auto rounded-md bg-surface p-3"><Prose md={item.content} /></div>;
          return <article key={`${item.kind}:${index}`} className="rounded-lg bg-bg-elevated p-4"><div className="flex items-start justify-between gap-3"><div><p className="text-[11px] text-primary">{lang === "zh" ? `第 ${index + 1}/${result.documents.length} 份` : `${index + 1} of ${result.documents.length}`} · {documentKind(item.kind, lang)}</p><h3 className="mt-1 text-sm font-medium">{item.title}</h3>{dependencies.length ? <p className="mt-1 text-[11px] text-subtle">{lang === "zh" ? "依赖" : "Depends on"}: {dependencies.map((value) => documentKind(value, lang)).join(" · ")}</p> : null}{unmet.length ? <p className="mt-1 text-[11px] text-warn">{lang === "zh" ? "请先保存" : "Save first"}: {unmet.map((value) => documentKind(value, lang)).join(" · ")}</p> : null}</div><Button size="sm" variant="outline" disabled={Boolean(applied) || Boolean(unmet.length) || staleBlocked || applying === `document:${index}`} onClick={() => apply("document", index)}>{applied ? (lang === "zh" ? "已保存" : "Saved") : item.document_id ? (lang === "zh" ? "保存为新版本" : "Save new version") : (lang === "zh" ? "创建关联文档" : "Create document")}</Button></div>{compact ? <details className="mt-3"><summary className="cursor-pointer text-xs text-primary">{lang === "zh" ? "查看完整草案" : "View full draft"}</summary>{content}</details> : content}</article>;
        })}
      </div>
    </div> : null}
  </section>;
}

function ProposalList({ title, items, empty, note, collapseMeta }: { title: string; items: { title: string; text: string; meta?: string[] }[]; empty: string; note?: string; collapseMeta?: boolean }) {
  return <div><h3 className="text-sm font-medium">{title}</h3>{note ? <p className="mt-1 text-[11px] leading-5 text-subtle">{note}</p> : null}<div className="mt-2 space-y-2">{items.map((item, index) => <div key={`${item.title}:${index}`} className="rounded-md bg-bg-elevated p-3"><p className="text-sm">{item.title}</p>{item.text ? <p className="mt-1 text-xs leading-5 text-muted">{item.text}</p> : null}{item.meta?.length ? (collapseMeta ? <details className="mt-2 text-[10px] text-subtle"><summary className="cursor-pointer">依据 · {item.meta.length}</summary><code className="mt-1 block break-all rounded bg-chip px-1.5 py-0.5 font-mono">{item.meta.join(" · ")}</code></details> : <p className="mt-2 flex flex-wrap gap-1.5">{item.meta.map((value) => <span key={value} className="rounded bg-chip px-1.5 py-0.5 font-mono text-[10px] text-muted">{value}</span>)}</p>) : null}</div>)}{!items.length ? <p className="text-xs text-subtle">{empty}</p> : null}</div></div>;
}
