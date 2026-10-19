import type { ProjectTask, ProjectWorkspace } from "./atlas";

export type ProjectStageId = "understand" | "scope" | "plan" | "execute";

export type ProjectStatusCount = {
  value: number;
  zh: string;
  en: string;
};

export type ProjectLifecycleStep = {
  done: boolean;
  zh: string;
  en: string;
  stage: ProjectStageId;
};

export function projectLifecycleSteps(
  workspace: ProjectWorkspace,
  hasBaseline: boolean | null,
): ProjectLifecycleStep[] {
  const confirmed = workspace.requirements.some((item) => item.confirmed_scope === "current");
  const documentsReady = workspace.documents.some((item) =>
    item.review.status === "current" && item.review.approval === "approved");
  const latestIteration = workspace.iterations
    .slice()
    .sort((a, b) => b.sequence - a.sequence)[0] || null;
  const currentIteration = workspace.iterations.find((item) => item.status === "active")
    || (latestIteration?.status === "completed" ? latestIteration : null);
  const currentTasks = currentIteration
    ? workspace.tasks.filter((item) => item.iteration_id === currentIteration.id)
    : [];
  const currentTaskIds = new Set(currentTasks.map((item) => item.id));
  const currentExecutions = workspace.executions.filter((item) => currentTaskIds.has(item.task_id));
  const latestExecution = (task: ProjectTask) =>
    currentExecutions.find((execution) => execution.task_id === task.id);
  const iterationComplete = currentIteration?.status === "completed";
  const executed = iterationComplete || (currentTasks.length > 0 && currentTasks.every((task) =>
    task.execution_status === "completed" || task.acceptance_status === "waived"));
  const applied = iterationComplete || (currentTasks.length > 0 && currentTasks.every((task) => {
    if (task.acceptance_status === "waived") return true;
    const execution = latestExecution(task);
    if (task.kind === "analysis") {
      return execution?.status === "completed" && execution.application_status === "not_applicable";
    }
    return execution?.status === "completed"
      && execution.application_status === "applied"
      && !execution.application_state.baseline_adoption_error;
  }));
  const accepted = iterationComplete || (currentTasks.length > 0
    && currentTasks.every((item) => ["passed", "waived"].includes(item.acceptance_status)));
  return [
    { done: workspace.references.length > 0, zh: "收集资料", en: "Sources", stage: "understand" },
    { done: confirmed, zh: "确认需求", en: "Scope", stage: "scope" },
    { done: documentsReady, zh: "形成文档", en: "Documents", stage: "plan" },
    { done: hasBaseline === true, zh: "确认工作区", en: "Workspace", stage: "understand" },
    { done: Boolean(currentIteration), zh: "建立迭代", en: "Iteration", stage: "plan" },
    { done: executed, zh: "执行改动", en: "Execution", stage: "execute" },
    { done: applied, zh: "应用结果", en: "Apply", stage: "execute" },
    { done: accepted, zh: "产品验收", en: "Acceptance", stage: "execute" },
    { done: iterationComplete, zh: "完成迭代", en: "Complete", stage: "execute" },
  ];
}

export function projectBlockingCounts(
  workspace: ProjectWorkspace,
  activeIteration: ProjectWorkspace["iterations"][number] | null,
  hasBaseline: boolean | null,
): ProjectStatusCount[] {
  const openItems = (workspace.open_items || []).filter((item) => item.current && item.status === "open");
  if (!activeIteration) {
    if (hasBaseline === null) return [];
    return [
      { value: workspace.references.length ? 0 : 1, zh: "缺少固定资料", en: "Sources missing" },
      { value: workspace.requirements.some((item) => item.confirmed_scope === "current") ? 0 : 1, zh: "缺少已确认需求", en: "Confirmed scope missing" },
      { value: workspace.documents.some((item) => item.review.status === "current" && item.review.approval === "approved") ? 0 : 1, zh: "缺少可冻结文档", en: "Approved document missing" },
      { value: hasBaseline ? 0 : 1, zh: "缺少工作区基线", en: "Workspace baseline missing" },
    ];
  }

  const selectedDocumentVersions = new Set(activeIteration.input_document_versions);
  const selectedDocumentsNeedReview = workspace.documents.filter((item) =>
    selectedDocumentVersions.has(item.version_id)
    && (item.review.status === "needs_review" || item.review.approval !== "approved"));
  const currentTasks = workspace.tasks.filter((item) => item.iteration_id === activeIteration.id);
  const currentTaskIds = new Set(currentTasks.map((item) => item.id));
  const currentExecutions = workspace.executions.filter((item) => currentTaskIds.has(item.task_id));
  const latestExecution = (task: ProjectTask) =>
    currentExecutions.find((execution) => execution.task_id === task.id);
  const unresolvedTasks = currentTasks.filter((item) => item.acceptance_status !== "waived");
  return [
    { value: openItems.filter((item) => item.kind === "question").length, zh: "开放问题", en: "Open questions" },
    { value: openItems.filter((item) => item.kind === "conflict").length, zh: "明确冲突", en: "Conflicts" },
    { value: workspace.requirements.filter((item) => !item.confirmed_scope).length, zh: "待确认需求", en: "Pending requirements" },
    { value: selectedDocumentsNeedReview.length, zh: "本轮文档待复核", en: "Current documents to review" },
    { value: unresolvedTasks.filter((item) => ["planned", "queued"].includes(item.execution_status)).length, zh: "等待执行", en: "Awaiting execution" },
    { value: unresolvedTasks.filter((item) => ["running", "waiting_permission", "waiting_input"].includes(item.execution_status)).length, zh: "执行中", en: "Execution in progress" },
    { value: unresolvedTasks.filter((item) => ["failed", "stopped", "unknown"].includes(item.execution_status)).length, zh: "执行异常", en: "Execution exceptions" },
    { value: unresolvedTasks.filter((item) => {
      if (item.kind === "analysis" || item.execution_status !== "completed") return false;
      const execution = latestExecution(item);
      return execution?.application_status !== "applied" || Boolean(execution.application_state.baseline_adoption_error);
    }).length, zh: "结果待应用", en: "Results awaiting application" },
    { value: unresolvedTasks.filter((item) => {
      if (item.execution_status !== "completed" || ["passed", "waived"].includes(item.acceptance_status)) return false;
      if (item.kind === "analysis") return true;
      const execution = latestExecution(item);
      return execution?.application_status === "applied" && !execution.application_state.baseline_adoption_error;
    }).length, zh: "待产品验收", en: "Awaiting product acceptance" },
  ];
}
