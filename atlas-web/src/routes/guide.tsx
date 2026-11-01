import { Link } from "react-router-dom";
import { ArrowRight, Bookmark, Compass, Layers3, Server, ShieldCheck } from "lucide-react";
import { useLang } from "@/lib/lang";
import { Button } from "@/components/ui/button";

export function Guide() {
  const { lang } = useLang(); const zh = lang === "zh";
  return <main className="mx-auto max-w-5xl px-4 py-10 md:py-14">
    <p className="text-xs font-medium uppercase tracking-widest text-primary">A FIELD GUIDE TO ATLAS</p>
    <h1 className="mt-3 font-serif text-4xl font-medium">{zh ? "从一个想法，找到值得了解的项目" : "Find projects worth exploring"}</h1>
    <p className="mt-4 max-w-2xl text-sm leading-7 text-muted">{zh ? "Atlas 把软件类型、使用场景和真实仓库连接起来。你可以先了解一类软件，再按具体用途探索项目，保存感兴趣的结果。" : "Atlas connects software types, use cases and real repositories. Learn about a type, explore projects by what you need, and save what interests you."}</p>
    <div className="mt-8 grid gap-4 md:grid-cols-3">{[
      { icon: Layers3, n: "01", title: zh ? "确定方向" : "Find a direction", text: zh ? "从已有分类浏览，或用名称、别名和用途搜索软件类型。类型页解释定义、边界与相邻类型。" : "Browse the taxonomy or search by name, alias and purpose. Type pages explain definitions and boundaries.", to: "/browse", action: zh ? "浏览软件类型" : "Browse software types" },
      { icon: Compass, n: "02", title: zh ? "按场景发现" : "Explore by scenario", text: zh ? "结合用途和许可证筛选项目，展开卡片查看功能、适用条件、缺项及官方来源。" : "Filter by use case and license. Expand a card for features, conditions, missing information and official sources.", to: "/discover", action: zh ? "进入项目库" : "Explore projects" },
      { icon: Bookmark, n: "03", title: zh ? "收藏与回访" : "Save and return", text: zh ? "点击项目右上角的书签保存收藏。收藏保存在本机服务中，可从导航随时回访。" : "Use the bookmark on a project card. Favorites are saved by the local service and remain available from navigation.", to: "/discover?favorites=1", action: zh ? "打开我的收藏" : "Open favorites" },
    ].map(step => <section key={step.n} className="flex flex-col rounded-2xl border border-border bg-surface p-6"><div className="flex items-center justify-between text-primary"><step.icon className="size-5" /><span className="font-mono text-xs text-subtle">{step.n}</span></div><h2 className="mt-5 font-serif text-xl font-medium">{step.title}</h2><p className="mt-3 flex-1 text-sm leading-7 text-muted">{step.text}</p><Link className="mt-5 inline-flex items-center gap-2 text-sm font-medium text-primary" to={step.to}>{step.action}<ArrowRight className="size-4" /></Link></section>)}</div>
    <section className="mt-10 rounded-2xl bg-primary/[0.05] p-6 md:p-8">
      <div className="flex items-center gap-3"><ShieldCheck className="size-5 text-primary" /><h2 className="font-serif text-2xl font-medium">{zh ? "读懂一张项目卡片" : "Reading a project card"}</h2></div>
      <dl className="mt-5 grid gap-5 text-sm md:grid-cols-2">{[
        [zh ? "来源与核验时间" : "Sources and dates", zh ? "项目介绍依据公开仓库、README、官方文档与许可文件。展开原文依据可回查采集版本；最近核验时间不代表项目最近发布的时间。" : "Descriptions use public repository metadata, READMEs, documentation and license files. Evidence links identify the collected version. Last checked is not the project's release date."],
        [zh ? "许可证状态" : "License status", zh ? "已核验开源、源码可见但有限制、待核验分别显示。请结合原项目的许可文件判断使用范围。" : "Verified open source, source available with restrictions, and pending review are shown separately. Review the upstream license before use."],
        [zh ? "关联依据与资料缺项" : "Fit and completeness", zh ? "直接依据、条件适用和待核实推断会分别标注。资料不完整的真实项目可以先收录，缺项会继续保留。" : "Direct evidence, conditional fit and unverified inferences have distinct labels. Real projects with partial information stay visible with their gaps."],
        [zh ? "覆盖范围" : "Coverage", zh ? "分类资料与项目采集分别积累。某个类型暂无项目，不代表没有可用项目；当前目录也不代表穷尽搜索结果或经过运行实测。" : "Taxonomy and project coverage grow separately. An empty type does not mean no projects exist. Inclusion does not imply exhaustive discovery or runtime testing."],
      ].map(([title, text]) => <div key={title}><dt className="font-medium">{title}</dt><dd className="mt-2 leading-7 text-muted">{text}</dd></div>)}</dl>
    </section>
    <section id="service" className="mt-10 scroll-mt-36 rounded-2xl border border-border bg-surface p-6 md:p-8">
      <div className="flex items-center gap-3"><Server className="size-5 text-primary" /><h2 className="font-serif text-2xl font-medium">{zh ? "本地服务与资料更新" : "Local service and updates"}</h2></div>
      <p className="mt-4 text-sm leading-7 text-muted">{zh ? "阅读分类资料不需要模型服务。项目库、收藏和设置依赖本地 API；采集新项目还需要可用的模型服务及 GitHub 访问额度。" : "Reading the taxonomy needs no model. Repositories, favorites and settings use the local API. Collecting new projects also requires a model provider and GitHub quota."}</p>
      <p className="mt-4 text-sm font-medium">{zh ? "连接失败时，在仓库根目录启动 API：" : "If disconnected, start the API from the repository root:"}</p>
      <pre className="mt-3 overflow-x-auto rounded-xl bg-bg-elevated p-4 text-xs leading-6"><code>python3 application-atlas-production-pack/drafts_api.py</code></pre>
      <p className="mt-3 text-xs leading-6 text-muted">{zh ? "默认 API 地址为 127.0.0.1:5199。若页面提示接口不存在，请停止旧 API 进程后重新启动，再点击重新读取。" : "The default API listens on 127.0.0.1:5199. If a route is missing, restart the old API process and retry."}</p>
      <p className="mt-4 text-sm leading-7 text-muted">{zh ? "在项目库展开“批量采集”，选择要处理的类型。任务会保存进度；暂停或中断后可以继续。浏览已有资料不会启动采集。" : "Expand Batch collection in the catalog and select types. Jobs save progress and can resume after pauses or interruptions. Browsing saved data does not start collection."}</p>
      <Button asChild variant="outline" className="mt-5"><Link to="/settings">{zh ? "配置 GitHub 与模型服务" : "Configure GitHub and model providers"}<ArrowRight className="size-4" /></Link></Button>
    </section>
    <p className="mt-8 text-sm leading-7 text-muted">{zh ? "需要找回之前的模板、项目或问答？" : "Looking for previous templates, workspaces or conversations?"} <Link className="text-primary underline underline-offset-4" to="/history">{zh ? "打开历史工作区" : "Open historical workspaces"}</Link></p>
  </main>;
}
