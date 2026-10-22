import { AssistedTemplates } from "@/components/assisted-templates";
import { useEffect, useMemo, useState } from "react";
import { Link, useSearchParams } from "react-router-dom";
import { AlertCircle, BookOpen, Copy, ExternalLink, RefreshCw } from "lucide-react";
import { Button } from "@/components/ui/button";
import { EmptyState, Loading } from "@/components/loaders";
import { useLang } from "@/lib/lang";
import { displayUnknown, factoryV1Request, type V1Application, type V1Case, type V1Observation } from "@/lib/factory-v1";

function asList<T>(value: unknown): T[] {
  if (Array.isArray(value)) return value as T[];
  if (value && typeof value === "object") {
    const object = value as Record<string, unknown>;
    for (const key of ["items", "applications", "cases", "results"]) if (Array.isArray(object[key])) return object[key] as T[];
  }
  return [];
}

export function CaseLibrary() {
  const { lang } = useLang();
  const zh = lang === "zh";
  const [params, setParams] = useSearchParams();
  const requestedApp = params.get("app_id") || "";
  const requestedCase = params.get("case_id")
    ? `${params.get("case_id")}:r${params.get("case_revision") || 1}`
    : "";
  const [apps, setApps] = useState<V1Application[]>([]);
  const [cases, setCases] = useState<V1Case[]>([]);
  const selectedApp = requestedApp || apps[0]?.app_id || "";
  const selectedKey = requestedCase || (cases[0] ? `${cases[0].case_id}:r${cases[0].revision}` : "");
  const [detail, setDetail] = useState<V1Case | null>(null);
  const [appsLoading, setAppsLoading] = useState(true);
  const [casesLoading, setCasesLoading] = useState(false);
  const [error, setError] = useState("");
  const [copyState, setCopyState] = useState("");
  const selected = useMemo(() => cases.find(item => `${item.case_id}:r${item.revision}` === selectedKey), [cases, selectedKey]);

  async function loadApps(signal?: AbortSignal) {
    setAppsLoading(true);
    try {
      const value = await factoryV1Request<unknown>("applications", undefined, signal);
      const list = asList<V1Application>(value);
      if (signal?.aborted) return;
      setApps(list);
      setError("");
    } catch (cause) {
      if (!signal?.aborted) setError(String(cause));
    } finally {
      if (!signal?.aborted) setAppsLoading(false);
    }
  }

  useEffect(() => {
    const controller = new AbortController();
    void loadApps(controller.signal);
    return () => controller.abort();
  }, []);

  useEffect(() => {
    if (!selectedApp) { setCases([]); setDetail(null); return; }
    const controller = new AbortController();
    setCasesLoading(true);
    setCases([]);
    factoryV1Request<unknown>(`cases?app_id=${encodeURIComponent(selectedApp)}`, undefined, controller.signal)
      .then(value => {
        if (controller.signal.aborted) return;
        setCases(asList<V1Case>(value));
      })
      .catch(cause => { if (!controller.signal.aborted) setError(String(cause)); })
      .finally(() => { if (!controller.signal.aborted) setCasesLoading(false); });
    return () => controller.abort();
  }, [selectedApp]);

  useEffect(() => {
    if (!selected) { setDetail(null); return; }
    const controller = new AbortController();
    setDetail(null);
    factoryV1Request<V1Case>(`cases/${encodeURIComponent(selected.case_id)}/revisions/${selected.revision}`, undefined, controller.signal)
      .then(value => { if (!controller.signal.aborted) setDetail(value); }).catch(cause => { if (!controller.signal.aborted) setError(String(cause)); });
    return () => controller.abort();
  }, [selected?.case_id, selected?.revision]);

  const appName = (app: V1Application) => app.name || app.slug || app.app_id;
  const fixedRef = detail ? `atlas:case:${detail.case_id}:r${detail.revision}` : "";
  async function copyRef() {
    if (!fixedRef) return;
    try {
      await navigator.clipboard.writeText(fixedRef);
      setCopyState(zh ? "已复制固定引用" : "Pinned reference copied");
      window.setTimeout(() => setCopyState(""), 1800);
    } catch { setCopyState(zh ? "无法访问剪贴板，请手动复制" : "Clipboard unavailable; copy the reference manually"); }
  }

  return <section aria-label={zh ? "共享案例库" : "Shared case library"} className="mt-10 rounded-2xl border border-border bg-surface p-5 shadow-card sm:p-6">
    <div className="flex flex-wrap items-start justify-between gap-3">
      <div>
        <p className="flex items-center gap-2 text-sm font-medium text-primary"><BookOpen className="size-4"/>{zh ? "共享案例库" : "Shared case library"}</p>
        <h2 className="mt-2 font-serif text-2xl font-medium">{zh ? "研究版本与证据" : "Research versions and evidence"}</h2>
        <p className="mt-2 max-w-3xl text-sm leading-6 text-muted">{zh ? "这里读取工厂保存的应用实证、固定源码版本和证据。历史应用目录仍在下方独立显示；案例库暂不可用时不会隐藏目录卡片。" : "Browse saved app research, pinned source revisions and evidence. The legacy catalog remains below and stays visible if this shared library is unavailable."}</p>
      </div>
      <Button size="sm" variant="outline" onClick={() => void loadApps()}><RefreshCw className="size-4"/>{zh ? "刷新实证" : "Refresh evidence"}</Button>
    </div>
    {error ? <p role="status" className="mt-4 flex items-start gap-2 rounded-lg bg-warn/10 p-3 text-xs text-warn"><AlertCircle className="mt-0.5 size-4 shrink-0"/>{zh ? "动态案例库加载失败；旧应用目录仍可用。" : "The dynamic case library could not load; the legacy catalog remains available."} <span className="break-all">{error}</span></p> : null}
    {appsLoading ? <Loading/> : !apps.length ? <EmptyState className="mt-5" title={zh ? "还没有已保存的应用实证" : "No saved application evidence yet"}>{zh ? "通过模板工厂研究并提交固定源码版本后，记录会出现在这里。" : "Applications appear here after fixed-source research is committed through the template factory."}</EmptyState> : <div className="mt-5 grid gap-5 lg:grid-cols-[minmax(14rem,0.75fr)_minmax(0,1.5fr)]">
      <div className="min-w-0">
        <label className="block text-sm">{zh ? "应用" : "Application"}<select aria-label={zh ? "共享案例应用" : "Shared case application"} className="mt-1.5 w-full rounded-md border border-border bg-bg-elevated px-3 py-2 text-sm" value={selectedApp} onChange={event => { const next = new URLSearchParams(params); next.set("app_id", event.target.value); next.delete("case_id"); next.delete("case_revision"); setParams(next); }}>
          {apps.map(app => <option key={app.app_id} value={app.app_id}>{appName(app)} · {app.catalog_status || app.status || (zh ? "已收录" : "Catalogued")}</option>)}
        </select></label>
        <div className="mt-3 space-y-2">
          {casesLoading ? <Loading/> : cases.map(item => <button key={`${item.case_id}:r${item.revision}`} type="button" onClick={() => { const next = new URLSearchParams(params); next.set("app_id", selectedApp); next.set("case_id", item.case_id); next.set("case_revision", String(item.revision)); setParams(next); }} aria-pressed={selectedKey === `${item.case_id}:r${item.revision}`} className={`w-full rounded-lg border p-3 text-left ${selectedKey === `${item.case_id}:r${item.revision}` ? "border-primary bg-primary/5" : "border-border hover:bg-bg-elevated"}`}>
            <span className="block break-all text-sm font-medium">{item.case_id} · r{item.revision}</span>
            <span className="mt-1 block line-clamp-2 text-xs text-muted">{item.research?.summary || (zh ? "研究摘要未知" : "Research summary unknown")}</span>
            <span className="mt-2 block text-[11px] text-subtle">{zh ? "证据摘要" : "Evidence digest"}: <code>{item.evidence_digest?.slice(0, 12) || displayUnknown(null, zh)}</code></span>
          </button>)}
          {!casesLoading && !cases.length ? <p className="rounded-lg border border-dashed border-border p-4 text-xs text-muted">{zh ? "此应用目前没有固定案例版本。" : "This application has no pinned case revision yet."}</p> : null}
        </div>
      </div>
      <div className="min-w-0 rounded-xl border border-border p-4">
        {!detail ? <p className="text-sm text-muted">{zh ? "选择案例版本查看固定来源和证据。" : "Select a case revision to inspect its pinned sources and evidence."}</p> : <>
          <div className="flex flex-wrap items-start justify-between gap-3"><div><h3 className="break-all font-medium">{detail.case_id} · r{detail.revision}</h3><p className="mt-1 text-xs text-muted">{zh ? "固定摘要" : "Pinned digest"}: <code className="break-all">{detail.digest}</code></p><p className="mt-1 text-xs text-muted">{zh ? "证据摘要" : "Evidence digest"}: <code className="break-all">{displayUnknown(detail.evidence_digest, zh)}</code></p></div><Button size="sm" variant="outline" onClick={() => void copyRef()}><Copy className="size-3.5"/>{zh ? "复制固定引用" : "Copy pinned reference"}</Button></div>
          {copyState ? <p role="status" className="mt-2 text-xs text-primary">{copyState}</p> : null}
          <p className="mt-4 text-sm leading-6">{detail.research?.summary || (zh ? "研究摘要未知" : "Research summary unknown")}</p>
          <div className="mt-3 flex flex-wrap gap-2 text-xs text-muted"><span>{zh ? "资料深度" : "Coverage"}: {detail.observations?.length ?? 0} {zh ? "条证据" : "evidence records"}</span><span>{zh ? "场景关联" : "Scenario links"}: {detail.scenario_links?.length ?? 0}</span><span>{zh ? "创建时间" : "Recorded"}: {displayUnknown(detail.created_at, zh)}</span></div>
          <h4 className="mt-5 text-sm font-medium">{zh ? "固定源码版本" : "Pinned source revisions"}</h4>
          <div className="mt-2 space-y-2">{detail.source_snapshots?.length ? detail.source_snapshots.map((snapshot, index) => <div key={`${snapshot.commit_sha}-${index}`} className="rounded-lg bg-bg-elevated p-3 text-xs"><a href={snapshot.repository} target="_blank" rel="noreferrer" className="inline-flex max-w-full items-center gap-1 break-all text-primary underline"><span>{snapshot.repository || (zh ? "仓库未知" : "Repository unknown")}</span><ExternalLink className="size-3 shrink-0"/></a><p className="mt-1">{zh ? "Commit" : "Commit"}: <code className="break-all">{displayUnknown(snapshot.commit_sha, zh)}</code></p><p className="mt-1">{zh ? "文件清单" : "File manifest"}: {Object.keys(snapshot.files || {}).length} · SHA-256 {displayUnknown(snapshot.file_manifest_digest || snapshot.digest, zh)}</p></div>) : <p className="text-xs text-muted">{zh ? "没有固定源码快照信息" : "No pinned source snapshot details"}</p>}</div>
          <h4 className="mt-5 text-sm font-medium">{zh ? "代码观察、运行结果与未知项" : "Code observations, runtime results and unknowns"}</h4>
          <div className="mt-2 space-y-2">{detail.observations?.length ? detail.observations.map((observation: V1Observation) => <Observation key={observation.evidence_id} observation={observation} zh={zh}/>) : <p className="text-xs text-muted">{zh ? "没有观察记录；不可推断为运行通过。" : "No observations recorded; this does not imply runtime success."}</p>}</div>
          {detail.research?.unknowns?.length ? <div className="mt-4 rounded-lg bg-warn/10 p-3 text-xs"><p className="font-medium text-warn">{zh ? "仍未知" : "Still unknown"}</p><ul className="mt-1 list-disc space-y-1 pl-4">{detail.research.unknowns.map((item, index) => <li key={index}>{item}</li>)}</ul></div> : null}
          <h4 className="mt-5 text-sm font-medium">{zh ? "被哪些场景和模板采用" : "Scenario and template use"}</h4>
          <div className="mt-2 flex flex-wrap gap-2">{detail.scenario_links?.length ? detail.scenario_links.map(link => <Link key={`${link.scenario_id}:${link.scenario_revision}`} className="inline-flex items-center gap-1 rounded-md border border-border px-2 py-1 text-xs text-primary hover:bg-bg-elevated" to={`/factory?view=artifacts&scenario_id=${encodeURIComponent(link.scenario_id)}&case_id=${encodeURIComponent(detail.case_id)}&case_revision=${detail.revision}`}>{link.scenario_id} · r{link.scenario_revision} <ExternalLink className="size-3"/></Link>) : <span className="text-xs text-muted">{zh ? "没有场景采用记录" : "No scenario adoption recorded"}</span>}
            <Link className="inline-flex items-center gap-1 rounded-md border border-border px-2 py-1 text-xs text-primary hover:bg-bg-elevated" to={`/factory?view=artifacts&case_id=${encodeURIComponent(detail.case_id)}&case_revision=${detail.revision}`}>{zh ? "打开模板目录与导出" : "Open template catalog and export"}<ExternalLink className="size-3"/></Link>
          </div>
          <AssistedTemplates caseId={detail.case_id} caseRevision={detail.revision}/>
          {detail.templates?.length ? <ul className="mt-3 space-y-2">{detail.templates.map((template, index) => <li key={String(template.id || index)} className="flex flex-wrap items-center justify-between gap-2 rounded-lg border border-border p-3 text-xs"><span><strong>{String((template.manifest as Record<string, unknown> | undefined)?.name || template.id || (zh ? "模板" : "Template"))}</strong> · {String(template.publication_status || template.state || (zh ? "未发布" : "Unpublished"))} · {zh ? "审阅" : "Review"}: {String(template.review_status || (zh ? "未知" : "Unknown"))} · {zh ? "运行" : "Runtime"}: {String(template.runtime_status || (zh ? "未知" : "Unknown"))}</span><Link className="inline-flex items-center gap-1 text-primary underline" to={`/factory?view=artifacts&artifact_id=${encodeURIComponent(String(template.id || ""))}`}>{zh ? "查看 / 导出" : "View / export"}<ExternalLink className="size-3"/></Link></li>)}</ul> : null}
        </>}
      </div>
    </div>}
  </section>;
}

