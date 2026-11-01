import { Link, useParams } from "react-router-dom";
import { useLang } from "@/lib/lang";
import { getLeaf } from "@/lib/atlas";
import { useAsync, ErrorBox, Loading } from "@/components/loaders";
import { LeafScenarios } from "@/components/leaf-scenarios";

export function History() {
  const { lang } = useLang(); const zh = lang === "zh";
  const entries = [
    ["/factory", "模板工厂", "Template factory", "已有模板、案例与生产记录。", "Existing templates, cases and production records."],
    ["/projects", "项目工作台", "Project workspaces", "此前的需求、文档、开发与验收记录。", "Previous requirements, documents and execution records."],
    ["/apps", "应用实证", "Case studies", "此前归类的产品与案例。", "Previously classified products and cases."],
    ["/ask", "历史问答", "Previous conversations", "此前的类型检索与问答。", "Previous type research and conversations."],
    ["/drafts", "分类草稿", "Type drafts", "已有分类研究草稿。", "Existing taxonomy research drafts."],
    ["/tutorial", "旧版使用教程", "Previous guide", "历史工作流程的操作说明。", "Instructions for historical workflows."],
  ];
  return <main className="mx-auto max-w-4xl px-4 py-10"><h1 className="font-serif text-3xl font-medium">{zh ? "历史工作区" : "Historical workspaces"}</h1><p className="mt-3 text-sm leading-6 text-muted">{zh ? "已有数据和原地址保留。当前版本围绕叶子、场景与真实项目组织内容。" : "Existing data and URLs are preserved. The current version focuses on types, scenarios and real repositories."}</p><div className="mt-8 grid gap-4 sm:grid-cols-2">{entries.map(([url, title, titleEn, description, descriptionEn]) => <Link key={url} to={url} className="rounded-xl bg-surface p-5 shadow-card"><h2 className="font-medium">{zh ? title : titleEn} →</h2><p className="mt-2 text-sm text-muted">{zh ? description : descriptionEn}</p></Link>)}</div></main>;
}

export function HistoricalLeaf() {
  const { slug } = useParams();
  const { lang } = useLang(); const zh = lang === "zh";
  const leaf = useAsync(() => getLeaf(slug!), [slug]);
  if (leaf.loading) return <Loading />;
  if (!leaf.data || leaf.error) return <ErrorBox message={leaf.error || "类型不存在"} />;
  return <main className="mx-auto max-w-4xl px-4 py-10"><Link className="text-sm text-primary underline" to="/history">{zh ? "历史工作区" : "Historical workspaces"}</Link><h1 className="mt-4 font-serif text-3xl font-medium">{zh ? "历史模板：" : "Historical templates: "}{zh ? leaf.data.name_zh || leaf.data.name : leaf.data.name}</h1><p className="mt-3 text-sm text-muted">{zh ? "此处保留旧版场景与模板记录。" : "Previous scenarios and template records are preserved here."} <Link className="text-primary underline" to={`/types/${slug}`}>{zh ? "查看当前类型页" : "Open the current type page"}</Link></p><LeafScenarios leaf={slug!} /></main>;
}
