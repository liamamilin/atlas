import { useEffect, useState, type FormEvent } from "react";
import { AlertTriangle, BookMarked, FolderKanban, Plus, RefreshCw, Save } from "lucide-react";
import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { ErrorBox, Loading, useAsync } from "@/components/loaders";
import { Prose } from "@/components/prose";
import {
  createProject,
  getProject,
  getProjectReferences,
  getProjects,
  invalidateAtlasCache,
  updateProjectReference,
  type AtlasProject,
  type ProjectReference,
} from "@/lib/atlas";
import { t, useLang } from "@/lib/lang";
import { useCurrentProjectId } from "@/lib/project-selection";

export function Projects() {
  const { lang } = useLang();
  const [revision, setRevision] = useState(0);
  const { data: projects, error, loading } = useAsync(getProjects, [revision]);
  const [selectedId, select] = useCurrentProjectId();
  const [saving, setSaving] = useState(false);
  const [saveError, setSaveError] = useState<string | null>(null);
  const [form, setForm] = useState({ name: "", objective: "", workspace: "", mode: "new" as AtlasProject["mode"] });

  useEffect(() => {
    if (!selectedId) return;
    let active = true;
    getProject(selectedId).catch(() => {
      if (active) select("");
    });
    return () => { active = false; };
  }, [selectedId, select]);

  const submit = async (event: FormEvent) => {
    event.preventDefault();
    setSaving(true);
    setSaveError(null);
    try {
      const project = await createProject(form);
      select(project.id);
      setForm({ name: "", objective: "", workspace: "", mode: "new" });
      setRevision((value) => value + 1);
    } catch (cause) {
      setSaveError(String(cause));
    } finally {
      setSaving(false);
    }
  };

  return (
    <main className="mx-auto max-w-6xl px-4 py-10">
      <p className="text-sm font-medium tracking-wide text-primary">U17</p>
      <h1 className="mt-2 font-serif text-3xl font-medium">{t("projectsTitle", lang)}</h1>
      <p className="mt-2 max-w-2xl text-sm leading-6 text-muted">{t("projectsP", lang)}</p>

      <div className="mt-8 grid gap-6 lg:grid-cols-[minmax(0,1fr)_22rem]">
        <section>
          {loading ? <Loading /> : error ? <ErrorBox message={error} /> : projects?.length ? (
            <div className="grid gap-3">
              {projects.map((project) => {
                const selected = project.id === selectedId;
                return (
                  <article key={project.id} className={`rounded-xl bg-surface p-5 shadow-card ${selected ? "ring-2 ring-primary/35" : ""}`}>
                    <div className="flex items-start gap-3">
                      <FolderKanban className="mt-0.5 size-5 shrink-0 text-primary" />
                      <div className="min-w-0 flex-1">
                        <div className="flex flex-wrap items-center gap-2">
                          <h2 className="font-medium">{project.name}</h2>
                          {selected ? <span className="rounded-full bg-chip px-2 py-0.5 text-xs text-primary">{t("projectCurrent", lang)}</span> : null}
                        </div>
                        <p className="mt-2 text-sm leading-6 text-muted">{project.objective}</p>
                        <p className="mt-3 break-all font-mono text-xs text-subtle">{project.workspace}</p>
                        <div className="mt-4 flex flex-wrap items-center justify-between gap-3">
                          <span className="text-xs text-subtle">
                            {project.mode === "new" ? t("projectModeNew", lang) : t("projectModeExisting", lang)}
                          </span>
                          <div className="flex gap-2">
                            {!selected ? <Button size="sm" variant="outline" onClick={() => select(project.id)}>{t("projectSelect", lang)}</Button> : null}
                            <Button size="sm" asChild><Link to={`/projects/${project.id}`}>{lang === "zh" ? "打开工作区" : "Open workspace"}</Link></Button>
                          </div>
                        </div>
                      </div>
                    </div>
                  </article>
                );
              })}
            </div>
          ) : <div className="rounded-xl bg-surface p-8 text-sm text-muted shadow-card">{t("projectsEmpty", lang)}</div>}
        </section>

        <section className="h-fit rounded-xl bg-surface p-5 shadow-card">
          <h2 className="flex items-center gap-2 font-medium"><Plus className="size-4" />{t("projectNew", lang)}</h2>
          <form className="mt-5 space-y-4" onSubmit={submit}>
            <Field label={t("projectName", lang)} value={form.name} onChange={(name) => setForm({ ...form, name })} />
            <Field label={t("projectObjective", lang)} value={form.objective} onChange={(objective) => setForm({ ...form, objective })} multiline />
            <Field label={t("projectWorkspace", lang)} value={form.workspace} onChange={(workspace) => setForm({ ...form, workspace })} mono required={form.mode === "existing"} />
            <label className="block text-sm">
              <span className="text-muted">{t("projectMode", lang)}</span>
              <select value={form.mode} onChange={(event) => setForm({ ...form, mode: event.target.value as AtlasProject["mode"] })}
                className="mt-1.5 h-11 w-full rounded-md border border-border bg-bg-elevated px-3 outline-none focus:ring-2 focus:ring-primary/35">
                <option value="new">{t("projectModeNew", lang)}</option>
                <option value="existing">{t("projectModeExisting", lang)}</option>
              </select>
            </label>
            {saveError ? <p className="text-sm text-danger">{saveError}</p> : null}
            <Button className="w-full" disabled={saving}>{saving ? t("projectCreating", lang) : t("projectCreate", lang)}</Button>
          </form>
        </section>
      </div>
      {selectedId ? <ProjectReferences projectId={selectedId} /> : null}
    </main>
  );
}