function Observation({ observation, zh }: { observation: V1Observation; zh: boolean }) {
  const runtime = observation.kind === "runtime_verification";
  const unknowns = observation.unknowns || [];
  return <details className="rounded-lg border border-border p-3 text-xs">
    <summary className="cursor-pointer"><span className={runtime ? "rounded-full bg-chip px-2 py-1 font-medium" : "rounded-full bg-bg-elevated px-2 py-1"}>{runtime ? (zh ? "独立运行记录" : "Runtime record") : observation.kind === "code_observation" ? (zh ? "代码观察" : "Code observation") : observation.kind}</span><span className="ml-2 break-all">{observation.evidence_id}</span>{runtime ? <span className="ml-2 text-muted">{zh ? "状态" : "Status"}: {displayUnknown(observation.status || observation.outcome, zh)}</span> : null}</summary>
    <p className="mt-3 whitespace-pre-wrap leading-5">{observation.statement || observation.summary || observation.content || (zh ? "观察内容未知" : "Observation content unknown")}</p>
    {observation.location?.path ? <p className="mt-2">{zh ? "代码位置" : "Code location"}: <code>{observation.location.path}:{displayUnknown(observation.location.line_start, zh)}</code></p> : null}
    <p className="mt-2">{zh ? "证据摘要" : "Evidence digest"}: <code className="break-all">{displayUnknown(observation.digest, zh)}</code></p>
    <p className="mt-2">{zh ? "观察状态" : "Observation status"}: {displayUnknown(observation.observation_status || observation.status || observation.outcome, zh)}</p>
    <p className="mt-2">{zh ? "审阅" : "Review"}: {(observation.reviews || []).map(review => `${review.outcome} (${review.reviewer || review.reviewer_kind || "unknown"})`).join(", ") || (zh ? "未审阅" : "Not reviewed")}</p>
    {unknowns.length ? <ul className="mt-2 list-disc space-y-1 pl-4 text-warn">{unknowns.map((item, index) => <li key={index}>{item}</li>)}</ul> : null}
  </details>;
}
