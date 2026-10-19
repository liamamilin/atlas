import { useEffect, useMemo, useState } from "react";
import { Link, useSearchParams } from "react-router-dom";
import { Activity, ClipboardCheck, ExternalLink, Pause, Play, RefreshCw, XCircle } from "lucide-react";
import { Button } from "@/components/ui/button";
import { EmptyState, Loading } from "@/components/loaders";
import { useLang } from "@/lib/lang";
import { factoryRequest } from "@/lib/factory";
import { displayUnknown, factoryV1Request, isTerminalPlan, planDigest, planId, unwrapPlan, type V1Application, type V1Plan, type V1Scenario } from "@/lib/factory-v1";

const field = "mt-1.5 w-full rounded-md border border-border bg-bg-elevated px-3 py-2 text-sm";
const terminal = (state?: string) => ["completed", "failed", "cancelled", "blocked", "needs_attention"].includes(state || "");
const planItems = (plan: V1Plan) => Array.isArray(plan.seeds) ? plan.seeds : Array.isArray(plan.items) ? plan.items : Array.isArray(plan.scenarios) ? plan.scenarios : [];
const planExcluded = (plan: V1Plan) => Array.isArray(plan.excluded) ? plan.excluded : Array.isArray(plan.exclusions) ? plan.exclusions : [];
const preferredModel = (models: string[]) => {
  const preferred = ["opencode-go/deepseek-v4.1-flash", "opencode-go/longcat-2.5-preview-free"];
  return preferred.find(item => models.includes(item)) || models.find(item => item.startsWith("opencode-go/")) || models.find(item => item.toLowerCase().includes("deepseek")) || models[0] || "";
};
const savedPlanKey = "atlas.factory.v1.lastPlanId";
function readSavedPlan(planIdFromUrl?: string | null): V1Plan | null {
  try {
    const id = planIdFromUrl || localStorage.getItem(savedPlanKey);
    if (!id) return null;
    const value = localStorage.getItem(`atlas.factory.v1.plan:${id}`);
    if (!value) return null;
    const saved = JSON.parse(value) as V1Plan;
    return planId(saved) && planId(saved) !== id ? null : saved;
  } catch { return null; }
}
function initialPlan(planIdFromUrl: string | null): V1Plan | null {
  if (!planIdFromUrl) return readSavedPlan();
  return readSavedPlan(planIdFromUrl) || { plan_id: planIdFromUrl, state: "loading" };
}
function mergeBatchResult(base: V1Plan, value: unknown): V1Plan {
  const outer = value && typeof value === "object" ? value as Record<string, unknown> : {};
  const payload = outer.plan && typeof outer.plan === "object" ? outer.plan as Record<string, unknown> : outer;
  const nestedBatch = (payload.batch || outer.batch) as Record<string, unknown> | undefined;
  const batchOnly = !nestedBatch && !payload.plan_id && !payload.plan_digest && !payload.digest && typeof payload.state === "string";
  const batch = nestedBatch || (batchOnly ? payload : undefined);
  const planFields = batchOnly ? {} : payload;
  return {
    ...base,
    ...planFields,
    id: base.id || (typeof planFields.id === "string" ? planFields.id : undefined),
    plan_id: base.plan_id || (typeof planFields.plan_id === "string" ? planFields.plan_id : undefined),
    plan_digest: base.plan_digest || (typeof planFields.plan_digest === "string" ? planFields.plan_digest : undefined),
    digest: base.digest || (typeof planFields.digest === "string" ? planFields.digest : undefined),
    batch: batch ? { ...batch, state: typeof batch.state === "string" ? batch.state : base.state } : base.batch,
    state: typeof batch?.state === "string" ? batch.state : (typeof planFields.state === "string" ? planFields.state : base.state),
  };
}

