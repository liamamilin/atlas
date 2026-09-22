import { useState } from "react";
import { ArrowRight, FolderKanban, Plus } from "lucide-react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { getLeaf, saveProjectReference, type LeafDetail } from "@/lib/atlas";
import { useAsync, Loading, ErrorBox } from "@/components/loaders";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { REL_KIND_ZH } from "@/lib/atlas";
import { Prose } from "@/components/prose";
import { SourceReader } from "@/components/source-reader";
import { useLang, pick, t, type Lang } from "@/lib/lang";
import { useCurrentProjectId } from "@/lib/project-selection";

export function Leaf() {
  const { slug } = useParams<{ slug: string }>();
  const { lang } = useLang();
  const { data, error, loading } = useAsync(() => getLeaf(slug!), [slug]);
  if (loading) return <Loading />;
  if (error || !data) return <ErrorBox message={error ?? t("notExist", lang)} />;
  const relKinds = [...new Set(data.relations.map((r) => r.kind))];

  return (
    <main className="mx-auto max-w-4xl px-4 py-10">
      <nav className="text-xs text-muted">
        <Link to="/browse" className="hover:text-fg">{t("typeTree", lang)}</Link>
        <span className="mx-1.5">/</span>
        <span>{pick(lang, data.section_name_zh, data.section_name)}</span>
      </nav>
      <div className="mt-3 flex flex-wrap items-baseline gap-3">
        <h1 className="font-serif text-4xl font-medium tracking-tight">{pick(lang, data.name_zh, data.name)}</h1>
        {pick(lang, data.name_zh, data.name) !== data.name ? (
          <span className="font-mono text-sm text-subtle">{data.name}</span>
        ) : null}
      </div>
      {data.aliases_zh.length ? (
        <div className="mt-3 flex flex-wrap gap-1.5">
          {data.aliases_zh.map((a) => (
            <Badge key={a} tone="default">{a}</Badge>
          ))}
        </div>
      ) : null}

      <TypeProjectActions leaf={data} />

      {data.dc ? (
        <section className="mt-8 rounded-xl bg-primary/[0.06] p-5 ring-1 ring-primary/15">
          <h2 className="text-xs font-medium uppercase tracking-widest text-primary">{t("definingCore", lang)}</h2>
          <Prose md={pick(lang, data.dc_zh, data.dc)} className="mt-3" />
          {lang === "zh" && data.dc && data.dc.trim() !== (data.dc_zh || "").trim() ? (
            <details className="mt-3">
              <summary className="cursor-pointer text-xs text-subtle hover:text-fg">{t("enOriginal", lang)}</summary>
              <Prose md={data.dc} className="mt-2" />
            </details>
          ) : null}
        </section>
      ) : null}

      {data.overview ? (
        <section className="mt-8">
          <h2 className="font-serif text-xl font-medium">{t("overview", lang)}</h2>
          <Prose md={pick(lang, data.overview_zh, data.overview)} className="mt-3" />
        </section>
      ) : null}

      {data.how ? (
        <section className="mt-8">
          <h2 className="font-serif text-xl font-medium">{t("howItWorks", lang)}</h2>
          <Prose md={pick(lang, data.how_zh, data.how)} className="mt-3" />
        </section>
      ) : null}

      {data.rules ? (
        <section className="mt-8">
          <h2 className="font-serif text-xl font-medium">{t("rules", lang)}</h2>
          <Prose md={pick(lang, data.rules_zh, data.rules)} className="mt-3" />
        </section>
      ) : null}

      {data.variants ? (
        <section className="mt-8">
          <h2 className="font-serif text-xl font-medium">{t("variants", lang)}</h2>
          <Prose md={pick(lang, data.variants_zh, data.variants)} className="mt-3" />
        </section>
      ) : null}

      {data.apps.length ? (
        <section className="mt-8">
          <h2 className="font-serif text-xl font-medium">{t("realProducts", lang)}</h2>
          <div className="mt-3 flex flex-wrap gap-2">
            {data.apps.map((a) => (
              <Link key={a.slug} to={`/apps#${a.slug}`}>
                <Badge tone="primary">{a.name}</Badge>
              </Link>
            ))}
          </div>
        </section>
      ) : null}

      {data.products ? (
        <section className="mt-8">
          <h2 className="font-serif text-xl font-medium">{t("corpusProducts", lang)}</h2>
          <Prose md={pick(lang, data.products_zh, data.products)} className="mt-3 text-muted" />
        </section>
      ) : null}

      {relKindsBlock(data.relations, relKinds, lang)}
      {data.sources ? (
        <section className="mt-8">
          <h2 className="font-serif text-xl font-medium">{t("sources", lang)}</h2>
          <Prose md={data.sources} className="mt-3 text-sm" />
        </section>
      ) : null}
      <SourceReader slug={data.slug} />
    </main>
  );
}

