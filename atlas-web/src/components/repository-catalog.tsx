import { useEffect, useMemo, useRef, useState } from "react";
import { Link, useNavigationType, useSearchParams } from "react-router-dom";
import { ArrowRight, Bookmark, ExternalLink, RefreshCw, Search, Star } from "lucide-react";
import { useAsync } from "@/components/loaders";
import { Button } from "@/components/ui/button";
import { useLang } from "@/lib/lang";
import { getMeta } from "@/lib/atlas";
import { RepositoryBatch } from "@/components/repository-batch";
import {
  favoriteRepository, getCatalogRun, getRepositoryCatalog, PKM_LEAF, refreshRepositoryCatalog,
  type CatalogRun, type CatalogScenario, type Evidence, type LicenseStatus, type RepositoryProject,
} from "@/lib/oss-catalog";

const PAGE_SIZE = 24;
const SORTS = ["recommended", "name", "recent"] as const;
type Sort = typeof SORTS[number];

export const licenseLabels: Record<LicenseStatus, [string, string]> = {
  open_source: ["已核验开源许可证", "Verified open-source license"],
  source_available: ["源码可见 · 使用有限制", "Source available · restrictions apply"],
  pending: ["许可证待核验", "License review pending"],
};
const projectTypeLabels: Record<string, [string, string]> = {
  application: ["应用", "Application"], library: ["库 / SDK", "Library / SDK"], collection: ["项目集合", "Collection"],
  resource: ["资源", "Resource"], unknown: ["类型待确认", "Type unconfirmed"],
};

/** Taxonomy names by slug, in the reader's language when a translation exists. */
export function useLeafNames() {
  const { lang } = useLang();
  const meta = useAsync(getMeta, []);
  return useMemo(() => {
    const names = new Map<string, string>();
    for (const leaf of meta.data?.leafIndex || []) names.set(leaf.slug, lang === "zh" ? leaf.name_zh || leaf.name : leaf.name);
    return (slug: string, fallback = slug) => names.get(slug) || fallback;
  }, [meta.data, lang]);
}

export function formatStars(stars: number) {
  return stars >= 1000 ? `${(stars / 1000).toFixed(stars >= 10_000 ? 0 : 1)}k` : String(stars);
}

