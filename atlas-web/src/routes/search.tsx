import { useEffect, useState, type FormEvent } from "react";
import { Boxes } from "lucide-react";
import { Link, useSearchParams } from "react-router-dom";
import { getApps, getMeta } from "@/lib/atlas";
import { useAsync, Loading, ErrorBox } from "@/components/loaders";
import { LeafCard } from "@/components/leaf-card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { AppReferenceButton } from "@/components/app-reference-button";
import { useLang, pick, t } from "@/lib/lang";
import { useCurrentProjectId } from "@/lib/project-selection";

const MAX_SEARCH_RESULTS = 100;

async function loadSearchIndex() {
  const [meta, apps] = await Promise.all([getMeta(), getApps()]);
  return { meta, apps };
}

export function Search() {
  const { lang } = useLang();
  const [projectId] = useCurrentProjectId();
  const [params, setParams] = useSearchParams();
  const q = (params.get("q") ?? "").trim();
  const [query, setQuery] = useState(q);
  useEffect(() => setQuery(q), [q]);
  const { data, error, loading } = useAsync(loadSearchIndex, []);
  const submitSearch = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const next = query.trim();
    setParams(next ? { q: next } : {});
  };
  if (loading) return <Loading />;
  if (error || !data) return <ErrorBox message={error ?? ""} />;

  const ql = q.toLowerCase();
  const types = ql
    ? data.meta.leafIndex
        .map((leaf) => {
          let score = 0;
          const nameZh = (leaf.name_zh || "").toLowerCase();
          if (leaf.slug.toLowerCase().includes(ql)) score += 6;
          if (nameZh.includes(ql)) score += 5;
          if ((leaf.aliases_zh || []).some((alias) => alias.toLowerCase().includes(ql))) score += 4;
          if (leaf.name.toLowerCase().includes(ql)) score += 4;
          if (leaf.dc.toLowerCase().includes(ql)) score += 1;
          if ((leaf.dc_zh || "").toLowerCase().includes(ql)) score += 1;
          return { ...leaf, l0: leaf.dc, l0_zh: leaf.dc_zh, score };
        })
        .filter((leaf) => leaf.score > 0)
        .sort((a, b) => b.score - a.score || a.name.localeCompare(b.name))
    : [];
  const apps = ql
    ? data.apps
        .map((app) => {
          let score = 0;
          const names = [app.name, app.nameEn || "", app.nameZh || "", ...(app.aliases || [])];
          const taglines = [app.tagline, app.taglineEn || ""];
          const taskLabels = app.taskLabels ? [...app.taskLabels.zh, ...app.taskLabels.en] : app.tasks;
          const leafNames = [app.leaf, app.leafName, app.leafNameZh || "", app.leafNameEn || ""];
          if (names.some((value) => value.toLowerCase().includes(ql))) score += 7;
          if ((app.aliases || []).some((alias) => alias.toLowerCase().includes(ql))) score += 6;
          if (app.vendor.toLowerCase().includes(ql)) score += 5;
          if (taglines.some((value) => value.toLowerCase().includes(ql))) score += 3;
          if (taskLabels.some((value) => value.toLowerCase().includes(ql))) score += 2;
          if (leafNames.some((value) => value.toLowerCase().includes(ql))) score += 1;
          return { ...app, score };
        })
        .filter((app) => app.score > 0)
        .sort((a, b) => b.score - a.score || a.name.localeCompare(b.name))
    : [];
  const total = types.length + apps.length;
  const visibleTypes = types.slice(0, MAX_SEARCH_RESULTS);
  const visibleApps = apps.slice(0, MAX_SEARCH_RESULTS);
  const truncated = total > visibleTypes.length + visibleApps.length;

  return (
    <main className="mx-auto max-w-5xl px-4 py-10">
      <h1 className="font-serif text-3xl font-medium">{t("searchTitle", lang, { q })}</h1>
      <form className="mt-5 flex flex-wrap items-end gap-2" onSubmit={submitSearch} role="search">
        <label className="min-w-0 flex-1 text-sm">
          <span className="text-muted">{t("searchLabel", lang)}</span>
          <input
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder={t("searchPlaceholder", lang)}
            className="mt-1 h-11 w-full rounded-lg border border-border bg-surface px-3 outline-none focus:ring-2 focus:ring-primary/35"
          />
        </label>
        <Button type="submit">{t("searchBtn", lang)}</Button>
        {q ? <Button type="button" variant="outline" onClick={() => { setQuery(""); setParams({}); }}>{lang === "zh" ? "清空" : "Clear"}</Button> : null}
      </form>
      <p className="mt-2 text-sm text-muted">
        {total
          ? (lang === "zh" ? `${types.length} 个软件类型 · ${apps.length} 个真实应用` : `${types.length} types · ${apps.length} real applications`)
          : t("searchNone", lang)}
      </p>

      {visibleTypes.length ? (
        <section className="mt-8">
          <h2 className="font-serif text-xl font-medium">{lang === "zh" ? "软件类型" : "Software types"}</h2>
          <p className="mt-1 text-xs text-subtle">
            {lang === "zh" ? "可进入类型页阅读正式正文和研究笔记。" : "Open a type to read its canonical document and research notes."}
          </p>
          <div className="mt-4 grid gap-4 sm:grid-cols-2">
            {visibleTypes.map((hit) => <LeafCard key={hit.slug} leaf={hit} />)}
          </div>
        </section>
      ) : null}

      {visibleApps.length ? (
        <section className="mt-8">
          <h2 className="font-serif text-xl font-medium">{lang === "zh" ? "真实应用" : "Real applications"}</h2>
          <p className="mt-1 text-xs text-subtle">
            {lang === "zh" ? "当前为目录级资料，可沿归属类型继续查看定义和边界。" : "Current coverage is catalog-level; follow the classified type for definitions and boundaries."}
          </p>
          <div className="mt-4 grid gap-4 sm:grid-cols-2">
            {visibleApps.map((app) => (
              <article key={app.slug} className="rounded-xl bg-surface p-5 shadow-card">
                <div className="flex items-start gap-3">
                  <Boxes className="mt-0.5 size-5 shrink-0 text-primary" />
                  <div className="min-w-0 flex-1">
                    <div className="flex flex-wrap items-baseline gap-2">
                      <Link to={`/apps#${app.slug}`} className="font-medium hover:underline">{pick(lang, app.nameZh, app.nameEn || app.name)}</Link>
                      <span className="text-xs text-subtle">{app.vendor}</span>
                    </div>
                    <p className="mt-2 text-[13px] leading-relaxed text-muted">{lang === "zh" ? app.tagline : (app.taglineEn || app.tagline)}</p>
                    <div className="mt-3 flex flex-wrap gap-1.5">
                      {(app.taskLabels?.[lang] || app.tasks).slice(0, 4).map((task) => <Badge key={task}>{task}</Badge>)}
                    </div>
                    {app.leaf ? (
                      <Link to={`/types/${app.leaf}`} className="mt-4 inline-block text-sm text-primary hover:underline">
                        {lang === "zh" ? "归属类型：" : "Classified type: "}{pick(lang, app.leafNameZh, app.leafNameEn || app.leafName || app.leaf)}
                      </Link>
                    ) : null}
                    <div className="mt-4"><AppReferenceButton slug={app.slug} /></div>
                  </div>
                </div>
              </article>
            ))}
          </div>
        </section>
      ) : null}

      {truncated ? <p className="mt-6 text-xs text-subtle">{lang === "zh" ? `结果较多，当前显示前 ${MAX_SEARCH_RESULTS} 条类型和前 ${MAX_SEARCH_RESULTS} 条应用；请缩小关键词范围。` : `Many results; showing the first ${MAX_SEARCH_RESULTS} types and ${MAX_SEARCH_RESULTS} applications. Narrow the query for a focused list.`}</p> : null}

      {!total ? (
        <div className="mt-8 rounded-xl bg-surface p-6 shadow-card">
          <p className="text-sm font-medium">
            {q
              ? (lang === "zh" ? "暂时没有匹配的类型或应用" : "No matching types or applications yet")
              : (lang === "zh" ? "从一个关键词开始探索" : "Start with a keyword")}
          </p>
          <p className="mt-2 max-w-2xl text-sm leading-6 text-muted">
            {q
              ? (lang === "zh"
                ? "可以换一个更短的关键词，先浏览类型目录，或直接查看应用目录。没有匹配结果不会阻止项目继续。"
                : "Try a shorter keyword, browse the type directory, or open the application catalog. A missing match does not block your project.")
              : (lang === "zh"
                ? "搜索会同时查找软件类型和真实应用；也可以先浏览完整类型目录，再从叶子页面创建项目。"
                : "Search covers software types and real applications. You can also browse the full type directory and start a project from a leaf page.")}
          </p>
          <div className="mt-4 flex flex-wrap gap-2">
            <Button asChild size="sm"><Link to="/browse">{lang === "zh" ? "浏览类型目录" : "Browse types"}</Link></Button>
            <Button asChild size="sm" variant="outline"><Link to="/apps">{lang === "zh" ? "查看应用目录" : "Open application catalog"}</Link></Button>
            {projectId ? <Button asChild size="sm" variant="outline"><Link to="/projects">{lang === "zh" ? "回到当前项目" : "Return to current project"}</Link></Button> : null}
          </div>
        </div>
      ) : null}
    </main>
  );
}