function TypeProjectActions({ leaf }: { leaf: LeafDetail }) {
  const { lang } = useLang();
  const [projectId] = useCurrentProjectId();
  const navigate = useNavigate();
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");
  const projectLink = `/projects?fromType=${encodeURIComponent(leaf.slug)}`;

  const addToCurrentProject = async () => {
    if (!projectId) return;
    setSaving(true);
    setError("");
    try {
      await saveProjectReference(projectId, {
        kind: "application",
        slug: leaf.slug,
        note: lang === "zh" ? "从类型详情页加入，作为项目开发起点。" : "Added from the type page as a project starting point.",
        read_status: "read",
      });
      navigate(`/projects/${projectId}`);
    } catch (cause) {
      if (String(cause).includes("already saved")) navigate(`/projects/${projectId}`);
      else setError(String(cause));
    } finally {
      setSaving(false);
    }
  };

  return (
    <section className="mt-8 rounded-xl bg-primary/[0.06] p-5 ring-1 ring-primary/15">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div className="max-w-2xl">
          <h2 className="flex items-center gap-2 font-serif text-xl font-medium">
            <FolderKanban className="size-5 text-primary" />
            {lang === "zh" ? "基于这个类型开发项目" : "Build a project from this type"}
          </h2>
          <p className="mt-2 text-sm leading-6 text-muted">
            {lang === "zh"
              ? "把完整类型正文固定为项目依据，然后进入项目工作区继续分析、生成文档和开发。"
              : "Pin the complete type document as project evidence, then continue analysis, documentation, and development in the workspace."}
          </p>
        </div>
        <div className="flex flex-wrap gap-2">
          {projectId ? (
            <Button onClick={addToCurrentProject} disabled={saving}>
              <ArrowRight className="size-4" />
              {saving
                ? (lang === "zh" ? "加入中…" : "Adding…")
                : (lang === "zh" ? "加入当前项目并开发" : "Add to current project")}
            </Button>
          ) : null}
          <Button asChild variant={projectId ? "outline" : "default"}>
            <Link to={projectLink}>
              <Plus className="size-4" />
              {projectId
                ? (lang === "zh" ? "创建新项目" : "Create a new project")
                : (lang === "zh" ? "基于此类型创建项目" : "Create a project from this type")}
            </Link>
          </Button>
        </div>
      </div>
      {error ? <p className="mt-3 text-sm text-danger">{error}</p> : null}
    </section>
  );
}

function relKindsBlock(rels: LeafDetail["relations"], kinds: string[], lang: Lang) {
  if (!rels.length) return null;
  return (
    <section className="mt-8">
      <h2 className="font-serif text-xl font-medium">{t("neighbors", lang)}</h2>
      <div className="mt-3 space-y-4">
        {kinds.map((k) => (
          <div key={k}>
            <h3 className="text-xs font-medium uppercase tracking-widest text-subtle">{REL_KIND_ZH[k] ?? k}</h3>
            <div className="mt-2 space-y-2">
              {rels.filter((r) => r.kind === k).map((r) => (
                <div key={r.to} className="rounded-lg bg-surface p-3 shadow-card">
                  <div className="flex items-baseline justify-between gap-2">
                    <Link to={`/types/${r.to}`} className="text-sm font-medium hover:underline">
                      {r.toName}
                    </Link>
                    <details className="text-[10px] text-subtle"><summary className="cursor-pointer">{lang === "zh" ? "技术信息" : "Technical details"}</summary><code className="mt-1 block rounded bg-chip px-1.5 py-0.5 font-mono">{r.to}</code></details>
                  </div>
                  {r.distinction ? (
                    <p className="mt-1 text-[13px] leading-relaxed text-muted">{pick(lang, r.distinction_zh, r.distinction)}</p>
                  ) : null}
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
