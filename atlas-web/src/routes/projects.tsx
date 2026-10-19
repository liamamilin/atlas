import { useEffect, useState, type FormEvent } from "react";
import { AlertTriangle, BookMarked, Download, FolderKanban, Plus, RefreshCw, Save, Trash2 } from "lucide-react";
import { Link, useNavigate, useSearchParams } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { ErrorBox, Loading, useAsync } from "@/components/loaders";
import { Prose } from "@/components/prose";
import {
  createProject,
  createProjectBackup,
  deleteProject,
  deleteProjectBackup,
  getLeaf,
  getProject,
  getProjectReferences,
  getProjects,
  getProjectRestoreStatus,
  invalidateAtlasCache,
  listProjectBackups,
  prepareProjectBackupRestore,
  recoverProjectRestore,
  restoreProjectBackup,
  updateProjectReference,
  type AtlasProject,
  type ProjectReference,
  type ProjectRestoreStatus,
  type ProjectRestoreTarget,
} from "@/lib/atlas";
import { pick, t, useLang } from "@/lib/lang";
import { useCurrentProjectId } from "@/lib/project-selection";

export function Projects() {
  const { lang } = useLang();
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const starterSlug = searchParams.get("fromType")?.trim() || "";
  const starterState = useAsync(
    () => starterSlug ? getLeaf(starterSlug) : Promise.resolve(null),
    [starterSlug],
  );
  const [revision, setRevision] = useState(0);
  const { data: projects, error, loading } = useAsync(getProjects, [revision]);
  const [selectedId, select] = useCurrentProjectId();
  const selectedProject = projects?.find((project) => project.id === selectedId);
  const [saving, setSaving] = useState(false);
  const [saveError, setSaveError] = useState<string | null>(null);
  const [deletingId, setDeletingId] = useState("");
  const [backingUpId, setBackingUpId] = useState("");
  const [backupRevision, setBackupRevision] = useState(0);
  const [deleteError, setDeleteError] = useState("");
  const [deleteNotice, setDeleteNotice] = useState("");
  const [form, setForm] = useState({ name: "", objective: "", workspace: "", mode: (searchParams.get("mode") === "existing" ? "existing" : "new") as AtlasProject["mode"] });

  useEffect(() => {
    if (!starterState.data) return;
    const name = pick(lang, starterState.data.name_zh, starterState.data.name);
    setForm((current) => ({
      ...current,
      name: current.name || (lang === "zh" ? `${name}项目` : `${name} project`),
      objective: current.objective || (lang === "zh"
        ? `基于${name}类型资料，形成项目方案并开发首个可验收范围。`
        : `Use the ${name} type evidence to define the project and build its first acceptable scope.`),
      mode: "new",
    }));
  }, [starterState.data?.slug, lang]);

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
      const project = await createProject({
        ...form,
        starter_reference: starterState.data ? {
          kind: "application",
          slug: starterState.data.slug,
          note: lang === "zh" ? "从类型详情页创建项目并固定完整类型正文。" : "Project created from the type page with the complete type document pinned.",
          read_status: "read",
        } : undefined,
      });
      select(project.id);
      navigate(`/projects/${project.id}`);
    } catch {
      setSaveError(lang === "zh" ? "项目创建失败，请检查填写内容后重试。" : "Project creation failed. Check the form and try again.");
    } finally {
      setSaving(false);
    }
  };

  const backup = async (project: AtlasProject) => {
    if (backingUpId) return;
    setBackingUpId(project.id);
    setDeleteError("");
    setDeleteNotice("");
    try {
      const result = await createProjectBackup(project.id);
      const anchor = document.createElement("a");
      anchor.href = result.download_url;
      anchor.download = "";
      document.body.appendChild(anchor);
      anchor.click();
      anchor.remove();
      invalidateAtlasCache();
      setBackupRevision((value) => value + 1);
      setDeleteNotice(lang === "zh"
        ? `项目“${project.name}”的备份已创建并开始下载；用户源码不包含在备份中。`
        : `A backup of “${project.name}” was created and is downloading; source files are not included.`);
    } catch (cause) {
      setDeleteError(cause instanceof Error ? cause.message
        : (lang === "zh" ? "项目备份失败，请确认没有活动执行或生成任务。" : "Backup failed. Confirm that no generation or execution is active."));
    } finally {
      setBackingUpId("");
    }
  };

  const remove = async (project: AtlasProject) => {
    const message = lang === "zh"
      ? `删除项目“${project.name}”及其 Atlas 文档、需求、执行副本、证据和导出包？\n\n本地工作区和源码不会删除。此操作不可撤销。`
      : `Delete “${project.name}” and its Atlas documents, requirements, execution copies, evidence, and exports?\n\nThe local workspace and source files will be preserved. This cannot be undone.`;
    if (!window.confirm(message)) return;
    setDeletingId(project.id);
    setDeleteError("");
    setDeleteNotice("");
    try {
      const result = await deleteProject(project.id);
      if (selectedId === project.id) select("");
      const cleanupFailed = Object.keys(result.artifact_cleanup_errors || {});
      setDeleteNotice(cleanupFailed.length
        ? (lang === "zh"
          ? `项目“${project.name}”已删除，但部分 Atlas 产物清理失败：${cleanupFailed.join("、")}。`
          : `“${project.name}” was deleted, but some Atlas artifacts could not be cleaned: ${cleanupFailed.join(", ")}.`)
        : (lang === "zh"
          ? `项目“${project.name}”及其 Atlas 产物已删除；本地工作区和源码未受影响。`
          : `“${project.name}” and its Atlas artifacts were deleted; the local workspace and source files were not changed.`));
      setRevision((value) => value + 1);
    } catch {
      setDeleteError(lang === "zh" ? "项目删除失败，请稍后重试。" : "Project deletion failed. Please try again.");
    } finally {
      setDeletingId("");
    }
  };

  return (
    <main className="mx-auto max-w-6xl px-4 py-10">
      <p className="text-sm font-medium tracking-wide text-primary">U17</p>
      <h1 className="mt-2 font-serif text-3xl font-medium">{t("projectsTitle", lang)}</h1>
      <p className="mt-2 max-w-2xl text-sm leading-6 text-muted">{t("projectsP", lang)}</p>

      <div className="mt-8 grid gap-6 lg:grid-cols-[minmax(0,1fr)_22rem]">
        <section>
          {deleteNotice ? <p className="mb-3 rounded-md bg-primary/10 p-3 text-sm text-primary" role="status">{deleteNotice}</p> : null}
          {deleteError ? <p className="mb-3 rounded-md bg-danger/10 p-3 text-sm text-danger" role="alert">{deleteError}</p> : null}
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
                        <details className="mt-3 text-xs text-subtle">
                          <summary className="cursor-pointer">{lang === "zh" ? "工作区位置" : "Workspace location"}</summary>
                          <code className="mt-1 block break-all rounded bg-chip px-2 py-1 font-mono">{project.workspace}</code>
                        </details>
                        <div className="mt-4 flex flex-wrap items-center justify-between gap-3">
                          <span className="text-xs text-subtle">
                            {project.mode === "new" ? t("projectModeNew", lang) : t("projectModeExisting", lang)}
                          </span>
                          <div className="flex flex-wrap gap-2">
                            {!selected ? <Button size="sm" variant="outline" onClick={() => select(project.id)}>{t("projectSelect", lang)}</Button> : null}
                            <Button size="sm" asChild><Link to={`/projects/${project.id}`}>{lang === "zh" ? "打开工作区" : "Open workspace"}</Link></Button>
                            <Button
                              size="sm"
                              variant="outline"
                              disabled={Boolean(backingUpId) || deletingId === project.id}
                              onClick={() => backup(project)}
                            >
                              <Download className="size-3.5" />
                              {backingUpId === project.id
                                ? (lang === "zh" ? "备份中…" : "Backing up…")
                                : (lang === "zh" ? "备份" : "Back up")}
                            </Button>
                            <Button
                              size="sm"
                              variant="outline"
                              disabled={Boolean(backingUpId) || deletingId === project.id}
                              onClick={() => {
                                select(project.id);
                                document.getElementById("backup-restore")?.scrollIntoView({ behavior: "smooth", block: "start" });
                              }}
                            >
                              <RefreshCw className="size-3.5" />
                              {lang === "zh" ? "管理备份" : "Manage backups"}
                            </Button>
                            <Button
                              size="sm"
                              variant="ghost"
                              className="text-danger hover:bg-danger/10"
                              disabled={deletingId === project.id || Boolean(backingUpId)}
                              onClick={() => remove(project)}
                            >
                              <Trash2 className="size-3.5" />
                              {deletingId === project.id
                                ? (lang === "zh" ? "删除中…" : "Deleting…")
                                : (lang === "zh" ? "删除" : "Delete")}
                            </Button>
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
          {starterSlug ? (
            <div className="mt-4 rounded-lg bg-primary/[0.06] p-3 ring-1 ring-primary/15">
              {starterState.loading ? (
                <p className="text-xs text-muted">{lang === "zh" ? "读取类型资料…" : "Loading type evidence…"}</p>
              ) : starterState.error || !starterState.data ? (
                <div className="text-xs leading-5 text-danger">
                  <p>{lang === "zh" ? "无法读取作为起点的类型。" : "The starting type could not be loaded."}</p>
                  <Link to="/projects" className="underline">{lang === "zh" ? "不使用该类型" : "Continue without it"}</Link>
                </div>
              ) : (
                <div className="text-xs leading-5 text-muted">
                  <p>{lang === "zh" ? "项目起点" : "Project starting point"}</p>
                  <Link to={`/types/${starterState.data.slug}`} className="font-medium text-primary hover:underline">
                    {pick(lang, starterState.data.name_zh, starterState.data.name)}
                  </Link>
                  <p>{lang === "zh" ? "创建时将自动固定完整类型正文。" : "The complete type document will be pinned when the project is created."}</p>
                </div>
              )}
            </div>
          ) : null}
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
            {saveError ? <p className="text-sm text-danger" role="alert">{saveError}</p> : null}
            <Button className="w-full" disabled={saving || Boolean(starterSlug && !starterState.data)}>{saving ? t("projectCreating", lang) : t("projectCreate", lang)}</Button>
          </form>
        </section>
      </div>
      {selectedProject ? (
        <>
          <ProjectReferences projectId={selectedProject.id} />
          <BackupRestorePanel key={selectedProject.id} project={selectedProject} revision={backupRevision} />
        </>
      ) : null}
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
    } catch {
      setSaveError(lang === "zh" ? "资料状态保存失败，请稍后重试。" : "Could not save the research status. Please try again.");
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
      {saveError ? <p className="mt-3 text-sm text-danger" role="alert">{saveError}</p> : null}
    </section>
  );
}

