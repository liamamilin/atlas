import { useNavigate, Link } from "react-router-dom";
import { ArrowRight, Boxes, Compass, FolderKanban, Layers, Sparkles, Wrench } from "lucide-react";
import { useState } from "react";
import { getMeta } from "@/lib/atlas";
import { useAsync, Loading, ErrorBox } from "@/components/loaders";
import { Button } from "@/components/ui/button";
import { useLang, t, pick } from "@/lib/lang";

export function Home() {
  const navigate = useNavigate();
  const { lang } = useLang();
  const [q, setQ] = useState("");
  const { data: meta, error, loading } = useAsync(getMeta, []);

  return (
    <main>
      <section className="border-b border-border">
        <div className="mx-auto max-w-3xl px-4 py-16 md:py-24">
          <p className="text-sm font-medium tracking-wide text-primary">{t("heroKicker", lang)}</p>
          <h1 className="mt-3 font-serif text-4xl font-medium leading-[1.15] tracking-tight md:text-5xl">
            {t("heroTitle", lang, { n: meta?.leafCount ?? "…" })}
          </h1>
          <div className="mt-5 max-w-xl">
            <p className="text-base font-medium leading-relaxed text-foreground md:text-lg">
              {t("heroLead", lang)}
            </p>
            <p className="mt-3 text-base leading-relaxed text-muted md:text-lg">
              {t("heroP", lang)}
            </p>
          </div>
          <form
            className="mt-8"
            onSubmit={(e) => {
              e.preventDefault();
              navigate({ pathname: "/search", search: `?q=${encodeURIComponent(q.trim())}` });
            }}
          >
            <label className="block">
              <span className="sr-only">{t("searchLabel", lang)}</span>
              <input
                value={q}
                onChange={(e) => setQ(e.target.value)}
                placeholder={t("searchPlaceholder", lang)}
                className="h-14 w-full rounded-xl bg-surface px-4 text-base shadow-card placeholder:text-subtle focus:outline-none focus:ring-2 focus:ring-primary/35"
              />
            </label>
            <div className="mt-3 flex flex-wrap gap-2">
              <Button type="submit" size="lg">
                {t("searchBtn", lang)} <ArrowRight className="size-4" />
              </Button>
              <Button asChild size="lg" variant="outline">
                <Link to="/browse">{t("browseAll", lang)}</Link>
              </Button>
            </div>
          </form>
        </div>
      </section>

      {loading ? <Loading /> : error ? <ErrorBox message={error} /> : meta ? (
        <>
          <section className="mx-auto max-w-6xl px-4 py-10">
            <div className="grid gap-4 sm:grid-cols-3">
              {[
                { icon: Layers, n: meta.leafCount, label: t("leafCount", lang), to: "/browse" },
                { icon: Compass, n: meta.sectionCount, label: t("secCount", lang), to: "/browse" },
                { icon: Boxes, n: meta.appCount, label: t("appCount", lang), to: "/apps" },
              ].map((s) => (
                <Link
                  key={s.label}
                  to={s.to}
                  className="block rounded-xl bg-surface p-5 shadow-card transition-shadow hover:shadow-card-hover"
                >
                  <s.icon className="size-5 text-primary" />
                  <div className="mt-3 font-serif text-3xl font-medium">{s.n}</div>
                  <div className="mt-1 text-sm text-muted">{s.label}</div>
                </Link>
              ))}
            </div>
          </section>

          <section className="mx-auto max-w-6xl px-4 pb-10">
            <div className="rounded-2xl bg-primary/[0.06] p-6 ring-1 ring-primary/15 md:p-8">
              <div className="max-w-2xl">
                <p className="text-xs font-medium tracking-wide text-primary">{lang === "zh" ? "从案例开始" : "Start with a case"}</p>
                <h2 className="mt-2 font-serif text-2xl font-medium">{lang === "zh" ? "先选一种工作方式，再进入项目工作台" : "Choose a working mode, then enter the project workspace"}</h2>
                <p className="mt-2 text-sm leading-6 text-muted">
                  {lang === "zh"
                    ? "Atlas 先固定类型资料，再帮助你形成需求、文档、开发计划和验收记录。你可以从新想法、已有项目或 Agent Harness 调研开始。"
                    : "Atlas pins type evidence first, then helps you form requirements, documents, a development plan, and acceptance records. Start with a new idea, an existing project, or an Agent Harness study."}
                </p>
              </div>
              <div className="mt-6 grid gap-3 md:grid-cols-3">
                <CaseEntry
                  icon={Sparkles}
                  title={lang === "zh" ? "新想法" : "New idea"}
                  description={lang === "zh" ? "从一句目标开始，逐步收敛范围。" : "Start with one objective and narrow the scope."}
                  to="/projects"
                  action={lang === "zh" ? "创建项目" : "Create project"}
                />
                <CaseEntry
                  icon={Wrench}
                  title={lang === "zh" ? "已有项目改进" : "Improve an existing project"}
                  description={lang === "zh" ? "读取本地工作区，先建立基线再规划改动。" : "Read a local workspace, accept a baseline, then plan changes."}
                  to="/projects?mode=existing"
                  action={lang === "zh" ? "进入改进流程" : "Start improvement"}
                />
                <CaseEntry
                  icon={FolderKanban}
                  title={lang === "zh" ? "Agent Harness 调研" : "Agent Harness study"}
                  description={lang === "zh" ? "用 Atlas 调研类型，生成文档并验证一个最小纵向切片。" : "Research the type in Atlas, generate docs, and validate a vertical slice."}
                  to="/projects?fromType=ai-coding-agent"
                  action={lang === "zh" ? "从类型创建" : "Create from type"}
                />
              </div>
            </div>
          </section>

          <section className="mx-auto max-w-6xl px-4 pb-16">
            <h2 className="font-serif text-2xl font-medium">{t("byDomain", lang)}</h2>
            <p className="mt-2 text-sm text-muted">{t("byDomainP", lang)}</p>
            <div className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {meta.l0s.map((l0) => {
                const leafN = meta.leafIndex.filter((x) => x.sec === l0.id || l0.subs.some((s) => s.id === x.sec)).length;
                return (
                  <Link
                    key={l0.id}
                    to={`/browse#${l0.id}`}
                    className="rounded-xl bg-surface p-5 shadow-card transition-shadow hover:shadow-card-hover"
                  >
                    <div className="text-xs text-subtle">{l0.id}</div>
                    <h3 className="mt-1 font-medium">{pick(lang, l0.name_zh, l0.name)}</h3>
                    <div className="mt-1.5 text-xs text-muted">
                      {l0.subs.length > 0 ? (
                        <>
                          {l0.subs.length}{t("subs", lang)} ·{" "}
                        </>
                      ) : null}
                      {leafN}{t("types", lang)}
                    </div>
                  </Link>
                );
              })}
            </div>
          </section>
        </>
      ) : null}
    </main>
  );
}

function CaseEntry({ icon: Icon, title, description, to, action }: {
  icon: typeof Sparkles;
  title: string;
  description: string;
  to: string;
  action: string;
}) {
  return (
    <Link to={to} className="group rounded-xl bg-surface p-5 shadow-card transition-shadow hover:shadow-card-hover">
      <Icon className="size-5 text-primary" />
      <h3 className="mt-3 font-medium">{title}</h3>
      <p className="mt-1.5 min-h-10 text-sm leading-5 text-muted">{description}</p>
      <span className="mt-4 inline-flex items-center gap-1 text-sm font-medium text-primary">
        {action}<ArrowRight className="size-4 transition-transform group-hover:translate-x-0.5" />
      </span>
    </Link>
  );
}
