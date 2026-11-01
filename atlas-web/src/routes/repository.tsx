import { Link, useNavigate, useParams } from "react-router-dom";
import { ArrowLeft, ExternalLink } from "lucide-react";
import { Loading, useAsync } from "@/components/loaders";
import { Button } from "@/components/ui/button";
import { FavoriteButton, RepositoryDetails, RepositoryFacts, useFavorite, useLeafNames } from "@/components/repository-catalog";
import { getRepositoryProject, type RepositoryDetail } from "@/lib/oss-catalog";
import { useLang } from "@/lib/lang";

export function Repository() {
  const { id = "" } = useParams();
  const { lang } = useLang(); const zh = lang === "zh";
  const valid = /^\d{1,12}$/.test(id);
  const detail = useAsync(() => valid ? getRepositoryProject(id) : Promise.reject(new Error("not found")), [id]);
  return <main className="mx-auto max-w-4xl px-4 py-10">
    <BackLink />
    {detail.loading ? <Loading>{zh ? "读取项目资料…" : "Loading project…"}</Loading>
      : detail.error || !detail.data ? <div role="alert" className="mt-8 rounded-xl border border-border bg-surface p-6 text-sm">
        <h1 className="font-serif text-2xl font-medium">{zh ? "找不到这个项目" : "Project not found"}</h1>
        <p className="mt-2 text-muted">{!valid || /不存在|not found/i.test(detail.error || "") ? (zh ? "项目库中没有这个仓库，可能已被移除或地址有误。" : "This repository is not in the catalog.") : (zh ? "项目库暂时无法读取，请检查本地 API 服务后重试。" : "The catalog is unavailable. Check the local API and retry.")}</p>
        <Link className="mt-4 inline-block text-primary underline" to="/discover">{zh ? "前往项目库" : "Open the catalog"}</Link>
      </div>
        : <RepositoryPage detail={detail.data} />}
  </main>;
}

function BackLink() {
  const { lang } = useLang(); const zh = lang === "zh";
  const navigate = useNavigate();
  const fromApp = typeof window !== "undefined" && (window.history.state?.idx ?? 0) > 0;
  return fromApp
    ? <button type="button" onClick={() => navigate(-1)} className="inline-flex min-h-9 items-center gap-1 text-sm text-muted hover:text-primary"><ArrowLeft className="size-4" />{zh ? "返回" : "Back"}</button>
    : <Link to="/discover" className="inline-flex min-h-9 items-center gap-1 text-sm text-muted hover:text-primary"><ArrowLeft className="size-4" />{zh ? "项目库" : "Catalog"}</Link>;
}

function RepositoryPage({ detail }: { detail: RepositoryDetail }) {
  const { lang } = useLang(); const zh = lang === "zh";
  const leafName = useLeafNames();
  const { project } = detail;
  const state = useFavorite(project);
  return <>
    <header className="mt-6">
      <div className="flex items-start justify-between gap-4">
        <div className="min-w-0">
          <h1 className="font-serif text-4xl font-medium break-words">{project.name}</h1>
          <p className="mt-2 break-all font-mono text-xs text-subtle">{project.full_name}</p>
        </div>
        <FavoriteButton project={project} state={state} />
      </div>
      {project.positioning && <p className="mt-4 text-lg leading-8">{project.positioning}</p>}
      <p className="mt-3 text-sm leading-7 text-muted">{project.summary}</p>
      <div className="mt-4"><RepositoryFacts project={project} /></div>
      {detail.leaves.length > 0 && <div className="mt-4 flex flex-wrap items-center gap-2 text-xs">
        <span className="text-muted">{zh ? "所属类型" : "Types"}</span>
        {detail.leaves.map(leaf => <Link key={leaf.slug} to={`/types/${leaf.slug}`} className="rounded-full border border-border px-3 py-1 hover:border-primary hover:text-primary">{leafName(leaf.slug, leaf.name)}</Link>)}
      </div>}
      {state.error && <p role="alert" className="mt-3 text-xs text-danger">{state.error}</p>}
      <div className="mt-6 flex flex-wrap items-center gap-4">
        <Button asChild><a href={project.github_url} target="_blank" rel="noopener noreferrer">{zh ? "在 GitHub 查看" : "View on GitHub"}<ExternalLink className="size-4" /></a></Button>
        <span className="text-xs text-subtle">{zh ? "最近核验 " : "Last checked "}{new Date(project.checked_at).toLocaleDateString(zh ? "zh-CN" : "en-US")}</span>
      </div>
    </header>
    <div className="mt-10 border-t border-border pt-8"><RepositoryDetails project={project} scenarios={detail.scenarios} /></div>
  </>;
}
