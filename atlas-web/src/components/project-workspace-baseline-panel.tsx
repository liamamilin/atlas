import { useEffect, useState } from "react";
import { AlertTriangle, FolderGit2, RefreshCw } from "lucide-react";
import { Prose } from "@/components/prose";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  captureWorkspaceBaseline,
  checkWorkspaceChanges,
  listWorkspaceBaselines,
  type WorkspaceBaselineCheck,
  type WorkspaceBaselineSummary,
} from "@/lib/atlas";
import { useLang } from "@/lib/lang";
import {
  actionError,
  ChangePaths,
  lines,
  TechnicalMeta,
  TextArea,
} from "@/components/project-detail-shared";

export function WorkspaceBaselinePanel({ projectId, onSaved, onBaselineChange }: {
  projectId: string; onSaved: () => void;
  onBaselineChange: (value: boolean, latestId: string | null) => void;
}) {
  const { lang } = useLang();
  const [baselines, setBaselines] = useState<WorkspaceBaselineSummary[]>([]);
  const [check, setCheck] = useState<WorkspaceBaselineCheck | null>(null);
  const [focus, setFocus] = useState("");
  const [loading, setLoading] = useState(true);
  const [working, setWorking] = useState<"capture" | "check" | "">("");
  const [error, setError] = useState("");
  const latest = baselines[0] || null;

  useEffect(() => {
    let alive = true;
    setLoading(true); setError(""); setCheck(null);
    listWorkspaceBaselines(projectId).then(
      (items) => {
        if (!alive) return;
        setBaselines(items);
        onBaselineChange(items.length > 0, items[0]?.id || null);
        setFocus(items[0]?.coverage.focus_paths.join("\n") || "");
      },
      (cause) => {
        if (!alive) return;
        setError(actionError(cause, lang));
        onBaselineChange(false, null);
      },
    ).finally(() => { if (alive) setLoading(false); });
    return () => { alive = false; };
  }, [projectId]);

  const capture = async () => {
    if (latest && !check) {
      setError(lang === "zh" ? "请先检查当前工作区变化。" : "Check the current workspace before adoption.");
      return;
    }
    setWorking("capture"); setError("");
    try {
      const created = await captureWorkspaceBaseline(projectId, {
        focus_paths: lines(focus),
        ...(latest && check ? {
          expected_baseline_id: latest.id,
          expected_content_fingerprint: check.current.content_fingerprint,
        } : {}),
      });
      setBaselines((items) => [created, ...items]);
      onBaselineChange(true, created.id);
      setFocus(created.coverage.focus_paths.join("\n"));
      setCheck(null);
      onSaved();
    } catch (cause) { setError(actionError(cause, lang)); } finally { setWorking(""); }
  };

  const inspect = async () => {
    setWorking("check"); setError("");
    try { setCheck(await checkWorkspaceChanges(projectId)); }
    catch (cause) { setError(actionError(cause, lang)); } finally { setWorking(""); }
  };

  const changes = check?.changes;
  const focusChanged = Boolean(latest && lines(focus).join("\n") !== latest.coverage.focus_paths.join("\n"));
  const mayAdopt = Boolean(changes && (
    changes.changed || changes.git_state_changed || changes.comparison_limited_by_errors || focusChanged));
  return <section className="mt-8 rounded-xl bg-surface p-5 shadow-card">
    <div className="flex flex-wrap items-start justify-between gap-4">
      <div className="flex max-w-2xl items-start gap-3">
        <FolderGit2 className="mt-0.5 size-5 shrink-0 text-primary" />
        <div><h2 className="font-serif text-xl font-medium">{lang === "zh" ? "项目工作区基线" : "Project workspace baseline"}</h2>
          <p className="mt-1 text-xs leading-5 text-subtle">{lang === "zh" ? "记录文件指纹、Git 状态、已读取证据和未检查范围。检查变化不会修改已接受基线；确认后才采用当前状态。" : "Record file fingerprints, Git state, read evidence, and unchecked scope. Change checks do not mutate the accepted baseline; the current state is adopted only after review."}</p></div>
      </div>
      <div className="flex flex-wrap gap-2">
        {latest ? <Button size="sm" variant="outline" disabled={Boolean(working)} onClick={inspect}><RefreshCw className={`size-4 ${working === "check" ? "animate-spin" : ""}`} />{lang === "zh" ? "检查外部变化" : "Check external changes"}</Button> : null}
        {!latest ? <Button size="sm" disabled={Boolean(working) || loading} onClick={capture}><FolderGit2 className="size-4" />{lang === "zh" ? "建立项目基线" : "Create baseline"}</Button> : null}
      </div>
    </div>

    <div className="mt-5 grid gap-5 lg:grid-cols-[minmax(0,1fr)_20rem]">
      <div>
        {loading ? <p className="text-sm text-subtle">{lang === "zh" ? "正在读取基线…" : "Loading baselines…"}</p> : null}
        {!loading && !latest ? <div className="rounded-lg bg-bg-elevated p-4 text-sm leading-6 text-muted">{lang === "zh" ? "还没有已接受基线。首次建立会扫描工作区全部文件的元数据和内容指纹，并读取入口文档、工程清单及重点路径中的文本。" : "There is no accepted baseline yet. The first capture fingerprints all workspace files and reads entry documents, manifests, and text under the focus paths."}</div> : null}
        {latest ? <div className="rounded-lg bg-bg-elevated p-4">
          <div className="flex flex-wrap items-center gap-2"><Badge tone="ok">{lang === "zh" ? "已接受基线" : "Accepted baseline"}</Badge><TechnicalMeta label={lang === "zh" ? "基线技术信息" : "Baseline details"} value={latest.id} inline /></div>
          <div className="mt-3 grid gap-2 text-xs text-muted sm:grid-cols-2 lg:grid-cols-4">
            <div><span className="text-subtle">{lang === "zh" ? "文件" : "Files"}</span><p className="mt-1 font-medium text-fg">{latest.inventory.file_count}</p></div>
            <div><span className="text-subtle">{lang === "zh" ? "读取正文" : "Read content"}</span><p className="mt-1 font-medium text-fg">{latest.coverage.read_paths.length}</p></div>
            <div><span className="text-subtle">Git</span><p className="mt-1 truncate font-medium text-fg">{latest.git.repository ? (latest.git.branch || "detached") : (lang === "zh" ? "非仓库" : "Not a repo")}</p></div>
            <div><span className="text-subtle">{lang === "zh" ? "记录时间" : "Captured"}</span><p className="mt-1 font-medium text-fg">{new Date(latest.created_at).toLocaleString(lang === "zh" ? "zh-CN" : "en")}</p></div>
          </div>
          <TechnicalMeta label={lang === "zh" ? "指纹技术信息" : "Fingerprint details"} value={`content ${latest.content_fingerprint.slice(0, 16)} · record ${latest.fingerprint.slice(0, 16)}`} />
          <details className="mt-4 border-t border-border pt-3"><summary className="cursor-pointer text-sm text-primary">{lang === "zh" ? "查看现状证据报告" : "View evidence report"}</summary><div className="mt-4"><Prose md={latest.report_markdown} /></div></details>
        </div> : null}

        {changes ? <div className="mt-4 rounded-lg border border-border p-4">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <div className="flex flex-wrap items-center gap-2"><Badge tone={changes.requires_focused_review ? "warn" : "ok"}>{changes.requires_focused_review ? (lang === "zh" ? "重点范围需要复核" : "Focus review required") : (lang === "zh" ? "重点范围未变化" : "Focus scope unchanged")}</Badge><span className="text-xs text-subtle">+{changes.added.length} · ~{changes.modified.length} · −{changes.removed.length}</span></div>
            {mayAdopt ? <Button size="sm" disabled={Boolean(working)} onClick={capture}>{lang === "zh" ? "采用当前状态为新基线" : "Adopt current state"}</Button> : null}
          </div>
          {changes.git_revision_changed ? <p className="mt-3 flex gap-2 text-xs leading-5 text-warn"><AlertTriangle className="mt-0.5 size-4 shrink-0" />{lang === "zh" ? "Git 分支、提交或仓库边界已变化，需要复核重点范围。" : "The Git branch, revision, or repository boundary changed and requires focus review."}</p> : null}
          <ChangePaths title={lang === "zh" ? "已读取或重点范围内" : "Read or focused scope"} paths={changes.reviewed_scope_changes} />
          <ChangePaths title={lang === "zh" ? "当前审阅范围外" : "Outside current review scope"} paths={changes.outside_review_scope_changes} />
          {changes.has_unread_changes ? <p className="mt-3 text-xs leading-5 text-subtle">{lang === "zh" ? "范围外变化只表示本次没有读取其正文；系统不会据此断言它无关，也不会强制重做整份分析。" : "Outside-scope changes mean their content was not read in this review. They are not declared irrelevant and do not force a full reanalysis."}</p> : null}
          {focusChanged ? <p className="mt-3 text-xs leading-5 text-primary">{lang === "zh" ? "重点读取路径已编辑；采用后会按新范围建立报告。" : "The focus paths were edited. Adoption will create a report with the new scope."}</p> : null}
          {!changes.changed && !changes.git_state_changed && !changes.comparison_limited_by_errors ? <p className="mt-3 text-sm text-ok">{lang === "zh" ? "工作区与已接受基线一致。" : "The workspace matches the accepted baseline."}</p> : null}
          {changes.comparison_limited_by_errors ? <p className="mt-3 text-xs text-danger">{lang === "zh" ? "部分路径读取失败，比较结论受限。" : "Some paths could not be read, so the comparison is limited."}</p> : null}
        </div> : null}
        {error ? <p className="mt-4 rounded-md bg-danger/10 p-3 text-xs leading-5 text-danger">{error}</p> : null}
      </div>

      <div className="rounded-lg border border-border p-4">
        <TextArea label={lang === "zh" ? "重点读取路径（每行一个相对路径）" : "Focus paths (one relative path per line)"} value={focus} onChange={setFocus} rows={6} />
        <p className="mt-2 text-[11px] leading-5 text-subtle">{lang === "zh" ? "留空时仍读取 README、docs 文档和工程清单。修改此列表会在采用下一份基线时生效。" : "README files, docs, and manifests are still read when empty. Changes take effect when the next baseline is adopted."}</p>
        {latest ? <div className="mt-4 border-t border-border pt-4 text-xs leading-5 text-muted"><p>{lang === "zh" ? `共 ${baselines.length} 份不可变基线` : `${baselines.length} immutable baseline(s)`}</p><TechnicalMeta label={lang === "zh" ? "工作区技术信息" : "Workspace details"} value={[latest.root, latest.git.head ? `HEAD ${latest.git.head.slice(0, 12)}${latest.git.dirty ? " · dirty" : ""}` : ""].filter(Boolean).join(" · ")} /></div> : null}
      </div>
    </div>
  </section>;
}
