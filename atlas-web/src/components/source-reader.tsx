import { useEffect, useMemo, useState } from "react";
import { BookmarkPlus, BookOpen, CheckCircle2 } from "lucide-react";
import { Link } from "react-router-dom";
import { ErrorBox, Loading, useAsync } from "@/components/loaders";
import { Prose } from "@/components/prose";
import { Button } from "@/components/ui/button";
import {
  getCompleteSource,
  getSourceManifest,
  saveProjectReference,
  type AtlasSourceKind,
} from "@/lib/atlas";
import { useLang } from "@/lib/lang";
import { useCurrentProjectId } from "@/lib/project-selection";

export function SourceReader({ slug }: { slug: string }) {
  const { lang } = useLang();
  const [projectId] = useCurrentProjectId();
  const [kind, setKind] = useState<AtlasSourceKind>("application");
  const [section, setSection] = useState("");
  const [note, setNote] = useState("");
  const [saving, setSaving] = useState(false);
  const [saveState, setSaveState] = useState<{ ok: boolean; message: string } | null>(null);
  const manifestState = useAsync(() => getSourceManifest(slug), [slug]);
  const source = useMemo(
    () => manifestState.data?.sources.find((item) => item.kind === kind) ?? null,
    [manifestState.data, kind],
  );
  const contentState = useAsync(
    () => source ? getCompleteSource(slug, kind, section || undefined) : Promise.resolve(null),
    [slug, kind, section, source?.fingerprint],
  );

  useEffect(() => {
    const sources = manifestState.data?.sources;
    if (sources?.length && !sources.some((item) => item.kind === kind)) {
      setKind(sources[0].kind);
      setSection("");
    }
  }, [manifestState.data, kind]);

  useEffect(() => {
    if (section && source && !source.outline.some((item) => item.id === section)) setSection("");
  }, [source, section]);

  const collect = async () => {
    if (!projectId || !source) return;
    setSaving(true);
    setSaveState(null);
    try {
      await saveProjectReference(projectId, {
        kind,
        slug,
        section: section || undefined,
        note,
        read_status: "read",
      });
      setSaveState({
        ok: true,
        message: lang === "zh" ? "已按当前来源版本收藏到项目。" : "Saved to the project at this source version.",
      });
    } catch (cause) {
      const message = String(cause).includes("already saved")
        ? (lang === "zh" ? "这个版本和章节已经收藏。" : "This version and section are already saved.")
        : String(cause);
      setSaveState({ ok: false, message });
    } finally {
      setSaving(false);
    }
  };

  if (manifestState.loading && !manifestState.data) return <Loading />;
  if (manifestState.error || !manifestState.data) {
    return <ErrorBox message={manifestState.error || "source manifest unavailable"} />;
  }

  return (
    <section className="mt-8 rounded-xl bg-surface p-5 shadow-card">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div>
          <h2 className="flex items-center gap-2 font-serif text-xl font-medium">
            <BookOpen className="size-5 text-primary" />
            {lang === "zh" ? "正式资料阅读器" : "Canonical source reader"}
          </h2>
          <p className="mt-1 text-xs leading-5 text-subtle">
            {lang === "zh"
              ? "直接读取语料中的正式 Markdown；收藏时由服务端再次读取并固定来源版本。"
              : "Reads canonical corpus Markdown; collection re-reads and pins the source version on the server."}
          </p>
        </div>
        <div className="flex rounded-lg bg-chip p-1">
          {manifestState.data.sources.map((item) => (
            <button
              key={item.kind}
              type="button"
              disabled={saving}
              onClick={() => { setKind(item.kind); setSection(""); setSaveState(null); }}
              className={`rounded-md px-3 py-1.5 text-xs font-medium ${kind === item.kind ? "bg-surface text-primary shadow-card" : "text-muted"}`}
            >
              {sourceLabel(item.kind, lang)}
            </button>
          ))}
        </div>
      </div>

      {source ? (
        <div className="mt-5 grid gap-3 sm:grid-cols-[minmax(0,1fr)_auto] sm:items-end">
          <label className="block text-sm">
            <span className="text-muted">{lang === "zh" ? "阅读范围" : "Reading scope"}</span>
            <select
              value={section}
              disabled={saving}
              onChange={(event) => { setSection(event.target.value); setSaveState(null); }}
              className="mt-1.5 h-11 w-full rounded-md border border-border bg-bg-elevated px-3 outline-none focus:ring-2 focus:ring-primary/35"
            >
              <option value="">{lang === "zh" ? "完整文档" : "Full document"}</option>
              {source.outline.map((item) => (
                <option key={item.id} value={item.id}>
                  {`${"　".repeat(Math.max(0, item.level - 1))}${item.title}`}
                </option>
              ))}
            </select>
          </label>
          <p className="pb-3 font-mono text-[11px] text-subtle">
            {source.lines} {lang === "zh" ? "行" : "lines"} · {source.chars.toLocaleString()} chars · {source.fingerprint.slice(0, 10)}
          </p>
        </div>
      ) : null}

      {contentState.loading ? <Loading>{lang === "zh" ? "读取正式资料中…" : "Reading source…"}</Loading> :
        contentState.error ? <ErrorBox message={contentState.error} /> : contentState.data ? (
          <div className="mt-5 max-h-[42rem] overflow-y-auto rounded-lg border border-border bg-bg-elevated p-5">
            <Prose md={contentState.data.content} />
          </div>
        ) : null}

      <div className="mt-5 border-t border-border pt-5">
        {projectId ? (
          <div className="grid gap-3 sm:grid-cols-[minmax(0,1fr)_auto] sm:items-end">
            <label className="block text-sm">
              <span className="text-muted">{lang === "zh" ? "借鉴点 / 项目备注（可选）" : "Takeaway / project note (optional)"}</span>
              <textarea
                rows={2}
                value={note}
                onChange={(event) => setNote(event.target.value)}
                placeholder={lang === "zh" ? "记录准备借鉴什么、哪些边界需要保留…" : "Record what to borrow and which boundaries to preserve…"}
                className="mt-1.5 w-full rounded-md border border-border bg-bg-elevated px-3 py-2.5 text-sm outline-none focus:ring-2 focus:ring-primary/35"
              />
            </label>
            <Button onClick={collect} disabled={saving || !source || contentState.loading}>
              <BookmarkPlus className="size-4" />
              {saving ? (lang === "zh" ? "收藏中…" : "Saving…") : (lang === "zh" ? "收藏当前范围" : "Save current scope")}
            </Button>
          </div>
        ) : (
          <p className="text-sm text-muted">
            {lang === "zh" ? "先在" : "Select a project in "}
            <Link to={`/projects?fromType=${encodeURIComponent(slug)}`} className="mx-1 text-primary hover:underline">
              {lang === "zh" ? "项目工作台" : "Projects"}
            </Link>
            {lang === "zh" ? "选择项目，再收藏全文或当前章节。" : "before saving a document or section."}
          </p>
        )}
        {saveState ? (
          <p className={`mt-3 flex items-center gap-2 text-sm ${saveState.ok ? "text-ok" : "text-danger"}`}>
            {saveState.ok ? <CheckCircle2 className="size-4" /> : null}{saveState.message}
          </p>
        ) : null}
      </div>
    </section>
  );
}

function sourceLabel(kind: AtlasSourceKind, lang: "zh" | "en") {
  if (kind === "application") return lang === "zh" ? "类型正文" : "Type document";
  return lang === "zh" ? "研究笔记" : "Research notes";
}
