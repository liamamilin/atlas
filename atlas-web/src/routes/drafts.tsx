import { useEffect, useRef, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { FilePlus2, RefreshCw, Trash2, ExternalLink } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Prose } from "@/components/prose";
import { Loading, ErrorBox } from "@/components/loaders";
import { useLang, t, type Lang } from "@/lib/lang";
import { invalidateAtlasCache } from "@/lib/atlas";
import { cn } from "@/lib/utils";

interface DraftItem {
  slug: string;
  name: string;
  name_zh: string;
  status: string;
  created: string;
  engine: string;
  size: number;
  lint_ok: boolean;
  lint_errors: number;
  dup?: { verdict: string; best: string | null } | null;
}
interface Collision {
  slug: string;
  sim: number;
}
interface DraftDetail {
  slug: string;
  front: Record<string, string>;
  body: string;
  research: string | null;
  research_zh: string | null;
  zh: Record<string, string> | null;
  lint: { ok: boolean; errors: string[]; warnings: string[]; size: number };
  progress?: {
    body_chars: number;
    research_chars: number;
    last_h2: string;
    sections_done: number;
    log_tail: string[];
    updated_at: number;
  };
  collision: [string, number][];
  review: {
    current?: boolean;
    final_slug?: string;
    verdict?: string;
    best?: string | null;
    reason?: string;
    section_hint?: string | null;
    top?: [string, number][];
    promote_error?: string;
    promoted?: boolean;
    gate?: string;
    gate_ok?: boolean;
    identity?: { verdict?: string; best?: string | null; reason?: string } | null;
  };
}

async function get<T>(path: string): Promise<T> {
  const r = await fetch(path);
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  return r.json() as Promise<T>;
}

function useDrafts() {
  const [state, setState] = useState<{ data: DraftItem[] | null; error: string | null }>({
    data: null,
    error: null,
  });
  const [loading, setLoading] = useState(true);
  const [reload, setReload] = useState(0);
  useEffect(() => {
    let alive = true;
    setLoading(true);
    get<DraftItem[]>("/api/drafts").then(
      (d) => alive && (setState({ data: d, error: null }), setLoading(false)),
      (e) => alive && (setState({ data: null, error: String(e) }), setLoading(false)),
    );
    return () => {
      alive = false;
    };
  }, [reload]);
  const generating = state.data?.some((d) => ["generating", "promoting"].includes(d.status)) ?? false;
  useEffect(() => {
    if (!generating) return;
    const id = setInterval(() => {
      get<DraftItem[]>("/api/drafts").then(
        (d) => setState({ data: d, error: null }),
        () => {},
      );
    }, 4000);
    return () => clearInterval(id);
  }, [generating]);
  return { ...state, loading, refetch: () => setReload((v) => v + 1) };
}

const STATUS: Record<string, { zh: string; en: string }> = {
  generating: { zh: "生成中", en: "generating" },
  draft: { zh: "草稿", en: "draft" },
  failed: { zh: "生成失败", en: "failed" },
  promoting: { zh: "入库中", en: "promoting" },
  promoted: { zh: "已入库", en: "promoted" },
};

function GenProgress({ p, lang }: { p: DraftDetail["progress"]; lang: Lang }) {
  const [now, setNow] = useState(Date.now());
  useEffect(() => {
    const id = setInterval(() => setNow(Date.now()), 1000);
    return () => clearInterval(id);
  }, []);
  const age = p?.updated_at ? Math.max(0, Math.floor((now / 1000 - p.updated_at))) : null;
  return (
    <div className="mt-4 rounded-xl bg-surface p-4 text-xs shadow-card">
      <div className="flex flex-wrap items-center gap-x-4 gap-y-1 text-muted">
        <span>
          {t("genResearch", lang)}{" "}
          {p && p.research_chars > 0 ? (
            <b className="text-fg">{p.research_chars.toLocaleString()}</b>
          ) : (
            <span className="text-yellow-700">…</span>
          )}
        </span>
        <span>
          {t("genBody", lang)} <b className="text-fg tabular-nums">{(p?.body_chars ?? 0).toLocaleString()}</b>
        </span>
        {p?.last_h2 ? (
          <span>
            {t("genSection", lang)} <b className="text-fg">{p.last_h2}</b>
            {p.sections_done ? <span className="text-subtle"> · H2×{p.sections_done}</span> : null}
          </span>
        ) : null}
        <span className="text-subtle">
          {t("genUpdated", lang)} {age ?? "–"}s
        </span>
      </div>
      {p && p.log_tail.length ? (
        <details className="mt-2 text-[11px] text-subtle">
          <summary className="cursor-pointer select-none hover:text-muted">{t("genLog", lang)}</summary>
          <pre className="mt-1 overflow-hidden whitespace-pre-wrap font-mono leading-relaxed">
            {p.log_tail.slice(-3).join("\n")}
          </pre>
        </details>
      ) : null}
      <p className="mt-2 text-[11px] text-subtle">{t("draftGenBanner", lang)}</p>
    </div>
  );
}

