import { useEffect, useState, type FormEvent, type ReactNode } from "react";
import { AlertTriangle, CheckCircle2, FileClock, Plus, Save, Sparkles } from "lucide-react";
import { useAsync } from "@/components/loaders";
import { Prose } from "@/components/prose";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  addProjectDocumentVersion,
  applyProjectGenerationItem,
  createProjectDocument,
  getProjectDocumentDiff,
  getProjectDocumentVersions,
  getProjectGeneration,
  reviewProjectDocument,
  startProjectGeneration,
  type DocumentBasis,
  type ProjectDocument,
  type ProjectDocumentKind,
  type ProjectGenerationRun,
  type ProjectWorkspace,
} from "@/lib/atlas";
import { useLang } from "@/lib/lang";
import {
  actionError,
  DOCUMENT_KINDS,
  documentKind,
  inputClass,
  TechnicalError,
  TechnicalMeta,
  TextArea,
} from "@/components/project-detail-shared";

export function DocumentForm({ projectId, workspace, onSaved }: { projectId: string; workspace: ProjectWorkspace; onSaved: () => void }) {
  const { lang } = useLang(); const [kind, setKind] = useState<ProjectDocumentKind>("analysis");
  const [title, setTitle] = useState(""); const [content, setContent] = useState(""); const [keys, setKeys] = useState<string[]>([]);
  const [saving, setSaving] = useState(false); const [error, setError] = useState("");
  const submit = async (event: FormEvent) => { event.preventDefault(); setSaving(true); setError(""); try {
    await createProjectDocument(projectId, { kind, title, content, basis: basisFromKeys(keys), author: "human", change_summary: lang === "zh" ? "创建人工初稿" : "Created manual draft" });
    setTitle(""); setContent(""); setKeys([]); onSaved();
  } catch (cause) { setError(actionError(cause, lang)); } finally { setSaving(false); } };
  return <SideForm title={lang === "zh" ? "新建关联文档" : "Create linked document"} icon={Plus}><form className="space-y-4" onSubmit={submit}>
    <label className="block text-sm"><span className="text-muted">{lang === "zh" ? "文档类型" : "Document kind"}</span><select value={kind} onChange={(event) => setKind(event.target.value as ProjectDocumentKind)} className={inputClass}>{DOCUMENT_KINDS.map((item) => <option key={item.value} value={item.value}>{lang === "zh" ? item.zh : item.en}</option>)}</select></label>
    <Field label={lang === "zh" ? "标题" : "Title"} value={title} onChange={setTitle} required />
    <TextArea label="Markdown" value={content} onChange={setContent} required rows={9} />
    <BasisPicker workspace={workspace} selected={keys} onChange={setKeys} />
    {error ? <p className="text-xs text-danger">{error}</p> : null}<Button className="w-full" disabled={saving}>{lang === "zh" ? "创建文档 v1" : "Create document v1"}</Button>
  </form></SideForm>;
}

