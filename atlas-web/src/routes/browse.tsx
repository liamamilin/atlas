import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import { ChevronDown, Search } from "lucide-react";
import { getMeta, getSection } from "@/lib/atlas";
import { useAsync, EmptyState, Loading, ErrorBox } from "@/components/loaders";
import { LeafCard } from "@/components/leaf-card";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { useLang, t, type Lang } from "@/lib/lang";
const pick2 = (zh: string | undefined, en: string, lang: Lang) =>
  lang === "zh" ? (zh && zh.trim()) || en : en || zh || "";

export function Browse() {
  const { lang } = useLang();
  const { data: meta, error, loading } = useAsync(getMeta, []);
  const [query, setQuery] = useState("");
  const hash = useLocation().hash;
  useEffect(() => {
    if (!meta || !hash) return;
    document.getElementById(hash.slice(1))?.scrollIntoView();
  }, [meta, hash]);
  if (loading) return <Loading />;
  if (error || !meta) return <ErrorBox message={error ?? ""} />;
  const keyword = query.trim().toLocaleLowerCase();
  const matches = (item: { name: string; name_zh?: string }) => `${item.name} ${item.name_zh || ""}`.toLocaleLowerCase().includes(keyword);
  const domains = meta.l0s.map(l0 => ({ ...l0, subs: !keyword || matches(l0) ? l0.subs : l0.subs.filter(matches) })).filter(l0 => l0.subs.length > 0);
  return (
    <main className="mx-auto max-w-6xl px-4 py-10">
      <h1 className="font-serif text-3xl font-medium">{t("browseTitle", lang)}</h1>
      <p className="mt-2 text-sm text-muted">
        {t("browseP", lang, { l0: meta.l0Count, sec: meta.sectionCount, leaf: meta.leafCount })}
      </p>
      <div className="mt-6 flex flex-wrap items-end gap-3 rounded-xl border border-border bg-surface p-4">
        <label className="min-w-0 basis-60 flex-1 text-xs text-muted">{lang === "zh" ? "筛选领域与子域" : "Filter domains and subdomains"}<span className="mt-2 flex items-center gap-2"><Search className="size-4 shrink-0" /><input value={query} onChange={e => setQuery(e.target.value)} placeholder={lang === "zh" ? "例如：设计、社交、数据…" : "e.g. design, social, data…"} className="h-10 w-full rounded-lg border border-border bg-bg-elevated px-3 text-sm text-fg" /></span></label>
        <label className="min-w-0 w-full text-xs text-muted sm:w-64">{lang === "zh" ? "快速跳转" : "Jump to a domain"}<select value="" className="mt-2 h-10 w-full rounded-lg border border-border bg-bg-elevated px-3 text-sm text-fg" onChange={e => { if (e.target.value) document.getElementById(e.target.value)?.scrollIntoView({ block: "start" }); }}><option value="">{lang === "zh" ? "选择一个领域" : "Choose a domain"}</option>{domains.map(l0 => <option key={l0.id} value={l0.id}>{l0.id} · {pick2(l0.name_zh, l0.name, lang)}</option>)}</select></label>
        {query && <Button variant="ghost" size="sm" onClick={() => setQuery("")}>{lang === "zh" ? "清除筛选" : "Clear filter"}</Button>}
      </div>
      {domains.length ? (
        <div className="mt-8 space-y-6">
          {domains.map((l0) => (
            <DomainBlock key={l0.id} l0={l0} subs={l0.subs} />
          ))}
        </div>
      ) : (
        <EmptyState
          className="mt-8"
          title={keyword ? (lang === "zh" ? "没有匹配的领域" : "No matching domains") : (lang === "zh" ? "类型目录为空" : "The type catalog is empty")}
        >
          {keyword ? (lang === "zh" ? "可以缩短关键词，或通过导航搜索具体的软件类型。" : "Try a shorter keyword, or use Search to find specific software types.") : (lang === "zh" ? "当前没有可浏览的领域或类型。" : "There are no domains or types to browse yet.")}
        </EmptyState>
      )}
    </main>
  );
}

function DomainBlock({
  l0,
  subs,
}: {
  l0: { id: string; name: string; name_zh?: string };
  subs: { id: string; name: string; name_zh?: string; path: string }[];
}) {
  const { lang } = useLang();
  const [open, setOpen] = useState<string | null>(null);
  return (
    <section id={l0.id} className="scroll-mt-20">
      <h2 className="border-b border-border pb-2 font-serif text-xl font-medium">
        <span className="mr-2 text-sm text-subtle">{l0.id}</span>
        {pick2(l0.name_zh, l0.name, lang)}
      </h2>
      <div className="mt-4 grid min-w-0 items-start gap-4 lg:grid-cols-2">
        {subs.map((s) => (
          <SubBlock key={s.id} sub={s} open={open === s.id} onToggle={() => setOpen(open === s.id ? null : s.id)} />
        ))}
      </div>
    </section>
  );
}

function SubBlock({
  sub,
  open,
  onToggle,
}: {
  sub: { id: string; name: string; name_zh?: string; path: string };
  open: boolean;
  onToggle: () => void;
}) {
  const { lang } = useLang();
  const [retry, setRetry] = useState(0);
  const { data, error } = useAsync(() => (open ? getSection(sub.id) : Promise.resolve(null)), [open, sub.id, retry]);
  return (
    <div className="min-w-0 rounded-xl bg-surface shadow-card">
      <button
        type="button"
        aria-expanded={open}
        aria-controls={`section-${sub.id}`}
        onClick={onToggle}
        className="flex min-w-0 w-full items-center gap-3 p-4 text-left"
      >
        <ChevronDown className={cn("size-4 shrink-0 text-subtle transition-transform", !open && "-rotate-90")} />
        <div className="min-w-0">
          <h3 className="truncate text-[15px] font-medium">{pick2(sub.name_zh, sub.name, lang)}</h3>
          <div className="truncate text-xs text-subtle">{lang === "zh" ? sub.name : sub.path}</div>
        </div>
      </button>
      {open ? (
        <div id={`section-${sub.id}`} className="border-t border-border p-4">
          {error ? (
            <div className="flex flex-wrap items-center justify-between gap-3">
              <p className="text-sm text-danger">{t("loadFailed", lang)}</p>
              <Button size="sm" variant="outline" onClick={() => setRetry((value) => value + 1)}>
                {lang === "zh" ? "重试此领域" : "Retry this section"}
              </Button>
            </div>
          ) : data ? (
            <div className="grid gap-3 sm:grid-cols-2">
              {data.leaves.map((l) => (
                <LeafCard key={l.slug} leaf={l} />
              ))}
            </div>
          ) : (
            <Loading>{t("loadTypes", lang)}</Loading>
          )}
        </div>
      ) : null}
    </div>
  );
}