function StatusChip({ status, lint_ok }: { status: string; lint_ok: boolean }) {
  const { lang } = useLang();
  const s = STATUS[status];
  const color =
    status === "draft" && lint_ok
      ? "bg-primary/10 text-primary"
      : status === "generating"
        ? "bg-yellow-500/10 text-yellow-700"
        : status === "failed" || (status !== "generating" && !lint_ok)
          ? "bg-red-500/10 text-red-700"
          : "bg-chip text-muted";
  return (
    <span className={cn("rounded-full px-2.5 py-0.5 text-xs font-medium", color)}>
      {(s ? s[lang] : status) + (status === "draft" && !lint_ok ? " · lint FAIL" : "")}
    </span>
  );
}

function DraftRow({ d, lang }: { d: DraftItem; lang: Lang }) {
  const name = d.dup
    ? (lang === "zh" ? "查重拦截 · " : "Dedupe stop · ") + (d.dup.best ?? "")
    : lang === "zh"
      ? d.name_zh || d.name
      : d.name;
  return (
    <div className="flex items-center gap-4 rounded-xl bg-surface p-4 shadow-card">
      <div className="min-w-0 flex-1">
        <div className="flex items-center gap-2">
          <h3 className="truncate font-medium">{name}</h3>
          {d.dup ? (
            <span className="rounded-full bg-yellow-500/10 px-2.5 py-0.5 text-xs font-medium text-yellow-700">
              {t("dupChip", lang)}
            </span>
          ) : (
            <StatusChip status={d.status} lint_ok={d.lint_ok} />
          )}
        </div>
        <div className="mt-0.5 text-xs text-subtle">
          {d.slug} · {d.size.toLocaleString()} 字符 · {d.created} · {d.engine}
        </div>
      </div>
      <Link to={`/drafts/${d.slug}`} className="text-xs text-primary hover:underline">
        {lang === "zh" ? "查看" : "Open"}
      </Link>
    </div>
  );
}

export function Drafts() {
  const { lang } = useLang();
  const { data, error, loading, refetch } = useDrafts();
  const [creating, setCreating] = useState(false);
  if (loading) return <Loading />;
  if (error || !data) return <ErrorBox message={error ?? ""} />;
  return (
    <main className="mx-auto max-w-5xl px-4 py-10">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="font-serif text-3xl font-medium">{t("draftsTitle", lang)}</h1>
          <p className="mt-2 text-sm text-muted">{t("draftsP", lang)}</p>
        </div>
        <Button onClick={() => setCreating((v) => !v)}>
          <FilePlus2 className="size-4" /> {t("draftNew", lang)}
        </Button>
      </div>
      {creating ? <CreateForm onDone={refetch} /> : null}
      <div className="mt-8 space-y-3">
        {data.length === 0 ? <p className="text-sm text-subtle">{t("draftsEmpty", lang)}</p> : null}
        {data.map((d) => (
          <DraftRow key={d.slug} d={d} lang={lang} />
        ))}
      </div>
    </main>
  );
}

