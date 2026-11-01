import { useEffect, useLayoutEffect, useRef } from "react";
import { Link, Outlet, useLocation, useNavigationType } from "react-router-dom";
import { Bookmark, Compass, House, Layers3, Search, Settings2, ArrowUpRight, BookOpen } from "lucide-react";
import { cn } from "@/lib/utils";
import { useLang, t } from "@/lib/lang";
import { ServiceStatus } from "@/components/service-status";
import { PageBoundary } from "@/components/page-boundary";

const historical = /^\/(history|factory|projects|apps|drafts|ask|tutorial)(\/|$)/;
const pageNames: Record<string, [string, string]> = {
  "/": ["首页", "Home"], "/browse": ["浏览类型", "Browse types"],
  "/discover": ["发现项目", "Discover projects"], "/search": ["搜索", "Search"],
  "/settings": ["设置", "Settings"], "/guide": ["使用指南", "Guide"],
  "/history": ["历史工作区", "Historical workspaces"], "/factory": ["模板工厂", "Template factory"],
  "/projects": ["项目工作台", "Project workspaces"], "/apps": ["应用实证", "Case studies"],
  "/drafts": ["分类草稿", "Type drafts"], "/ask": ["历史问答", "Conversations"], "/tutorial": ["旧版使用教程", "Previous guide"],
};

