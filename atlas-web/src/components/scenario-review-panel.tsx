import { useState } from "react";
import { scenarioReviewState, type Scenario, type ScenarioReview } from "@/lib/factory";

const dimensions: Record<string, [string, string]> = {
  leaf_fit: ["类型匹配", "Type fit"], distinctness: ["场景区分", "Distinctness"],
  workflow: ["流程完整性", "Workflow"], testability: ["验收可验证性", "Testability"],
  scope: ["范围与一致性", "Scope and consistency"],
};
const outcomes: Record<string, [string, string]> = {
  passed: ["通过", "Passed"], needs_changes: ["需要修改", "Needs changes"],
  rejected: ["不建议采用", "Not recommended"],
};

function Report({review, zh}: {review: ScenarioReview; zh: boolean}) {
  const label = (value: string) => outcomes[value]?.[zh ? 0 : 1] || value;
  return <div className="mt-3 space-y-3 text-xs leading-5 text-muted">
    <p>{review.summary}</p>
    <p>{review.model} · r{review.scenario_revision} · {new Date(review.created_at).toLocaleString()}</p>
    <ul className="space-y-2">{review.checks.map(check => <li key={check.dimension}>
      <span className="font-medium text-fg">{dimensions[check.dimension]?.[zh ? 0 : 1] || check.dimension} · {label(check.outcome)}</span>
      <p>{check.reason}</p>
    </li>)}</ul>
    <div><p className="font-medium text-fg">{zh ? "引用的类型定义" : "Quoted type evidence"}</p>
      {review.leaf_quotes.map((quote, i) => <blockquote key={i} className="mt-1 border-l-2 border-border pl-3">
        {review.leaf_evidence?.[i] ? <p className="text-subtle">{zh?"类型正文行号：":"Type document lines: "}{review.leaf_evidence[i].start_line}–{review.leaf_evidence[i].end_line}</p> : null}
        <p className="whitespace-pre-wrap">{quote}</p>
      </blockquote>)}
    </div>
    {review.suggestions.length > 0 ? <div><p className="font-medium text-fg">{zh ? "修改建议" : "Suggested revisions"}</p>
      <ul className="list-inside list-disc">{review.suggestions.map((suggestion, i) => <li key={i}>{suggestion}</li>)}</ul>
    </div> : null}
    <p>{zh ? `本次对照同类型的 ${review.peer_scenarios.length} 个场景，不代表全库去重或实际运行验证。` : `Compared with ${review.peer_scenarios.length} same-type scenarios; this is not corpus-wide deduplication or runtime verification.`}</p>
    {review.related_scenario_ids.length > 0 ? <p>{zh ? "重叠场景：" : "Overlapping scenarios: "}
      {review.related_scenario_ids.map(id => review.peer_scenarios.find(p => p.id === id)?.name || id).join("、")}</p> : null}
    <p>{zh ? "Agent 审阅提供建议；是否确认场景由你决定。" : "Agent review advises; you decide whether to confirm the scenario."}</p>
  </div>;
}

export function ScenarioReviewPanel({scenario, zh}: {scenario: Scenario; zh: boolean}) {
  const [open, setOpen] = useState(false);
  const reviews = scenario.reviews || [];
  const {current, latestJob, pending, failed} = scenarioReviewState(scenario);
  const displayed = current || reviews[0];
  const outdatedPending = scenario.review_jobs?.some(job => !job.current && ["queued", "running"].includes(job.state));
  const label = displayed ? outcomes[displayed.outcome]?.[zh ? 0 : 1] : null;
  return <section className={`mt-3 rounded-lg border p-3 ${current?.outcome === "passed" && !pending && !failed ? "border-primary/25 bg-primary/5" : "border-border"}`} aria-label={zh ? "场景独立审阅" : "Independent scenario review"}>
    <p className="text-xs font-medium">{zh ? "场景独立审阅" : "Independent scenario review"} · {pending
      ? latestJob?.state === "queued" ? (zh ? "排队中" : "Queued") : (zh ? "审阅中" : "Reviewing")
      : displayed ? `${label}${displayed.current ? "" : zh ? "（已过期，需重新审阅）" : " (outdated; review again)"}`
      : zh ? "尚未审阅" : "Not reviewed"}</p>
    {current?.outcome === "passed" && scenario.status === "draft" ? <p className="mt-2 text-xs font-medium text-primary">{zh ? "Agent 审阅已通过 · 待你人工确认" : "Agent review passed · Awaiting your confirmation"}</p> : null}
    {scenario.status === "draft" ? <p className="mt-2 text-xs leading-5 text-muted">{zh ? "点击“编辑 / 确认场景”，将场景状态改为“已确认，可以生产”并保存；Agent 不会自动确认场景。" : "Choose “Edit / confirm”, set the scenario status to “Confirmed, ready to produce” and save. Agent review does not confirm scenarios automatically."}</p> : null}
    {failed ? <p role="status" className="mt-2 text-xs text-danger">{zh ? "最近一次审阅未完成，可重新发起；已有结论保留。" : "The latest review did not complete; request it again. Earlier reports are retained."}{latestJob?.error ? ` ${latestJob.error}` : ""}</p> : null}
    {outdatedPending ? <p className="mt-2 text-xs text-muted">{zh ? "另有旧版本审阅仍在处理，其结果不会作为当前版本结论。" : "An older version is still under review; its report will not apply to the current version."}</p> : null}
    {displayed && !displayed.current ? <p className="mt-2 text-xs text-muted">{zh ? "场景、类型正文或对照场景已有更新，旧结论仅供参考。" : "The scenario, type document or peer scenarios changed; this report is historical."}</p> : null}
    {displayed ? <>
      <button type="button" className="mt-2 text-xs text-primary underline" aria-expanded={open} onClick={() => setOpen(value => !value)}>{open ? (zh ? "收起审阅结论" : "Hide review") : (zh ? "查看审阅理由与建议" : "Review reasons and suggestions")}</button>
      {open ? <Report review={displayed} zh={zh}/> : null}
    </> : null}
    {reviews.length > 1 ? <details className="mt-3 text-xs"><summary className="cursor-pointer text-primary">{zh ? "历史审阅" : "Review history"} · {reviews.length - 1}</summary>
      {reviews.filter(review => review.id !== displayed?.id).map(review => <details key={review.id} className="mt-2"><summary className="cursor-pointer">r{review.scenario_revision} · {outcomes[review.outcome]?.[zh ? 0 : 1]} · {review.current ? (zh ? "当前版本" : "Current") : (zh ? "已过期" : "Outdated")}</summary><Report review={review} zh={zh}/></details>)}
    </details> : null}
  </section>;
}