function CreateForm({ onDone }: { onDone: () => void }) {
  const { lang } = useLang();
  const nav = useNavigate();
  const [form, setForm] = useState({ name: "", name_zh: "", desc: "", link: "" });
  const [force, setForce] = useState(false);
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState("");
  const submit = async () => {
    setBusy(true);
    setErr("");
    try {
      const r = await fetch("/api/drafts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ...form, force }),
      });
      const j = await r.json();
      if (!r.ok) {
        setErr(
          [j.error, ...(j.collision ?? []).map((c: Collision) => `${c.sim.toFixed(3)} ${c.slug}`)].join(" · "),
        );
      } else {
        onDone();
        nav(`/drafts/${j.slug}`);
      }
    } catch (e) {
      setErr(String(e));
    } finally {
      setBusy(false);
    }
  };
  const input = (k: keyof typeof form, label: string, ph = "") => (
    <label className="block text-sm">
      <span className="text-muted">{label}</span>
      <input
        value={form[k]}
        onChange={(e) => setForm({ ...form, [k]: e.target.value })}
        placeholder={ph}
        className="mt-1 h-10 w-full rounded-lg bg-bg px-3 shadow-card placeholder:text-subtle focus:outline-none focus:ring-2 focus:ring-primary/35"
      />
    </label>
  );
  return (
    <form
      className="mt-6 space-y-3 rounded-xl bg-surface p-5 shadow-card"
      onSubmit={(e) => {
        e.preventDefault();
        submit();
      }}
    >
      <div className="grid gap-3 sm:grid-cols-2">
        {input("name", t("draftNameEn", lang), "CLI Accounting Tool")}
        {input("name_zh", t("draftNameZh", lang), "命令行记账工具")}
      </div>
      {input("desc", t("draftDesc", lang), t("draftDescPh", lang))}
      {input("link", t("draftLink", lang), "https://…")}
      <label className="flex items-center gap-2 text-xs text-muted">
        <input type="checkbox" checked={force} onChange={(e) => setForce(e.target.checked)} />
        {t("draftForce", lang)}
      </label>
      {err ? <p className="text-xs text-danger">{err}</p> : null}
      <Button type="submit" disabled={busy || (!form.desc.trim() && !form.link.trim())}>
        {busy ? t("draftCreating", lang) : t("draftCreate", lang)}
      </Button>
      <p className="text-xs text-subtle">{t("draftCreateHint", lang)}</p>
    </form>
  );
}