function BackupRestorePanel({ project, revision }: { project: AtlasProject; revision: number }) {
  const { lang } = useLang();
  const [localRevision, setLocalRevision] = useState(0);
  const [selectedBackup, setSelectedBackup] = useState("");
  const [target, setTarget] = useState<ProjectRestoreTarget | null>(null);
  const [status, setStatus] = useState<ProjectRestoreStatus | null>(null);
  const [busy, setBusy] = useState(false);
  const [notice, setNotice] = useState("");
  const [error, setError] = useState("");
  const { data, error: listError, loading } = useAsync(
    () => listProjectBackups(project.id),
    [project.id, revision, localRevision],
  );
  const backups = data?.backups || [];

  const refresh = () => {
    invalidateAtlasCache();
    setLocalRevision((value) => value + 1);
    setError("");
  };

  const prepare = async (backupName: string) => {
    if (busy) return;
    setBusy(true);
    setError("");
    setNotice("");
    try {
      const prepared = await prepareProjectBackupRestore(project.id, backupName);
      setSelectedBackup(backupName);
      setTarget(prepared);
      setStatus(null);
      setNotice(lang === "zh"
        ? "恢复目标已由 Atlas 准备好；请确认后写入新的空项目库。"
        : "Atlas prepared a controlled restore target. Confirm before writing a new empty project store.");
    } catch (cause) {
      setError(cause instanceof Error ? cause.message
        : (lang === "zh" ? "无法准备恢复目标。" : "Could not prepare a restore target."));
    } finally {
      setBusy(false);
    }
  };

  const removeBackup = async (backupName: string) => {
    if (busy) return;
    const message = lang === "zh"
      ? `删除备份“${backupName}”？\n\n只删除 Atlas 备份归档，不删除项目或用户源码；此操作不可撤销。`
      : `Delete backup “${backupName}”?\n\nOnly the Atlas archive is deleted; the project and user source are not removed. This cannot be undone.`;
    if (!window.confirm(message)) return;
    setBusy(true);
    setError("");
    setNotice("");
    try {
      await deleteProjectBackup(project.id, backupName);
      invalidateAtlasCache();
      setSelectedBackup("");
      setTarget(null);
      setLocalRevision((value) => value + 1);
      setNotice(lang === "zh" ? "备份归档已删除。" : "Backup archive deleted.");
    } catch (cause) {
      setError(cause instanceof Error ? cause.message
        : (lang === "zh" ? "备份删除失败。" : "Could not delete the backup."));
    } finally {
      setBusy(false);
    }
  };

  const restore = async () => {
    if (!target || !selectedBackup || busy) return;
    const message = lang === "zh"
      ? `将备份恢复到新的空项目库？\n\n不会覆盖当前项目库，也不会写入用户源码。恢复目标由 Atlas 管理。`
      : `Restore this backup to a new empty project store?\n\nThe current store will not be overwritten, user source files will not be included, and Atlas manages the target.`;
    if (!window.confirm(message)) return;
    setBusy(true);
    setError("");
    setNotice("");
    try {
      const result = await restoreProjectBackup(
        project.id, selectedBackup, target.restore_id,
      );
      setStatus({
        restore_id: result.restore_id,
        project_id: result.project_id,
        status: "completed",
        interrupted: false,
        phase: "verified",
        database_installed: true,
        installed_artifact_count: result.artifacts_restored_count,
      });
      setTarget(null);
      setLocalRevision((value) => value + 1);
      setNotice(lang === "zh"
        ? "恢复完成；当前项目库和用户源码未被覆盖。"
        : "Restore completed; the current store and user source files were not overwritten.");
    } catch (cause) {
      setError(cause instanceof Error ? cause.message
        : (lang === "zh" ? "恢复失败；请检查恢复状态。" : "Restore failed; inspect the restore status."));
    } finally {
      setBusy(false);
    }
  };

  const recoverInterrupted = async () => {
    if (!status || status.status !== "interrupted" || busy) return;
    const message = lang === "zh"
      ? "清理这次中断的恢复目标？\n\n只会删除 restore journal 记录且指纹未变化的 Atlas 产物；不会删除用户源码。"
      : "Clean up this interrupted restore target?\n\nOnly Atlas artifacts recorded by the restore journal and unchanged by fingerprint will be removed; user source is not removed.";
    if (!window.confirm(message)) return;
    setBusy(true);
    setError("");
    try {
      const result = await recoverProjectRestore(project.id, status.restore_id);
      setStatus({
        restore_id: result.restore_id,
        project_id: result.project_id,
        status: "not_started",
        interrupted: false,
        phase: "recovered",
        database_installed: false,
        installed_artifact_count: 0,
      });
      setNotice(lang === "zh"
        ? "中断恢复已清理；可以重新准备一个恢复目标。"
        : "Interrupted restore cleanup completed; a new target can be prepared.");
    } catch (cause) {
      setError(cause instanceof Error ? cause.message
        : (lang === "zh" ? "中断恢复清理失败。" : "Interrupted restore cleanup failed."));
    } finally {
      setBusy(false);
    }
  };

  const refreshStatus = async () => {
    if (!status || busy) return;
    setBusy(true);
    setError("");
    try {
      setStatus(await getProjectRestoreStatus(project.id, status.restore_id));
    } catch (cause) {
      setError(cause instanceof Error ? cause.message
        : (lang === "zh" ? "无法读取恢复状态。" : "Could not read restore status."));
    } finally {
      setBusy(false);
    }
  };

  return (
    <section id="backup-restore" className="mt-8 rounded-xl bg-surface p-5 shadow-card">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div>
          <h2 className="font-serif text-xl font-medium">{lang === "zh" ? "备份与恢复" : "Backup and restore"}</h2>
          <p className="mt-1 max-w-3xl text-xs leading-5 text-subtle">
            {lang === "zh"
              ? "备份包含 Atlas 项目状态和受控证据，不包含用户源码。恢复只能写入服务端生成的新的空项目库，不接受任意主机路径。Atlas 不会自动清理备份；删除归档需要逐项确认。"
              : "Backups contain Atlas project state and controlled evidence, not user source. Restore only writes a new empty store generated by the server; arbitrary host paths are rejected. Atlas does not automatically clean backups; deleting an archive requires item-by-item confirmation."}
          </p>
        </div>
        <Button size="sm" variant="ghost" onClick={refresh} disabled={busy} aria-label={lang === "zh" ? "刷新备份列表" : "Refresh backup list"}>
          <RefreshCw className="size-3.5" />{lang === "zh" ? "刷新" : "Refresh"}
        </Button>
      </div>

      {notice ? <p className="mt-4 rounded-md bg-primary/10 p-3 text-sm text-primary" role="status">{notice}</p> : null}
      {error || listError ? <p className="mt-4 rounded-md bg-danger/10 p-3 text-sm text-danger" role="alert">{error || String(listError)}</p> : null}
      {loading ? <Loading /> : backups.length ? (
        <div className="mt-4 space-y-3">
          {backups.map((backup) => (
            <div key={backup.name} className="rounded-lg border border-border bg-bg-elevated p-4">
              <div className="flex flex-wrap items-start justify-between gap-3">
                <div className="min-w-0">
                  <p className="truncate font-mono text-xs">{backup.name}</p>
                  <p className="mt-1 text-xs text-muted">
                    {backup.created_at ? new Date(backup.created_at).toLocaleString(lang === "zh" ? "zh-CN" : "en-US") : (lang === "zh" ? "时间未知" : "Unknown time")}
                    {backup.size !== undefined ? ` · ${formatBytes(backup.size)}` : ""}
                  </p>
                  {backup.sha256 ? <p className="mt-1 font-mono text-[11px] text-subtle">SHA-256 {backup.sha256.slice(0, 16)}…</p> : null}
                </div>
                <div className="flex items-center gap-2">
                  <span className={`rounded-full px-2 py-1 text-[11px] ${backup.valid ? "bg-primary/10 text-primary" : "bg-danger/10 text-danger"}`}>
                    {backup.valid ? (lang === "zh" ? "校验通过" : "Validated") : (lang === "zh" ? "不可恢复" : "Unavailable")}
                  </span>
                  <Button size="sm" variant="outline" disabled={!backup.valid || busy} onClick={() => prepare(backup.name)}>
                    {lang === "zh" ? "准备恢复" : "Prepare restore"}
                  </Button>
                  <Button size="sm" variant="ghost" disabled={busy} onClick={() => removeBackup(backup.name)}>
                    {lang === "zh" ? "删除归档" : "Delete archive"}
                  </Button>
                </div>
              </div>
              {backup.valid ? (
                <p className="mt-3 text-xs text-subtle">
                  {lang === "zh" ? "不包含用户源码；恢复不会覆盖当前项目库。" : "User source is not included; restore cannot overwrite the current store."}
                </p>
              ) : <p className="mt-3 text-xs text-danger">{lang === "zh" ? "备份校验失败，不能作为恢复来源。" : "This backup failed validation and cannot be restored."}</p>}
            </div>
          ))}
        </div>
      ) : (
        <p className="mt-4 text-sm text-muted">{lang === "zh" ? "还没有可用备份。先在项目卡片中创建备份。" : "No backups are available yet. Create one from the project card first."}</p>
      )}

      {target ? (
        <div className="mt-4 rounded-lg border border-warn/40 bg-warn/10 p-4">
          <p className="text-sm font-medium">{lang === "zh" ? "恢复到新的空项目库" : "Restore to a new empty project store"}</p>
          <p className="mt-1 text-xs leading-5 text-muted">
            {lang === "zh" ? `备份：${selectedBackup}。目标由 Atlas 管理（${target.restore_id}）；不会接受主机路径。` : `Backup: ${selectedBackup}. Atlas manages the target (${target.restore_id}); host paths are not accepted.`}
          </p>
          <div className="mt-3 flex flex-wrap gap-2">
            <Button size="sm" disabled={busy} onClick={restore}>
              {lang === "zh" ? "确认恢复到新空库" : "Confirm restore to new store"}
            </Button>
            <Button size="sm" variant="ghost" disabled={busy} onClick={() => setTarget(null)}>
              {lang === "zh" ? "取消" : "Cancel"}
            </Button>
          </div>
        </div>
      ) : null}

      {status ? (
        <div className={`mt-4 rounded-lg border p-4 text-sm ${status.status === "interrupted" ? "border-warn/40 bg-warn/10 text-warn" : "border-primary/20 bg-primary/5"}`} role="status">
          <div className="flex flex-wrap items-center justify-between gap-2">
            <span>
              {lang === "zh" ? `恢复状态：${status.status}` : `Restore status: ${status.status}`}
              {status.phase ? ` · ${status.phase}` : ""}
            </span>
            <Button size="sm" variant="ghost" disabled={busy} onClick={refreshStatus}>
              {lang === "zh" ? "刷新状态" : "Refresh status"}
            </Button>
          </div>
          {status.status === "interrupted" ? (
            <div className="mt-2">
              <p className="text-xs">{lang === "zh" ? "检测到中断的恢复；清理前请核对 journal 和目标未被替换。" : "An interrupted restore was detected; verify the journal and target were not replaced before cleanup."}</p>
              <Button size="sm" variant="outline" className="mt-2" disabled={busy} onClick={recoverInterrupted}>
                {lang === "zh" ? "确认清理中断恢复" : "Confirm interrupted cleanup"}
              </Button>
            </div>
          ) : null}
        </div>
      ) : null}
    </section>
  );
}

function formatBytes(value: number) {
  if (value < 1024) return `${value} B`;
  if (value < 1024 * 1024) return `${(value / 1024).toFixed(1)} KB`;
  return `${(value / (1024 * 1024)).toFixed(1)} MB`;
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