export function DocumentCard({ projectId, document, onSaved }: { projectId: string; document: ProjectDocument; onSaved: () => void }) {
  const { lang } = useLang(); const [content, setContent] = useState(document.content); const [summary, setSummary] = useState("");
  const [reviewNote, setReviewNote] = useState("");
  const [saving, setSaving] = useState(false); const [error, setError] = useState(""); const [diff, setDiff] = useState<string | null>(null);
  const approval = document.review.approval || "pending";
  const review = async (status: "approved" | "rejected") => { setSaving(true); setError(""); try {
    await reviewProjectDocument(projectId, document.id, { status, note: reviewNote, expected_current_version: document.current_version }); setReviewNote(""); onSaved();
  } catch (cause) { setError(actionError(cause, lang)); } finally { setSaving(false); } };
  const headings = markdownHeadings(document.content);
  const [sectionHeading, setSectionHeading] = useState(headings[0] || "");
  const [revisionInstruction, setRevisionInstruction] = useState("");
  const [revisionRun, setRevisionRun] = useState<ProjectGenerationRun | null>(null);
  const [revisionBusy, setRevisionBusy] = useState("");
  const [revisionError, setRevisionError] = useState("");
  const versions = useAsync(() => getProjectDocumentVersions(projectId, document.id), [projectId, document.id, document.current_version]);
  const revisionActive = revisionRun?.status === "queued" || revisionRun?.status === "running";
  useEffect(() => {
    if (!revisionActive || !revisionRun) return;
    let alive = true;
    const timer = window.setInterval(() => getProjectGeneration(projectId, revisionRun.id).then(
      (next) => { if (alive) setRevisionRun(next); },
      (cause) => { if (alive) setRevisionError(actionError(cause, lang)); },
    ), 1200);
    return () => { alive = false; window.clearInterval(timer); };
  }, [projectId, revisionActive, revisionRun?.id]);
  const save = async () => { setSaving(true); setError(""); try {
    await addProjectDocumentVersion(projectId, document.id, { content, basis: document.basis, expected_current_version: document.current_version, author: "human", change_summary: summary }); onSaved();
  } catch (cause) { setError(actionError(cause, lang)); } finally { setSaving(false); } };
  const compare = async () => { setError(""); try { setDiff((await getProjectDocumentDiff(projectId, document.id)).diff || (lang === "zh" ? "两个版本正文相同。" : "The two versions have identical content.")); } catch (cause) { setError(actionError(cause, lang)); } };
  const startRevision = async () => {
    setRevisionBusy("start"); setRevisionError("");
    try {
      setRevisionRun(await startProjectGeneration(projectId, {
        mode: "revision", document_id: document.id, section_heading: sectionHeading,
        revision_instruction: revisionInstruction.trim(),
      }));
    } catch (cause) { setRevisionError(actionError(cause, lang)); } finally { setRevisionBusy(""); }
  };
  const applyRevision = async () => {
    if (!revisionRun) return;
    setRevisionBusy("apply"); setRevisionError("");
    try {
      const result = await applyProjectGenerationItem(
        projectId, revisionRun.id, { item_kind: "document", index: 0 });
      setRevisionRun(result.run); onSaved();
    } catch (cause) { setRevisionError(actionError(cause, lang)); } finally { setRevisionBusy(""); }
  };
  const revisionCandidate = revisionRun?.result?.documents[0];
  return <article className={`rounded-xl bg-surface p-5 shadow-card ${document.review.status === "needs_review" ? "ring-2 ring-warn/25" : ""}`}>
    <div className="flex flex-wrap items-start justify-between gap-3"><div><div className="flex flex-wrap items-center gap-2"><h3 className="font-medium">{document.title}</h3><Badge tone={document.review.status === "current" ? "ok" : "warn"}>{document.review.status === "current" ? (lang === "zh" ? "依据为当前" : "Current") : (lang === "zh" ? "需要复核" : "Needs review")}</Badge><Badge tone={approval === "approved" ? "ok" : approval === "rejected" ? "danger" : "warn"}>{approval === "approved" ? (lang === "zh" ? "已批准" : "Approved") : approval === "rejected" ? (lang === "zh" ? "已拒绝" : "Rejected") : (lang === "zh" ? "待人工审阅" : "Awaiting review")}</Badge></div>
      <p className="mt-1 text-xs text-subtle">{documentKind(document.kind, lang)} · v{document.current_version} · {document.author === "ai" ? (lang === "zh" ? "AI 生成" : "AI generated") : (lang === "zh" ? "人工创建" : "Human created")} <TechnicalMeta label={lang === "zh" ? "版本技术信息" : "Version details"} value={document.version_id} inline /></p></div></div>
    {document.review.status === "needs_review" ? <p className="mt-3 flex gap-2 rounded-md bg-warn/10 p-3 text-xs leading-5 text-warn"><AlertTriangle className="mt-0.5 size-4 shrink-0" />{lang === "zh" ? "关联需求、上游文档或工作区基线已有变化。正文未被自动改写，请比较后保存新版本。" : "A linked requirement, upstream document, or workspace baseline changed. The content was preserved; review it before saving a new version."}</p> : null}
    <div className="mt-3 rounded-md bg-bg-elevated p-3">
      <div className="flex flex-wrap items-end gap-2">
        <label className="min-w-56 flex-1 text-xs"><span className="text-subtle">{lang === "zh" ? "人工审阅说明（可选）" : "Review note (optional)"}</span><input value={reviewNote} onChange={(event) => setReviewNote(event.target.value)} className={inputClass} /></label>
        <Button size="sm" disabled={saving} onClick={() => review("approved")}><CheckCircle2 className="size-4" />{lang === "zh" ? "批准当前版本" : "Approve current version"}</Button>
        <Button size="sm" variant="outline" disabled={saving} onClick={() => review("rejected")}>{lang === "zh" ? "拒绝当前版本" : "Reject current version"}</Button>
      </div>
      <p className="mt-2 text-[11px] leading-5 text-subtle">{lang === "zh" ? `只有已批准且依据为当前的版本才能固定为迭代输入。${document.review.note ? `上次审阅：${document.review.note}${document.review.reviewed_at ? `（${new Date(document.review.reviewed_at).toLocaleString("zh-CN")}）` : ""}` : ""}` : `Only approved versions with current basis can be pinned into an iteration.${document.review.note ? ` Last review: ${document.review.note}${document.review.reviewed_at ? ` (${new Date(document.review.reviewed_at).toLocaleString("en")})` : ""}` : ""}`}</p>
      {approval !== "approved" && document.review.status === "current" ? <p className="mt-1 text-[11px] text-warn">{lang === "zh" ? "该版本尚未批准，不能用于新的迭代。" : "This version is not approved and cannot seed a new iteration."}</p> : null}
      {approval === "approved" && document.review.status === "needs_review" ? <p className="mt-1 text-[11px] text-warn">{lang === "zh" ? "依赖已变化，批准状态不足以让该版本进入迭代；请先复核并保存新版本。" : "Dependencies changed, so the approval alone cannot seed an iteration; review and save a new version."}</p> : null}
    </div>
    <details className="mt-4"><summary className="cursor-pointer text-sm text-primary">{lang === "zh" ? "查看正文、编辑和版本" : "View, edit, and versions"}</summary>
      <div className="mt-4 rounded-md border border-border bg-bg-elevated p-4"><Prose md={document.content} /></div>
      <div className="mt-5 grid gap-4 lg:grid-cols-2"><div><TextArea label={lang === "zh" ? "编辑完整 Markdown（从当前版开始）" : "Edit full Markdown (starts from current)"} value={content} onChange={setContent} required rows={12} /><Field label={lang === "zh" ? "修改说明" : "Change summary"} value={summary} onChange={setSummary} required /><Button className="mt-3" size="sm" onClick={save} disabled={saving || !summary.trim()}><Save className="size-4" />{lang === "zh" ? "保存新版本" : "Save new version"}</Button></div>
        <div><h4 className="text-sm font-medium">{lang === "zh" ? "版本历史" : "Version history"}</h4>{versions.loading ? <p className="mt-2 text-xs text-subtle">…</p> : versions.data?.map((version) => <div key={version.version_id} className="mt-2 rounded-md bg-chip p-3 text-xs"><div>v{version.version} · {version.author === "ai" ? (lang === "zh" ? "AI 生成" : "AI generated") : (lang === "zh" ? "人工创建" : "Human created")} · {version.change_summary || (lang === "zh" ? "无说明" : "No summary")}</div><TechnicalMeta label={lang === "zh" ? "版本技术信息" : "Version details"} value={[`version ${version.version_id}`, `sha256 ${version.content_sha256.slice(0, 12)}…`].join(" · ")} /></div>)}
          <Button className="mt-3" size="sm" variant="outline" disabled={document.current_version < 2} onClick={compare}><FileClock className="size-4" />{lang === "zh" ? "比较最近两版" : "Compare latest two"}</Button></div></div>
      {diff ? <pre className="mt-4 max-h-96 overflow-auto whitespace-pre-wrap rounded-md bg-fg p-4 font-mono text-xs text-bg">{diff}</pre> : null}{error ? <p className="mt-3 text-xs text-danger">{error}</p> : null}
      <div className="mt-5 border-t border-border pt-5"><h4 className="text-sm font-medium">{lang === "zh" ? "用自然语言修改一个章节" : "Revise one section in natural language"}</h4><p className="mt-1 text-[11px] leading-5 text-subtle">{lang === "zh" ? "Atlas 固定当前版本；AI 只能改所选章节正文，章节标题与其它人工内容必须逐字保持。结果先显示差异，确认后才保存。" : "Atlas pins the current version. AI may change only the selected section body; the heading and all other content must remain byte-for-byte identical. Review the diff before saving."}</p>
        {headings.length ? <div className="mt-3 grid gap-3 lg:grid-cols-[minmax(0,16rem)_minmax(0,1fr)_auto] lg:items-end"><label className="block text-sm"><span className="text-muted">{lang === "zh" ? "目标章节" : "Target section"}</span><select value={sectionHeading} onChange={(event) => setSectionHeading(event.target.value)} className={inputClass}>{headings.map((heading) => <option key={heading} value={heading}>{heading}</option>)}</select></label><TextArea label={lang === "zh" ? "修改要求" : "Revision instruction"} value={revisionInstruction} onChange={setRevisionInstruction} rows={2} /><Button size="sm" variant="outline" disabled={Boolean(revisionBusy) || revisionActive || !revisionInstruction.trim()} onClick={startRevision}><Sparkles className="size-4" />{lang === "zh" ? "生成修改候选" : "Generate revision"}</Button></div> : <p className="mt-3 text-xs text-warn">{lang === "zh" ? "正文没有 Markdown 标题，请先用完整编辑加入章节结构。" : "This document has no Markdown headings. Add section structure with the full editor first."}</p>}
        {revisionActive ? <p className="mt-3 text-xs text-muted">{lang === "zh" ? "正在生成章节修改候选…" : "Generating a section revision…"}</p> : null}
        {revisionRun?.status === "failed" ? <div className="mt-3 rounded-md bg-danger/10 p-3"><p className="text-xs text-danger">{lang === "zh" ? "章节修改生成失败，请检查要求后重试。" : "The section revision failed. Check the instruction and try again."}</p><TechnicalError message={revisionRun.error} lang={lang} /></div> : null}
        {revisionCandidate ? <div className="mt-4 rounded-md border border-border p-4"><div className="flex flex-wrap items-start justify-between gap-3"><div><Badge tone="ok">{lang === "zh" ? "修改候选" : "Revision candidate"}</Badge><p className="mt-2 text-xs text-muted">{revisionRun?.revision?.section_heading}</p></div><Button size="sm" disabled={Boolean(revisionRun?.applied.documents["0"]) || revisionBusy === "apply"} onClick={applyRevision}>{revisionRun?.applied.documents["0"] ? (lang === "zh" ? "已保存" : "Saved") : (lang === "zh" ? "保存为新版本" : "Save as new version")}</Button></div>{revisionCandidate.diff ? <pre className="mt-3 max-h-80 overflow-auto whitespace-pre-wrap rounded-md bg-fg p-4 font-mono text-xs text-bg">{revisionCandidate.diff}</pre> : null}<details className="mt-3"><summary className="cursor-pointer text-xs text-primary">{lang === "zh" ? "查看候选全文" : "View full candidate"}</summary><div className="mt-3 max-h-80 overflow-auto rounded-md bg-bg-elevated p-3"><Prose md={revisionCandidate.content} /></div></details></div> : null}
        {revisionError ? <p className="mt-3 text-xs text-danger">{revisionError}</p> : null}
      </div>
    </details>
  </article>;
}

