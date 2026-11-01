import { useEffect, useMemo, useState, type FormEvent } from "react";
import { Link, useSearchParams } from "react-router-dom";
import { Search as SearchIcon } from "lucide-react";
import { getMeta } from "@/lib/atlas";
import { getRepositoryCatalog } from "@/lib/oss-catalog";
import { RepositoryCard } from "@/components/repository-catalog";
import { useAsync, Loading } from "@/components/loaders";
import { LeafCard } from "@/components/leaf-card";
import { Button } from "@/components/ui/button";
import { useLang, t } from "@/lib/lang";

export function Search() {
  const { lang } = useLang(); const zh = lang === "zh";
  const [params, setParams] = useSearchParams();
  const q = (params.get("q") ?? "").trim();
  const [query, setQuery] = useState(q);
  const [revision, setRevision] = useState(0);
  useEffect(() => setQuery(q), [q]);
  const meta = useAsync(getMeta, [revision]);
  const catalog = useAsync(() => q ? getRepositoryCatalog({ q, limit: "12" }) : Promise.resolve(null), [q, revision]);
  function submitSearch(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const next = query.trim();
    setParams(next ? { q: next } : {});
  }
  const types = useMemo(() => {
    const keyword = q.toLowerCase();
    if (!keyword || !meta.data) return [];
    return meta.data.leafIndex.map(leaf => {
      let score = 0;
      if (leaf.slug.toLowerCase().includes(keyword)) score += 6;
      if ((leaf.name_zh || "").toLowerCase().includes(keyword)) score += 5;
      if ((leaf.aliases_zh || []).some(alias => alias.toLowerCase().includes(keyword))) score += 4;
      if (leaf.name.toLowerCase().includes(keyword)) score += 4;
      if (leaf.dc.toLowerCase().includes(keyword)) score += 1;
      if ((leaf.dc_zh || "").toLowerCase().includes(keyword)) score += 1;
      return { ...leaf, l0: leaf.dc, l0_zh: leaf.dc_zh, score };
    }).filter(leaf => leaf.score > 0).sort((a, b) => b.score - a.score || a.name.localeCompare(b.name));
  }, [q, meta.data]);
  const projects = catalog.data?.projects.slice(0, 12) || [];
  const totalProjects = catalog.data?.pagination?.total ?? projects.length;
  const loading = meta.loading || (!!q && catalog.loading);
  const noResults = !!q && !loading && !catalog.error && !meta.error && !totalProjects && !types.length;
  return <main className="mx-auto max-w-5xl px-4 py-10">
    <p className="text-xs font-medium tracking-widest text-primary">{zh ? "从一个关键词开始" : "START WITH A KEYWORD"}</p>
    <h1 className="mt-3 font-serif text-3xl font-medium">{q ? t("searchTitle", lang, { q }) : (zh ? "搜索类型与项目" : "Search types and projects")}</h1>
    <form className="mt-6 flex flex-wrap items-end gap-2" onSubmit={submitSearch} role="search">
      <label className="min-w-0 basis-60 flex-1 text-sm"><span className="text-muted">{t("searchLabel", lang)}</span><input maxLength={200} value={query} onChange={e => setQuery(e.target.value)} placeholder={t("searchPlaceholder", lang)} className="mt-2 h-12 w-full rounded-xl border border-border bg-surface px-4 outline-none focus:ring-2 focus:ring-primary/35" /></label>
      <Button className="h-12" type="submit"><SearchIcon className="size-4" />{t("searchBtn", lang)}</Button>
      {q && <Button className="h-12" type="button" variant="outline" onClick={() => { setQuery(""); setParams({}); }}>{zh ? "清空" : "Clear"}</Button>}
    </form>
    {q && <p role="status" className="mt-4 text-sm text-muted">{loading ? (zh ? "正在搜索，分类与项目结果会分别显示…" : "Searching types and repositories…") : (zh ? `${totalProjects} 个项目 · ${types.length} 个软件类型` : `${totalProjects} repositories · ${types.length} software types`)}</p>}
    {(catalog.error || meta.error) && <div role="alert" className="mt-5 flex flex-wrap items-center justify-between gap-3 rounded-xl border border-warn/20 bg-warn/5 p-4 text-sm text-warn"><p>{catalog.error ? (zh ? "项目库暂不可用，分类结果仍可浏览。" : "Repositories are unavailable; taxonomy results remain accessible.") : (zh ? "分类资料暂不可用，项目结果仍可浏览。" : "Taxonomy is unavailable; repositories remain accessible.")}</p><Button size="sm" variant="outline" onClick={() => setRevision(v => v + 1)}>{zh ? "重试搜索" : "Retry search"}</Button></div>}
    {q && !catalog.error && !noResults && <section className="mt-8" aria-label={zh ? "项目搜索结果" : "Repository results"}>
      <div className="flex flex-wrap items-baseline justify-between gap-3"><h2 className="font-serif text-xl font-medium">{zh ? "项目" : "Projects"}{!catalog.loading && <span className="ml-2 font-sans text-xs text-subtle">{totalProjects}</span>}</h2><Link className="text-sm text-primary hover:underline" to={`/discover?q=${encodeURIComponent(q)}`}>{zh ? "查看全部与筛选" : "View all and filter"} →</Link></div>
      {catalog.loading ? <Loading>{zh ? "搜索项目中…" : "Searching repositories…"}</Loading> : projects.length ? <div className="mt-4 grid items-start gap-4 sm:grid-cols-2">{projects.map(project => <RepositoryCard key={project.repository_id} project={project} scenarios={catalog.data?.scenarios} />)}</div> : <p className="mt-4 text-sm text-muted">{zh ? "项目库中还没有匹配结果，试试更短的关键词。" : "No matching repositories yet. Try a shorter keyword."}</p>}
      {!catalog.loading && totalProjects > projects.length && <Link className="mt-5 inline-block text-sm text-primary underline" to={`/discover?q=${encodeURIComponent(q)}`}>{zh ? `查看全部 ${totalProjects} 个项目` : `View all ${totalProjects} projects`} →</Link>}
    </section>}
    {q && !noResults && <section className="mt-8"><h2 className="font-serif text-xl font-medium">{zh ? "软件类型" : "Software types"}<span className="ml-2 font-sans text-xs text-subtle">{meta.loading ? "…" : types.length}</span></h2>{meta.loading ? <Loading /> : types.length ? <div className="mt-4 grid gap-4 sm:grid-cols-2">{types.slice(0, 100).map(leaf => <LeafCard key={leaf.slug} leaf={leaf} />)}</div> : !meta.error && <p className="mt-4 text-sm text-muted">{zh ? "没有匹配的软件类型，可以尝试名称、别名或用途。" : "No matching software types. Try a name, alias or purpose."}</p>}{types.length > 100 && <p className="mt-4 text-xs text-muted">{zh ? "当前显示前 100 个类型，请缩小关键词范围。" : "Showing the first 100 types. Narrow your query."}</p>}</section>}
    {noResults && <div role="status" className="mt-8 rounded-xl border border-dashed border-border bg-surface p-6 text-sm text-muted"><p>{zh ? "没有匹配的类型、场景或项目。试试更短的关键词，或浏览已有分类。" : "No matching types, scenarios or projects. Try a shorter keyword or browse the taxonomy."}</p><Link className="mt-4 inline-block text-primary underline" to="/browse">{zh ? "浏览已有分类" : "Browse the taxonomy"} →</Link></div>}
    {!q && <div className="mt-8 rounded-2xl border border-border bg-surface p-6 md:p-8"><h2 className="font-serif text-xl font-medium">{zh ? "你想完成什么？" : "What would you like to do?"}</h2><p className="mt-3 text-sm leading-7 text-muted">{zh ? "用一个类型、功能或项目名称开始。也可以直接浏览分类，沿场景发现项目。" : "Start with a type, feature or project name, or browse the taxonomy to discover projects by scenario."}</p><div className="mt-5 flex flex-wrap gap-2">{["Markdown", "Foam", zh ? "知识管理" : "knowledge", zh ? "密码管理" : "password"].map(term => <button key={term} type="button" className="rounded-lg bg-chip px-3 py-2 text-sm hover:bg-border" onClick={() => setParams({ q: term })}>{term}</button>)}</div><div className="mt-6 flex flex-wrap gap-5 text-sm"><Link className="text-primary underline underline-offset-4" to="/browse">{zh ? "浏览已有分类" : "Browse the taxonomy"}</Link><Link className="text-primary underline underline-offset-4" to="/discover">{zh ? "发现场景与项目" : "Discover projects"}</Link></div></div>}
  </main>;
}