export function RepositoryCatalog({ leaf = "", showHeading = true }: { leaf?: string; showHeading?: boolean }) {
  const { lang } = useLang();
  const zh = lang === "zh";
  const leafName = useLeafNames();
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
  const sortParam = params.get("sort") as Sort | null;
  const sort: Sort = sortParam && SORTS.includes(sortParam) ? sortParam : "recommended";
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
  const visibleScenarios = showAllScenarios ? scenarios : scenarios.filter((item, i) => i < 6 || item.id === scenario);
  const hasFilters = !!(q || scenario || favorites || license);
  const typeOptions = useMemo(() => (data?.supported_leaves || [])
    .filter(item => item.slug === activeLeaf || (item.project_count ?? 0) > 0)
    .map(item => ({ slug: item.slug, name: leafName(item.slug, item.name), count: item.project_count ?? 0 }))
    .sort((a, b) => a.name.localeCompare(b.name, zh ? "zh-CN" : "en")), [data?.supported_leaves, activeLeaf, leafName, zh]);
  function clearFilters() {
    const next = new URLSearchParams(params);
    for (const key of ["q", "scenario", "favorites", "license", "page"]) next.delete(key);
    setQuery(""); setParams(next);
  }
  const shownRun = run || (activeLeaf && data?.latest_run?.leaf === activeLeaf ? data.latest_run : null);
  const canRefresh = !!activeLeaf && !!data?.supported_leaves.some(item => item.slug === activeLeaf);
  return <section className="mt-6" aria-label={zh ? "场景与开源项目" : "Scenarios and repositories"}>
    {showHeading && <div>
      <h2 className="font-serif text-2xl font-medium">{zh ? "场景与开源项目" : "Scenarios and open-source projects"}</h2>
      <p className="mt-2 max-w-2xl text-sm leading-6 text-muted">{zh ? "从想完成的事情出发，发现真实项目。介绍依据官方仓库资料，保留来源与核验时间。" : "Start with what you want to do. Explore real repositories with source-backed descriptions and verification dates."}</p>
    </div>}
    {activeId && run && <p role="status" className="mt-4 flex items-center gap-2 text-xs text-muted"><RefreshCw className="size-3.5 animate-spin" />{zh ? `正在更新项目资料：${run.processed}/${run.total || "…"}` : `Updating repositories: ${run.processed}/${run.total || "…"}`}</p>}
    <form role="search" className="mt-6 flex flex-wrap items-end gap-3" onSubmit={event => { event.preventDefault(); filter("q", query.trim()); }}>
      {!leaf && <label className="min-w-0 w-full text-xs text-muted sm:w-auto sm:max-w-64">{zh ? "软件类型" : "Type"}<select value={selectedLeaf} onChange={e => { setSelectedLeaf(e.target.value); filter("leaf", e.target.value); }} className="mt-1 block h-11 w-full max-w-full rounded-lg border border-border bg-surface px-3 text-sm text-fg"><option value="">{zh ? "全部类型" : "All types"}</option>{typeOptions.map(item => <option key={item.slug} value={item.slug}>{item.name} · {item.count}</option>)}</select></label>}
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
    {activeLeaf && scenarios.length ? <div className="mt-5 flex flex-wrap gap-2" aria-label={zh ? "场景筛选" : "Filter scenarios"}>
      <Button size="sm" variant={!scenario ? "default" : "outline"} aria-pressed={!scenario} onClick={() => filter("scenario", "")}>{zh ? "全部场景" : "All scenarios"}</Button>
      {visibleScenarios.map(item => <Button key={item.id} size="sm" className="h-auto min-h-9 max-w-full whitespace-normal py-2 text-left" variant={scenario === item.id ? "default" : "outline"} aria-pressed={scenario === item.id} onClick={() => filter("scenario", item.id)}>{item.name} · {item.project_count}</Button>)}
      {scenarios.length > 6 && <Button size="sm" variant="ghost" onClick={() => setShowAllScenarios(v => !v)} aria-expanded={showAllScenarios}>{showAllScenarios ? (zh ? "收起场景" : "Fewer scenarios") : (zh ? `查看全部 ${scenarios.length} 个场景` : `All ${scenarios.length} scenarios`)}</Button>}
    </div> : null}
    {scenario && data && !data.scenarios.some(item => item.id === scenario) && <Button className="mt-4" variant="outline" onClick={() => filter("scenario", "")}>{zh ? "清除无效场景筛选" : "Clear invalid scenario"}</Button>}
    {data?.scenarios.filter(item => item.id === scenario).map(item => <p className="mt-4 text-sm leading-6 text-muted" key={item.id}>{!activeLeaf && <span className="font-medium text-fg">{item.name}：</span>}{item.description}</p>)}
    <div ref={results} className="mt-5 flex scroll-mt-32 flex-wrap items-center justify-between gap-3 border-t border-border pt-4">
      <p role="status" className="text-xs text-muted">{catalog.loading ? (zh ? "正在读取项目…" : "Loading projects…") : (zh ? `${total} 个项目 · 一个项目可适用于多个场景` : `${total} projects · each project may serve multiple scenarios`)}</p>
      <div className="flex items-center gap-3">
        {hasFilters && <button type="button" className="min-h-9 text-xs text-primary underline underline-offset-4" onClick={clearFilters}>{zh ? "清除筛选" : "Clear filters"}</button>}
        <label className="flex items-center gap-2 text-xs text-muted">{zh ? "排序" : "Sort"}<select className="h-9 rounded-lg border border-border bg-surface px-2 text-fg" value={sort} onChange={e => filter("sort", e.target.value === "recommended" ? "" : e.target.value)}><option value="recommended">{zh ? "推荐" : "Recommended"}</option><option value="name">{zh ? "项目名称" : "Name"}</option><option value="recent">{zh ? "最近核验" : "Recently checked"}</option></select></label>
      </div>
    </div>
    {catalog.error ? <div role="alert" className="mt-6 rounded-xl border border-border bg-surface p-5 text-sm"><p>{zh ? "项目库暂时无法读取，请检查本地 API 服务后重试。" : "Repository catalog unavailable. Check the local API and retry."}</p><div className="mt-3 flex items-center gap-4"><Button variant="outline" onClick={() => setRevision(v => v + 1)}>{zh ? "重新读取" : "Retry"}</Button><Link className="text-primary underline" to="/guide#service">{zh ? "查看连接帮助" : "Connection help"}</Link></div></div>
      : catalog.loading && !data ? <p role="status" className="py-10 text-center text-sm text-muted">{zh ? "读取已保存的项目…" : "Loading saved projects…"}</p>
        : data && <div aria-busy={catalog.loading} className={catalog.loading ? "opacity-60 transition-opacity" : ""}>
          {projects.length ? <div className="mt-4 grid gap-4 md:grid-cols-2">{projects.map(project => <RepositoryCard key={project.repository_id} project={project} scenarios={data.scenarios} onFavorite={() => setRevision(v => v + 1)} />)}</div>
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
    {data && <div id="collection-tools" className="mt-12 border-t border-border pt-6">
      <h2 className="font-serif text-xl font-medium">{zh ? "资料更新与采集" : "Collection and updates"}</h2>
      <p className="mt-2 text-xs leading-6 text-muted">{zh ? "需要补充更多项目时，可以在这里更新当前类型，或选择类型启动批量任务。自动发现：场景来自现有分类，项目来自真实搜索；资料不全先收录，合理推断标注待核实。" : "Refresh this type or start a batch when you want more projects. Scenarios come from the taxonomy and projects from live search; partial information is saved and inferences are labeled."}</p>
      {canRefresh && <Button className="mt-3" variant="outline" onClick={() => void refresh()} disabled={starting || !!activeId}>
        <RefreshCw className={`size-4 ${starting || activeId ? "animate-spin" : ""}`} />
        {starting || activeId ? (zh ? "更新中…" : "Updating…") : (zh ? "更新项目资料" : "Refresh repositories")}
      </Button>}
      {shownRun && <RunStatus run={shownRun} />}
      {error && <p role="alert" className="mt-3 text-sm text-danger">{error}</p>}
      <RepositoryBatch leaves={data.supported_leaves} activeLeaf={activeLeaf} onUpdate={() => setRevision(value => value + 1)} />
      {!!activeLeaf && !!data.discovery?.total && <details className="mt-4 rounded-lg border border-border bg-surface p-3" aria-label={zh ? "候选读取队列" : "Candidate reading queue"}>
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

function RunStatus({ run }: { run: CatalogRun }) {
  const { lang } = useLang(); const zh = lang === "zh";
  return <div role="status" className="mt-4 rounded-lg border border-border bg-surface p-3 text-sm">
    {run.status === "running"
      ? (zh ? `${({ scenarios: "生成场景", search: "搜索真实项目", screen: "筛选候选", read_sources: "读取仓库资料", extract: "提取项目介绍", store: "保存资料" } as Record<string, string>)[run.phase || ""] || "核验仓库资料"}：${run.processed}/${run.total || "…"}` : `Checking repositories (${run.phase || "refresh"}): ${run.processed}/${run.total || "…"}`)
      : (zh ? `${({ completed: "更新完成", partial: "部分更新完成", failed: "更新失败", interrupted: "上次更新已中断", paused_model: "模型服务不可用，已暂停" })[run.status]}：新增 ${run.created}，更新 ${run.updated}，未变 ${run.unchanged}，失败 ${run.failed}。`
        : `Refresh ${run.status}: ${run.created} new, ${run.updated} updated, ${run.unchanged} unchanged, ${run.failed} failed.`)}
    {run.errors.length > 0 && <><p className="mt-1 text-xs text-muted">{zh ? "未能更新的项目保留上次成功资料与核验时间。" : "Failed updates retain the last successful data and verification date."}</p><ul className="mt-2 space-y-1 text-xs text-danger">{run.errors.map((item, index) => <li key={index}>{item.repo}: {item.error}</li>)}</ul></>}
    {run.mode === "automatic" && <p className="mt-1 text-xs text-muted">{zh ? `实际搜索发现 ${run.discovered ?? 0} 个去重候选 · 本批读取 ${run.total ?? 0} 个 · 新读官方文档 ${run.document_fetches ?? 0} 份` : `${run.discovered ?? 0} search candidates · ${run.total ?? 0} in this batch · ${run.document_fetches ?? 0} documentation files fetched`}</p>}
  </div>;
}

export function useFavorite(project: RepositoryProject, onFavorite?: () => void) {
  const [favorite, setFavorite] = useState(project.favorite);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");
  useEffect(() => setFavorite(project.favorite), [project.favorite]);
  async function toggle() {
    setSaving(true); setError("");
    try { await favoriteRepository(project.repository_id, !favorite); setFavorite(!favorite); onFavorite?.(); }
    catch (cause) { setError(String(cause)); }
    finally { setSaving(false); }
  }
  return { favorite, saving, error, toggle };
}

export function FavoriteButton({ project, state }: { project: RepositoryProject; state: ReturnType<typeof useFavorite> }) {
  const { lang } = useLang(); const zh = lang === "zh";
  return <button aria-label={`${state.favorite ? (zh ? "取消收藏" : "Unfavorite") : (zh ? "收藏" : "Favorite")} ${project.name}`} aria-pressed={state.favorite} disabled={state.saving} className="flex size-11 shrink-0 items-center justify-center rounded-lg p-2 text-primary hover:bg-chip disabled:opacity-50" onClick={() => void state.toggle()}><Bookmark className={`size-5 ${state.favorite ? "fill-primary" : ""}`} /></button>;
}

/** Facts shown on both the compact card and the detail page header. */
export function RepositoryFacts({ project }: { project: RepositoryProject }) {
  const { lang } = useLang(); const zh = lang === "zh";
  const license = project.license;
  return <div className="flex flex-wrap items-center gap-2 text-xs">
    {typeof project.stars === "number" && <span className="inline-flex items-center gap-1 py-1 tabular-nums text-muted" title={zh ? "收录时的 GitHub Stars" : "GitHub stars at collection time"}><Star className="size-3.5" aria-hidden="true" />{formatStars(project.stars)}<span className="sr-only">{zh ? "收录时 Stars" : "stars at collection"}</span></span>}
    <span className={`rounded-md px-2 py-1 ${license.status === "open_source" ? "bg-primary/10 text-primary" : "bg-warn/10 text-warn"}`} title={licenseLabels[license.status][zh ? 0 : 1]}>{license.spdx || (license.status === "source_available" ? (zh ? "源码可见" : "Source available") : (zh ? "许可待核验" : "Unverified license"))}</span>
    {project.project_type && <span className="py-1 text-subtle">{(projectTypeLabels[project.project_type] || projectTypeLabels.unknown)[zh ? 0 : 1]}</span>}
    {project.languages[0] && <span className="py-1 text-subtle">{project.languages[0]}</span>}
    {project.completeness === "partial" && <span className="rounded bg-warn/10 px-2 py-1 text-warn">{zh ? "资料待补充" : "Partial information"}</span>}
    {project.archived && <span className="py-1 text-warn">{zh ? "仓库已归档" : "Archived repository"}</span>}
  </div>;
}

export function RepositoryCard({ project, scenarios = [], onFavorite }: {
  project: RepositoryProject; scenarios?: { id: string; name: string }[]; onFavorite?: () => void;
}) {
  const { lang } = useLang(); const zh = lang === "zh";
  const state = useFavorite(project, onFavorite);
  const href = `/repos/${project.repository_id}`;
  const named = project.matches.map(match => scenarios.find(s => s.id === match.scenario_id)?.name).filter((name): name is string => !!name);
  return <article className="flex min-w-0 flex-col rounded-xl border border-border bg-surface p-5" aria-label={project.name}>
    <div className="flex items-start justify-between gap-3">
      <div className="min-w-0"><h3 className="font-serif text-xl font-medium"><Link to={href} className="hover:text-primary hover:underline">{project.name}</Link></h3><p className="mt-1 break-all font-mono text-[11px] text-subtle">{project.full_name}</p></div>
      <FavoriteButton project={project} state={state} />
    </div>
    {project.positioning && <p className="mt-2 text-sm font-medium leading-6">{project.positioning}</p>}
    <p className="mt-2 line-clamp-3 text-sm leading-6 text-muted">{project.summary}</p>
    <div className="mt-3"><RepositoryFacts project={project} /></div>
    {named.length > 0 && <ul className="mt-3 flex flex-wrap gap-1.5" aria-label={zh ? "适用场景" : "Scenarios"}>{named.slice(0, 3).map(name => <li key={name} className="rounded-full bg-chip px-2.5 py-1 text-xs text-muted">{name}</li>)}{named.length > 3 && <li className="px-1 py-1 text-xs text-subtle">+{named.length - 3}</li>}</ul>}
    {state.error && <p role="alert" className="mt-3 text-xs text-danger">{state.error}</p>}
    <div className="mt-auto flex flex-wrap items-center justify-between gap-2 pt-5">
      <div className="flex flex-wrap items-center gap-4">
        <Link to={href} className="inline-flex items-center gap-1 text-sm font-medium text-primary hover:underline">{zh ? "查看详情" : "Details"}<ArrowRight className="size-3.5" /></Link>
        <a href={project.github_url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1.5 text-sm text-muted hover:text-primary hover:underline">GitHub<ExternalLink className="size-3.5" /></a>
      </div>
      <span className="text-[11px] text-subtle">{zh ? "最近核验 " : "Last checked "}{new Date(project.checked_at).toLocaleDateString(zh ? "zh-CN" : "en-US")}</span>
    </div>
  </article>;
}

/** Every saved fact of one repository, with scenario fit, sources and evidence. */
export function RepositoryDetails({ project, scenarios }: { project: RepositoryProject; scenarios: CatalogScenario[] }) {
  const { lang } = useLang(); const zh = lang === "zh";
  const leafName = useLeafNames();
  const license = project.license;
  return <div className="space-y-8 text-sm leading-6">
    <section aria-labelledby="repo-scenarios">
      <h2 id="repo-scenarios" className="font-serif text-xl font-medium">{zh ? "适用场景" : "Scenarios"}</h2>
      {project.matches.length ? <ul className="mt-3 space-y-4">{project.matches.map(match => {
        const item = scenarios.find(s => s.id === match.scenario_id);
        return <li key={match.scenario_id} className="rounded-xl border border-border bg-surface p-4">
          {item?.leaf && <Link to={`/types/${item.leaf}?scenario=${encodeURIComponent(item.id)}`} className="text-xs text-primary hover:underline">{leafName(item.leaf, item.leaf_name)}</Link>}
          <p><span className="font-medium">{item?.name || (zh ? "场景适用依据" : "Scenario fit")}</span>
            {match.applicability && <span className={`ml-2 inline-block rounded px-1.5 text-xs ${match.applicability !== "direct" ? "bg-warn/10 text-warn" : "bg-primary/10 text-primary"}`}>{match.applicability === "conditional" ? (zh ? "条件适用" : "Conditional fit") : match.applicability === "unverified" ? (zh ? "合理推断 · 待核实" : "Inference · unverified") : (zh ? "直接依据" : "Direct evidence")}</span>}</p>
          <p className="mt-1 text-muted">{match.reason}</p>
          {!!match.conditions?.length && <ul className="mt-1 list-disc pl-4 text-xs text-muted">{match.conditions.map(condition => <li key={condition}>{zh ? "适用条件：" : "Condition: "}{condition}</li>)}</ul>}
        </li>;
      })}</ul> : <p className="mt-2 text-muted">{zh ? "尚未建立场景关联；仍可按类型浏览。" : "No scenario associations yet; still browsable by type."}</p>}
    </section>
    <section aria-labelledby="repo-features">
      <h2 id="repo-features" className="font-serif text-xl font-medium">{zh ? "核心功能" : "Features"}</h2>
      {project.features.length ? <ul className="mt-2 list-disc space-y-1 pl-4 text-muted">{project.features.map(fact => <li key={fact.text}>{fact.text}{fact.evidence.verification === "inferred" && <span className="ml-2 text-xs text-warn">{zh ? "推断 · 待核实" : "Inference · unverified"}</span>}</li>)}</ul> : <p className="mt-2 text-muted">{zh ? "功能说明待补充" : "Feature information pending"}</p>}
    </section>
    <section aria-labelledby="repo-scope">
      <h2 id="repo-scope" className="font-serif text-xl font-medium">{zh ? "适用范围" : "Scope"}</h2>
      <p className="mt-2 text-muted">{project.scope}</p>
      {!!project.missing_fields?.length && <p className="mt-2 text-xs text-warn">{zh ? "待补充：" : "Missing: "}{project.missing_fields.map(field => (zh ? ({ positioning: "定位", summary: "介绍", scope: "适用范围", features: "功能", scenario_associations: "场景关联", license_verification: "许可证核验" } as Record<string, string>)[field] || field : field)).join("、")}</p>}
      {!!project.collection_notes?.length && <ul className="mt-2 space-y-1 text-xs text-muted">{project.collection_notes.map((note, i) => <li key={i}>{note}</li>)}</ul>}
    </section>
    <section aria-labelledby="repo-license" className="grid gap-6 sm:grid-cols-2">
      <div><h2 id="repo-license" className="font-serif text-xl font-medium">{zh ? "许可证核验" : "License verification"}</h2><p className="mt-2 text-xs text-muted">{licenseLabels[license.status][zh ? 0 : 1]}{license.detected_spdx && license.detected_spdx !== "NOASSERTION" && license.detected_spdx !== license.spdx ? ` · ${zh ? "检测到" : "detected"} ${license.detected_spdx}` : ""}</p><p className="mt-1 text-muted">{license.note}</p>{license.source && <p className="mt-1 flex flex-wrap gap-x-3"><SourceLink url={license.source.url}>{zh ? "许可证原文" : "License file"}</SourceLink>{license.source.immutable_url && <SourceLink url={license.source.immutable_url}>{zh ? "核验版本" : "Verified blob"}</SourceLink>}</p>}</div>
      <div><h2 className="font-serif text-xl font-medium">{zh ? "技术信息" : "Technology"}</h2><p className="mt-2 text-muted">{project.languages.join(" · ") || (zh ? "未提供语言信息" : "Not available")}</p><p className="text-xs text-subtle">{zh ? "语言来自 GitHub 仓库元数据；具体运行环境请查看原项目。" : "Languages from GitHub repository metadata. See upstream for runtime requirements."}</p></div>
    </section>
    <section aria-labelledby="repo-sources">
      <h2 id="repo-sources" className="font-serif text-xl font-medium">{zh ? "资料来源" : "Sources"}</h2>
      <ul className="mt-2 space-y-1">{project.sources.map(source => <li key={source.url}><SourceLink url={source.url}>{source.kind === "readme" ? `README · ${source.path}` : source.kind === "documentation" ? `${zh ? "官方文档" : "Official documentation"} · ${source.path}` : source.kind === "languages" ? (zh ? "语言统计" : "Language statistics") : (zh ? "仓库元数据" : "Repository metadata")}</SourceLink><span className="ml-2 text-xs text-subtle">{new Date(source.retrieved_at).toLocaleString(zh ? "zh-CN" : "en-US")}</span></li>)}</ul>
      <details className="mt-3"><summary className="cursor-pointer text-xs text-muted">{zh ? "展开介绍与关联的原文依据" : "Show evidence excerpts"}</summary><div className="mt-2 space-y-3">
        {project.positioning_evidence && <EvidenceQuote label={zh ? "项目定位" : "Positioning"} evidence={project.positioning_evidence} />}
        <EvidenceQuote label={zh ? "项目介绍" : "Description"} evidence={project.summary_evidence} />
        <EvidenceQuote label={zh ? "适用范围" : "Scope"} evidence={project.scope_evidence} />
        {license.restriction_evidence && <EvidenceQuote label={zh ? "额外许可声明" : "Additional licensing terms"} evidence={license.restriction_evidence} />}
        {project.features.map(f => <EvidenceQuote key={f.text} label={f.text} evidence={f.evidence} />)}
        {project.matches.map(m => <EvidenceQuote key={m.scenario_id} label={m.reason} evidence={m.evidence} />)}
      </div></details>
      {project.quality_review && <p className="mt-3 text-xs text-muted">{zh ? "资料复核：" : "Source review: "}{project.quality_review.reason}</p>}
      <p className="mt-3 text-xs text-subtle">{project.editorial_method}</p>
    </section>
  </div>;
}

function SourceLink({ url, children }: { url: string; children: React.ReactNode }) {
  return <a className="text-primary underline underline-offset-2" href={url} target="_blank" rel="noopener noreferrer">{children}</a>;
}
function EvidenceQuote({ label, evidence }: { label: string; evidence: Evidence }) {
  const { lang } = useLang();
  return <blockquote className="border-l-2 border-border pl-3 text-xs text-muted"><p className="font-medium">{label}</p><p className="mt-1 break-words">{evidence.excerpt || (evidence.verification === "inferred" ? (lang === "zh" ? "该条为推断，待核实；下方为参考资料。" : "Unverified inference; reference source below.") : (lang === "zh" ? "依据下方资料概述，未附逐字引文。" : "Summarized from the source below; no direct quote."))}</p><p className="mt-1"><SourceLink url={evidence.immutable_url || evidence.source_url}>GitHub · {evidence.source_sha256.slice(0, 12)}</SourceLink></p></blockquote>;
}
