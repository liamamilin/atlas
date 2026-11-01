import { Link, useParams } from "react-router-dom";
import { getLeaf, type LeafDetail } from "@/lib/atlas";
import { useAsync, Loading, ErrorBox } from "@/components/loaders";
import { Badge } from "@/components/ui/badge";
import { relationKindLabel } from "@/lib/atlas";
import { Prose } from "@/components/prose";
import { SourceReader } from "@/components/source-reader";
import { useLang, pick, t, type Lang } from "@/lib/lang";
import { RepositoryCatalog } from "@/components/repository-catalog";

export function Leaf() {
  const { slug } = useParams<{ slug: string }>();
  const { lang } = useLang();
  const { data, error, loading } = useAsync(() => getLeaf(slug!), [slug]);
  if (loading) return <Loading />;
  if (error || !data) return <ErrorBox message={error ?? t("notExist", lang)} />;
  const relKinds = [...new Set(data.relations.map((r) => r.kind))];

  return (
    <main className="mx-auto max-w-4xl px-4 py-10">
      <nav aria-label={lang === "zh" ? "类型位置" : "Type breadcrumb"} className="text-xs text-muted">
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

      <nav aria-label={lang === "zh" ? "本页内容" : "On this page"} className="mt-6 flex flex-wrap gap-2 border-y border-border py-3 text-xs text-muted">
        {[["repositories", lang === "zh" ? "场景与项目" : "Scenarios and projects"], ["definition", lang === "zh" ? "类型介绍" : "About this type"], ...(data.relations.length ? [["neighbors", lang === "zh" ? "相邻类型" : "Related types"]] : []), ["source-material", lang === "zh" ? "原始资料" : "Source material"]].map(([id, label]) => <a className="rounded-lg px-3 py-2 hover:bg-chip hover:text-primary" key={id} href={`#${id}`}>{label}</a>)}
      </nav>
      <div id="repositories"><RepositoryCatalog key={data.slug} leaf={data.slug} /></div>

      {data.dc ? (
        <section id="definition" className="mt-8 rounded-xl bg-primary/[0.06] p-5 ring-1 ring-primary/15">
          <h2 className="text-xs font-medium uppercase tracking-widest text-primary">{t("definingCore", lang)}</h2>
          <Prose md={pick(lang, data.dc_zh, data.dc)} className="mt-3" resolveTypeLinks />
          {lang === "zh" && data.dc && data.dc.trim() !== (data.dc_zh || "").trim() ? (
            <details className="mt-3">
              <summary className="cursor-pointer text-xs text-subtle hover:text-fg">{t("enOriginal", lang)}</summary>
              <Prose md={data.dc} className="mt-2" resolveTypeLinks />
            </details>
          ) : null}
        </section>
      ) : null}

      {data.overview ? (
        <section className="mt-8">
          <h2 className="font-serif text-xl font-medium">{t("overview", lang)}</h2>
          <Prose md={pick(lang, data.overview_zh, data.overview)} className="mt-3" resolveTypeLinks />
        </section>
      ) : null}

      {data.how ? (
        <section className="mt-8">
          <h2 className="font-serif text-xl font-medium">{t("howItWorks", lang)}</h2>
          <Prose md={pick(lang, data.how_zh, data.how)} className="mt-3" resolveTypeLinks />
        </section>
      ) : null}

      {data.rules ? (
        <section className="mt-8">
          <h2 className="font-serif text-xl font-medium">{t("rules", lang)}</h2>
          <Prose md={pick(lang, data.rules_zh, data.rules)} className="mt-3" resolveTypeLinks />
        </section>
      ) : null}

      {data.variants ? (
        <section className="mt-8">
          <h2 className="font-serif text-xl font-medium">{t("variants", lang)}</h2>
          <Prose md={pick(lang, data.variants_zh, data.variants)} className="mt-3" resolveTypeLinks />
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
          <Prose md={pick(lang, data.products_zh, data.products)} className="mt-3 text-muted" resolveTypeLinks />
        </section>
      ) : null}

      {relKindsBlock(data.relations, relKinds, lang)}
      {data.sources ? (
        <section className="mt-8">
          <h2 className="font-serif text-xl font-medium">{t("sources", lang)}</h2>
          <Prose md={data.sources} className="mt-3 text-sm" resolveTypeLinks />
        </section>
      ) : null}
      <div id="source-material"><SourceReader slug={data.slug} fallbackMarkdown={data.full_md} /></div>
      <Link className="mt-8 inline-block text-xs text-muted underline" to={`/history/types/${data.slug}`}>{lang === "zh" ? "查看此类型的历史模板" : "View historical templates for this type"}</Link>
    </main>
  );
}

function relKindsBlock(rels: LeafDetail["relations"], kinds: string[], lang: Lang) {
  if (!rels.length) return null;
  return (
    <section id="neighbors" className="mt-8">
      <h2 className="font-serif text-xl font-medium">{t("neighbors", lang)}</h2>
      <div className="mt-3 space-y-4">
        {kinds.map((k) => (
          <div key={k}>
            <h3 className="text-xs font-medium uppercase tracking-widest text-subtle">{relationKindLabel(k, lang)}</h3>
            <div className="mt-2 space-y-2">
              {rels.filter((r) => r.kind === k).map((r, index) => (
                <div key={r.id || `${r.kind}:${r.to}:${index}`} className="rounded-lg bg-surface p-3 shadow-card">
                  <div className="flex items-baseline justify-between gap-2">
                    <Link to={`/types/${r.to}`} className="text-sm font-medium hover:underline">
                      {pick(lang, r.toNameZh, r.toNameEn || r.toName)}
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
