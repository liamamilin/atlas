import { ArrowRight, CheckCircle2, FileText, FolderKanban, Search, ShieldCheck } from "lucide-react";
import { useMemo } from "react";
import { Link } from "react-router-dom";
import tutorialMd from "../../../TUTORIAL.md?raw";
import { Prose } from "@/components/prose";
import { useLang, t } from "@/lib/lang";

/**
 * The tutorial is authored as repo Markdown. Relative links such as `README.md`
 * have no route in the web app, so render the path as inline code instead.
 */
function forWeb(md: string) {
  return md
    .replace(/^# .*\n/, "")
    .replace(/\[([^\]]+)\]\((?!https?:\/\/|#|mailto:)([^)]+)\)/g, (_match, _label, href: string) => `\`${href}\``);
}

export function Tutorial() {
  const { lang } = useLang();
  const md = useMemo(() => forWeb(tutorialMd), []);
  return (
    <main className="mx-auto max-w-3xl px-4 py-10">
      <h1 className="font-serif text-3xl font-medium">{t("tutorial", lang)}</h1>
      <section className="mt-6 rounded-2xl bg-primary/[0.06] p-6 ring-1 ring-primary/15">
        <p className="text-xs font-medium tracking-wide text-primary">{lang === "zh" ? "第一次使用" : "First run"}</p>
        <h2 className="mt-2 font-serif text-2xl font-medium">{lang === "zh" ? "用一条完整路径理解 Atlas" : "Understand Atlas through one complete path"}</h2>
        <p className="mt-2 text-sm leading-6 text-muted">
          {lang === "zh" ? "Atlas 管理项目知识和验收边界，OpenCode 负责实际 agent 执行。每一步都先记录、再确认，不会自动覆盖你的项目。" : "Atlas manages project knowledge and acceptance boundaries; OpenCode performs the agent work. Each step is recorded and reviewed before it can affect your project."}
        </p>
        <div className="mt-5 grid gap-3 sm:grid-cols-2">
          <GuideStep icon={Search} title={lang === "zh" ? "1. 选择案例" : "1. Choose a case"} text={lang === "zh" ? "从新想法、已有项目改进或 Agent Harness 调研开始。" : "Start with a new idea, an existing project, or an Agent Harness study."} />
          <GuideStep icon={FileText} title={lang === "zh" ? "2. 固定资料" : "2. Pin evidence"} text={lang === "zh" ? "浏览类型或搜索产品，把完整正文固定为项目依据。" : "Browse a type or search products, then pin the complete document as evidence."} />
          <GuideStep icon={FolderKanban} title={lang === "zh" ? "3. 形成项目" : "3. Shape the project"} text={lang === "zh" ? "在工作台处理问题、冲突和建议，确认需求并生成文档。" : "Resolve questions, conflicts, and suggestions, then confirm requirements and generate docs."} />
          <GuideStep icon={ShieldCheck} title={lang === "zh" ? "4. 冻结与执行" : "4. Freeze and execute"} text={lang === "zh" ? "批准文档、建立迭代；OpenCode 在隔离副本中执行任务。" : "Approve docs and create an iteration; OpenCode executes in an isolated copy."} />
          <GuideStep icon={CheckCircle2} title={lang === "zh" ? "5. 应用与验收" : "5. Apply and accept"} text={lang === "zh" ? "查看差异和验证证据，明确应用结果并完成产品验收。" : "Review diffs and verification evidence, explicitly apply results, and accept the product outcome."} />
          <div className="rounded-lg bg-surface p-4 shadow-card">
            <p className="text-sm leading-5 text-muted">{lang === "zh" ? "想直接开始？" : "Ready to start?"}</p>
            <div className="mt-3 flex flex-wrap gap-2">
              <Link to="/projects" className="inline-flex items-center gap-1 text-sm font-medium text-primary hover:underline">{lang === "zh" ? "打开项目工作台" : "Open project workspace"}<ArrowRight className="size-4" /></Link>
              <Link to="/browse" className="inline-flex items-center gap-1 text-sm text-muted hover:text-fg">{lang === "zh" ? "先浏览类型" : "Browse types first"}<ArrowRight className="size-4" /></Link>
            </div>
          </div>
        </div>
      </section>
      <div className="mt-8">
        <Prose md={md} />
      </div>
    </main>
  );
}

function GuideStep({ icon: Icon, title, text }: { icon: typeof Search; title: string; text: string }) {
  return <div className="rounded-lg bg-surface p-4 shadow-card"><Icon className="size-4 text-primary" /><h3 className="mt-2 text-sm font-medium">{title}</h3><p className="mt-1 text-xs leading-5 text-muted">{text}</p></div>;
}
