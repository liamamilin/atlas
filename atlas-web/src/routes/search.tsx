import { Boxes } from "lucide-react";
import { Link, useSearchParams } from "react-router-dom";
import { getApps, getMeta } from "@/lib/atlas";
import { useAsync, Loading, ErrorBox } from "@/components/loaders";
import { LeafCard } from "@/components/leaf-card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { AppReferenceButton } from "@/components/app-reference-button";
import { useLang, t } from "@/lib/lang";
import { useCurrentProjectId } from "@/lib/project-selection";

async function loadSearchIndex() {
  const [meta, apps] = await Promise.all([getMeta(), getApps()]);
  return { meta, apps };
}

export function Search() {
  const { lang } = useLang();
  const [projectId] = useCurrentProjectId();
  const [params] = useSearchParams();
  const q = (params.get("q") ?? "").trim();
  const { data, error, loading } = useAsync(loadSearchIndex, []);
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
          if (app.name.toLowerCase().includes(ql)) score += 7;
          if (app.vendor.toLowerCase().includes(ql)) score += 5;
          if (app.tagline.toLowerCase().includes(ql)) score += 3;
          if (app.tasks.some((task) => task.toLowerCase().includes(ql))) score += 2;
          if (app.leaf.toLowerCase().includes(ql) || app.leafName.toLowerCase().includes(ql)) score += 1;
          return { ...app, score };
        })
        .filter((app) => app.score > 0)
        .sort((a, b) => b.score - a.score || a.name.localeCompare(b.name))
    : [];
  const total = types.length + apps.length;

  return (
    <main className="mx-auto max-w-5xl px-4 py-10">
      <h1 className="font-serif text-3xl font-medium">{t("searchTitle", lang, { q })}</h1>
      <p className="mt-2 text-sm text-muted">
        {total
          ? (lang === "zh" ? `${types.length} 个软件类型 · ${apps.length} 个真实应用` : `${types.length} types · ${apps.length} real applications`)
          : t("searchNone", lang)}
      </p>

      {types.length ? (
        <section className="mt-8">
          <h2 className="font-serif text-xl font-medium">{lang === "zh" ? "软件类型" : "Software types"}</h2>
          <p className="mt-1 text-xs text-subtle">
            {lang === "zh" ? "可进入类型页阅读正式正文和研究笔记。" : "Open a type to read its canonical document and research notes."}
          </p>
          <div className="mt-4 grid gap-4 sm:grid-cols-2">
            {types.map((hit) => <LeafCard key={hit.slug} leaf={hit} />)}
          </div>
        </section>
      ) : null}

      {apps.length ? (
        <section className="mt-8">
          <h2 className="font-serif text-xl font-medium">{lang === "zh" ? "真实应用" : "Real applications"}</h2>
          <p className="mt-1 text-xs text-subtle">
            {lang === "zh" ? "当前为目录级资料，可沿归属类型继续查看定义和边界。" : "Current coverage is catalog-level; follow the classified type for definitions and boundaries."}
          </p>
          <div className="mt-4 grid gap-4 sm:grid-cols-2">
            {apps.map((app) => (
              <article key={app.slug} className="rounded-xl bg-surface p-5 shadow-card">
                <div className="flex items-start gap-3">
                  <Boxes className="mt-0.5 size-5 shrink-0 text-primary" />
                  <div className="min-w-0 flex-1">
                    <div className="flex flex-wrap items-baseline gap-2">
                      <Link to={`/apps#${app.slug}`} className="font-medium hover:underline">{app.name}</Link>
                      <span className="text-xs text-subtle">{app.vendor}</span>
                    </div>
                    <p className="mt-2 text-[13px] leading-relaxed text-muted">{app.tagline}</p>
                    <div className="mt-3 flex flex-wrap gap-1.5">
                      {app.tasks.slice(0, 4).map((task) => <Badge key={task}>{task}</Badge>)}
                    </div>
                    {app.leaf ? (
                      <Link to={`/types/${app.leaf}`} className="mt-4 inline-block text-sm text-primary hover:underline">
                        {lang === "zh" ? "归属类型：" : "Classified type: "}{app.leafName || app.leaf}
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