function ProjectReferences({ projectId }: { projectId: string }) {
  const { lang } = useLang();
  const [revision, setRevision] = useState(0);
  const [notes, setNotes] = useState<Record<string, string>>({});
  const [overrides, setOverrides] = useState<Record<string, Partial<ProjectReference>>>({});
  const [busyId, setBusyId] = useState("");
  const [saveError, setSaveError] = useState("");
  const { data: references, error, loading } = useAsync(
    () => getProjectReferences(projectId),
    [projectId, revision],
  );

  useEffect(() => {
    if (!references) return;
    setNotes(Object.fromEntries(references.map((reference) => [reference.id, reference.note])));
    setOverrides({});
  }, [references]);

  const visibleReferences = references?.map((reference) => ({
    ...reference,
    ...overrides[reference.id],
  }));
  const hasUnsavedNotes = visibleReferences?.some(
    (reference) => (notes[reference.id] ?? "") !== reference.note,
  ) ?? false;

  const update = async (
    reference: ProjectReference,
    input: { note?: string; read_status?: ProjectReference["read_status"] },
  ) => {
    setBusyId(reference.id);
    setSaveError("");
    try {
      const saved = await updateProjectReference(projectId, reference.id, input);
      setOverrides((current) => ({
        ...current,
        [reference.id]: { ...current[reference.id], ...saved },
      }));
    } catch (cause) {
      setSaveError(String(cause));
    } finally {
      setBusyId("");
    }
  };

  return (
    <section className="mt-8 rounded-xl bg-surface p-5 shadow-card">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div className="flex items-start gap-3">
          <BookMarked className="mt-0.5 size-5 text-primary" />
          <div>
            <h2 className="font-serif text-xl font-medium">{lang === "zh" ? "项目资料集" : "Project research collection"}</h2>
            <p className="mt-1 text-xs leading-5 text-subtle">
              {lang === "zh" ? "摘录和来源版本在收藏时固定；正式资料变化时会提示，但不会改写旧记录。" : "Excerpts and source versions are pinned when saved. Later source changes are flagged without rewriting the record."}
            </p>
          </div>
        </div>
        <Button
          size="sm"
          variant="ghost"
          disabled={hasUnsavedNotes}
          title={hasUnsavedNotes ? (lang === "zh" ? "请先保存备注" : "Save notes before refreshing") : undefined}
          onClick={() => {
            invalidateAtlasCache();
            setRevision((value) => value + 1);
          }}
        >
          <RefreshCw className="size-3.5" />{lang === "zh" ? "刷新版本状态" : "Refresh versions"}
        </Button>
      </div>

      {loading && !references ? <Loading /> : error ? <ErrorBox message={error} /> : visibleReferences?.length ? (
        <div className="mt-5 space-y-4">
          {visibleReferences.map((reference) => (
            <article key={reference.id} className="rounded-lg border border-border bg-bg-elevated p-4">
              <div className="flex flex-wrap items-start justify-between gap-3">
                <div>
                  <div className="flex flex-wrap items-center gap-2">
                    {reference.source_kind.startsWith("atlas:") ? (
                      <Link to={reference.source_kind === "atlas:app" ? `/apps#${reference.source_ref}` : `/types/${reference.source_ref}`} className="font-medium text-primary hover:underline">
                        {reference.source_ref}
                      </Link>
                    ) : <span className="font-medium">{reference.source_ref}</span>}
                    <span className="rounded-full bg-chip px-2 py-0.5 text-[11px] text-muted">
                      {referenceKind(reference.source_kind, lang)}
                    </span>
                    {reference.locator ? <span className="font-mono text-[11px] text-subtle">#{reference.locator}</span> : null}
                  </div>
                  <p className="mt-2 font-mono text-[11px] text-subtle">
                    {lang === "zh" ? "收藏版本" : "Saved version"}: {reference.source_version.slice(0, 12)}
                    {reference.current_version ? ` · ${lang === "zh" ? "当前" : "current"}: ${reference.current_version.slice(0, 12)}` : ""}
                  </p>
                </div>
                <select
                  value={reference.read_status}
                  aria-label={lang === "zh" ? `${reference.source_ref} 阅读状态` : `${reference.source_ref} reading status`}
                  disabled={busyId === reference.id}
                  onChange={(event) => update(reference, { read_status: event.target.value as ProjectReference["read_status"] })}
                  className="h-9 rounded-md border border-border bg-surface px-2 text-xs outline-none focus:ring-2 focus:ring-primary/35"
                >
                  <option value="unread">{lang === "zh" ? "未读" : "Unread"}</option>
                  <option value="read">{lang === "zh" ? "已读" : "Read"}</option>
                  <option value="reviewed">{lang === "zh" ? "已复核" : "Reviewed"}</option>
                </select>
              </div>

              {reference.stale ? (
                <p className="mt-3 flex items-start gap-2 rounded-md bg-warn/10 px-3 py-2 text-xs leading-5 text-warn">
                  <AlertTriangle className="mt-0.5 size-3.5 shrink-0" />
                  {reference.source_available
                    ? (lang === "zh" ? "正式资料已有新版本；此记录仍引用收藏时的固定版本。可回到类型页复核并收藏新版。" : "The source has a newer version. This record still cites the pinned saved version; review and save the new version from the type page.")
                    : (lang === "zh" ? "当前找不到原始资料；已保存的摘录和版本仍保留。" : "The original source is unavailable; the saved excerpt and version remain available.")}
                </p>
              ) : null}

              <details className="mt-3">
                <summary className="cursor-pointer text-xs text-muted hover:text-fg">
                  {lang === "zh" ? `查看固定摘录（${reference.excerpt.length.toLocaleString()} 字符）` : `View pinned excerpt (${reference.excerpt.length.toLocaleString()} chars)`}
                </summary>
                <div className="mt-3 max-h-80 overflow-y-auto rounded-md border border-border bg-surface p-4">
                  <Prose md={reference.excerpt} />
                </div>
              </details>

              <div className="mt-4 flex items-end gap-2">
                <label className="min-w-0 flex-1 text-xs text-muted">
                  {lang === "zh" ? "借鉴点 / 项目备注" : "Takeaway / project note"}
                  <textarea
                    rows={2}
                    value={notes[reference.id] ?? ""}
                    onChange={(event) => setNotes({ ...notes, [reference.id]: event.target.value })}
                    className="mt-1.5 w-full rounded-md border border-border bg-surface px-3 py-2 text-sm text-fg outline-none focus:ring-2 focus:ring-primary/35"
                  />
                </label>
                <Button
                  size="sm"
                  variant="outline"
                  disabled={busyId === reference.id || (notes[reference.id] ?? "") === reference.note}
                  onClick={() => update(reference, { note: notes[reference.id] ?? "" })}
                >
                  <Save className="size-3.5" />{lang === "zh" ? "保存备注" : "Save note"}
                </Button>
              </div>
            </article>
          ))}
        </div>
      ) : (
        <p className="mt-5 text-sm text-muted">
          {lang === "zh" ? "还没有收藏资料。先搜索类型或应用，然后在类型页阅读并收藏全文或章节。" : "No saved research yet. Search for a type or application, then read and save a document or section from its type page."}
        </p>
      )}
      {saveError ? <p className="mt-3 text-sm text-danger">{saveError}</p> : null}
    </section>
  );
}

function referenceKind(kind: string, lang: "zh" | "en") {
  if (kind === "atlas:application") return lang === "zh" ? "类型正文" : "Type document";
  if (kind === "atlas:research") return lang === "zh" ? "研究笔记" : "Research notes";
  if (kind === "atlas:app") return lang === "zh" ? "应用目录资料" : "Application catalog record";
  return kind;
}

function Field({ label, value, onChange, multiline, mono, required }: {
  label: string;
  value: string;
  onChange: (value: string) => void;
  multiline?: boolean;
  mono?: boolean;
  required?: boolean;
}) {
  const classes = `mt-1.5 w-full rounded-md border border-border bg-bg-elevated px-3 outline-none focus:ring-2 focus:ring-primary/35 ${mono ? "font-mono text-xs" : ""}`;
  return (
    <label className="block text-sm">
      <span className="text-muted">{label}</span>
      {multiline ? (
        <textarea required rows={3} value={value} onChange={(event) => onChange(event.target.value)} className={`${classes} py-2.5`} />
      ) : (
        <input required={required ?? true} value={value} onChange={(event) => onChange(event.target.value)} className={`${classes} h-11`} />
      )}
    </label>
  );
}