export function AppShell() {
  const { lang, setLang } = useLang(); const zh = lang === "zh";
  const location = useLocation(); const navigation = useNavigationType();
  const favorites = location.pathname === "/discover" && new URLSearchParams(location.search).get("favorites") === "1";
  const content = useRef<HTMLDivElement>(null);
  const positions = useRef(new Map<string, number>());
  const previousPath = useRef(location.pathname);
  useLayoutEffect(() => {
    const position = positions.current.get(location.key) || 0;
    let observer: ResizeObserver | undefined;
    let timer: ReturnType<typeof setTimeout> | undefined;
    const stopRestoring = () => { observer?.disconnect(); clearTimeout(timer); };
    const restore = () => {
      if (location.hash) {
        const target = document.getElementById(location.hash.slice(1));
        if (!target) return;
        target.scrollIntoView(); stopRestoring();
      } else {
        window.scrollTo(0, position);
        if (document.documentElement.scrollHeight >= position + window.innerHeight) stopRestoring();
      }
    };
    if (location.hash || navigation === "POP") {
      // Lazy pages and data can increase the page height after navigation.
      observer = new ResizeObserver(restore);
      if (content.current) observer.observe(content.current);
      timer = setTimeout(stopRestoring, 3000);
      restore();
      window.addEventListener("wheel", stopRestoring, { passive: true });
      window.addEventListener("touchstart", stopRestoring, { passive: true });
    } else if (previousPath.current !== location.pathname) {
      window.scrollTo(0, 0);
    }
    if (previousPath.current !== location.pathname) content.current?.focus({ preventScroll: true });
    previousPath.current = location.pathname;
    return () => {
      positions.current.set(location.key, window.scrollY);
      stopRestoring();
      window.removeEventListener("wheel", stopRestoring);
      window.removeEventListener("touchstart", stopRestoring);
    };
  }, [location.key, location.pathname, location.hash, navigation]);
  useEffect(() => {
    const base = pageNames[location.pathname] || pageNames[`/${location.pathname.split("/")[1]}`];
    const heading = content.current?.querySelector("h1")?.textContent;
    document.title = `${favorites ? (zh ? "我的收藏" : "Favorites") : base?.[zh ? 0 : 1] || heading || (zh ? "类型详情" : "Type details")} · ${t("appName", lang)}`;
    // Update the title once a lazy page's heading becomes available.
    const observer = new MutationObserver(() => {
      if (base || favorites) return;
      const title = content.current?.querySelector("h1")?.textContent;
      if (title) document.title = `${title} · ${t("appName", lang)}`;
    });
    if (content.current) observer.observe(content.current, { childList: true, subtree: true });
    return () => observer.disconnect();
  }, [location.pathname, favorites, zh, lang]);
  const links = [
    { to: "/", label: t("home", lang), icon: House, active: location.pathname === "/" },
    { to: "/browse", label: t("browse", lang), icon: Layers3, active: location.pathname === "/browse" || location.pathname.startsWith("/types/") },
    { to: "/discover", label: zh ? "发现项目" : "Discover", icon: Compass, active: location.pathname === "/discover" && !favorites },
    { to: "/discover?favorites=1", label: zh ? "我的收藏" : "Favorites", icon: Bookmark, active: favorites },
    { to: "/search", label: zh ? "搜索" : "Search", icon: Search, active: location.pathname === "/search" },
  ];
  return <div className="flex min-h-dvh flex-col">
    <a className="skip-link" href="#main-content">{zh ? "跳到主要内容" : "Skip to content"}</a>
    <header className="sticky top-0 z-20 border-b border-border bg-bg/95 backdrop-blur-md">
      <div className="mx-auto flex min-h-16 max-w-6xl flex-wrap items-center gap-x-6 px-4">
        <Link to="/" className="flex shrink-0 items-center gap-2.5 py-3" aria-label={zh ? "应用图谱首页" : "Application Atlas home"}>
          <img src="/favicon.svg" alt="" width="28" height="28" />
          <span className="font-serif text-lg font-medium tracking-tight">{t("appName", lang)}</span>
        </Link>
        <nav aria-label={zh ? "主导航" : "Main navigation"} className="order-3 -mx-1 flex w-full items-center justify-between gap-1 border-t border-border/70 pt-1 text-xs lg:order-none lg:mx-0 lg:w-auto lg:justify-start lg:gap-1 lg:border-0 lg:pt-0 lg:text-sm">
          {links.map(item => <Link key={item.to} to={item.to} aria-current={item.active ? "page" : undefined} className={cn("flex min-h-11 items-center justify-center gap-1.5 rounded-lg px-2 py-2 transition-colors hover:bg-chip/60 lg:px-3", item.active ? "bg-primary/[0.08] font-medium text-primary" : "text-muted")}>
            <item.icon aria-hidden="true" className="hidden size-4 sm:block" />{item.label}
          </Link>)}
        </nav>
        <div className="ml-auto flex items-center gap-1 text-muted">
          <Link to="/guide" aria-label={zh ? "使用指南" : "Guide"} title={zh ? "使用指南" : "Guide"} className={cn("flex size-10 items-center justify-center rounded-lg hover:bg-chip", location.pathname === "/guide" && "bg-chip text-primary")}><BookOpen className="size-4" /></Link>
          <Link to="/settings" aria-label={t("settings", lang)} title={t("settings", lang)} className={cn("flex size-10 items-center justify-center rounded-lg hover:bg-chip", location.pathname === "/settings" && "bg-chip text-primary")}><Settings2 className="size-4" /></Link>
          <button type="button" aria-label={zh ? "切换到英文" : "Switch to Chinese"} title={zh ? "切换到英文" : "Switch to Chinese"} onClick={() => setLang(zh ? "en" : "zh")} className="ml-1 flex size-10 items-center justify-center rounded-lg border border-border text-xs font-medium text-fg hover:bg-chip">{zh ? "EN" : "中"}</button>
        </div>
      </div>
    </header>
    <ServiceStatus />
    {historical.test(location.pathname) && location.pathname !== "/history" && <div className="border-b border-border bg-bg-elevated"><div className="mx-auto flex max-w-6xl flex-wrap items-center justify-between gap-2 px-4 py-2.5 text-xs text-muted"><Link to="/history" className="hover:text-primary">← {zh ? "历史工作区" : "Historical workspaces"}</Link><Link to="/discover" className="inline-flex items-center gap-1 text-primary">{zh ? "前往当前项目库" : "Open the current catalog"}<ArrowUpRight className="size-3.5" /></Link></div></div>}
    <div ref={content} id="main-content" tabIndex={-1} className="min-w-0 flex-1 outline-none">
      <PageBoundary key={location.pathname} zh={zh}><Outlet /></PageBoundary>
    </div>
    <footer className="mt-16 border-t border-border bg-bg-elevated">
      <div className="mx-auto flex max-w-6xl flex-wrap items-start justify-between gap-6 px-4 py-8">
        <div><p className="font-serif text-base font-medium">Application Atlas</p><p className="mt-2 max-w-sm text-xs leading-6 text-muted">{zh ? "以场景发现真实项目。每一份介绍，都有迹可循。" : "Discover real projects by scenario, with sources you can follow."}</p></div>
        <nav aria-label={zh ? "页脚导航" : "Footer navigation"} className="flex flex-wrap gap-x-6 gap-y-3 text-xs text-muted">
          <Link className="hover:text-primary" to="/guide">{zh ? "使用指南与资料说明" : "Guide and sources"}</Link>
          <Link className="hover:text-primary" to="/settings">{t("settings", lang)}</Link>
          <Link className="hover:text-primary" to="/history">{zh ? "历史工作区与模板工厂" : "Historical workspaces and template factory"}</Link>
        </nav>
      </div>
    </footer>
  </div>;
}
