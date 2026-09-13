import { useNavigate, Link } from "react-router-dom";
import { ArrowRight, Compass, Layers, Boxes } from "lucide-react";
import { useState } from "react";
import { getMeta } from "@/lib/atlas";
import { useAsync, Loading, ErrorBox } from "@/components/loaders";
import { Button } from "@/components/ui/button";
import { useLang, t, pick } from "@/lib/lang";

export function Home() {
  const navigate = useNavigate();
  const { lang } = useLang();
  const [q, setQ] = useState("");
  const { data: meta, error, loading } = useAsync(getMeta, []);

  return (
    <main>
      <section className="border-b border-border">
        <div className="mx-auto max-w-3xl px-4 py-16 md:py-24">
          <p className="text-sm font-medium tracking-wide text-primary">{t("heroKicker", lang)}</p>
          <h1 className="mt-3 font-serif text-4xl font-medium leading-[1.15] tracking-tight md:text-5xl">
            {t("heroTitle", lang)}
          </h1>
          <p className="mt-5 max-w-xl text-base leading-relaxed text-muted md:text-lg">
            {t("heroP", lang)}
          </p>
          <form
            className="mt-8"
            onSubmit={(e) => {
              e.preventDefault();
              navigate({ pathname: "/search", search: `?q=${encodeURIComponent(q.trim())}` });
            }}
          >
            <label className="block">
              <span className="sr-only">搜索类型</span>
              <input
                value={q}
                onChange={(e) => setQ(e.target.value)}
                placeholder={t("searchPlaceholder", lang)}
                className="h-14 w-full rounded-xl bg-surface px-4 text-base shadow-card placeholder:text-subtle focus:outline-none focus:ring-2 focus:ring-primary/35"
              />
            </label>
            <div className="mt-3 flex flex-wrap gap-2">
              <Button type="submit" size="lg">
                {t("searchBtn", lang)} <ArrowRight className="size-4" />
              </Button>
              <Button asChild size="lg" variant="outline">
                <Link to="/browse">{t("browseAll", lang)}</Link>
              </Button>
            </div>
          </form>
        </div>
      </section>

      {loading ? <Loading /> : error ? <ErrorBox message={error} /> : meta ? (
        <>
          <section className="mx-auto max-w-6xl px-4 py-10">
            <div className="grid gap-4 sm:grid-cols-3">
              {[
                { icon: Layers, n: meta.leafCount, label: t("leafCount", lang), to: "/browse" },
                { icon: Compass, n: meta.sectionCount, label: t("secCount", lang), to: "/browse" },
                { icon: Boxes, n: meta.appCount, label: t("appCount", lang), to: "/apps" },
              ].map((s) => (
                <Link
                  key={s.label}
                  to={s.to}
                  className="block rounded-xl bg-surface p-5 shadow-card transition-shadow hover:shadow-card-hover"
                >
                  <s.icon className="size-5 text-primary" />
                  <div className="mt-3 font-serif text-3xl font-medium">{s.n}</div>
                  <div className="mt-1 text-sm text-muted">{s.label}</div>
                </Link>
              ))}
            </div>
          </section>

          <section className="mx-auto max-w-6xl px-4 pb-16">
            <h2 className="font-serif text-2xl font-medium">{t("byDomain", lang)}</h2>
            <p className="mt-2 text-sm text-muted">{t("byDomainP", lang)}</p>
            <div className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {meta.l0s.map((l0) => {
                const leafN = meta.leafIndex.filter((x) => x.sec === l0.id || l0.subs.some((s) => s.id === x.sec)).length;
                return (
                  <Link
                    key={l0.id}
                    to={`/browse#${l0.id}`}
                    className="rounded-xl bg-surface p-5 shadow-card transition-shadow hover:shadow-card-hover"
                  >
                    <div className="text-xs text-subtle">{l0.id}</div>
                    <h3 className="mt-1 font-medium">{pick(lang, l0.name_zh, l0.name)}</h3>
                    <div className="mt-1.5 text-xs text-muted">
                      {l0.subs.length > 0 ? (
                        <>
                          {l0.subs.length}{t("subs", lang)} ·{" "}
                        </>
                      ) : null}
                      {leafN}{t("types", lang)}
                    </div>
                  </Link>
                );
              })}
            </div>
          </section>
        </>
      ) : null}
    </main>
  );
}