export function DraftDetailPage({ slug }: { slug: string }) {
  const { lang } = useLang();
  const { data, error, loading, refetch } = useAsyncDraft(slug);
  useEffect(() => {
    if (data?.review.promoted) invalidateAtlasCache();
  }, [data?.review.promoted]);
  const bodyRef = useRef<HTMLTextAreaElement>(null);
  const [msg, setMsg] = useState("");
  if (loading) return <Loading />;
  if (error || !data) return <ErrorBox message={error ?? ""} />;
  const dirty = bodyRef.current && bodyRef.current.value !== data.body;
  const save = async () => {
    if (!bodyRef.current) return;
    const r = await fetch(`/api/drafts/${slug}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ body: bodyRef.current.value }),
    });
    setMsg(r.ok ? t("draftSaved", lang) : `HTTP ${r.status}`);
    if (r.ok) refetch();
  };
  const del = async () => {
    if (!confirm(t("draftDelConfirm", lang))) return;
    await fetch(`/api/drafts/${slug}`, { method: "DELETE" });
    location.href = "/drafts";
  };
  const dedupe = async () => {
    const r = await fetch("/api/dedupe", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ slug }),
    });
    setMsg(r.ok ? t("draftDeduped", lang) : `HTTP ${r.status}`);
    setTimeout(() => location.reload(), 500);
  };
  const translate = async () => {
    const r = await fetch(`/api/drafts/${slug}/translate`, { method: "POST" });
    setMsg(r.ok ? t("draftTranslating", lang) : `HTTP ${r.status}`);
    if (r.ok) setTimeout(() => location.reload(), 60000);
  };
  const name = lang === "zh" ? data.front.name_zh || data.front.name : data.front.name;
  const dup = data.review?.identity && (data.review.identity.verdict === "same" ||
    data.review.identity.verdict === "variant") ? data.review.identity : null;
  const dupName = dup ? (lang === "zh" ? "查重拦截 · " : "Dedupe stop · ") + dup.best : "";
  return (
    <main className="mx-auto max-w-5xl px-4 py-10">
      <div className="flex items-start justify-between gap-4">
        <div>
          <h1 className="font-serif text-2xl font-medium">{dup ? dupName : name}</h1>
          <div className="mt-1 flex items-center gap-2 text-xs text-subtle">
            {dup ? (
              <span className="rounded-full bg-yellow-500/10 px-2.5 py-0.5 text-xs font-medium text-yellow-700">
                {t("dupChip", lang)}
              </span>
            ) : (
              <StatusChip status={data.front.status} lint_ok={data.lint.ok} />
            )}
            <span>{slug}</span>
            <span>·</span>
            <span>{data.lint.size.toLocaleString()} 字符</span>
          </div>
        </div>
        <div className="flex shrink-0 gap-2">
          <Button variant="outline" size="sm" onClick={dedupe}>
            <RefreshCw className="size-4" /> {t("draftDedupe", lang)}
          </Button>
          <Button variant="outline" size="sm" onClick={del}>
            <Trash2 className="size-4" /> {t("draftDelete", lang)}
          </Button>
        </div>
      </div>
      {msg ? <p className="mt-2 text-xs text-muted">{msg}</p> : null}
      {data.front.status === "generating" ? <GenProgress p={data.progress} lang={lang} /> : null}
      {data.front.name_source === "model" && data.front.status !== "generating" ? (
        <div className="mt-4 rounded-xl bg-surface p-4 text-xs shadow-card">
          <p>
            <span className="font-medium text-muted">{t("genNamedLabel", lang)} </span>
            <b>{data.front.name}</b>
            {data.front.name_zh ? <span>（{data.front.name_zh}）</span> : null}
          </p>
          {data.front.desc ? <p className="mt-1 text-muted">{data.front.desc}</p> : null}
          <p className="mt-1 text-subtle">{t("genNamedHint", lang)}</p>
        </div>
      ) : null}
      {data.lint.size > 0 &&
      (data.lint.errors.length || data.lint.warnings.length) ? (
        <div className="mt-4 rounded-xl bg-surface p-4 text-xs shadow-card">
          {data.lint.errors.map((e) => (
            <p key={e} className="text-danger">ERROR {e}</p>
          ))}
          {data.lint.warnings.map((w) => (
            <p key={w} className="text-muted">warn {w}</p>
          ))}
        </div>
      ) : null}
      {data.collision.length ? (
        <div className="mt-4 rounded-xl bg-surface p-4 text-xs shadow-card">
          <p className="font-medium text-muted">{t("draftCollision", lang)}</p>
          <div className="mt-2 grid gap-1 sm:grid-cols-2">
            {data.collision.map(([s, sim]) => (
              <Link key={s} to={`/types/${s}`} className="flex items-center gap-2 text-muted hover:text-fg">
                <span className="tabular-nums">{sim.toFixed(3)}</span>
                {s} <ExternalLink className="size-3" />
              </Link>
            ))}
          </div>
        </div>
      ) : null}
      <VerdictPanel data={data} lang={lang} onChanged={refetch} />
      <div className="mt-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <h2 className="text-sm font-medium text-muted">{t("draftBody", lang)}</h2>
            {lang === "zh" && data.zh ? (
              <span className="text-xs text-subtle">{t("draftViewZh", lang)}</span>
            ) : null}
            {!data.zh ? (
              <button
                type="button"
                onClick={translate}
                className="text-xs text-primary hover:underline"
              >
                {t("draftTranslate", lang)}
              </button>
            ) : null}
          </div>
          {!(lang === "zh" && data.zh) && dirty ? (
            <Button size="sm" onClick={save}>
              {t("draftSave", lang)}
            </Button>
          ) : null}
        </div>
        {lang === "zh" && data.zh ? (
          <div className="mt-2 max-h-[70vh] overflow-y-auto rounded-xl bg-surface p-4 shadow-card">
            {(["overview", "how", "rules", "variants", "products"] as const).map((k) =>
              data.zh?.[k] ? (
                <div key={k} className="mb-4">
                  <p className="mb-1 text-xs font-medium text-subtle">
                    {({ overview: "概览", how: "工作结构", rules: "重要规则", variants: "变体", products: "代表产品" })[k]}
                  </p>
                  <Prose md={data.zh[k]!} />
                </div>
              ) : null,
            )}
          </div>
        ) : (
          <textarea
            key={slug}
            ref={bodyRef}
            defaultValue={data.body}
            spellCheck={false}
            className="mt-2 h-[70vh] w-full rounded-xl bg-surface p-4 font-mono text-xs leading-relaxed shadow-card focus:outline-none focus:ring-2 focus:ring-primary/30"
          />
        )}
      </div>
      {data.research ? (
        <details className="mt-4 rounded-xl bg-surface p-4 shadow-card">
          <summary className="cursor-pointer text-sm font-medium text-muted">
            {t("draftResearch", lang)}
            {data.research_zh ? (
              <span className="ml-2 text-xs font-normal text-subtle">
                ({t("draftResearchZh", lang)})
              </span>
            ) : null}
          </summary>
          <ResearchBilingual en={data.research} zh={data.research_zh} lang={lang} />
        </details>
      ) : null}
    </main>
  );
}

function ResearchBilingual({ en, zh, lang }: { en: string; zh: string | null; lang: Lang }) {
  const showZh = lang === "zh" && zh;
  return <Prose className="mt-3" md={showZh ? zh! : en} />;
}

function VerdictPanel({
  data,
  lang,
  onChanged,
}: {
  data: DraftDetail;
  lang: Lang;
  onChanged: () => void;
}) {
  const rv = data.review;
  const ready = data.front.status === "draft" && data.lint.ok;
  const [action, setAction] = useState<"new" | "merge">(rv.verdict === "same" || rv.verdict === "variant" ? "merge" : "new");
  const { data: sections } = useAsyncSections();
  const [section, setSection] = useState(rv.section_hint ?? "");
  const [into, setInto] = useState(rv.best ?? "");
  const canPromote = ready && rv.current && (action === "new"
    ? rv.verdict === "new" && Boolean(section)
    : (rv.verdict === "same" || rv.verdict === "variant") && into === rv.best);
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState("");
  const verdictLabel: Record<string, { zh: string; en: string }> = {
    same: { zh: "同一物（不建议成叶）", en: "same type (no new leaf)" },
    variant: { zh: "变体（建议并入）", en: "variant (merge recommended)" },
    new: { zh: "真新类型", en: "genuinely new" },
    error: { zh: "裁决出错", en: "error" },
  };
  const promote = async () => {
    setBusy(true);
    setErr("");
    try {
      const r = await fetch("/api/promote", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ slug: data.slug, action, section, into }),
      });
      const j = await r.json();
      if (!r.ok) setErr(j.error ?? `HTTP ${r.status}`);
      else onChanged();
    } catch (e) {
      setErr(String(e));
    } finally {
      setBusy(false);
    }
  };
  return (
    <div className="mt-4 rounded-xl bg-surface p-4 shadow-card">
      <div className="flex items-center justify-between">
        <p className="text-sm font-medium text-muted">{t("draftVerdict", lang)}</p>
        {rv.promoted ? (
          <span className={cn("rounded-full px-2.5 py-0.5 text-xs font-medium", rv.gate_ok === false ? "bg-danger/10 text-danger" : "bg-primary/10 text-primary")}>
            {t("draftPromoted", lang)} {rv.gate ? `· gate ${rv.gate}` : ""}
          </span>
        ) : (
          <Button size="sm" disabled={busy || !canPromote} onClick={promote}>
            {busy ? t("draftPromoting", lang) : t("draftPromote", lang)}
          </Button>
        )}
      </div>
      {!canPromote && !rv.promoted ? (
        <p className="mt-1 text-xs text-subtle">{!ready ? t("draftPromoteLocked", lang) : !rv.current
          ? (lang === "zh" ? "请先对当前正文重新查重。" : "Run deduplication on the current draft first.")
          : (lang === "zh" ? "请选择与查重裁决一致的操作和目标。" : "Choose the action and target approved by deduplication.")}</p>
      ) : null}
      {rv.verdict ? (
        <div className="mt-2 text-xs text-muted">
          <span className={cn("font-medium", rv.verdict === "new" ? "text-primary" : "text-muted")}>
            {verdictLabel[rv.verdict]?.[lang] ?? rv.verdict}
          </span>
          {rv.best ? (
            <>
              {" · "}
              <Link to={`/types/${rv.best}`} className="hover:text-fg">
                {rv.best}
              </Link>
            </>
          ) : null}
          {rv.reason ? <span> — {rv.reason}</span> : null}
        </div>
      ) : (
        <p className="mt-1 text-xs text-subtle">{t("draftNoVerdict", lang)}</p>
      )}
      {rv.promote_error || err ? <p className="mt-2 text-xs text-danger">{err || rv.promote_error}</p> : null}
      {rv.promoted && rv.final_slug ? <Link className="mt-2 block text-sm text-primary" to={`/types/${rv.final_slug}`}>{lang === "zh" ? "查看正式类型" : "View published type"}</Link> : null}
      {!rv.promoted && ready ? (
        <div className="mt-3 flex flex-wrap items-center gap-2 text-xs">
          <label className="flex items-center gap-1">
            <input
              type="radio"
              checked={action === "new"}
              onChange={() => setAction("new")}
            />
            {t("draftActionNew", lang)}
          </label>
          {action === "new" ? (
            <select
              value={section}
              onChange={(e) => setSection(e.target.value)}
              className="h-8 max-w-72 rounded-lg bg-bg px-2 shadow-card focus:outline-none"
            >
              <option value="">{t("draftPickSection", lang)}</option>
              {(sections ?? []).map((s) => (
                <option key={s.id} value={s.id}>
                  {s.id} {lang === "zh" ? s.name_zh || s.name : s.name}
                </option>
              ))}
            </select>
          ) : null}
          <label className="flex items-center gap-1">
            <input
              type="radio"
              checked={action === "merge"}
              onChange={() => setAction("merge")}
            />
            {t("draftActionMerge", lang)}
          </label>
          {action === "merge" ? (
            <input
              value={into}
              onChange={(e) => setInto(e.target.value)}
              placeholder="bookkeeping-application"
              className="h-8 w-64 rounded-lg bg-bg px-2 shadow-card focus:outline-none"
            />
          ) : null}
        </div>
      ) : null}
    </div>
  );
}

interface SectionItem {
  id: string;
  name: string;
  name_zh: string;
}

function useAsyncSections() {
  const [state, setState] = useState<{ data: SectionItem[] | null; error: string | null }>({
    data: null,
    error: null,
  });
  useEffect(() => {
    let alive = true;
    get<SectionItem[]>("/api/sections").then(
      (d) => alive && setState({ data: d, error: null }),
      (e) => alive && setState({ data: null, error: String(e) }),
    );
    return () => {
      alive = false;
    };
  }, []);
  return state;
}

function useAsyncDraft(slug: string) {
  const [state, setState] = useState<{ data: DraftDetail | null; error: string | null; loading: boolean }>({
    data: null,
    error: null,
    loading: true,
  });
  const [reload, setReload] = useState(0);
  useEffect(() => {
    let alive = true;
    setState((s) => ({ ...s, loading: true }));
    get<DraftDetail>(`/api/drafts/${slug}`).then(
      (d) => alive && setState({ data: d, error: null, loading: false }),
      (e) => alive && setState({ data: null, error: String(e), loading: false }),
    );
    return () => {
      alive = false;
    };
  }, [slug, reload]);
  const generating = ["generating", "promoting"].includes(state.data?.front.status ?? "");
  useEffect(() => {
    if (!generating) return;
    const id = setInterval(() => {
      get<DraftDetail>(`/api/drafts/${slug}`).then(
        (d) => setState({ data: d, error: null, loading: false }),
        () => {},
      );
    }, 4000);
    return () => clearInterval(id);
  }, [generating, slug]);
  return { ...state, refetch: () => setReload((v) => v + 1) };
}
