import { lazy, Suspense, type ReactNode } from "react";
import { Link, isRouteErrorResponse, Routes, Route, useParams, useRouteError } from "react-router-dom";
import { AppShell } from "@/components/app-shell";
import { Loading } from "@/components/loaders";
import { useLang } from "@/lib/lang";

const Home = lazy(() => import("@/routes/home").then(({ Home: page }) => ({ default: page })));
const Browse = lazy(() => import("@/routes/browse").then(({ Browse: page }) => ({ default: page })));
const Leaf = lazy(() => import("@/routes/leaf").then(({ Leaf: page }) => ({ default: page })));
const Search = lazy(() => import("@/routes/search").then(({ Search: page }) => ({ default: page })));
const Apps = lazy(() => import("@/routes/apps").then(({ Apps: page }) => ({ default: page })));
const Drafts = lazy(() => import("@/routes/drafts").then(({ Drafts: page }) => ({ default: page })));
const DraftDetailPage = lazy(() => import("@/routes/drafts").then(({ DraftDetailPage: page }) => ({ default: page })));
const Projects = lazy(() => import("@/routes/projects").then(({ Projects: page }) => ({ default: page })));
const ProjectDetail = lazy(() => import("@/routes/project-detail").then(({ ProjectDetail: page }) => ({ default: page })));
const Tutorial = lazy(() => import("@/routes/tutorial").then(({ Tutorial: page }) => ({ default: page })));
const Settings = lazy(() => import("@/routes/settings").then(({ Settings: page }) => ({ default: page })));
const Ask = lazy(() => import("@/routes/ask").then(({ Ask: page }) => ({ default: page })));
const Factory = lazy(() => import("@/routes/factory").then(({ Factory: page }) => ({ default: page })));

export function NotFoundPage() {
  const { lang } = useLang();
  return (
    <main className="mx-auto max-w-3xl px-4 py-16 text-center">
      <p className="font-mono text-sm text-primary">404</p>
      <h1 className="mt-3 font-serif text-3xl font-medium">{lang === "zh" ? "页面不存在" : "Page not found"}</h1>
      <p className="mt-3 text-sm text-muted">{lang === "zh" ? "这个地址没有对应的 Atlas 页面。" : "This address does not match an Atlas page."}</p>
      <div className="mt-6 flex justify-center gap-3 text-sm">
        <Link className="text-primary hover:underline" to="/">{lang === "zh" ? "返回首页" : "Go home"}</Link>
        <Link className="text-primary hover:underline" to="/search">{lang === "zh" ? "搜索类型" : "Search types"}</Link>
      </div>
    </main>
  );
}

export function RouteErrorPage() {
  const error = useRouteError();
  const { lang } = useLang();
  const status = isRouteErrorResponse(error) ? error.status : null;
  const message = status
    ? (lang === "zh" ? `页面加载失败（${status}）。` : `The page could not be loaded (${status}).`)
    : (lang === "zh" ? "页面遇到未预期的错误。" : "The page encountered an unexpected error.");
  return (
    <main className="mx-auto max-w-3xl px-4 py-16 text-center">
      <p className="font-mono text-sm text-danger">ERROR</p>
      <h1 className="mt-3 font-serif text-3xl font-medium">{lang === "zh" ? "页面加载失败" : "Page failed to load"}</h1>
      <p className="mt-3 text-sm text-muted">{message}</p>
      <div className="mt-6 flex justify-center gap-3 text-sm">
        <Link className="text-primary hover:underline" to="/">{lang === "zh" ? "返回首页" : "Go home"}</Link>
        <button type="button" className="text-primary hover:underline" onClick={() => window.location.reload()}>{lang === "zh" ? "重新加载" : "Reload"}</button>
      </div>
    </main>
  );
}

export default function App() {
  return (
    <Routes>
      <Route element={<AppShell />}>
        <Route path="/" element={<Page><Home /></Page>} />
        <Route path="/browse" element={<Page><Browse /></Page>} />
        <Route path="/types/:slug" element={<Page><Leaf /></Page>} />
        <Route path="/search" element={<Page><Search /></Page>} />
        <Route path="/apps" element={<Page><Apps /></Page>} />
        <Route path="/drafts" element={<Page><Drafts /></Page>} />
        <Route path="/drafts/:slug" element={<DraftDetailRoute />} />
        <Route path="/projects" element={<Page><Projects /></Page>} />
        <Route path="/projects/:projectId" element={<Page><ProjectDetail /></Page>} />
        <Route path="/tutorial" element={<Page><Tutorial /></Page>} />
        <Route path="/settings" element={<Page><Settings /></Page>} />
        <Route path="/ask" element={<Page><Ask /></Page>} />
        <Route path="/factory" element={<Page><Factory /></Page>} />
        <Route path="*" element={<Page><NotFoundPage /></Page>} />
      </Route>
    </Routes>
  );
}

function Page({ children }: { children: ReactNode }) {
  return <Suspense fallback={<Loading />}>{children}</Suspense>;
}

function DraftDetailRoute() {
  const { slug } = useParams();
  return slug ? <Page><DraftDetailPage slug={slug} /></Page> : <Page><Home /></Page>;
}
