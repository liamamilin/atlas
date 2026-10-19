import { useEffect, useState } from "react";
import { Link, useLocation } from "react-router-dom";
import { getApps, type AppEntry } from "@/lib/atlas";
import { useAsync, EmptyState, Loading, ErrorBox } from "@/components/loaders";
import { Badge } from "@/components/ui/badge";
import { AppReferenceButton } from "@/components/app-reference-button";
import { CaseLibrary } from "@/components/case-library";
import { useLang, pick, t } from "@/lib/lang";

export function Apps() {
  const { lang } = useLang();
  const { data, error, loading } = useAsync(getApps, []);
  const { hash } = useLocation();
  const [missingHash, setMissingHash] = useState(false);
  useEffect(() => {
    if (!data || !hash) {
      setMissingHash(false);
      return;
    }
    const target = document.getElementById(hash.slice(1));
    if (!target) {
      setMissingHash(true);
      return;
    }
    setMissingHash(false);
    requestAnimationFrame(() => {
      target.scrollIntoView({ block: "start" });
      target.focus({ preventScroll: true });
    });
  }, [data, hash]);
  const apps = data || [];
  return (
    <main className="mx-auto max-w-6xl px-4 py-10">
      <h1 className="font-serif text-3xl font-medium">{t("appsTitle", lang)}</h1>
      <p className="mt-2 max-w-2xl text-sm leading-relaxed text-muted">
        {t("appsP", lang, { n: apps.length })}
      </p>
      <CaseLibrary />
      <section aria-label={lang === "zh" ? "历史应用目录" : "Legacy application catalog"} className="mt-12">
      <h2 className="font-serif text-2xl font-medium">{lang === "zh" ? "应用目录" : "Application catalog"}</h2>
      {loading ? <Loading /> : null}
      {error ? <ErrorBox message={error} /> : null}
      {missingHash ? <p className="mt-3 text-sm text-warn" role="status">{lang === "zh" ? "链接的应用不存在，请返回应用目录重新选择。" : "The linked application does not exist. Return to the catalog and choose another."}</p> : null}
      {apps.length ? (
        <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {apps.map((a) => {
          const appName = pick(lang, a.nameZh, a.nameEn || a.name);
          const appTagline = lang === "zh" ? a.tagline : (a.taglineEn || a.tagline);
          const appTasks = a.taskLabels?.[lang] || a.tasks;
          const leafName = pick(lang, a.leafNameZh, a.leafNameEn || a.leafName || a.leaf);
          return (
            <div key={a.slug} id={a.slug} tabIndex={-1} className="scroll-mt-20 rounded-xl bg-surface p-5 shadow-card focus:outline-none focus:ring-2 focus:ring-primary/35">
              <div className="flex items-baseline justify-between gap-2">
                <h2 className="font-medium">{appName}</h2>
                <span className="truncate text-xs text-subtle">{a.vendor}</span>
              </div>
              <p className="mt-2 line-clamp-2 text-[13px] leading-relaxed text-muted">{appTagline}</p>
              {appTasks.length ? <div className="mt-3 flex flex-wrap gap-1.5">{appTasks.slice(0, 6).map((task) => <Badge key={task} tone="default">{task}</Badge>)}</div> : null}
              <p className="mt-3 text-[11px] text-subtle">
                {lang === "zh" ? "资料深度：目录级（名称、简介、任务标签、Atlas 归类）" : "Coverage: catalog-level (name, description, task tags, Atlas classification)"}
              </p>
              {a.leaf ? (
                <div className="mt-3 border-t border-border pt-3">
                  <div className="text-[11px] text-subtle">{t("classified", lang)}</div>
                  <Link to={`/types/${a.leaf}`} className="mt-1 inline-flex items-center gap-1.5 text-sm text-primary hover:underline">
                    {leafName || a.leaf}
                  </Link>
                </div>
              ) : (
                <Badge tone="warn" className="mt-3">{t("unclassified", lang)}</Badge>
              )}
              <ClassificationEvidence evidence={a.classificationEvidence} lang={lang} />
              <div className="mt-4"><AppReferenceButton slug={a.slug} /></div>
            </div>
          );
        })}
        </div>
      ) : !loading && !error ? (
        <EmptyState
          className="mt-8"
          title={lang === "zh" ? "应用目录为空" : "The application catalog is empty"}
        >
          {lang === "zh" ? "当前没有可展示的真实应用；类型正文仍然可以浏览。" : "There are no applications to show yet; the type catalog remains available."}
        </EmptyState>
      ) : null}
      </section>
    </main>
  );
}

function ClassificationEvidence({ evidence, lang }: {
  evidence?: AppEntry["classificationEvidence"];
  lang: "zh" | "en";
}) {
  if (!evidence) return null;
  return (
    <details className="mt-3 border-t border-border pt-3 text-[11px] text-subtle">
      <summary className="cursor-pointer text-primary">
        {lang === "zh" ? "查看分类证据" : "View classification evidence"}
      </summary>
      <div className="mt-2 space-y-2 leading-5">
        <p>{lang === "zh" ? "来源记录：" : "Source record:"} <code>{evidence.source}</code></p>
        <p>{lang === "zh" ? "分类方法：" : "Classification method:"} {evidence.method}</p>
        {evidence.selectedLeaf ? (
          <p>{lang === "zh" ? "选定类型：" : "Selected type:"} <span className="font-mono">{evidence.selectedLeaf}</span></p>
        ) : null}
        {evidence.scores.length ? (
          <div>
            <p>{lang === "zh" ? "分类分数（最高 5 项）" : "Top classification scores"}</p>
            <ul className="mt-1 space-y-1">
              {evidence.scores.map((score) => (
                <li key={score.leaf} className="flex justify-between gap-2 font-mono">
                  <span>{score.leaf}</span><span>{score.score}</span>
                </li>
              ))}
            </ul>
          </div>
        ) : null}
        {lang === "zh" && evidence.sourceSummary ? <p>来源摘要：{evidence.sourceSummary}</p> : null}
        {lang === "en" ? <p>The selected type and scores are copied from the Atlas classification record.</p> : null}
      </div>
    </details>
  );
}
