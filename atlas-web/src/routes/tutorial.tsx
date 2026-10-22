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

const tutorialEnglish = forWeb(`
# Atlas Tutorial

## 1. Choose a starting point

Start from a new idea, an existing project, or an Agent Harness study. Choose a concrete outcome before opening a provider session.

## 2. Pin evidence

Browse the type tree or search the catalog. Pin the complete type document, the relevant section, and a short project note so later runs use a reviewable source version.

## 3. Shape the project

Use the project workspace to record open questions, conflicts, suggestions, requirements, and decisions. AI output remains a proposal until you review and confirm it.

## 4. Create an iteration and execute

Approve the documents you want to freeze, create an iteration, and define bounded write paths and fixed verification commands. OpenCode runs in an isolated copy; the source workspace is not changed automatically.

## 5. Apply and accept

Inspect the diff and verification evidence, explicitly apply or reject the result, then record product acceptance separately from engine completion.

## Safety boundaries

Atlas does not automatically commit, push, deploy, publish, delete repositories, or write outside the declared project boundary. Keep credentials out of prompts and evidence, and stop when a decision requires human review.
`);

export function Tutorial() {
  const { lang } = useLang();
  const md = useMemo(
    () => lang === "zh" ? forWeb(tutorialMd) : tutorialEnglish,
    [lang],
  );
  return (
    <main className="mx-auto max-w-3xl px-4 py-10">
      <h1 className="font-serif text-3xl font-medium">{t("tutorial", lang)}</h1>
      <section aria-labelledby="template-start" className="mt-6 rounded-2xl border border-border bg-surface p-6 shadow-card">
        <p className="text-xs font-medium text-primary">{lang === "zh" ? "使用现有模板" : "Use an existing template"}</p>
        <h2 id="template-start" className="mt-2 font-serif text-2xl font-medium">{lang === "zh" ? "从场景到开发包" : "From a scenario to a development package"}</h2>
        <ol className="mt-4 list-decimal space-y-3 pl-5 text-sm leading-6 text-muted">
          <li>{lang === "zh" ? "在「浏览类型」打开对应叶子，查看具体场景与辅助模板；也可直接在「模板制品」中查找。" : "Open a leaf in Browse types to find its scenarios and assisted templates, or search Artifacts directly."}</li>
          <li>{lang === "zh" ? "阅读适用用户、核心能力和限制，回查固定案例。静态审阅通过与应用运行验证是两种状态；已有运行证据也不表示示例服务此刻在线。" : "Read the audience, capabilities and limits, and inspect pinned cases. Static review and application runtime verification are separate; recorded evidence does not mean an example service is currently online."}</li>
          <li>{lang === "zh" ? "下载标准开发包，将详情页的「Codex 开始说明」与开发包一起交给新开发上下文。从 HANDOFF 开始阅读，按当前阶段实现与自检。" : "Download the standard development package and give it, together with the template's Codex start instructions, to a fresh development context. Start with HANDOFF, then implement and verify the current phase."}</li>
        </ol>
        <div className="mt-5 flex flex-wrap gap-4 text-sm">
          <Link to="/factory?view=artifacts" className="inline-flex items-center gap-1 font-medium text-primary hover:underline">{lang === "zh" ? "查找辅助模板" : "Find assisted templates"}<ArrowRight className="size-4" /></Link>
          <Link to="/browse" className="inline-flex items-center gap-1 text-primary hover:underline">{lang === "zh" ? "从叶子类型开始" : "Start from a type"}<ArrowRight className="size-4" /></Link>
        </div>
      </section>
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