function Field({ label, value, onChange, required }: { label: string; value: string; onChange: (value: string) => void; required?: boolean }) {
  return <label className="block text-sm"><span className="text-muted">{label}</span><input required={required} value={value} onChange={(event) => onChange(event.target.value)} className={inputClass} /></label>;
}

function SideForm({ title, icon: Icon, children }: { title: string; icon: typeof Plus; children: ReactNode }) {
  return <aside className="h-fit rounded-xl bg-surface p-5 shadow-card"><h3 className="mb-5 flex items-center gap-2 font-medium"><Icon className="size-4" />{title}</h3>{children}</aside>;
}

function BasisPicker({ workspace, selected, onChange }: { workspace: ProjectWorkspace; selected: string[]; onChange: (value: string[]) => void }) {
  const { lang } = useLang();
  const options = [
    ...workspace.references.map((item) => ({ key: `reference:${item.id}`, label: `${lang === "zh" ? "资料" : "Source"} · ${item.source_ref}${item.locator ? `#${item.locator}` : ""}` })),
    ...workspace.requirements.map((item) => ({ key: `requirement:${item.id}`, label: `${lang === "zh" ? "需求" : "Requirement"} · ${item.content}` })),
    ...workspace.decisions.map((item) => ({ key: `decision:${item.id}`, label: `${lang === "zh" ? "决定" : "Decision"} · ${item.statement}` })),
    ...workspace.documents.map((item) => ({ key: `document_version:${item.version_id}`, label: `${lang === "zh" ? "上游文档" : "Upstream document"} · ${item.title} v${item.current_version}` })),
  ];
  return <Picker label={lang === "zh" ? "固定依据" : "Pinned basis"} options={options} selected={selected} onChange={onChange} />;
}

function Picker({ label, options, selected, onChange }: { label: string; options: { key: string; label: string }[]; selected: string[]; onChange: (value: string[]) => void }) {
  return <fieldset><legend className="text-sm text-muted">{label}</legend><div className="mt-2 max-h-40 space-y-2 overflow-y-auto">{options.map((item) => <label key={item.key} className="flex items-start gap-2 text-xs leading-5 text-muted"><input type="checkbox" className="mt-1" checked={selected.includes(item.key)} onChange={(event) => onChange(event.target.checked ? [...selected, item.key] : selected.filter((value) => value !== item.key))} /><span>{item.label}</span></label>)}{!options.length ? <p className="text-xs text-subtle">—</p> : null}</div></fieldset>;
}

function basisFromKeys(keys: string[]): DocumentBasis[] {
  return keys.map((key) => {
    const [kind, id] = key.split(":", 2);
    return { kind: kind as NonNullable<DocumentBasis["kind"]>, id };
  });
}

function markdownHeadings(content: string) {
  const values = Array.from(content.matchAll(/^(#{1,6})[ \t]+(.+?)[ \t]*$/gm), (match) => match[0].trim());
  return values.filter((value, index) => values.indexOf(value) === index && values.lastIndexOf(value) === index);
}
