import assert from "node:assert/strict";
import test from "node:test";
import {
  projectBlockingCounts,
  projectLifecycleSteps,
} from "../src/lib/project-status.ts";
import type { ProjectWorkspace } from "../src/lib/atlas";

function workspace(overrides: Partial<ProjectWorkspace> = {}): ProjectWorkspace {
  return {
    project: {
      id: "prj_test",
      name: "Test",
      objective: "Test state truthfulness",
      workspace: "/tmp/test",
      mode: "new",
      created_at: "2026-01-01T00:00:00Z",
      updated_at: "2026-01-01T00:00:00Z",
    },
    references: [],
    requirements: [],
    decisions: [],
    documents: [],
    iterations: [],
    tasks: [],
    executions: [],
    open_items: [],
    ...overrides,
  } as ProjectWorkspace;
}

function approvedDocument() {
  return {
    id: "doc_test",
    project_id: "prj_test",
    kind: "technical-plan",
    title: "Technical plan",
    current_version: 1,
    version_id: "dver_test",
    content: "Plan",
    content_sha256: "hash",
    basis: [],
    author: "human",
    change_summary: "Initial",
    review: { status: "current", approval: "approved", freshness: "current" },
    created_at: "2026-01-01T00:00:00Z",
    updated_at: "2026-01-01T00:00:00Z",
    version_created_at: "2026-01-01T00:00:00Z",
  } as ProjectWorkspace["documents"][number];
}

function activeIteration() {
  return {
    id: "itr_test",
    project_id: "prj_test",
    sequence: 1,
    title: "Iteration",
    objective: "Ship safely",
    status: "active",
    input_document_versions: ["dver_test"],
    requirement_ids: ["req_test"],
    created_at: "2026-01-01T00:00:00Z",
    updated_at: "2026-01-01T00:00:00Z",
  } as ProjectWorkspace["iterations"][number];
}

function task(overrides: Partial<ProjectWorkspace["tasks"][number]> = {}) {
  return {
    id: "tsk_test",
    project_id: "prj_test",
    iteration_id: "itr_test",
    title: "Task",
    objective: "Complete the task",
    kind: "code",
    execution_status: "planned",
    acceptance_status: "pending",
    acceptance_evidence: [],
    requirement_ids: ["req_test"],
    requirement_revisions: [],
    input_document_versions: ["dver_test"],
    write_paths: ["src"],
    verification_commands: [],
    created_at: "2026-01-01T00:00:00Z",
    updated_at: "2026-01-01T00:00:00Z",
    ...overrides,
  } as ProjectWorkspace["tasks"][number];
}

function execution(overrides: Partial<ProjectWorkspace["executions"][number]> = {}) {
  return {
    id: "exe_test",
    task_id: "tsk_test",
    engine: "opencode",
    status: "completed",
    application_status: "applied",
    application_state: { accepted_baseline_id: "snap_test" },
    ...overrides,
  } as ProjectWorkspace["executions"][number];
}

function count(counts: ReturnType<typeof projectBlockingCounts>, english: string) {
  return counts.find((item) => item.en === english)?.value || 0;
}

test("new projects expose setup blockers instead of an empty state", () => {
  const current = workspace();
  const counts = projectBlockingCounts(current, null, false);
  assert.equal(count(counts, "Sources missing"), 1);
  assert.equal(count(counts, "Confirmed scope missing"), 1);
  assert.equal(count(counts, "Approved document missing"), 1);
  assert.equal(count(counts, "Workspace baseline missing"), 1);
});

test("a current but unapproved document is not ready to freeze", () => {
  const current = workspace({
    references: [{ id: "ref_test" } as ProjectWorkspace["references"][number]],
    requirements: [{ id: "req_test", confirmed_scope: "current" } as ProjectWorkspace["requirements"][number]],
    documents: [{
      ...approvedDocument(),
      review: { status: "current", approval: "pending", freshness: "current" },
    }],
  });
  const steps = projectLifecycleSteps(current, true);
  assert.equal(steps.find((item) => item.en === "Documents")?.done, false);
  assert.equal(count(projectBlockingCounts(current, null, true), "Approved document missing"), 1);
});

test("failed stopped and unknown executions never count as completed", () => {
  for (const status of ["failed", "stopped", "unknown"] as const) {
    const current = workspace({
      references: [{ id: "ref_test" } as ProjectWorkspace["references"][number]],
      requirements: [{ id: "req_test", confirmed_scope: "current" } as ProjectWorkspace["requirements"][number]],
      documents: [approvedDocument()],
      iterations: [activeIteration()],
      tasks: [task({ execution_status: status })],
      executions: [execution({ status })],
    });
    const steps = projectLifecycleSteps(current, true);
    assert.equal(steps.find((item) => item.en === "Execution")?.done, false);
    assert.equal(count(projectBlockingCounts(current, activeIteration(), true), "Execution exceptions"), 1);
  }
});

test("a completed applied task waits for independent acceptance", () => {
  const iteration = activeIteration();
  const current = workspace({
    references: [{ id: "ref_test" } as ProjectWorkspace["references"][number]],
    requirements: [{ id: "req_test", confirmed_scope: "current" } as ProjectWorkspace["requirements"][number]],
    documents: [approvedDocument()],
    iterations: [iteration],
    tasks: [task({ execution_status: "completed" })],
    executions: [execution()],
  });
  const steps = projectLifecycleSteps(current, true);
  assert.equal(steps.find((item) => item.en === "Execution")?.done, true);
  assert.equal(steps.find((item) => item.en === "Apply")?.done, true);
  assert.equal(steps.find((item) => item.en === "Acceptance")?.done, false);
  assert.equal(count(projectBlockingCounts(current, iteration, true), "Awaiting product acceptance"), 1);
});

test("a completed historical iteration remains complete for legacy records", () => {
  const completed = { ...activeIteration(), status: "completed" as const };
  const current = workspace({
    references: [{ id: "ref_test" } as ProjectWorkspace["references"][number]],
    requirements: [{ id: "req_test", confirmed_scope: "current" } as ProjectWorkspace["requirements"][number]],
    documents: [approvedDocument()],
    iterations: [completed],
    tasks: [task({ execution_status: "planned", acceptance_status: "passed" })],
  });
  assert.equal(projectLifecycleSteps(current, true).every((item) => item.done), true);
});
