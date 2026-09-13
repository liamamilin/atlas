import { NavLink, Link, Outlet, useLocation } from "react-router-dom";
import { getMeta } from "@/lib/atlas";
import { useAsync } from "@/components/loaders";
import { cn } from "@/lib/utils";
import { useLang, t } from "@/lib/lang";

export function AppShell() {
  const { lang, setLang } = useLang();
  const location = useLocation();
  const { data: meta } = useAsync(getMeta, [location.pathname]);
  return (
    <div className="min-h-dvh">
      <header className="sticky top-0 z-20 border-b border-border bg-bg/90 backdrop-blur">
        <div className="mx-auto flex h-14 max-w-6xl items-center gap-6 px-4">
          <Link to="/" className="flex items-center gap-2">
            <img src="/favicon.svg" alt="" className="size-5" />
            <span className="font-serif text-lg font-medium">{t("appName", lang)}</span>
          </Link>
          <nav className="flex items-center gap-4 text-sm text-muted">
            {[
              { to: "/", label: t("home", lang) },
              { to: "/browse", label: t("browse", lang) },
              { to: "/apps", label: t("apps", lang) },
              { to: "/drafts", label: t("drafts", lang) },
            ].map((l) => (
              <NavLink
                key={l.to}
                to={l.to}
                end={l.to === "/"}
                className={() => cn("hover:text-fg", "aria-[current=page]:font-medium aria-[current=page]:text-fg")}
              >
                {l.label}
              </NavLink>
            ))}
          </nav>
          <div className="ml-auto flex items-center gap-3 text-xs text-subtle">
            <span>{t("headerNote", lang, { n: meta?.leafCount ?? "…" })}</span>
            <button
              type="button"
              onClick={() => setLang(lang === "zh" ? "en" : "zh")}
              className="rounded-full bg-chip px-2.5 py-1 font-medium text-fg transition-colors hover:bg-border"
            >
              {lang === "zh" ? "EN" : "中"}
            </button>
          </div>
        </div>
      </header>
      <Outlet />
      <footer className="mt-16 border-t border-border py-8 text-center text-xs text-subtle">
        {t("footer", lang, { n: meta?.leafCount ?? "…" })}
      </footer>
    </div>
  );
}
