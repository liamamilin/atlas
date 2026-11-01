import { Link, useSearchParams } from "react-router-dom";
import { RepositoryCatalog } from "@/components/repository-catalog";
import { useLang } from "@/lib/lang";

export function Discover() {
  const { lang } = useLang(); const zh = lang === "zh";
  const [params] = useSearchParams();
  const favorites = params.get("favorites") === "1";
  return <main className="mx-auto max-w-6xl px-4 py-10">
    <p className="text-xs font-medium tracking-widest text-primary">APPLICATION ATLAS</p>
    <h1 className="mt-3 font-serif text-4xl font-medium">{favorites ? (zh ? "我的收藏" : "My favorites") : (zh ? "发现开源项目" : "Discover open-source projects")}</h1>
    <p className="mt-3 text-sm leading-6 text-muted">{favorites ? (zh ? "留在手边的项目，随时回来继续了解。收藏保存在本机。" : "Your saved projects, ready to revisit. Favorites are stored locally.") : (zh ? "按软件类型和具体用途筛选，了解项目的能力、来源与许可证。" : "Explore projects by software type and use case, with capabilities, sources and license information.")} {!favorites && <Link to="/browse" className="text-primary underline">{zh ? "按类型浏览" : "Browse by type"} →</Link>}</p>
    <RepositoryCatalog showHeading={false} />
  </main>;
}
