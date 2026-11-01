import { useEffect, useRef, useState } from "react";
import { Link, useNavigationType, useSearchParams } from "react-router-dom";
import { Bookmark, ExternalLink, RefreshCw, Search } from "lucide-react";
import { useAsync } from "@/components/loaders";
import { Button } from "@/components/ui/button";
import { useLang } from "@/lib/lang";
import { RepositoryBatch } from "@/components/repository-batch";
import {
  favoriteRepository, getCatalogRun, getRepositoryCatalog, PKM_LEAF, refreshRepositoryCatalog,
  type CatalogRun, type Evidence, type LicenseStatus, type RepositoryProject,
} from "@/lib/oss-catalog";

const PAGE_SIZE = 24;

const licenseLabels: Record<LicenseStatus, [string, string]> = {
  open_source: ["已核验开源许可证", "Verified open-source license"],
  source_available: ["源码可见 · 使用有限制", "Source available · restrictions apply"],
  pending: ["许可证待核验", "License review pending"],
};

export function RepositoryCatalog({ leaf = "", showHeading = true }: { leaf?: string; showHeading?: boolean }) {
  const { lang } = useLang();
  const zh = lang === "zh";
  const [params, setParams] = useSearchParams();
  const activeLeaf = leaf || params.get("leaf") || "";
  const [selectedLeaf, setSelectedLeaf] = useState(activeLeaf);
  const q = params.get("q") || "";
  const scenario = params.get("scenario") || "";
  const license = params.get("license") || "";
  const favorites = params.get("favorites") === "1";
  const pageValue = Number(params.get("page") || "1");
  const page = Number.isSafeInteger(pageValue) && pageValue > 0 ? pageValue : 1;
  const previousPage = useRef(page);
  const results = useRef<HTMLDivElement>(null);
  const navigation = useNavigationType();
  useEffect(() => {
    if (previousPage.current !== page && navigation !== "POP") results.current?.scrollIntoView({ block: "start" });
    previousPage.current = page;
  }, [page, navigation]);
  const sort = params.get("sort") === "recent" ? "recent" : "name";
  const [showAllScenarios, setShowAllScenarios] = useState(false);
  const [query, setQuery] = useState(q);
  const [favoritesChecked, setFavoritesChecked] = useState(favorites);
  const [selectedLicense, setSelectedLicense] = useState(license);
  const [revision, setRevision] = useState(0);
  const [run, setRun] = useState<CatalogRun | null>(null);
  const [starting, setStarting] = useState(false);
  const [error, setError] = useState("");
  const catalog = useAsync(() => getRepositoryCatalog({ leaf: activeLeaf, q, scenario, license, favorites: favorites ? "1" : "", limit: String(PAGE_SIZE), offset: String((page - 1) * PAGE_SIZE), sort }),
    [activeLeaf, q, scenario, license, favorites, page, sort, revision]);
  useEffect(() => setQuery(q), [q]);
  useEffect(() => setSelectedLeaf(activeLeaf), [activeLeaf]);
  useEffect(() => setRun(null), [activeLeaf]);
  useEffect(() => setFavoritesChecked(favorites), [favorites]);
  useEffect(() => setSelectedLicense(license), [license]);
  useEffect(() => {
    if (catalog.data?.latest_run?.status === "running") setRun(catalog.data.latest_run);
  }, [catalog.data?.latest_run]);
  const activeId = run?.status === "running" ? run.id : null;
  useEffect(() => {
    if (!activeId) return;
    let alive = true;
    let timer: ReturnType<typeof setTimeout>;
    const poll = async () => {
      try {
        const result = await getCatalogRun(activeId);
        if (!alive) return;
        setRun(result);
        setError("");
        if (result.status === "running") timer = setTimeout(poll, 1500);
        else setRevision(value => value + 1);
      } catch (cause) {
        if (alive) { setError(String(cause)); timer = setTimeout(poll, 5000); }
      }
    };
    void poll();
    return () => { alive = false; clearTimeout(timer); };
  }, [activeId]);

  function filter(key: string, value: string) {
    const next = new URLSearchParams(params);
    if (value) next.set(key, value); else next.delete(key);
    if (key === "leaf") { next.delete("scenario"); setRun(null); }
    if (key !== "page") next.delete("page");
    setParams(next);
  }
  async function refresh() {
    setStarting(true); setError("");
    try { setRun(await refreshRepositoryCatalog(activeLeaf)); }
    catch (cause) { setError(String(cause)); }
    finally { setStarting(false); }
  }
  const data = catalog.data;
  const total = data?.pagination?.total ?? data?.projects.length ?? 0;
  const projects = data?.pagination ? data.projects : data?.projects.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE) || [];
  const scenarios = data?.scenarios || [];
  const visibleScenarios = showAllScenarios ? scenarios : scenarios.filter((item, i) => i < (activeLeaf ? 6 : 3) || item.id === scenario);
  const hasFilters = !!(q || scenario || favorites || license);
  function clearFilters() {
    const next = new URLSearchParams(params);
    for (const key of ["q", "scenario", "favorites", "license", "page"]) next.delete(key);
    setQuery(""); setParams(next);
  }
  const shownRun = run || data?.latest_run;
  return <section className="mt-6" aria-label={zh ? "场景与开源项目" : "Scenarios and repositories"}>
    <div className="flex flex-wrap items-start justify-between gap-4">
      {showHeading && <div>
        <h2 className="font-serif text-2xl font-medium">{zh ? "场景与开源项目" : "Scenarios and open-source projects"}</h2>
        <p className="mt-2 max-w-2xl text-sm leading-6 text-muted">{zh ? "从想完成的事情出发，发现真实项目。介绍依据官方仓库资料，保留来源与核验时间。" : "Start with what you want to do. Explore real repositories with source-backed descriptions and verification dates."}</p>
      </div>}
      {data?.supported_leaves.some(item => item.slug === activeLeaf) && <Button variant="outline" onClick={() => void refresh()} disabled={starting || !!activeId}>
        <RefreshCw className={`size-4 ${starting || activeId ? "animate-spin" : ""}`} />
        {starting || activeId ? (zh ? "更新中…" : "Updating…") : (zh ? "更新项目资料" : "Refresh repositories")}
      </Button>}
    </div>
    {data?.supported_leaves.some(item => item.slug === activeLeaf && item.mode === "automatic") && <p className="mt-3 text-xs leading-5 text-muted">{zh ? "自动发现：场景来自现有分类，项目来自真实搜索；资料不全先收录，合理推断标注待核实。" : "Live discovery from the existing taxonomy. Partial information is saved and inferences are labeled."}</p>}
    {shownRun && <div role="status" className="mt-4 rounded-lg border border-border bg-surface p-3 text-sm">
      {!activeLeaf && <p className="mb-1 text-xs text-muted">{data?.supported_leaves.find(item => item.slug === shownRun.leaf)?.name}</p>}
      {shownRun.status === "running"
        ? (zh ? `${({ scenarios: "生成场景", search: "搜索真实项目", screen: "筛选候选", read_sources: "读取仓库资料", extract: "提取项目介绍", store: "保存资料" } as Record<string, string>)[shownRun.phase || ""] || "核验仓库资料"}：${shownRun.processed}/${shownRun.total || "…"}` : `Checking repositories (${shownRun.phase || "refresh"}): ${shownRun.processed}/${shownRun.total || "…"}`)
        : (zh ? `${({ completed: "更新完成", partial: "部分更新完成", failed: "更新失败", interrupted: "上次更新已中断", paused_model: "模型服务不可用，已暂停" })[shownRun.status]}：新增 ${shownRun.created}，更新 ${shownRun.updated}，未变 ${shownRun.unchanged}，失败 ${shownRun.failed}。`
          : `Refresh ${shownRun.status}: ${shownRun.created} new, ${shownRun.updated} updated, ${shownRun.unchanged} unchanged, ${shownRun.failed} failed.`)}
      {shownRun.errors.length > 0 && <><p className="mt-1 text-xs text-muted">{zh ? "未能更新的项目保留上次成功资料与核验时间。" : "Failed updates retain the last successful data and verification date."}</p><ul className="mt-2 space-y-1 text-xs text-danger">{shownRun.errors.map((item, index) => <li key={index}>{item.repo}: {item.error}</li>)}</ul></>}
      {shownRun.mode === "automatic" && <p className="mt-1 text-xs text-muted">{zh ? `实际搜索发现 ${shownRun.discovered ?? 0} 个去重候选 · 本批读取 ${shownRun.total ?? 0} 个 · 新读官方文档 ${shownRun.document_fetches ?? 0} 份` : `${shownRun.discovered ?? 0} search candidates · ${shownRun.total ?? 0} in this batch · ${shownRun.document_fetches ?? 0} documentation files fetched`}</p>}
    </div>}
    {error && <p role="alert" className="mt-3 text-sm text-danger">{error}</p>}
    <form role="search" className="mt-6 flex flex-wrap items-end gap-3" onSubmit={event => { event.preventDefault(); filter("q", query.trim()); }}>
      {!leaf && <label className="min-w-0 w-full text-xs text-muted sm:w-auto sm:max-w-64">{zh ? "软件类型" : "Type"}<select value={selectedLeaf} onChange={e => { setSelectedLeaf(e.target.value); filter("leaf", e.target.value); }} className="mt-1 block h-11 max-w-full rounded-lg border border-border bg-surface px-3 text-sm text-fg"><option value="">{zh ? "全部类型" : "All types"}</option>{data?.supported_leaves.map(item => <option key={item.slug} value={item.slug}>{item.name}</option>)}</select></label>}
      <label className="min-w-0 basis-48 flex-1 text-xs text-muted">{zh ? "搜索项目、功能或场景" : "Search projects, features or scenarios"}
        <input className="mt-1 block h-11 w-full rounded-lg border border-border bg-surface px-3 text-sm text-fg" value={query} onChange={e => setQuery(e.target.value)} placeholder={zh ? "例如：双向链接、Markdown、Foam" : "e.g. Markdown, Foam"} />
      </label>
      <Button type="submit"><Search className="size-4" />{zh ? "搜索项目" : "Search projects"}</Button>
      <label className="text-xs text-muted">{zh ? "许可证" : "License"}<select value={selectedLicense} onChange={e => { setSelectedLicense(e.target.value); filter("license", e.target.value); }} className="mt-1 block h-11 rounded-lg border border-border bg-surface px-3 text-sm text-fg">
        <option value="">{zh ? "全部许可状态" : "All license statuses"}</option>
        {Object.entries(licenseLabels).map(([key, labels]) => <option key={key} value={key}>{labels[zh ? 0 : 1]}</option>)}
      </select></label>
      <label className="flex h-11 items-center gap-2 text-sm"><input type="checkbox" checked={favoritesChecked} onChange={e => { setFavoritesChecked(e.target.checked); filter("favorites", e.target.checked ? "1" : ""); }} />{zh ? "只看收藏" : "Favorites"}</label>
    </form>
    {data?.scenarios.length ? <div className="mt-5 flex flex-wrap gap-2" aria-label={zh ? "场景筛选" : "Filter scenarios"}>
      <Button size="sm" variant={!scenario ? "default" : "outline"} aria-pressed={!scenario} onClick={() => filter("scenario", "")}>{zh ? "全部场景" : "All scenarios"}</Button>
      {visibleScenarios.map(item => <Button key={item.id} size="sm" className="h-auto min-h-9 max-w-full whitespace-normal py-2 text-left" variant={scenario === item.id ? "default" : "outline"} aria-pressed={scenario === item.id} onClick={() => filter("scenario", item.id)}>{!activeLeaf && item.leaf_name ? `${item.leaf_name} / ` : ""}{item.name} · {item.project_count}</Button>)}
      {scenarios.length > (activeLeaf ? 6 : 3) && <Button size="sm" variant="ghost" onClick={() => setShowAllScenarios(v => !v)} aria-expanded={showAllScenarios}>{showAllScenarios ? (zh ? "收起场景" : "Fewer scenarios") : (zh ? `查看全部 ${scenarios.length} 个场景` : `All ${scenarios.length} scenarios`)}</Button>}
    </div> : null}
    {scenario && data && !data.scenarios.some(item => item.id === scenario) && <Button className="mt-4" variant="outline" onClick={() => filter("scenario", "")}>{zh ? "清除无效场景筛选" : "Clear invalid scenario"}</Button>}
    {data?.scenarios.filter(item => item.id === scenario).map(item => <p className="mt-4 text-sm leading-6 text-muted" key={item.id}>{item.description}</p>)}
    <div ref={results} className="mt-5 flex scroll-mt-32 flex-wrap items-center justify-between gap-3 border-t border-border pt-4">
      <p role="status" className="text-xs text-muted">{catalog.loading ? (zh ? "正在读取项目…" : "Loading projects…") : (zh ? `${total} 个项目 · 一个项目可适用于多个场景` : `${total} projects · each project may serve multiple scenarios`)}</p>
      <div className="flex items-center gap-3">
        <a className="min-h-9 content-center text-xs text-primary underline underline-offset-4" href="#collection-tools">{zh ? "管理资料采集" : "Collection tools"}</a>
        {hasFilters && <button type="button" className="min-h-9 text-xs text-primary underline underline-offset-4" onClick={clearFilters}>{zh ? "清除筛选" : "Clear filters"}</button>}
        <label className="flex items-center gap-2 text-xs text-muted">{zh ? "排序" : "Sort"}<select className="h-9 rounded-lg border border-border bg-surface px-2 text-fg" value={sort} onChange={e => filter("sort", e.target.value)}><option value="name">{zh ? "项目名称" : "Name"}</option><option value="recent">{zh ? "最近核验" : "Recently checked"}</option></select></label>
      </div>
    </div>
    {catalog.error ? <div role="alert" className="mt-6 rounded-xl border border-border bg-surface p-5 text-sm"><p>{zh ? "项目库暂时无法读取，请检查本地 API 服务后重试。" : "Repository catalog unavailable. Check the local API and retry."}</p><div className="mt-3 flex items-center gap-4"><Button variant="outline" onClick={() => setRevision(v => v + 1)}>{zh ? "重新读取" : "Retry"}</Button><Link className="text-primary underline" to="/guide#service">{zh ? "查看连接帮助" : "Connection help"}</Link></div></div>
      : catalog.loading && !data ? <p role="status" className="py-10 text-center text-sm text-muted">{zh ? "读取已保存的项目…" : "Loading saved projects…"}</p>
        : data && <div aria-busy={catalog.loading} className={catalog.loading ? "opacity-60 transition-opacity" : ""}>
          {projects.length ? <div className="mt-4 grid items-start gap-4 md:grid-cols-2">{projects.map(project => <RepositoryCard key={project.repository_id} project={project} scenarios={data.scenarios} onFavorite={() => setRevision(v => v + 1)} />)}</div>
            : <div className="mt-4 rounded-xl border border-dashed border-border bg-surface p-6 text-sm text-muted">
              <p>{hasFilters ? (zh ? "没有符合当前筛选的项目。可以调整关键词、场景或许可状态。" : "No projects match these filters.") : page > 1 ? (zh ? "这一页没有项目。" : "No projects on this page.") : (zh ? "这个类型还没有已整理的项目。" : "No curated projects for this leaf yet.")}</p>
              {hasFilters && <Button variant="outline" className="mt-4" onClick={clearFilters}>{zh ? "重置筛选" : "Reset filters"}</Button>}
              {page > 1 && <Button variant="outline" className="mt-4" onClick={() => filter("page", "1")}>{zh ? "返回第一页" : "First page"}</Button>}
              {leaf && leaf !== PKM_LEAF && <Link className="mt-3 block text-primary underline" to={`/types/${PKM_LEAF}`}>{zh ? "查看个人知识管理应用试点" : "Explore the personal knowledge pilot"}</Link>}
            </div>}
          {(total > PAGE_SIZE || page > 1) && <nav aria-label={zh ? "项目分页" : "Project pages"} className="mt-6 flex flex-wrap items-center justify-between gap-3 rounded-xl border border-border bg-surface p-4">
            <p className="text-xs tabular-nums text-muted">{zh ? `第 ${page} / ${Math.max(1, Math.ceil(total / PAGE_SIZE))} 页 · 每页最多 ${PAGE_SIZE} 个项目` : `Page ${page} / ${Math.max(1, Math.ceil(total / PAGE_SIZE))} · Up to ${PAGE_SIZE} projects per page`}</p>
            <div className="flex gap-2"><Button size="sm" variant="outline" disabled={page <= 1 || catalog.loading} onClick={() => filter("page", String(page - 1))}>{zh ? "上一页" : "Previous"}</Button><Button size="sm" variant="outline" disabled={page * PAGE_SIZE >= total || catalog.loading} onClick={() => filter("page", String(page + 1))}>{zh ? "下一页" : "Next"}</Button></div>
          </nav>}
        </div>}
    {data && <div id="collection-tools" className="mt-10 border-t border-border pt-6">
      <h2 className="font-serif text-xl font-medium">{zh ? "资料更新与采集" : "Collection and updates"}</h2>
      <p className="mt-2 text-xs leading-6 text-muted">{zh ? "需要补充更多项目时，可以在这里选择类型并启动批量任务。" : "Choose types and start a batch here when you want to collect more projects."}</p>
      <RepositoryBatch leaves={data.supported_leaves} activeLeaf={activeLeaf} onUpdate={() => setRevision(value => value + 1)} />
    {!!data?.discovery?.total && <details className="mt-4 rounded-lg border border-border bg-surface p-3" aria-label={zh ? "候选读取队列" : "Candidate reading queue"}>
      <summary className="cursor-pointer text-sm font-medium">{zh ? `候选池 · ${data.discovery.total} 个 · 待读 ${data.discovery.counts.pending || 0} · 待补依据 ${data.discovery.counts.needs_evidence || 0}` : `Candidates · ${data.discovery.total} · Pending ${data.discovery.counts.pending || 0} · More evidence needed ${data.discovery.counts.needs_evidence || 0}`}</summary>
      <p className="mt-2 text-xs leading-5 text-muted">{zh ? "搜到的候选先保存，批量任务会自动续批。资料不足先生成初步卡片，未建立场景关联的项目仍可浏览。排除和失败均保留原因。" : "Batch jobs automatically continue the saved queue. Partial cards remain browsable, with exclusion and failure reasons retained."}</p>
      <ul className="mt-3 max-h-80 space-y-3 overflow-y-auto">{data.discovery.items.map(item => <li key={`${item.leaf}-${item.repository_id}`} className="text-xs leading-5">
        <SourceLink url={item.github_url}>{item.full_name}</SourceLink><span className="ml-2 text-subtle">{zh ? ({ pending: "等待读取", accepted: "已生成卡片", partial: "已收录 · 资料待补充", rejected: "已排除 · 保留记录", needs_evidence: "待补依据", failed: "采集待重试" } as Record<string, string>)[item.status] || item.status : item.status}</span>
        <p className="text-muted">{item.reason}</p>
      </li>)}</ul>
    </details>}
    </div>}

  </section>;
}

