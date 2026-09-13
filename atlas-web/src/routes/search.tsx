import { useSearchParams } from "react-router-dom";
import { getMeta } from "@/lib/atlas";
import { useAsync, Loading, ErrorBox } from "@/components/loaders";
import { LeafCard } from "@/components/leaf-card";
import { useLang, t } from "@/lib/lang";

export function Search() {
  const { lang } = useLang();
  const [params] = useSearchParams();
  const q = (params.get("q") ?? "").trim();
  const { data: meta, error, loading } = useAsync(getMeta, []);
  if (loading) return <Loading />;
  if (error || !meta) return <ErrorBox message={error ?? ""} />;

  const ql = q.toLowerCase();
  const hits = ql
    ? meta.leafIndex
        .map((l) => {
          let score = 0;
          const nz = (l.name_zh || "").toLowerCase();
          if (l.slug.toLowerCase().includes(ql)) score += 6;
          if (nz.includes(ql)) score += 5;
          if (l.name.toLowerCase().includes(ql)) score += 4;
          if (l.dc.toLowerCase().includes(ql)) score += 1;
          if ((l.dc_zh || "").toLowerCase().includes(ql)) score += 1;
          return { ...l, l0: l.dc, l0_zh: l.dc_zh, score };
        })
        .filter((l) => l.score > 0)
        .sort((a, b) => b.score - a.score || a.name.localeCompare(b.name))
    : [];

  return (
    <main className="mx-auto max-w-4xl px-4 py-10">
      <h1 className="font-serif text-3xl font-medium">{t("searchTitle", lang, { q })}</h1>
      <p className="mt-2 text-sm text-muted">
        {hits.length
          ? t("searchHits", lang, { n: hits.length })
          : t("searchNone", lang)}
      </p>
      <div className="mt-6 grid gap-4 sm:grid-cols-2">
        {hits.map((h) => (
          <LeafCard key={l_key(h)} leaf={h} />
        ))}
      </div>
    </main>
  );
}

function l_key(h: { slug: string }) {
  return h.slug;
}
