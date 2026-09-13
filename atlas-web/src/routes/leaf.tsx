import { Link, useParams } from "react-router-dom";
import { getLeaf, type LeafDetail } from "@/lib/atlas";
import { useAsync, Loading, ErrorBox } from "@/components/loaders";
import { Badge } from "@/components/ui/badge";
import { REL_KIND_ZH } from "@/lib/atlas";
import { Prose } from "@/components/prose";
import { useLang, pick, t, type Lang } from "@/lib/lang";

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
          <h2 className="font-serif text-xl font-medium">{lang === "zh" ? "资料来源" : "Sources"}</h2>
          <Prose md={data.sources} className="mt-3 text-sm" />
        </section>
      ) : null}
      {data.full_md ? (
        <details className="mt-8 rounded-xl bg-surface p-5 shadow-card">
          <summary className="cursor-pointer font-medium">{lang === "zh" ? "完整英文档案" : "Complete English document"}</summary>
          <Prose md={data.full_md} className="mt-4" />
        </details>
      ) : null}
    </main>
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
                    <span className="font-mono text-[11px] text-subtle">{r.to}</span>
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