export function RepositoryCard({ project, scenarios = [], onFavorite }: {
  project: RepositoryProject; scenarios?: { id: string; name: string }[]; onFavorite?: () => void;
}) {
  const { lang } = useLang(); const zh = lang === "zh";
  const [favorite, setFavorite] = useState(project.favorite);
  const [saving, setSaving] = useState(false);
  const [expanded, setExpanded] = useState(false);
  const [error, setError] = useState("");
  useEffect(() => setFavorite(project.favorite), [project.favorite]);
  async function toggle() {
    setSaving(true); setError("");
    try { await favoriteRepository(project.repository_id, !favorite); setFavorite(!favorite); onFavorite?.(); }
    catch (cause) { setError(String(cause)); }
    finally { setSaving(false); }
  }
  const license = project.license;
  return <article className="min-w-0 rounded-xl border border-border bg-surface p-5" aria-label={project.name}>
    <div className="flex items-start justify-between gap-3">
      <div className="min-w-0"><h3 className="font-serif text-xl font-medium">{project.name}</h3><p className="mt-1 break-all font-mono text-[11px] text-subtle">{project.full_name}</p><p className="mt-2 text-xs leading-5 text-muted">{project.positioning}</p></div>
      <button aria-label={`${favorite ? (zh ? "取消收藏" : "Unfavorite") : (zh ? "收藏" : "Favorite")} ${project.name}`} aria-pressed={favorite} disabled={saving} className="flex size-11 shrink-0 items-center justify-center rounded-lg p-2 text-primary hover:bg-chip disabled:opacity-50" onClick={() => void toggle()}><Bookmark className={`size-5 ${favorite ? "fill-primary" : ""}`} /></button>
    </div>
    <p className="mt-3 text-sm leading-6 text-muted">{project.summary}</p>
    <div className="mt-3 flex flex-wrap gap-2 text-xs">
      <span className={`rounded-md px-2 py-1 ${license.status === "open_source" ? "bg-primary/10 text-primary" : "bg-warn/10 text-warn"}`}>{license.spdx || (zh ? "许可待核验" : "Unverified license")}</span>
      <span className="py-1 text-muted">{licenseLabels[license.status][zh ? 0 : 1]}</span>
      {project.generation_method === "live_search_and_grounded_extraction" && <span className="py-1 text-subtle">{zh ? "自动提取 · 原文依据已比对" : "Automatically extracted · quotes checked"}</span>}
      {project.completeness === "partial" && <span className="rounded bg-warn/10 px-2 py-1 text-warn">{zh ? "已收录 · 资料待补充" : "Saved · partial information"}</span>}
      {project.generation_method === "live_search_coverage_first" && <span className="py-1 text-subtle">{zh ? "官方资料整理 · 待复核" : "Official sources · review pending"}</span>}
      {project.project_type && <span className="py-1 text-subtle">{zh ? ({ application: "应用", library: "库 / SDK", collection: "项目集合", resource: "资源", unknown: "类型待确认" } as Record<string, string>)[project.project_type] || "类型待确认" : project.project_type}</span>}
      {project.archived && <span className="py-1 text-warn">{zh ? "仓库已归档" : "Archived repository"}</span>}
    </div>
    <ul className="mt-4 space-y-2 text-sm leading-6">{project.matches.map(match => <li key={match.scenario_id}><span className="font-medium">{scenarios.find(s => s.id === match.scenario_id)?.name || (zh ? "场景适用依据" : "Scenario fit")}</span>
      {match.applicability && <span className={`ml-2 inline-block rounded px-1.5 text-xs ${match.applicability !== "direct" ? "bg-warn/10 text-warn" : "bg-primary/10 text-primary"}`}>{match.applicability === "conditional" ? (zh ? "条件适用" : "Conditional fit") : match.applicability === "unverified" ? (zh ? "合理推断 · 待核实" : "Inference · unverified") : (zh ? "直接依据" : "Direct evidence")}</span>}
      <p className="text-muted">{match.reason}</p>
      {!!match.conditions?.length && <ul className="mt-1 list-disc pl-4 text-xs text-muted">{match.conditions.map(condition => <li key={condition}>{zh ? "适用条件：" : "Condition: "}{condition}</li>)}</ul>}
    </li>)}</ul>
    <details className="mt-4 border-t border-border pt-3" onToggle={e => setExpanded(e.currentTarget.open)}>
      <summary className="cursor-pointer text-sm font-medium text-primary">{zh ? "查看功能、适用范围与来源" : "Features, scope and sources"}</summary>
      {expanded && <div className="mt-4 space-y-4 text-sm leading-6">
        <div><h4 className="font-medium">{zh ? "核心功能" : "Features"}</h4>{project.features.length ? <ul className="mt-1 list-disc space-y-1 pl-4 text-muted">{project.features.map(fact => <li key={fact.text}>{fact.text}{fact.evidence.verification === "inferred" && <span className="ml-2 text-xs text-warn">{zh ? "推断 · 待核实" : "Inference · unverified"}</span>}</li>)}</ul> : <p className="mt-1 text-muted">{zh ? "功能说明待补充" : "Feature information pending"}</p>}</div>
        {!!project.missing_fields?.length && <p className="text-xs text-warn">{zh ? "待补充：" : "Missing: "}{project.missing_fields.map(field => (zh ? ({ positioning: "定位", summary: "介绍", scope: "适用范围", features: "功能", scenario_associations: "场景关联", license_verification: "许可证核验" } as Record<string, string>)[field] || field : field)).join("、")}</p>}
        {!!project.collection_notes?.length && <ul className="space-y-1 text-xs text-muted">{project.collection_notes.map((note, i) => <li key={i}>{note}</li>)}</ul>}
        <div><h4 className="font-medium">{zh ? "适用范围" : "Scope"}</h4><p className="mt-1 text-muted">{project.scope}</p></div>
        <div><h4 className="font-medium">{zh ? "技术信息" : "Technology"}</h4><p className="mt-1 text-muted">{project.languages.join(" · ") || (zh ? "未提供语言信息" : "Not available")}</p><p className="text-xs text-subtle">{zh ? "语言来自 GitHub 仓库元数据；具体运行环境请查看原项目。" : "Languages from GitHub repository metadata. See upstream for runtime requirements."}</p></div>
        <div><h4 className="font-medium">{zh ? "许可证核验" : "License verification"}</h4><p className="mt-1 text-muted">{license.note}</p>{license.source && <p className="mt-1 flex flex-wrap gap-x-3"><SourceLink url={license.source.url}>{zh ? "许可证原文" : "License file"}</SourceLink>{license.source.immutable_url && <SourceLink url={license.source.immutable_url}>{zh ? "核验版本" : "Verified blob"}</SourceLink>}</p>}</div>
        <div><h4 className="font-medium">{zh ? "资料来源" : "Sources"}</h4><ul className="mt-1 space-y-1">{project.sources.map(source => <li key={source.url}><SourceLink url={source.url}>{source.kind === "readme" ? `README · ${source.path}` : source.kind === "documentation" ? `${zh ? "官方文档" : "Official documentation"} · ${source.path}` : source.kind === "languages" ? (zh ? "语言统计" : "Language statistics") : (zh ? "仓库元数据" : "Repository metadata")}</SourceLink><span className="ml-2 text-xs text-subtle">{new Date(source.retrieved_at).toLocaleString(zh ? "zh-CN" : "en-US")}</span></li>)}</ul></div>
        <details><summary className="cursor-pointer text-xs text-muted">{zh ? "展开介绍与关联的原文依据" : "Show evidence excerpts"}</summary><div className="mt-2 space-y-3">
          {project.positioning_evidence && <EvidenceQuote label={zh ? "项目定位" : "Positioning"} evidence={project.positioning_evidence} />}
          <EvidenceQuote label={zh ? "项目介绍" : "Description"} evidence={project.summary_evidence} />
          <EvidenceQuote label={zh ? "适用范围" : "Scope"} evidence={project.scope_evidence} />
          {license.restriction_evidence && <EvidenceQuote label={zh ? "额外许可声明" : "Additional licensing terms"} evidence={license.restriction_evidence} />}
          {project.features.map(f => <EvidenceQuote key={f.text} label={f.text} evidence={f.evidence} />)}
          {project.matches.map(m => <EvidenceQuote key={m.scenario_id} label={m.reason} evidence={m.evidence} />)}
        </div></details>
        {project.quality_review && <p className="text-xs text-muted">{zh ? "资料复核：" : "Source review: "}{project.quality_review.reason}</p>}
        <p className="text-xs text-subtle">{project.editorial_method}</p>
      </div>}
    </details>
    {error && <p role="alert" className="mt-3 text-xs text-danger">{error}</p>}
    <div className="mt-5 flex flex-wrap items-center justify-between gap-2"><a href={project.github_url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1.5 text-sm font-medium text-primary hover:underline">{zh ? "查看 GitHub 项目" : "View on GitHub"}<ExternalLink className="size-3.5" /></a><span className="text-[11px] text-subtle">{zh ? "最近核验 " : "Last checked "}{new Date(project.checked_at).toLocaleDateString(zh ? "zh-CN" : "en-US")}</span></div>
  </article>;
}

function SourceLink({ url, children }: { url: string; children: React.ReactNode }) {
  return <a className="text-primary underline underline-offset-2" href={url} target="_blank" rel="noopener noreferrer">{children}</a>;
}
function EvidenceQuote({ label, evidence }: { label: string; evidence: Evidence }) {
  const { lang } = useLang();
  return <blockquote className="border-l-2 border-border pl-3 text-xs text-muted"><p className="font-medium">{label}</p><p className="mt-1 break-words">{evidence.excerpt || (evidence.verification === "inferred" ? (lang === "zh" ? "该条为推断，待核实；下方为参考资料。" : "Unverified inference; reference source below.") : (lang === "zh" ? "依据下方资料概述，未附逐字引文。" : "Summarized from the source below; no direct quote."))}</p><p className="mt-1"><SourceLink url={evidence.immutable_url || evidence.source_url}>GitHub · {evidence.source_sha256.slice(0, 12)}</SourceLink></p></blockquote>;
}
