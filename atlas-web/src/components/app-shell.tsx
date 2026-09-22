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
        <div className="mx-auto flex h-14 max-w-6xl items-center gap-4 px-4 sm:gap-6">
          <Link to="/" className="flex shrink-0 items-center gap-2">
            <img src="/favicon.svg" alt="" className="size-5" />
            <span className="font-serif text-lg font-medium">{t("appName", lang)}</span>
          </Link>
          <nav aria-label={lang === "zh" ? "主导航" : "Main navigation"} className="min-w-0 flex-1 overflow-x-auto whitespace-nowrap text-sm text-muted [scrollbar-width:none] [&::-webkit-scrollbar]:hidden">
            {[
              { to: "/", label: t("home", lang) },
              { to: "/browse", label: t("browse", lang) },
              { to: "/apps", label: t("apps", lang) },
              { to: "/projects", label: t("projects", lang) },
              { to: "/drafts", label: t("drafts", lang) },
              { to: "/tutorial", label: t("tutorial", lang) },
            ].map((l) => (
              <NavLink
                key={l.to}
                to={l.to}
                end={l.to === "/"}
                className={() => cn("mr-4 inline-block whitespace-nowrap py-1 hover:text-fg last:mr-0", "aria-[current=page]:font-medium aria-[current=page]:text-fg")}
              >
                {l.label}
              </NavLink>
            ))}
          </nav>
          <div className="ml-auto flex shrink-0 items-center gap-2 text-xs text-subtle sm:gap-3">
            <span className="hidden lg:inline">{t("headerNote", lang, { n: meta?.leafCount ?? "…" })}</span>
            <button
              type="button"
              aria-label={lang === "zh" ? "切换到英文" : "Switch to Chinese"}
              title={lang === "zh" ? "切换到英文" : "Switch to Chinese"}
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
