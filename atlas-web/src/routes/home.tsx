import { useNavigate, Link } from "react-router-dom";
import { ArrowRight, Bookmark, Compass, GitFork, Layers, Search } from "lucide-react";
import { useMemo, useState } from "react";
import { getMeta } from "@/lib/atlas";
import { getRepositoryCatalog, PKM_LEAF } from "@/lib/oss-catalog";
import { useAsync, Loading, ErrorBox, EmptyState } from "@/components/loaders";
import { Button } from "@/components/ui/button";
import { useLang, t, pick } from "@/lib/lang";

export function Home() {
  const navigate = useNavigate();
  const { lang } = useLang(); const zh = lang === "zh";
  const [q, setQ] = useState("");
  const { data: meta, error, loading } = useAsync(getMeta, []);
  const catalog = useAsync(() => getRepositoryCatalog({ view: "overview" }), []);
  const { stats, covered } = useMemo(() => {
    const data = catalog.data;
    if (!data) return { stats: undefined, covered: [] };
    // Keep the UI usable while an older local API is awaiting restart.
    const counts = new Map<string, number>();
    if (!data.stats) for (const project of data.projects) for (const leaf of project.leaves || []) counts.set(leaf, (counts.get(leaf) || 0) + 1);
    return {
      stats: data.stats || { projects: data.projects.length, scenarios: data.scenarios.length, leaves: counts.size, favorites: 0 },
      covered: data.supported_leaves.map(l => ({ ...l, project_count: l.project_count ?? counts.get(l.slug) ?? 0 })).filter(l => l.project_count > 0 && l.slug !== PKM_LEAF).sort((a, b) => b.project_count - a.project_count),
    };
  }, [catalog.data]);
  return <main>
    <section className="border-b border-border bg-[radial-gradient(ellipse_at_top_right,rgba(44,74,68,0.06),transparent_65%)]">
      <div className="mx-auto max-w-6xl px-4 py-12 md:py-20">
        <div className="grid items-center gap-10 lg:grid-cols-[1fr_260px] lg:gap-16">
          <div>
            <p className="text-xs font-medium uppercase tracking-widest text-primary">{zh ? "以场景为索引的开源项目知识库" : "OPEN SOURCE, INDEXED BY SCENARIO"}</p>
            <h1 className="mt-5 max-w-3xl font-serif text-4xl font-medium leading-[1.3] tracking-tight md:text-5xl">{zh ? "想做一件事，先看看已有的可能性" : "See what already exists for what you want to do"}</h1>
            <p className="mt-5 max-w-2xl text-sm leading-8 text-muted md:text-base">{zh ? "从软件类型出发，找到真实的使用场景与项目。了解它能做什么、适合什么，以及每条介绍的出处。" : "Start with a software type. Find real projects for your use case, understand their capabilities, and follow the sources."}</p>
            <form className="mt-7 max-w-2xl" role="search" onSubmit={e => { e.preventDefault(); navigate(q.trim() ? `/search?q=${encodeURIComponent(q.trim())}` : "/search"); }}>
              <label className="flex items-center gap-3 rounded-xl border border-border bg-surface px-4 shadow-card"><Search aria-hidden="true" className="size-5 shrink-0 text-subtle" /><span className="sr-only">{t("searchLabel", lang)}</span><input value={q} onChange={e => setQ(e.target.value)} placeholder={zh ? "搜索知识管理、双向链接、Markdown、Foam…" : "Search knowledge management, Markdown, Foam…"} className="h-14 min-w-0 w-full bg-transparent text-sm outline-none placeholder:text-subtle" /></label>
              <div className="mt-4 flex flex-wrap gap-3"><Button size="lg" type="submit">{zh ? "搜索类型与项目" : "Search types and projects"}<ArrowRight className="size-4" /></Button><Button asChild variant="outline" size="lg"><Link to="/browse">{zh ? "浏览已有分类" : "Browse the taxonomy"}</Link></Button></div>
            </form>
            <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-2 text-xs text-muted"><span>{zh ? "试试" : "Try"}</span>{["Markdown", zh ? "密码管理器" : "password", "Foam"].map(term => <Link key={term} className="underline decoration-border-strong underline-offset-4 hover:text-primary" to={`/search?q=${encodeURIComponent(term)}`}>{term}</Link>)}</div>
          </div>
          <aside className="hidden rounded-2xl border border-border bg-surface/70 p-6 lg:block">
            <p className="text-xs font-medium tracking-widest text-subtle">{zh ? "一条清晰的探索路径" : "YOUR PATH THROUGH ATLAS"}</p>
            {[{ icon: Layers, title: zh ? "软件类型" : "Software type", text: zh ? "理解定义与边界" : "Understand its boundaries" }, { icon: Compass, title: zh ? "使用场景" : "Your use case", text: zh ? "找到具体的用途" : "Find a concrete purpose" }, { icon: GitFork, title: zh ? "真实项目" : "Real projects", text: zh ? "带着依据做选择" : "Explore with evidence" }].map((step, i) => <div key={step.title} className="mt-6 flex gap-3"><div className="flex flex-col items-center"><step.icon className="size-5 text-primary" />{i < 2 && <span className="mt-3 h-6 w-px bg-border" />}</div><div><p className="text-sm font-medium">{step.title}</p><p className="mt-1 text-xs text-muted">{step.text}</p></div></div>)}
          </aside>
        </div>
      </div>
    </section>
    <section className="mx-auto max-w-6xl px-4 py-8 md:py-10">
      <div className="grid gap-3 sm:grid-cols-3">{[
        { icon: Layers, value: meta?.leafCount, label: zh ? "已有软件类型" : "Software types", to: "/browse" },
        { icon: Compass, value: stats?.scenarios, label: zh ? "已整理的使用场景" : "Curated scenarios", to: "/discover" },
        { icon: GitFork, value: stats?.projects, label: zh ? "已整理的真实项目" : "Curated repositories", to: "/discover" },
      ].map(item => <Link key={item.label} to={item.to} className="interactive-card flex items-center gap-4 rounded-xl border border-border bg-surface p-5"><item.icon className="size-5 shrink-0 text-primary" /><div><p className="font-serif text-3xl tabular-nums">{item.value == null ? (catalog.error ? "—" : "…") : item.value.toLocaleString(zh ? "zh-CN" : "en-US")}</p><p className="mt-1 text-xs text-muted">{item.label}</p></div><ArrowRight className="ml-auto size-4 text-subtle" /></Link>)}</div>
      <div className="mt-8 rounded-2xl border border-primary/20 bg-primary/[0.04] p-6 md:p-8">
        <div className="flex flex-wrap items-start justify-between gap-4"><div><p className="text-xs font-medium tracking-wide text-primary">{zh ? "从这里开始探索" : "A PLACE TO START"}</p><h2 className="mt-2 font-serif text-2xl font-medium">{zh ? "个人知识管理应用" : "Personal Knowledge Management Application"}</h2></div><Button asChild variant="outline"><Link to={`/types/${PKM_LEAF}`}>{zh ? "探索场景与项目" : "Explore scenarios and projects"}<ArrowRight className="size-4" /></Link></Button></div>
        <p className="mt-3 max-w-2xl text-sm leading-7 text-muted">{zh ? "把笔记连成知识网络、在文本与编辑器中积累知识，或搭建自己掌控的个人 Wiki。从具体场景找到适合的项目。" : "Connect your notes, keep knowledge in text and editors, or build your own wiki. Find projects through concrete scenarios."}</p>
        {catalog.data && <div className="mt-6 grid gap-3 md:grid-cols-3">{catalog.data.scenarios.filter(s => !s.leaf || s.leaf === PKM_LEAF).map(s => <Link key={s.id} to={`/types/${PKM_LEAF}?scenario=${s.id}`} className="interactive-card rounded-xl border border-border/70 bg-surface p-4"><h3 className="text-sm font-medium leading-6">{s.name}</h3><p className="mt-3 text-xs text-muted">{s.project_count} {zh ? "个相关项目" : "related projects"} <span className="float-right text-primary">→</span></p></Link>)}</div>}
        {catalog.error && <p className="mt-4 text-sm text-muted">{zh ? "项目库暂不可用；分类资料仍可浏览。" : "Repository catalog unavailable; taxonomy pages remain accessible."}</p>}
      </div>
      {covered.length > 0 && <section className="mt-10"><div className="flex flex-wrap items-baseline justify-between gap-3"><div><h2 className="font-serif text-2xl font-medium">{zh ? "继续探索" : "Keep exploring"}</h2><p className="mt-2 text-xs text-muted">{zh ? `已有 ${stats?.leaves ?? covered.length} 个类型积累了项目资料，覆盖持续增加。` : `Projects collected across ${stats?.leaves ?? covered.length} types, with coverage growing.`}</p></div><Link className="text-sm text-primary hover:underline" to="/discover">{zh ? "查看全部项目" : "View all projects"} →</Link></div><div className="mt-5 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">{covered.slice(0, 6).map(item => <Link key={item.slug} to={`/types/${item.slug}`} className="interactive-card flex items-center justify-between gap-4 rounded-xl border border-border bg-surface p-5"><div><h3 className="text-sm font-medium">{pick(lang, meta?.leafIndex.find(l => l.slug === item.slug)?.name_zh, item.name)}</h3><p className="mt-2 text-xs text-muted">{item.project_count} {zh ? "个项目" : "projects"}</p></div><ArrowRight className="size-4 shrink-0 text-subtle" /></Link>)}</div></section>}
      <div className="mt-10 flex flex-wrap items-center justify-between gap-4 rounded-xl border border-dashed border-border p-5"><div className="flex items-start gap-3"><Bookmark className="mt-1 size-4 shrink-0 text-primary" /><div><p className="text-sm font-medium">{zh ? "把感兴趣的项目留在手边" : "Keep interesting projects close"}</p><p className="mt-1 text-xs leading-6 text-muted">{zh ? "项目卡片上的书签会保存到本机，随时回来继续了解。" : "Bookmark any card to save it locally and return when you need it."}</p></div></div><Link className="text-sm text-primary hover:underline" to="/discover?favorites=1">{zh ? "我的收藏" : "Favorites"} →</Link></div>
    </section>
    {loading ? <Loading /> : error ? <ErrorBox message={error} /> : meta && <section className="mx-auto max-w-6xl px-4 pb-6">
      <div className="flex flex-wrap items-baseline justify-between gap-3"><h2 className="font-serif text-2xl font-medium">{t("byDomain", lang)}</h2><Link className="text-sm text-primary hover:underline" to="/browse">{zh ? "浏览完整分类" : "Browse the full taxonomy"} →</Link></div>
      <p className="mt-2 text-sm text-muted">{zh ? "先确定方向，再深入具体的软件类型。" : "Find a direction, then explore specific software types."}</p>
      {!meta.l0s.length && <EmptyState className="mt-6" title={zh ? "类型目录为空" : "The type catalog is empty"} />}
      <div className="mt-5 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">{meta.l0s.map(domain => <Link key={domain.id} to={`/browse#${domain.id}`} className="group flex items-center gap-3 rounded-xl border border-transparent px-4 py-3 hover:border-border hover:bg-surface"><span className="font-mono text-xs text-subtle">{domain.id}</span><div className="min-w-0 flex-1"><h3 className="text-sm font-medium">{pick(lang, domain.name_zh, domain.name)}</h3><p className="mt-1 text-xs text-muted">{domain.subs.length} {zh ? "个子域" : "subdomains"}</p></div><ArrowRight className="size-3.5 text-subtle group-hover:text-primary" /></Link>)}</div>
    </section>}
  </main>;
}
