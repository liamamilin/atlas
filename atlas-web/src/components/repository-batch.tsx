import { useEffect, useRef, useState } from "react";
import { Button } from "@/components/ui/button";
import { useLang } from "@/lib/lang";
import { listBatchJobs, resumeBatchJob, startBatchJob, type BatchJob } from "@/lib/oss-catalog";

export function RepositoryBatch({ leaves, activeLeaf, onUpdate }: {
  leaves: { slug: string; name: string }[]; activeLeaf: string; onUpdate: () => void;
}) {
  const { lang } = useLang(); const zh = lang === "zh";
  const [selected, setSelected] = useState<string[]>(activeLeaf ? [activeLeaf] : []);
  const [choice, setChoice] = useState(activeLeaf || leaves[0]?.slug || "");
  const [existingOnly, setExistingOnly] = useState(false);
  const [firstRound, setFirstRound] = useState(true);
  const [jobs, setJobs] = useState<BatchJob[]>([]);
  const [busy, setBusy] = useState(false); const [error, setError] = useState("");
  const [pollError, setPollError] = useState("");
  const [pollVersion, setPollVersion] = useState(0);
  const updateRef = useRef(onUpdate); updateRef.current = onUpdate;
  const progressRef = useRef("");
  useEffect(() => {
    if (!activeLeaf) return;
    setChoice(activeLeaf);
    setSelected(current => current.length ? current : [activeLeaf]);
  }, [activeLeaf]);
  useEffect(() => {
    let alive = true; let timer: ReturnType<typeof setTimeout>;
    async function poll() {
      try {
        const result = await listBatchJobs();
        if (!alive) return;
        setJobs(result.jobs);
        setPollError("");
        const signature = result.jobs.map(j => `${j.id}:${j.processed}:${j.status}`).join(",");
        if (progressRef.current && progressRef.current !== signature) updateRef.current();
        progressRef.current = signature;
        if (alive) timer = setTimeout(() => void poll(), document.hidden ? 60_000 : result.jobs.some(j => j.status === "running" || j.status === "retry_wait") ? 3000 : 30_000);
      } catch (e) {
        if (alive) { setPollError(e instanceof Error ? e.message : String(e)); timer = setTimeout(() => void poll(), 15_000); }
      }
    }
    void poll(); return () => { alive = false; clearTimeout(timer); };
  }, [pollVersion]);
  async function act(id?: string) {
    setBusy(true); setError("");
    try {
      const job = id ? await resumeBatchJob(id) : await startBatchJob(selected, existingOnly, firstRound ? 60 : undefined);
      setJobs(current => [job, ...current.filter(j => j.id !== job.id)]); updateRef.current();
      setPollVersion(v => v + 1);
    } catch (e) { setError(e instanceof Error ? e.message : String(e)); }
    finally { setBusy(false); }
  }
  const latest = jobs[0]; const running = jobs.some(j => j.status === "running" || j.status === "retry_wait" || j.status === "awaiting_acceptance");
  const names = (slug: string) => leaves.find(l => l.slug === slug)?.name || slug;
  return <section className="mt-5 rounded-xl border border-border bg-surface p-4" aria-label={zh ? "批量采集" : "Batch collection"}>
    <details>
      <summary className="cursor-pointer font-medium text-primary">{zh ? "批量采集 · 选择类型并自动续批" : "Batch collection · choose types and continue automatically"}</summary>
      <p className="mt-3 text-xs leading-5 text-muted">{zh ? "选择软件类型，自动整理本次发现的候选项目。资料不全先收录并标注；失败跳过，进度保存，中断后可以继续。" : "Choose existing types. Candidates are processed automatically; partial cards and progress are saved, and failures are skipped."}</p>
      <div className="mt-3 flex flex-wrap items-end gap-2">
        <label className="min-w-0 flex-1 text-xs text-muted">{zh ? "加入软件类型" : "Add a type"}<select value={choice} onChange={e => setChoice(e.target.value)} className="mt-1 h-10 w-full max-w-full rounded-lg border border-border bg-surface px-2 text-fg">{leaves.map(l => <option key={l.slug} value={l.slug}>{l.name}</option>)}</select></label>
        <Button variant="outline" disabled={!choice || selected.includes(choice)} onClick={() => setSelected(current => [...current, choice])}>{zh ? "加入" : "Add"}</Button>
      </div>
      <div className="mt-3 flex flex-wrap gap-2">{selected.map(slug => <button className="max-w-full break-words rounded-lg bg-chip px-3 py-1 text-xs" key={slug} aria-label={`${zh ? "移除" : "Remove"} ${names(slug)}`} onClick={() => setSelected(current => current.filter(s => s !== slug))}>{names(slug)} ×</button>)}</div>
      <label className="mt-4 flex items-start gap-2 text-xs leading-5 text-muted"><input type="checkbox" checked={existingOnly} onChange={e => setExistingOnly(e.target.checked)} />{zh ? "仅处理已有候选，本次不扩大搜索" : "Process existing candidates without expanding search"}</label>
      <label className="mt-3 flex items-start gap-2 text-xs leading-5 text-muted"><input type="checkbox" checked={firstRound} onChange={e => setFirstRound(e.target.checked)} />{zh ? "首轮优先覆盖：每个类型先处理60个候选，其余保留待补" : "First-round coverage: process up to 60 candidates per type and retain the rest"}</label>
      <Button className="mt-3" disabled={busy || running || !selected.length} onClick={() => void act()}>{zh ? "开始批量采集" : "Start batch collection"}</Button>
    </details>
    {latest && <div className="mt-3 text-sm" role="status">
      <p>{zh ? (latest.scope === "first_round" && latest.status === "completed" ? "首轮处理完成" : latest.scope === "first_round" && latest.status === "partial" ? "首轮处理结束，部分候选失败" : ({ running: "批量采集中", retry_wait: "临时故障，等待自动恢复", interrupted: "批量任务已中断，可继续", paused_model: "服务配置需处理，批量任务已暂停", completed: "批量采集完成", partial: "批量采集完成，部分项目失败或资料读取异常", awaiting_acceptance: "试跑结束，等待实际验收" })[latest.status]) : latest.status} · {latest.scope === "first_round" ? (zh ? "已选候选 " : "Selected candidates ") : ""}{latest.processed}/{latest.total}</p>
      <p className="mt-1 break-words text-xs text-muted">{latest.leaves.slice(0, 3).map(names).join("、")}{latest.leaves.length > 3 ? (zh ? ` 等${latest.leaves.length}个类型` : ` · ${latest.leaves.length} types`) : ""}{latest.status === "running" && latest.current_leaf ? ` · ${zh ? "当前" : "Current"}：${names(latest.current_leaf)}` : ""}</p>
      {latest.scope === "first_round" ? <>
        <p className="mt-1 text-xs text-muted">{zh ? `首轮已结束 ${latest.completed_leaves?.length || 0}/${latest.leaves.length} 个类型 · 每类型最多 ${latest.first_round_limit} 个候选 · 其余 ${latest.deferred_total || 0} 个候选保留待补` : `First round: ${latest.completed_leaves?.length || 0}/${latest.leaves.length} types · Up to ${latest.first_round_limit} candidates per type · ${latest.deferred_total || 0} deferred`}</p>
        <p className="mt-1 text-xs text-muted">{zh ? "按场景均衡、相关性、维护活跃度和成熟度排序，无 Stars 门槛。待补候选保留在候选池。" : "Balanced by scenario, relevance, activity and maturity, with no star cutoff. Deferred candidates remain saved."}</p>
        {!!latest.pilot?.size && <p className="mt-1 text-xs text-muted">{zh ? (latest.pilot.status === "passed" ? "试跑验收已通过，后续自动续批，每100个类型保存检查点。" : `先完成${latest.pilot.size}个类型的试跑与实际验收，通过后自动续批，无需逐批确认。`) : "The pilot is reviewed before automatic continuation; checkpoints are saved every 100 types."}</p>}
      </> : <p className="mt-1 text-xs text-muted">{zh ? `已准备 ${latest.prepared.length}/${latest.leaves.length} 个类型；${latest.existing_only ? "固定已有队列" : "每个类型搜索后固定本次队列"}，处理完成自动结束。` : "Each job processes a finite saved queue."}</p>}
      {(latest.pause_reason || latest.status === "retry_wait" && latest.recovery?.last_error) && <p className="mt-2 text-xs text-warn">{latest.pause_reason || latest.recovery?.last_error}</p>}
      {latest.status === "retry_wait" && <p className="mt-2 text-xs text-muted">{zh ? `进度已保存，将于 ${latest.recovery?.next_retry_at ? new Date(latest.recovery.next_retry_at).toLocaleString() : "稍后"} 自动重试，无需手动继续。` : `Progress is saved. Automatic retry: ${latest.recovery?.next_retry_at ? new Date(latest.recovery.next_retry_at).toLocaleString() : "soon"}.`}</p>}
      {latest.status === "retry_wait" && <Button className="mt-2" variant="outline" disabled={busy} onClick={() => void act(latest.id)}>{zh ? "立即重试" : "Retry now"}</Button>}
      {(latest.status === "interrupted" || latest.status === "paused_model") && <Button className="mt-2" variant="outline" disabled={busy || running} onClick={() => void act(latest.id)}>{zh ? "继续批量任务" : "Resume batch"}</Button>}
      {latest.errors.length > 0 && <details className="mt-2 text-xs text-muted"><summary className="cursor-pointer">{zh ? `查看 ${latest.errors.length} 条异常记录` : "View errors"}</summary><ul className="mt-2 max-h-48 space-y-2 overflow-auto">{latest.errors.map((e, i) => <li className="break-words" key={i}>{e.leaf ? `${names(e.leaf)}：` : ""}{e.error}</li>)}</ul></details>}
    </div>}
    {pollError && <div role="status" className="mt-3 flex flex-wrap items-center gap-3 text-xs text-warn"><p>{zh ? "任务状态暂时无法刷新，已保存的进度保留。" : "Job status could not be refreshed. Saved progress is retained."}</p><button className="min-h-9 underline" onClick={() => setPollVersion(v => v + 1)}>{zh ? "重试状态" : "Retry status"}</button></div>}
    {error && <p role="alert" className="mt-3 break-words text-xs text-danger">{error}</p>}
  </section>;
}
