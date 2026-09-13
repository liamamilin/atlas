import { useEffect, useState, type FormEvent } from "react";
import { FolderKanban, Plus } from "lucide-react";
import { Button } from "@/components/ui/button";
import { ErrorBox, Loading, useAsync } from "@/components/loaders";
import { createProject, getProjects, type AtlasProject } from "@/lib/atlas";
import { t, useLang } from "@/lib/lang";

const CURRENT_PROJECT = "atlas-current-project";

export function Projects() {
  const { lang } = useLang();
  const [revision, setRevision] = useState(0);
  const { data: projects, error, loading } = useAsync(getProjects, [revision]);
  const [selectedId, setSelectedId] = useState(() => localStorage.getItem(CURRENT_PROJECT) || "");
  const [saving, setSaving] = useState(false);
  const [saveError, setSaveError] = useState<string | null>(null);
  const [form, setForm] = useState({ name: "", objective: "", workspace: "", mode: "new" as AtlasProject["mode"] });

  useEffect(() => {
    if (!projects || !selectedId) return;
    if (!projects.some((project) => project.id === selectedId)) {
      localStorage.removeItem(CURRENT_PROJECT);
      setSelectedId("");
    }
  }, [projects, selectedId]);

  const select = (id: string) => {
    localStorage.setItem(CURRENT_PROJECT, id);
    setSelectedId(id);
  };

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
                        <div className="mt-4 flex items-center justify-between gap-3">
                          <span className="text-xs text-subtle">
                            {project.mode === "new" ? t("projectModeNew", lang) : t("projectModeExisting", lang)}
                          </span>
                          {!selected ? <Button size="sm" variant="outline" onClick={() => select(project.id)}>{t("projectSelect", lang)}</Button> : null}
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
    </main>
  );
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
