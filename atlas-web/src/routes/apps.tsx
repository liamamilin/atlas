import { Link } from "react-router-dom";
import { getApps } from "@/lib/atlas";
import { useAsync, Loading, ErrorBox } from "@/components/loaders";
import { Badge } from "@/components/ui/badge";
import { useLang, t } from "@/lib/lang";

export function Apps() {
  const { lang } = useLang();
  const { data, error, loading } = useAsync(getApps, []);
  if (loading) return <Loading />;
  if (error || !data) return <ErrorBox message={error ?? ""} />;
  return (
    <main className="mx-auto max-w-6xl px-4 py-10">
      <h1 className="font-serif text-3xl font-medium">{t("appsTitle", lang)}</h1>
      <p className="mt-2 max-w-2xl text-sm leading-relaxed text-muted">
        {t("appsP", lang, { n: data.length })}
      </p>
      <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {data.map((a) => (
          <div key={a.slug} id={a.slug} className="scroll-mt-20 rounded-xl bg-surface p-5 shadow-card">
            <div className="flex items-baseline justify-between gap-2">
              <h2 className="font-medium">{a.name}</h2>
              <span className="truncate text-xs text-subtle">{a.vendor}</span>
            </div>
            <p className="mt-2 line-clamp-2 text-[13px] leading-relaxed text-muted">{a.tagline}</p>
            {a.leaf ? (
              <div className="mt-3 border-t border-border pt-3">
                <div className="text-[11px] text-subtle">{t("classified", lang)}</div>
                <Link to={`/types/${a.leaf}`} className="mt-1 inline-flex items-center gap-1.5 text-sm text-primary hover:underline">
                  {a.leafName || a.leaf}
                </Link>
              </div>
            ) : (
              <Badge tone="warn" className="mt-3">{t("unclassified", lang)}</Badge>
            )}
          </div>
        ))}
      </div>
    </main>
  );
}