export function FactoryV1() {
  const { lang } = useLang();
  const zh = lang === "zh";
  const [params, setSearchParams] = useSearchParams();
  const [scenarios, setScenarios] = useState<V1Scenario[]>([]);
  const [applications, setApplications] = useState<V1Application[]>([]);
  const [artifacts, setArtifacts] = useState<Record<string, unknown>[]>([]);
  const [models, setModels] = useState<string[]>([]);
  const [model, setModel] = useState("");
  const [selected, setSelected] = useState<string[]>(() => params.get("scenario") ? [params.get("scenario")!] : []);
  const [policy, setPolicy] = useState<"ready-only-v1" | "reviewed-draft-v1">("ready-only-v1");
  const [segment, setSegment] = useState<"G1" | "T08">("G1");
  const [runtimeIds, setRuntimeIds] = useState("");
  const [repositoryHints, setRepositoryHints] = useState("");
  const [plan, setPlan] = useState<V1Plan | null>(() => initialPlan(params.get("plan")));
  const [report, setReport] = useState<Record<string, unknown> | null>(null);
  const [basis, setBasis] = useState<Record<string, unknown>[]>([]);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [notice, setNotice] = useState("");
  const [reviewNotes, setReviewNotes] = useState<Record<string, string>>({});
  const [autoRefresh, setAutoRefresh] = useState(() => {
    const state = plan?.state || plan?.batch?.state || plan?.status;
    return !!state && state !== "preview" && state !== "loading" && !terminal(state);
  });

  const eligible = useMemo(() => scenarios.filter(item => item.status !== "archived" && (policy === "ready-only-v1" ? item.status === "ready" : item.status === "ready" || item.status === "draft")), [scenarios, policy]);
  const selectedScenarios = scenarios.filter(item => selected.includes(item.id));
  const currentPlanId = plan ? planId(plan) : "";
  const currentDigest = plan ? planDigest(plan) : "";
  const currentState = plan?.state || plan?.batch?.state || plan?.status || "preview";
  const currentTerminal = terminal(currentState) || (!!plan && isTerminalPlan(plan));

  async function load(signal?: AbortSignal) {
    const [sceneValue, appValue, status, artifactValue] = await Promise.all([
      factoryRequest<unknown>("catalog", undefined, signal),
      factoryV1Request<unknown>("applications", undefined, signal),
      factoryRequest<{ cli?: { models?: string[] } }>("status", undefined, signal),
      factoryRequest<unknown>("artifacts", undefined, signal),
    ]);
    const sceneList = Array.isArray(sceneValue) ? sceneValue as V1Scenario[] : [];
    const appList = Array.isArray(appValue) ? appValue as V1Application[] : [];
    setScenarios(sceneList);
    setApplications(appList);
    setArtifacts(Array.isArray(artifactValue) ? artifactValue as Record<string, unknown>[] : []);
    const availableModels = status.cli?.models || [];
    setModels(availableModels);
    setModel(current => current || preferredModel(availableModels));
    setSelected(current => current.filter(id => sceneList.some(scene => scene.id === id)));
  }

  useEffect(() => {
    const controller = new AbortController();
    load(controller.signal).then(() => setError("")).catch(cause => { if (!controller.signal.aborted) setError(String(cause)); }).finally(() => { if (!controller.signal.aborted) setLoading(false); });
    return () => controller.abort();
  }, []);

  useEffect(() => {
    if (!plan) return;
    const id = planId(plan);
    if (!id) return;
    try {
      localStorage.setItem(savedPlanKey, id);
      localStorage.setItem(`atlas.factory.v1.plan:${id}`, JSON.stringify(plan));
    } catch { /* Storage can be disabled; the active page state still works. */ }
    setSearchParams(current => {
      const next = new URLSearchParams(current);
      next.set("view", "v1");
      next.set("plan", id);
      return next;
    }, { replace: true });
  }, [plan, setSearchParams]);

  async function refreshPlan(signal?: AbortSignal, quiet = false) {
    if (!currentPlanId) return;
    if (!quiet) setRefreshing(true);
    try {
      const loaded = await factoryV1Request<unknown>(`plans/${encodeURIComponent(currentPlanId)}`, undefined, signal);
      const current = mergeBatchResult(plan || { plan_id: currentPlanId }, loaded);
      let executionReport: Record<string, unknown> | null = null;
      try {
        executionReport = await factoryV1Request<Record<string, unknown>>(`plans/${encodeURIComponent(currentPlanId)}/report`, undefined, signal);
      } catch (cause) { if (!signal?.aborted) setError(String(cause)); }
      const batch = executionReport?.batch as Record<string, unknown> | null;
      const batchState = typeof batch?.state === "string" ? batch.state : undefined;
      const currentWithState = batch ? mergeBatchResult(current, { batch: { ...batch, state: batchState } }) : current;
      setPlan(currentWithState);
      const state = currentWithState.state || currentWithState.status;
      const recoveredIds = planItems(currentWithState).map(value => {
        if (!value || typeof value !== "object") return "";
        const item = value as Record<string, unknown>;
        const scenario = item.scenario && typeof item.scenario === "object" ? item.scenario as Record<string, unknown> : {};
        return typeof item.scenario_id === "string" ? item.scenario_id : typeof scenario.id === "string" ? scenario.id : "";
      }).filter(Boolean);
      if (recoveredIds.length) {
        setSelected(recoveredIds);
        const samples = planItems(currentWithState).flatMap(value => {
          if (!value || typeof value !== "object") return [];
          const item = value as Record<string, unknown>;
          if (item.runtime_sample !== true) return [];
          const nested = item.scenario && typeof item.scenario === "object" ? item.scenario as Record<string, unknown> : {};
          const id = typeof item.scenario_id === "string" ? item.scenario_id : typeof nested.id === "string" ? nested.id : "";
          return id ? [id] : [];
        });
        setRuntimeIds(samples.join("\n"));
      }
      if (currentWithState.segment === "G1" || currentWithState.segment === "T08") setSegment(currentWithState.segment);
      if (currentWithState.admission_policy === "ready-only-v1" || currentWithState.admission_policy === "reviewed-draft-v1") {
        setPolicy(currentWithState.admission_policy);
      }
      if (terminal(state)) {
        setAutoRefresh(false);
        setReport(executionReport);
      } else if (executionReport) {
        setReport(executionReport);
      }
      setAutoRefresh(!!state && state !== "preview" && state !== "loading" && !terminal(state));
    } catch (cause) { if (!signal?.aborted) setError(String(cause)); }
    finally { if (!signal?.aborted && !quiet) setRefreshing(false); }
  }

  useEffect(() => {
    if (!currentPlanId || !autoRefresh || currentTerminal) return;
    const controller = new AbortController();
    const timer = window.setInterval(() => void refreshPlan(controller.signal, true), 4000);
    return () => { controller.abort(); window.clearInterval(timer); };
  }, [currentPlanId, autoRefresh, currentTerminal]);

  useEffect(() => {
    if (!selected.length) { setBasis([]); return; }
    const controller = new AbortController();
    Promise.all(selected.map(id => factoryV1Request<unknown>(`scenarios/${encodeURIComponent(id)}/basis`, undefined, controller.signal)
      .then(value => ({ ...(value as Record<string, unknown>), scenario_id: id }))
      .catch(cause => ({ scenario_id: id, error: String(cause) }))))
      .then(setBasis);
    return () => controller.abort();
  }, [selected.join("|")]);

  useEffect(() => {
    if (currentPlanId) void refreshPlan(undefined, true);
    // Refresh a restored or newly-previewed plan once to recover server state.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [currentPlanId]);

  useEffect(() => {
    const urlPlanId = params.get("plan");
    if (!urlPlanId || urlPlanId === currentPlanId) return;
    const restored = readSavedPlan(urlPlanId) || { plan_id: urlPlanId, state: "loading" };
    setPlan(restored);
    const state = restored.state || restored.batch?.state || restored.status;
    setAutoRefresh(!!state && state !== "preview" && state !== "loading" && !terminal(state));
  }, [params, currentPlanId]);

  async function preview() {
    setBusy(true); setError(""); setNotice(""); setReport(null);
    try {
      const created = unwrapPlan(await factoryV1Request<unknown>("plans/preview", {
        scenario_ids: selected,
        model,
        admission_policy: policy,
        segment,
        runtime_sample_ids: runtimeIds.split(/[\n,]/).map(value => value.trim()).filter(Boolean),
        repository_hints: Object.fromEntries(selected.map(id => [id, repositoryHints.split(/\n/).map(value => value.trim()).filter(Boolean)])),
      }));
      setPlan(created);
      setNotice(zh ? "已生成只读预览；尚未创建模型调用。" : "Read-only preview created; no model call was started.");
    } catch (cause) { setError(String(cause)); }
    finally { setBusy(false); }
  }

  async function runPlan() {
    if (!currentPlanId || !currentDigest) return;
    setBusy(true); setError(""); setNotice("");
    try {
      const result = await factoryV1Request<unknown>(`plans/${encodeURIComponent(currentPlanId)}/run`, {
        expected_plan_digest: currentDigest,
        idempotency_key: `run:${currentPlanId}:${currentDigest}`,
      });
      const runningPlan = mergeBatchResult(plan!, result);
      setPlan(runningPlan);
      setReport(null);
      setAutoRefresh(!terminal(runningPlan.state || runningPlan.status));
      setNotice(zh ? "計劃已提交；狀態將持續更新，終態後停止輪詢。" : "Plan submitted; status will refresh until it reaches a terminal state.");
      if (terminal(runningPlan.state || runningPlan.status)) await refreshPlan();
    } catch (cause) { setError(String(cause)); }
    finally { setBusy(false); }
  }

  async function control(action: "pause" | "resume" | "cancel") {
    if (!currentPlanId) return;
    setBusy(true); setError("");
    try {
      const result = await factoryV1Request<unknown>(`plans/${encodeURIComponent(currentPlanId)}/${action}`, {});
      const updated = mergeBatchResult(plan!, result);
      setPlan(updated);
      setAutoRefresh(!terminal(updated.state || updated.status));
      if (terminal(updated.state || updated.status)) await refreshPlan();
    } catch (cause) { setError(String(cause)); }
    finally { setBusy(false); }
  }

  async function publicationAction(artifact: Record<string, unknown>, action: "publish" | "withdraw") {
    const id = String(artifact.id || "");
    setBusy(true); setError(""); setNotice("");
    try {
      await factoryRequest(`artifacts/${encodeURIComponent(id)}/review`, {
        action, expected_digest: artifact.digest, review: reviewNotes[id]?.trim() || "",
      });
      await load();
      setNotice(action === "publish" ? (zh ? "模板已发布；其运行状态保持独立。" : "Template published; runtime status remains separate.") : (zh ? "模板已下架，历史记录仍保留。" : "Template withdrawn; its history remains available."));
    } catch (cause) { setError(String(cause)); }
    finally { setBusy(false); }
  }

  function planStateLabel(state: string) {
    const labels: Record<string, [string, string]> = {
      preview: ["只读预览", "Read-only preview"], queued: ["排队中", "Queued"], running: ["运行中", "Running"],
      paused: ["已暂停", "Paused"], completed: ["已完成", "Completed"], failed: ["失败", "Failed"],
      blocked: ["已阻止", "Blocked"], needs_attention: ["需要处理", "Needs attention"], cancelled: ["已取消", "Cancelled"],
    };
    return labels[state]?.[zh ? 0 : 1] || state;
  }

  const pickedRuntimeIds = runtimeIds.split(/[\n,]/).map(value => value.trim()).filter(Boolean);
  const runtimeSamplingReady = segment !== "T08" || pickedRuntimeIds.length >= 3;
  return <section aria-label={zh ? "模板工厂 V1 批次" : "Template factory V1 batches"} className="mt-6 space-y-5">
    <div className="rounded-xl border border-border bg-surface p-5 shadow-card">
      <div className="flex flex-wrap items-start justify-between gap-3"><div><h2 className="flex items-center gap-2 font-serif text-2xl font-medium"><Activity className="size-5 text-primary"/>{zh ? "V1 批次预览与执行" : "V1 batch preview and execution"}</h2><p className="mt-2 max-w-3xl text-sm leading-6 text-muted">{zh ? "先预览场景版本、证据准备度、排除原因和资源边界。只有确认固定摘要后才提交；暂停、恢复和取消由服务端执行。" : "Preview pinned scenario revisions, evidence readiness, exclusions and resource limits first. Submit only against the reviewed digest; pause, resume and cancel are enforced by the service."}</p></div><Button size="sm" variant="outline" disabled={loading || refreshing} onClick={() => { setRefreshing(true); load().catch(cause => setError(String(cause))).finally(() => setRefreshing(false)); }}><RefreshCw className="size-4"/>{zh ? "刷新目录" : "Refresh catalog"}</Button></div>
      {error ? <p role="alert" className="mt-4 rounded-md bg-danger/10 p-3 text-sm text-danger">{error}</p> : null}
      {notice ? <p role="status" className="mt-4 rounded-md bg-primary/10 p-3 text-sm text-primary">{notice}</p> : null}
      {loading ? <Loading/> : <>
        <div className="mt-5 grid gap-4 sm:grid-cols-2">
          <label className="text-sm">{zh ? "批次阶段" : "Campaign segment"}<select className={field} value={segment} onChange={event => setSegment(event.target.value as "G1" | "T08")}><option value="G1">G1 · {zh ? "里程碑验证" : "Milestone validation"}</option><option value="T08">T08 · {zh ? "首批受控生产" : "First controlled production"}</option></select></label>
          <label className="text-sm">{zh ? "模型" : "Model"}<select aria-label={zh ? "V1 模型" : "V1 model"} className={field} value={model} onChange={event => setModel(event.target.value)}><option value="">{zh ? "选择已配置模型" : "Choose configured model"}</option>{models.map(item => <option key={item} value={item}>{item}</option>)}</select></label>
          <label className="text-sm">{zh ? "准入策略" : "Admission policy"}<select className={field} value={policy} onChange={event => { setPolicy(event.target.value as typeof policy); setSelected([]); setRuntimeIds(""); }}><option value="ready-only-v1">{zh ? "仅已确认场景" : "Confirmed scenarios only"}</option><option value="reviewed-draft-v1">{zh ? "允许经过审阅的草案（明确选择）" : "Allow reviewed drafts (explicit opt-in)"}</option></select></label>
        <fieldset className="rounded-lg border border-border p-3 text-sm sm:col-span-2"><legend className="px-1">{zh ? "运行抽验场景" : "Runtime sample scenarios"}</legend><p className="mb-2 text-xs text-muted">{zh ? `从所选场景中预先固定样例。T08 至少需要 3 项；共享案例库当前有 ${applications.length} 个应用记录。` : `Pin samples from selected scenarios before execution. T08 requires at least 3; the shared library currently has ${applications.length} applications.`}</p>{selectedScenarios.length ? <div className="grid gap-2 sm:grid-cols-2">{selectedScenarios.map(scene => { const checked = pickedRuntimeIds.includes(scene.id); return <label key={scene.id} className="flex items-center gap-2 text-xs"><input type="checkbox" checked={checked} onChange={event => { const sampleChecked = event.target.checked; setRuntimeIds(current => { const values = current.split(/[\n,]/).map(value => value.trim()).filter(Boolean).filter(value => value !== scene.id); if (sampleChecked) values.push(scene.id); return values.join("\n"); }); }}/>{scene.name} · r{scene.revision}</label>; })}</div> : <p className="text-xs text-muted">{zh ? "先选择场景，再固定抽验样例。" : "Select scenarios before pinning runtime samples."}</p>}{segment === "T08" && !runtimeSamplingReady ? <p role="status" className="mt-2 text-xs text-warn">{zh ? `还需选择 ${3 - pickedRuntimeIds.length} 个抽验场景。` : `Select ${3 - pickedRuntimeIds.length} more runtime samples.`}</p> : null}</fieldset>
          <label className="text-sm sm:col-span-2">{zh ? "仓库提示（每行一个，可选）" : "Repository hints (one per line, optional)"}<textarea className={field} rows={2} value={repositoryHints} onChange={event => setRepositoryHints(event.target.value)} placeholder="https://github.com/owner/repository"/></label>
        </div>
        <div className="mt-5 flex flex-wrap items-center justify-between gap-2"><h3 className="font-medium">{zh ? "选择场景" : "Select scenarios"} <span className="text-xs text-muted">{zh ? `已选 ${selected.length} / 可选 ${eligible.length}` : `${selected.length} selected / ${eligible.length} eligible`}</span></h3><div className="flex gap-2"><Button size="sm" variant="outline" onClick={() => setSelected(eligible.map(item => item.id))}>{zh ? "选择全部可选" : "Select all eligible"}</Button><Button size="sm" variant="ghost" onClick={() => { setSelected([]); setRuntimeIds(""); }}>{zh ? "清空" : "Clear"}</Button></div></div>
        {!eligible.length ? <EmptyState title={zh ? "没有符合当前策略的场景" : "No scenarios match this policy"}>{zh ? "先在生产目录确认场景，或明确选择经过审阅的草案策略。" : "Confirm scenarios in the catalog, or explicitly choose the reviewed-draft policy."}</EmptyState> : <div className="mt-3 grid gap-3 md:grid-cols-2">{eligible.map(scene => {
          const review = scene.reviews?.find(item => item.current && item.scenario_revision === scene.revision);
          const checked = selected.includes(scene.id);
          return <label key={scene.id} className={`flex cursor-pointer gap-3 rounded-lg border p-4 ${checked ? "border-primary bg-primary/5" : "border-border"}`}><input className="mt-1" type="checkbox" checked={checked} onChange={event => { const selectedNow = event.target.checked; setSelected(current => selectedNow ? [...current, scene.id] : current.filter(id => id !== scene.id)); if (!selectedNow) setRuntimeIds(current => current.split(/[\n,]/).map(value => value.trim()).filter(value => value && value !== scene.id).join("\n")); }}/><span className="min-w-0 flex-1"><span className="block font-medium">{scene.name}</span><span className="mt-1 block text-xs text-muted">{scene.leaf_name || scene.leaf} · {scene.status} · r{scene.revision} · {zh ? "当前审阅" : "Current review"}: {displayUnknown(review?.outcome, zh)}</span><Link onClick={event => event.stopPropagation()} to={`/factory?scenario=${encodeURIComponent(scene.id)}`} className="mt-2 inline-flex items-center gap-1 text-xs text-primary hover:underline">{zh ? "打开场景目录" : "Open scenario catalog"}<ExternalLink className="size-3"/></Link></span></label>;
        })}</div>}
        {basis.length ? <details className="mt-4 rounded-lg border border-border p-3"><summary className="cursor-pointer text-sm font-medium">{zh ? "当前场景证据范围与阻塞项" : "Scenario evidence scope and blockers"}</summary><div className="mt-3 space-y-2">{basis.map((item, index) => <div key={String(item.scenario_id || index)} className="rounded-md bg-bg-elevated p-3 text-xs"><p className="font-medium">{String(item.scenario_name || item.name || item.scenario_id)}{(item.revision || item.scenario_revision) ? ` · r${String(item.revision || item.scenario_revision)}` : ""}</p><p className="mt-1">{zh ? "下一阶段" : "Next stage"}: {displayUnknown(item.next_stage || item.stage, zh)} · {zh ? "审阅" : "Review"}: {displayUnknown(item.review_status || item.review, zh)}</p><p className="mt-1">{zh ? "案例" : "Cases"}: {Array.isArray(item.cases) ? item.cases.length : displayUnknown(item.case_count, zh)} · {zh ? "证据范围" : "Evidence scope"}: {displayUnknown(item.evidence_scope, zh)}</p>{Array.isArray(item.blockers) && item.blockers.length ? <ul className="mt-1 list-disc pl-4 text-warn">{item.blockers.map((blocker, i) => <li key={i}>{typeof blocker === "string" ? blocker : JSON.stringify(blocker)}</li>)}</ul> : null}{item.error ? <p className="mt-1 text-warn">{String(item.error)}</p> : null}</div>)}</div></details> : null}
        <div className="mt-5 flex flex-wrap items-center justify-between gap-3 border-t border-border pt-4"><p className="max-w-2xl text-xs leading-5 text-muted">{zh ? "预览只读且不调用模型。服务端会冻结摘要并在运行时重新校验 revision；并发和预算由共享台账强制执行。" : "Preview is read-only and does not call a model. The service pins the digest and rechecks revisions at execution; shared ledger limits enforce concurrency and budget."}</p><Button disabled={busy || !selected.length || !model || !runtimeSamplingReady} onClick={() => void preview()}><ClipboardCheck className="size-4"/>{zh ? "生成只读预览" : "Create read-only preview"}</Button></div>
      </>}
    </div>
    {plan ? <section aria-label={zh ? "批次计划" : "Batch plan"} className="rounded-xl bg-surface p-5 shadow-card">
      <div className="flex flex-wrap items-start justify-between gap-3"><div><h2 className="font-serif text-xl font-medium">{zh ? "计划与运行状态" : "Plan and execution status"}</h2><p className="mt-1 break-all text-xs text-muted">{zh ? "计划 ID" : "Plan ID"}: {currentPlanId || displayUnknown(null, zh)} · {planStateLabel(currentState)}</p><p className="mt-1 break-all text-xs text-muted">{zh ? "固定计划摘要" : "Pinned plan digest"}: <code>{currentDigest || displayUnknown(null, zh)}</code></p></div><Button size="sm" variant="outline" disabled={refreshing || !currentPlanId} onClick={() => void refreshPlan()}><RefreshCw className="size-4"/>{zh ? "刷新计划" : "Refresh plan"}</Button></div>
      <div className="mt-4 grid gap-4 lg:grid-cols-2"><div><h3 className="text-sm font-medium">{zh ? "计划项" : "Planned items"} ({planItems(plan).length})</h3>{planItems(plan).length ? <ul className="mt-2 space-y-2">{planItems(plan).map((item, index) => <li key={index} className="rounded-md border border-border p-3 text-xs">{renderPlanItem(item, zh)}</li>)}</ul> : <p className="mt-2 text-xs text-muted">{zh ? "服务未返回计划项。" : "No planned items returned."}</p>}</div><div><h3 className="text-sm font-medium">{zh ? "排除项" : "Excluded items"} ({planExcluded(plan).length})</h3>{planExcluded(plan).length ? <ul className="mt-2 space-y-2">{planExcluded(plan).map((item, index) => <li key={index} className="rounded-md bg-warn/10 p-3 text-xs text-warn">{renderPlanItem(item, zh)}</li>)}</ul> : <p className="mt-2 text-xs text-muted">{zh ? "没有排除项" : "No exclusions"}</p>}</div></div>
      <h3 className="mt-5 text-sm font-medium">{zh ? "资源边界与累计用量" : "Resource limits and cumulative usage"}</h3><pre className="mt-2 max-h-52 overflow-auto whitespace-pre-wrap break-words rounded-md bg-bg-elevated p-3 text-xs">{JSON.stringify(plan.budget || report?.budget || plan.limits || { runtime_sample_ids: pickedRuntimeIds }, null, 2)}</pre>
      <div className="mt-4 flex flex-wrap gap-2">
        {!currentTerminal && currentState === "preview" ? <Button disabled={busy || !currentDigest} onClick={() => void runPlan()}><Play className="size-4"/>{zh ? "按固定摘要运行" : "Run against pinned digest"}</Button> : null}
        {!currentTerminal && currentState !== "preview" ? <Button size="sm" variant="outline" disabled={busy} onClick={() => void control(currentState === "paused" ? "resume" : "pause")}>{currentState === "paused" ? <Play className="size-4"/> : <Pause className="size-4"/>}{currentState === "paused" ? (zh ? "继续" : "Resume") : (zh ? "暂停" : "Pause")}</Button> : null}
        {!currentTerminal && currentState !== "preview" ? <Button size="sm" variant="ghost" disabled={busy} onClick={() => void control("cancel")}><XCircle className="size-4"/>{zh ? "取消批次" : "Cancel batch"}</Button> : null}
        {currentTerminal && report ? <span className="inline-flex items-center gap-2 rounded-md bg-chip px-3 text-xs">{zh ? "质量报告已载入；质量结果与运行状态分开。" : "Quality report loaded separately from execution state."}</span> : null}
      </div>
      {report ? <BatchReport report={report} zh={zh} busy={busy} onRetry={async jobId => { setBusy(true); setError(""); try { await factoryRequest(`jobs/${encodeURIComponent(jobId)}/retry`, {}); setAutoRefresh(true); await refreshPlan(); } catch (cause) { setError(String(cause)); } finally { setBusy(false); } }}/> : null}
    </section> : null}
    <section aria-label={zh ? "正式模板目录" : "Published template catalog"} className="rounded-xl border border-border bg-surface p-5 shadow-card">
      <h2 className="font-serif text-xl font-medium">{zh ? "模板审阅、发布与撤回" : "Template review, publication and withdrawal"}</h2>
      <p className="mt-2 text-xs leading-5 text-muted">{zh ? "发布由服务端检查当前摘要、独立认知审阅和固定案例证据。发布状态与目标运行状态分开展示；运行未验证时显示未运行。" : "The service checks the current digest, independent cognitive review and fixed case evidence before publication. Publication and target runtime remain separate; unverified runtime is shown as not run."}</p>
      {artifacts.filter(item => item.artifact_type === "product-blueprint").length ? <div className="mt-4 space-y-3">{artifacts.filter(item => item.artifact_type === "product-blueprint").map(artifact => {
        const id = String(artifact.id || "");
        const reviewStatus = String(artifact.review_status || "unavailable");
        const evidenceStatus = String(artifact.evidence_status || "legacy_unverified");
        const publicationStatus = String(artifact.publication_status || artifact.state || "draft");
        const canPublish = reviewStatus === "passed" && evidenceStatus === "fixed_case_basis";
        const manifest = artifact.manifest && typeof artifact.manifest === "object" ? artifact.manifest as Record<string, unknown> : {};
        const published = publicationStatus === "published";
        const runtimeRuns = Array.isArray(artifact.acceptances)
          ? (artifact.acceptances as Record<string, unknown>[]).filter(item => item.method === "blueprint-runtime")
          : [];
        return <article key={id} className="rounded-lg border border-border p-4"><div className="flex flex-wrap items-center justify-between gap-3"><div><h3 className="font-medium">{String(manifest.name || id)}</h3><p className="mt-1 break-all text-xs text-muted">{id} · {zh ? "发布" : "Publication"}: {publicationStatus} · {zh ? "审阅" : "Review"}: {reviewStatus} · {zh ? "案例依据" : "Case basis"}: {evidenceStatus}</p></div><Link to={`/factory?view=artifacts&artifact_id=${encodeURIComponent(id)}`} className="inline-flex items-center gap-1 text-xs text-primary underline">{zh ? "阅读 / 导出" : "Read / export"}<ExternalLink className="size-3"/></Link></div>
          <section className="mt-3 rounded-md bg-bg-elevated p-3" aria-label={zh ? "目标运行记录" : "Target runtime records"}>
            <h4 className="text-xs font-medium">{zh ? "目标运行记录" : "Target runtime records"}</h4>
            {runtimeRuns.length ? <ul className="mt-2 space-y-2">{runtimeRuns.map((run, index) => {
              const binding = run.target_binding && typeof run.target_binding === "object" ? run.target_binding as Record<string, unknown> : {};
              const runId = String(run.id || run.run_id || run.job_id || `runtime-${index + 1}`);
              const targetId = String(binding.application_digest || run.application_digest || "unknown");
              const phase = String(run.selected_phase || binding.selected_phase || "unknown");
              const suiteStatus = String(run.suite_status || "unknown");
              const phaseStatus = String(run.phase_status || "unknown");
              return <li key={runId} className="flex flex-wrap items-center justify-between gap-2 text-xs"><span className="break-all">{zh ? "运行" : "Run"}: {runId} · {zh ? "目标" : "Target"}: {targetId} · {zh ? "阶段" : "Phase"}: {phase} · suite_status: {suiteStatus} · phase_status: {phaseStatus}</span><Link to={`/factory?view=artifacts&artifact_id=${encodeURIComponent(id)}&runtime_run_id=${encodeURIComponent(runId)}`} className="shrink-0 text-primary underline">{zh ? "查看运行断言" : "View run assertions"}<ExternalLink className="ml-1 inline size-3"/></Link></li>;
            })}</ul> : <p className="mt-2 text-xs text-muted">{zh ? "未运行" : "Not run"}</p>}
          </section>
          <label className="mt-3 block text-xs">{zh ? "审阅记录（必填）" : "Review note (required)"}<textarea className={field} rows={2} value={reviewNotes[id] || ""} onChange={event => setReviewNotes(current => ({ ...current, [id]: event.target.value }))} placeholder={zh ? "说明发布或撤回的决定及依据" : "Record the decision and its basis"}/></label>
          <div className="mt-3 flex flex-wrap items-center gap-2">{published ? <Button size="sm" variant="outline" disabled={busy || !reviewNotes[id]?.trim()} onClick={() => void publicationAction(artifact, "withdraw")}>{zh ? "撤回目录发布" : "Withdraw publication"}</Button> : <Button size="sm" disabled={busy || !canPublish || !reviewNotes[id]?.trim()} onClick={() => void publicationAction(artifact, "publish")}>{zh ? "发布到正式目录" : "Publish to catalog"}</Button>}{!canPublish && !published ? <span className="text-xs text-warn">{zh ? `发布阻塞：审阅 ${reviewStatus}，固定案例依据 ${evidenceStatus}。` : `Publication blocked: review ${reviewStatus}; fixed case basis ${evidenceStatus}.`}</span> : null}</div>
        </article>;
      })}</div> : <EmptyState className="mt-4" title={zh ? "没有冻结认知模板" : "No frozen cognitive templates"}>{zh ? "V1 生产冻结候选后，可在这里检查审阅和发布资格。" : "Frozen candidates from V1 production appear here with their review and publication eligibility."}</EmptyState>}
    </section>
  </section>;
}

function BatchReport({ report, zh, busy, onRetry }: { report: Record<string, unknown>; zh: boolean; busy: boolean; onRetry: (jobId: string) => void }) {
  const counts = report.counts && typeof report.counts === "object" ? report.counts as Record<string, unknown> : {};
  const products = report.products && typeof report.products === "object" ? report.products as Record<string, Record<string, unknown>> : {};
  const artifacts = Array.isArray(report.artifacts) ? report.artifacts as Record<string, unknown>[] : [];
  const failures = Array.isArray(report.failed_items) ? report.failed_items as Record<string, unknown>[] : [];
  return <section aria-label={zh ? "批次质量报告" : "Batch quality report"} className="mt-5 rounded-lg border border-border p-4">
    <div className="flex flex-wrap items-baseline justify-between gap-2"><h3 className="font-medium">{zh ? "质量结果" : "Quality result"}</h3><span className="rounded-full bg-chip px-2 py-1 text-xs">{zh ? "质量" : "Quality"}: {displayUnknown(report.quality_result, zh)} · {zh ? "运行抽验门禁" : "Runtime sampling gate"}: {displayUnknown(report.runtime_sampling_gate, zh)}</span></div>
    <div className="mt-3 grid grid-cols-2 gap-2 sm:grid-cols-4">{Object.entries(counts).map(([name, value]) => <div key={name} className="rounded-md bg-bg-elevated p-2 text-xs"><span className="block text-muted">{name.replaceAll("_", " ")}</span><strong className="mt-1 block">{displayUnknown(value, zh)}</strong></div>)}</div>
    <h4 className="mt-4 text-sm font-medium">{zh ? "实际制品" : "Actual artifacts"}</h4>
    {artifacts.length ? <ul className="mt-2 space-y-2">{artifacts.map((artifact, index) => { const manifest = artifact.manifest && typeof artifact.manifest === "object" ? artifact.manifest as Record<string, unknown> : {}; return <li key={String(artifact.id || index)} className="flex flex-wrap items-center justify-between gap-2 rounded-md border border-border p-3 text-xs"><span>{String(manifest.name || artifact.id)} · {String(artifact.id)} · {zh ? "审阅" : "Review"}: {String(artifact.review_status || "unknown")} · {zh ? "发布" : "Published"}: {String(artifact.publication_status || artifact.state || "draft")}</span>{artifact.id ? <a className="text-primary underline" href={`/api/factory/artifacts/${encodeURIComponent(String(artifact.id))}/download`}>{zh ? "下载冻结制品" : "Download frozen artifact"}</a> : null}</li>; })}</ul> : <p className="mt-2 text-xs text-muted">{zh ? "尚无冻结制品。" : "No frozen artifact yet."}</p>}
    <h4 className="mt-4 text-sm font-medium">{zh ? "产品结果" : "Product outcomes"}</h4><div className="mt-2 space-y-2">{Object.entries(products).map(([id, product]) => <div key={id} className="rounded-md bg-bg-elevated p-3 text-xs"><p className="break-all font-medium">{id}</p><p className="mt-1">{zh ? "制品" : "Artifacts"}: {Array.isArray(product.artifact_ids) ? product.artifact_ids.length : 0} · {zh ? "已审阅" : "Reviewed"}: {String(product.reviewed)} · {zh ? "已发布" : "Published"}: {String(product.published)} · P0: {product.p0_runtime ? (zh ? "通过" : "Passed") : (zh ? "未运行 / 未通过" : "Not run / not passed")}</p></div>)}</div>
    <h4 className="mt-4 text-sm font-medium">{zh ? "失败项与恢复" : "Failed items and recovery"}</h4>{failures.length ? <ul className="mt-2 space-y-2">{failures.map((failure, index) => <li key={String(failure.job_id || index)} className="flex flex-wrap items-center justify-between gap-2 rounded-md bg-danger/5 p-3 text-xs"><span className="min-w-0 break-all">{String(failure.job_id)} · {String(failure.stage)} · {String(failure.state)} · {String(failure.error || "")}</span><Button size="sm" variant="outline" disabled={busy || typeof failure.job_id !== "string"} onClick={() => typeof failure.job_id === "string" && onRetry(failure.job_id)}>{zh ? "从检查点重试此项" : "Retry this item from checkpoint"}</Button></li>)}</ul> : <p className="mt-2 text-xs text-muted">{zh ? "没有报告失败项。" : "No failed items reported."}</p>}
    <details className="mt-4"><summary className="cursor-pointer text-xs text-primary">{zh ? "完整机器报告" : "Full machine report"}</summary><pre className="mt-2 max-h-80 overflow-auto whitespace-pre-wrap break-words text-xs">{JSON.stringify(report, null, 2)}</pre></details>
  </section>;
}

function renderPlanItem(item: unknown, zh: boolean) {
  if (typeof item === "string") return item;
  if (!item || typeof item !== "object") return String(item);
  const value = item as Record<string, unknown>;
  const scene = value.scenario && typeof value.scenario === "object" ? value.scenario as Record<string, unknown> : {};
  const primary = value.scenario_name || value.name || scene.name || value.scenario_id || scene.id || value.id;
  const revision = value.scenario_revision || scene.revision || value.revision;
  const nextStage = value.next_stage || value.stage;
  const caseStatus = value.case_status || value.evidence_status || value.template_input_status
    || (value.case_basis ? (zh ? "已固定案例证据" : "Fixed case evidence") : (value.template_input_ready === false ? (zh ? "需要案例研究" : "Research required") : undefined));
  const reason = value.exclusion_reason || value.reason || value.blocker;
  return <><span className="font-medium">{displayUnknown(primary, zh)}{revision ? ` · r${String(revision)}` : ""}</span>{nextStage ? <span> · {zh ? "下一阶段" : "Next"}: {String(nextStage)}</span> : null}{caseStatus ? <span> · {zh ? "案例证据" : "Case evidence"}: {String(caseStatus)}</span> : null}{reason ? <p className="mt-1 text-warn">{String(reason)}</p> : null}{Array.isArray(value.blockers) ? <ul className="mt-1 list-disc pl-4 text-warn">{value.blockers.map((blocker, index) => <li key={index}>{String(blocker)}</li>)}</ul> : null}</>;
}
