const cache = new Map<string, { promise: Promise<unknown>; expires: number }>();

export function invalidateAtlasCache() {
  cache.clear();
}

export function fetchJson<T>(url: string): Promise<T> {
  const entry = cache.get(url);
  if (entry && entry.expires > Date.now()) return entry.promise as Promise<T>;
  const promise = fetch(url, { cache: "no-cache" }).then((response) => {
    if (!response.ok) throw new Error(`${response.status} ${url}`);
    return response.json() as Promise<T>;
  });
  cache.set(url, { promise, expires: Date.now() + 15000 });
  promise.catch(() => {
    if (cache.get(url)?.promise === promise) cache.delete(url);
  });
  return promise;
}

async function requestJson<T>(url: string, init: RequestInit): Promise<T> {
  const response = await fetch(url, { ...init, cache: "no-cache" });
  const value = await response.json().catch(() => null) as { error?: string } | null;
  if (!response.ok) throw new Error(value?.error || `${response.status} ${url}`);
  return value as T;
}

export interface LeafIndexItem {
  slug: string;
  name: string;
  name_zh: string;
  sec: string;
  dc: string;
  dc_zh?: string;
}

export interface SubSection {
  id: string;
  name: string;
  name_zh?: string;
  path: string;
}

export interface L0 {
  id: string;
  name: string;
  name_zh?: string;
  subs: SubSection[];
}

export interface Meta {
  leafCount: number;
  sectionCount: number;
  l0Count: number;
  appCount: number;
  l0s: L0s[];
  leafIndex: LeafIndexItem[];
}
type L0s = L0;

export interface SectionData {
  id: string;
  name: string;
  name_zh?: string;
  path: string;
  leaves: { slug: string; name: string; name_zh: string; l0: string; l0_zh?: string }[];
}

export interface LeafDetail {
  slug: string;
  name: string;
  name_zh: string;
  aliases_zh: string[];
  section_id: string;
  section_name: string;
  section_name_zh?: string;
  overview: string;
  overview_zh?: string;
  dc: string;
  dc_zh?: string;
  how: string;
  how_zh?: string;
  rules: string;
  rules_zh?: string;
  variants: string;
  variants_zh?: string;
  products: string;
  products_zh?: string;
  sources?: string;
  full_md?: string;
  relations: { to: string; toName: string; kind: string; distinction: string; distinction_zh?: string }[];
  apps: { slug: string; name: string }[];
}

export interface AppEntry {
  slug: string;
  name: string;
  vendor: string;
  tagline: string;
  tasks: string[];
  leaf: string;
  leafName: string;
}

export interface AtlasProject {
  id: string;
  name: string;
  objective: string;
  workspace: string;
  mode: "new" | "existing";
  created_at: string;
  updated_at: string;
}

export interface CreateProjectInput {
  name: string;
  objective: string;
  workspace?: string;
  mode: AtlasProject["mode"];
  starter_reference?: {
    kind: AtlasSourceKind;
    slug: string;
    section?: string;
    note?: string;
    read_status?: ProjectReference["read_status"];
  };
}

export interface DeleteProjectResult {
  id: string;
  deleted: boolean;
  workspace: string;
  workspace_preserved: boolean;
  deleted_records: Record<string, number>;
}

export type AtlasSourceKind = "application" | "research";
export type AtlasReferenceKind = AtlasSourceKind | "app";

export interface SourceOutlineItem {
  id: string;
  title: string;
  level: number;
  line: number;
  chars: number;
}

export interface SourceManifest {
  slug: string;
  sources: {
    kind: AtlasSourceKind;
    chars: number;
    lines: number;
    fingerprint: string;
    outline: SourceOutlineItem[];
  }[];
}

export interface AtlasSourcePage {
  slug: string;
  kind: AtlasSourceKind;
  fingerprint: string;
  document_chars: number;
  document_lines: number;
  section: SourceOutlineItem | null;
  offset: number;
  limit: number;
  returned_chars: number;
  selected_chars: number;
  line_start: number;
  line_end: number;
  complete: boolean;
  next_offset: number | null;
  content: string;
  outline: SourceOutlineItem[];
}

export interface ProjectReference {
  id: string;
  project_id: string;
  source_kind: string;
  source_ref: string;
  source_version: string;
  locator: string;
  excerpt: string;
  note: string;
  read_status: "unread" | "read" | "reviewed";
  created_at: string;
  updated_at: string;
  source_available?: boolean;
  current_version?: string | null;
  stale?: boolean;
}

export type ProjectScope = "current" | "later" | "excluded";

export interface ProjectRequirement {
  id: string;
  project_id: string;
  content: string;
  revision?: number;
  recommended_scope: ProjectScope | null;
  recommendation_reason: string;
  confirmed_scope: ProjectScope | null;
  confirmation_reason: string;
  acceptance_conditions: string[];
  reference_ids: string[];
  created_at: string;
  updated_at: string;
}

export interface ProjectDecision {
  id: string;
  project_id: string;
  statement: string;
  rationale: string;
  reference_ids: string[];
  created_at: string;
}

export type ProjectDocumentKind =
  | "analysis"
  | "value-analysis"
  | "product-requirements"
  | "interaction"
  | "technical-plan"
  | "development-plan"
  | "acceptance-plan"
  | "current-state";

export interface DocumentBasis {
  kind?: "reference" | "requirement" | "decision" | "document_version" | "workspace_baseline";
  id?: string;
  source?: string;
  version?: string | number;
  fingerprint?: string;
}

export interface DocumentReview {
  status: "current" | "needs_review";
  freshness?: "current" | "needs_review";
  approval?: "pending" | "approved" | "rejected";
  note?: string;
  reviewed_at?: string | null;
  reasons: { kind: "requirement_changed" | "upstream_document_changed" | "workspace_baseline_changed"; id: string; document_id?: string; current_baseline_id?: string }[];
}

export type ProjectOpenItemKind = "question" | "conflict" | "suggestion";
export type ProjectOpenItemStatus = "open" | "answered" | "resolved" | "accepted" | "deferred" | "dismissed";

export interface ProjectOpenItem {
  id: string;
  run_id: string;
  mode: "analysis" | "improvement" | "value";
  kind: ProjectOpenItemKind;
  index: number;
  key: string;
  title: string;
  detail: string;
  affects: ProjectDocumentKind[];
  reference_ids: string[];
  created_at: string;
  status: ProjectOpenItemStatus;
  note: string;
  decision_id: string | null;
  requirement_id: string | null;
  current: boolean;
}

export interface ProjectDocument {
  id: string;
  project_id: string;
  kind: ProjectDocumentKind;
  title: string;
  current_version: number;
  version_id: string;
  content: string;
  content_sha256: string;
  basis: DocumentBasis[];
  author: "ai" | "human" | "import" | "unknown";
  change_summary: string;
  review: DocumentReview;
  created_at: string;
  updated_at: string;
  version_created_at: string;
}

export interface ProjectDocumentVersion {
  version_id: string;
  document_id: string;
  version: number;
  content: string;
  content_sha256: string;
  basis: DocumentBasis[];
  author: ProjectDocument["author"];
  change_summary: string;
  review: DocumentReview;
  created_at: string;
}

export interface ProjectWorkspace {
  project: AtlasProject;
  references: ProjectReference[];
  requirements: ProjectRequirement[];
  decisions: ProjectDecision[];
  documents: ProjectDocument[];
  iterations: ProjectIteration[];
  tasks: ProjectTask[];
  executions: ProjectExecution[];
  open_items?: ProjectOpenItem[];
}

export interface ProjectIteration {
  id: string;
  project_id: string;
  sequence: number;
  title: string;
  objective: string;
  status: "planned" | "active" | "completed" | "abandoned";
  input_document_versions: string[];
  requirement_ids: string[];
  requirement_revisions?: { requirement_id: string; revision: number }[];
  baseline_id?: string | null;
  baseline_history?: { baseline_id: string | null; rebased_at: string; note: string }[];
  created_at: string;
  updated_at: string;
  completed_at: string | null;
}

export interface ProjectTask {
  id: string;
  project_id: string;
  iteration_id: string | null;
  kind: "analysis" | "document" | "code";
  title: string;
  objective: string;
  write_paths: string[];
  verification_commands: string[];
  timeout_seconds?: number | null;
  execution_status: "planned" | "queued" | "running" | "waiting_permission" | "waiting_input" | "completed" | "failed" | "stopped" | "unknown";
  acceptance_status: "pending" | "passed" | "failed" | "waived";
  acceptance_evidence: { kind: string; summary: string; [key: string]: unknown }[];
  input_document_versions: string[];
  requirement_ids: string[];
  requirement_revisions?: { requirement_id: string; revision: number }[];
  created_at: string;
  updated_at: string;
}

export interface ExecutionFilesystemEvidence {
  added: string[];
  modified: string[];
  removed: string[];
  changed: boolean;
  write_scope: string[];
  out_of_scope_changes: string[];
  scope_compliant: boolean;
}

export interface ExecutionQuestion {
  question: string;
  header: string;
  options: { label: string; description: string }[];
  multiple?: boolean;
  custom?: boolean;
}

export interface HarnessPreflight {
  status: "passed" | "failed" | "not_configured";
  configPath?: string;
  executable?: string;
  version?: string;
  minimumVersion?: string;
  providerNames?: string[];
  code?: string;
  message?: string;
  checks?: {
    version?: { passed?: boolean; exitCode?: number };
    providers?: { passed?: boolean; exitCode?: number };
  };
  diagnostics?: { providerOutputPresent?: boolean; timedOut?: boolean };
}

export interface ProjectExecution {
  id: string;
  task_id: string;
  engine: "opencode" | "opencode-cli";
  engine_session_id: string;
  engine_message_id: string | null;
  status: Exclude<ProjectTask["execution_status"], "planned">;
  before_snapshot_id: string | null;
  after_snapshot_id: string | null;
  applied_snapshot_id: string | null;
  workdir: string;
  source_workdir: string;
  application_status: "not_applicable" | "pending" | "applying" | "applied" | "conflict" | "failed" | "superseded";
  application_state: {
    strategy?: "isolated_copy";
    source_workdir?: string;
    execution_workdir?: string;
    baseline_id?: string;
    accepted_baseline_id?: string | null;
    baseline_adoption_error?: string;
    added?: string[];
    modified?: string[];
    removed?: string[];
    error?: string;
    superseded_by_execution_id?: string;
    reason?: string;
  };
  input_state: {
    schema?: number;
    project_id?: string;
    iteration_id?: string;
    task_id?: string;
    task_kind?: ProjectTask["kind"];
    document_version_ids?: string[];
    requirement_ids?: string[];
    workspace_baseline?: { id: string; fingerprint: string; content_fingerprint: string };
    source_workdir?: string;
    workdir?: string;
    workspace_strategy?: "isolated_copy";
    omitted_dependency_names?: string[];
    write_paths?: string[];
    verification_commands?: string[];
    model?: string;
    transport?: "http" | "cli";
    continuation_of?: string;
    follow_up_instruction?: string;
    session_user_message_ids_before?: string[];
  };
  capabilities: Record<string, boolean>;
  raw_state: {
    state?: ProjectExecution["status"];
    engine_status?: string;
    evidence?: {
      message_ids?: string[];
      assistant_text?: string;
      engine_diff?: unknown[];
      filesystem?: ExecutionFilesystemEvidence;
      verification?: {
        planned_commands: string[];
        successful_commands: string[];
        missing_or_failed_commands: string[];
        all_planned_passed: boolean;
      };
      completion_report?: {
        reported: boolean;
        valid: boolean;
        error: string;
        requirements: { id: string; status: "satisfied" | "unsatisfied" | "not_checked"; evidence: string[] }[];
        unfinished: string[];
        deviations: string[];
      };
      tool_calls?: {
        commands: { command: string; planned: boolean; status: string; exit: number | null; output: string; truncated: boolean; durationMs?: number; timedOut?: boolean }[];
        file_edits: { tool: string; path: string; status: string; additions: number | null; deletions: number | null }[];
      };
      usage?: { cost: number; tokens: Record<string, number> };
      run_summary?: {
        status?: string;
        engineStatus?: string;
        exitCode?: number | null;
        timedOut?: boolean;
        verification?: Record<string, unknown>;
      };
      cli_run?: {
        directory?: string;
        files?: Record<string, string>;
        summary?: {
          status?: string;
          exitCode?: number | null;
          timedOut?: boolean;
          eventTypes?: string[];
          stdoutBytes?: number;
          stderrBytes?: number;
          jsonEventCount?: number;
          [key: string]: unknown;
        };
      };
      cleanup?: {
        status?: string;
        workdir?: string;
        evidence_directory?: string;
        evidence_preserved?: boolean;
      };
      error?: string;
      detail?: string;
    };
    interaction?: null | {
      type: "permission" | "question";
      request: {
        id: string;
        permission?: string;
        patterns?: string[];
        metadata?: Record<string, unknown>;
        questions?: ExecutionQuestion[];
      };
    };
  };
  created_at: string;
  updated_at: string;
  finished_at: string | null;
  applied_at: string | null;
}

export interface WorkspaceGitState {
  repository: boolean;
  root: string | null;
  head: string | null;
  branch: string | null;
  dirty: boolean | null;
  changes: string[];
  truncated: boolean;
  error: string;
}

export interface WorkspaceInventory {
  file_count: number;
  symlink_count: number;
  total_bytes: number;
  document_paths: string[];
  document_paths_truncated: boolean;
  manifest_paths: string[];
  test_paths: string[];
  test_paths_truncated: boolean;
  suffix_counts: Record<string, number>;
  code_suffix_counts: Record<string, number>;
}

export interface WorkspaceCoverage {
  ignore_names: string[];
  focus_paths: string[];
  hashed_paths: number;
  read_paths: string[];
  partial_paths: string[];
  skipped_count: number;
  skipped: { path: string; reason: string }[];
  skipped_truncated: boolean;
  read_chars: number;
  limits: { files: number; total_chars: number; per_file_chars: number };
}

export interface WorkspaceObservation {
  category: "document_claim" | "code_clue" | "runtime_verified" | "unknown";
  summary: string;
  path?: string;
  evidence?: { path: string; sha256: string; complete: boolean };
}

export interface WorkspaceBaselineSummary {
  id: string;
  project_id: string;
  phase: "observed";
  workspace_root: string;
  fingerprint: string;
  created_at: string;
  root: string;
  git: WorkspaceGitState;
  inventory: WorkspaceInventory;
  coverage: WorkspaceCoverage;
  observations: {
    document_claims: WorkspaceObservation[];
    code_clues: WorkspaceObservation[];
    runtime_verified: WorkspaceObservation[];
    unknown: WorkspaceObservation[];
  };
  report_markdown: string;
  snapshot_errors: { path: string; error: string }[];
  content_fingerprint: string;
  changes_from_previous?: WorkspaceChangeSet | null;
}

export interface WorkspaceChangeSet {
  root: string;
  added: string[];
  removed: string[];
  modified: string[];
  changed: boolean;
  before_errors: { path: string; error: string }[];
  after_errors: { path: string; error: string }[];
  changed_paths: string[];
  reviewed_scope_changes: string[];
  outside_review_scope_changes: string[];
  git_state_changed: boolean;
  git_revision_changed: boolean;
  git_worktree_state_changed: boolean;
  requires_focused_review: boolean;
  has_unread_changes: boolean;
  comparison_limited_by_errors: boolean;
}

export interface WorkspaceBaselineCheck {
  baseline: WorkspaceBaselineSummary;
  current: Omit<WorkspaceBaselineSummary, "id" | "project_id" | "phase" | "workspace_root" | "fingerprint" | "created_at">;
  changes: WorkspaceChangeSet;
}

export interface ProjectExport {
  project_id: string;
  directory: string;
  archive: string;
  archive_sha256: string;
  manifest: {
    schema: number;
    counts: Record<string, number>;
    workspace_baseline_id: string | null;
    workspace_baseline_fingerprint: string | null;
    active_iteration_id: string | null;
    unaccepted_task_ids: string[];
    unapplied_execution_ids: string[];
    invalid_completion_report_execution_ids: string[];
    unresolved_requirement_ids: string[];
    documents_needing_review: string[];
  };
}

export interface GeneratedQuestion {
  question: string;
  why: string;
  affects: ProjectDocumentKind[];
}

export interface GeneratedRequirement {
  key: string;
  content: string;
  recommended_scope: ProjectScope;
  recommendation_reason: string;
  acceptance_conditions: string[];
  reference_ids: string[];
}

export interface GeneratedSignal {
  summary: string;
  impact?: string;
  reason?: string;
  evidence: { kind: NonNullable<DocumentBasis["kind"]>; id: string }[];
}

export interface GeneratedDocument {
  document_id: string | null;
  kind: ProjectDocumentKind;
  title: string;
  content: string;
  basis: { kind: NonNullable<DocumentBasis["kind"]>; id: string }[];
  depends_on: ProjectDocumentKind[];
  diff?: string;
}

export interface AppliedGeneratedDocument {
  document_id: string;
  version_id: string;
}

export interface ProjectGenerationResult {
  input_fingerprint: string;
  questions: GeneratedQuestion[];
  requirements: GeneratedRequirement[];
  conflicts: GeneratedSignal[];
  suggestions: GeneratedSignal[];
  documents: GeneratedDocument[];
}

export interface ProjectGenerationRun {
  id: string;
  project_id: string;
  mode: "analysis" | "value" | "documents" | "improvement" | "revision";
  improvement_goal?: string;
  revision?: {
    document_id: string;
    version_id: string;
    current_version: number;
    kind: ProjectDocumentKind;
    title: string;
    content_sha256: string;
    section_heading: string;
    instruction: string;
  } | null;
  document_kinds: ProjectDocumentKind[];
  document_dependencies?: Partial<Record<ProjectDocumentKind, ProjectDocumentKind[]>>;
  engine: "opencode";
  model: string;
  status: "queued" | "running" | "completed" | "failed";
  input_fingerprint: string;
  basis_fingerprint?: string;
  stale?: boolean;
  stale_known?: boolean;
  result: ProjectGenerationResult | null;
  applied: {
    requirements: Record<string, string>;
    documents: Record<string, AppliedGeneratedDocument | string>;
  };
  error: string;
  engine_session_id: string | null;
  created_at: string;
  updated_at: string;
}

export const REL_KIND_ZH: Record<string, string> = {
  adjacent: "相邻",
  related: "相关",
  sibling: "同类",
  other: "其他",
  upstream: "上游",
  downstream: "下游",
  overlaps: "交叠",
  contrasts: "对照",
  variant_of: "变体",
  capability_of: "内嵌能力",
  component_of: "组件",
  parent_of: "父类",
  child_of: "子类",
  specializes: "特化",
  generalizes: "泛化",
  enabled_by: "依托",
};

export async function getMeta() {
  return fetchJson<Meta>("/data/meta.json");
}
export async function getSection(id: string) {
  return fetchJson<SectionData>(`/data/sections/${id}.json`);
}
export async function getLeaf(slug: string) {
  return fetchJson<LeafDetail>(`/data/leaves/${slug}.json`);
}
export async function getApps() {
  return fetchJson<AppEntry[]>("/data/apps.json");
}
export async function getSourceManifest(slug: string) {
  return fetchJson<SourceManifest>(`/api/sources/${encodeURIComponent(slug)}`);
}
export async function getSourcePage(
  slug: string,
  kind: AtlasSourceKind,
  section?: string,
  offset = 0,
  limit = 50_000,
) {
  const query = new URLSearchParams({ offset: String(offset), limit: String(limit) });
  if (section) query.set("section", section);
  return fetchJson<AtlasSourcePage>(
    `/api/sources/${kind}/${encodeURIComponent(slug)}?${query}`,
  );
}
export async function getCompleteSource(
  slug: string,
  kind: AtlasSourceKind,
  section?: string,
) {
  const first = await getSourcePage(slug, kind, section);
  let page = first;
  let content = first.content;
  for (let reads = 1; !page.complete && reads < 200; reads += 1) {
    if (page.next_offset === null) throw new Error("source pagination stopped unexpectedly");
    page = await getSourcePage(slug, kind, section, page.next_offset);
    if (page.fingerprint !== first.fingerprint) {
      throw new Error("source changed while reading; retry");
    }
    content += page.content;
  }
  if (!page.complete) throw new Error("source exceeds safe pagination limit");
  return {
    ...first,
    content,
    complete: true,
    returned_chars: content.length,
    next_offset: null,
  } satisfies AtlasSourcePage;
}
export async function getProjects() {
  return fetchJson<AtlasProject[]>("/api/projects");
}
export async function getProject(id: string) {
  return fetchJson<AtlasProject>(`/api/projects/${encodeURIComponent(id)}`);
}
export async function createProject(input: CreateProjectInput) {
  const project = await requestJson<AtlasProject>("/api/projects", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(input),
  });
  invalidateAtlasCache();
  return project;
}
export async function deleteProject(projectId: string) {
  const result = await requestJson<DeleteProjectResult>(
    `/api/projects/${encodeURIComponent(projectId)}`,
    {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ confirm: projectId }),
    },
  );
  invalidateAtlasCache();
  return result;
}
export async function getProjectReferences(projectId: string) {
  return fetchJson<ProjectReference[]>(
    `/api/projects/${encodeURIComponent(projectId)}/references`,
  );
}
export async function saveProjectReference(projectId: string, input: {
  kind: AtlasReferenceKind;
  slug: string;
  section?: string;
  note?: string;
  read_status?: ProjectReference["read_status"];
}) {
  const reference = await requestJson<ProjectReference>(
    `/api/projects/${encodeURIComponent(projectId)}/references`,
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    },
  );
  invalidateAtlasCache();
  return reference;
}
export async function updateProjectReference(
  projectId: string,
  referenceId: string,
  input: { note?: string; read_status?: ProjectReference["read_status"] },
) {
  const reference = await requestJson<ProjectReference>(
    `/api/projects/${encodeURIComponent(projectId)}/references/${encodeURIComponent(referenceId)}`,
    {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    },
  );
  invalidateAtlasCache();
  return reference;
}
export async function getProjectWorkspace(projectId: string) {
  return fetchJson<ProjectWorkspace>(`/api/projects/${encodeURIComponent(projectId)}/workspace`);
}
export async function getProjectHarnessPreflight(projectId: string) {
  return fetchJson<HarnessPreflight>(
    `/api/projects/${encodeURIComponent(projectId)}/harness/preflight`);
}
export async function listWorkspaceBaselines(projectId: string) {
  return fetchJson<WorkspaceBaselineSummary[]>(
    `/api/projects/${encodeURIComponent(projectId)}/workspace-baselines`);
}
export async function captureWorkspaceBaseline(projectId: string, input: {
  focus_paths: string[];
  expected_baseline_id?: string;
  expected_content_fingerprint?: string;
}) {
  const result = await requestJson<WorkspaceBaselineSummary>(
    `/api/projects/${encodeURIComponent(projectId)}/workspace-baselines`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "capture", ...input }),
    });
  invalidateAtlasCache();
  return result;
}
export async function checkWorkspaceChanges(projectId: string) {
  return requestJson<WorkspaceBaselineCheck>(
    `/api/projects/${encodeURIComponent(projectId)}/workspace-baselines`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "check" }),
    });
}
export async function createProjectRequirement(projectId: string, input: {
  content: string;
  recommended_scope?: ProjectScope;
  recommendation_reason?: string;
  acceptance_conditions?: string[];
  reference_ids?: string[];
}) {
  const result = await requestJson<ProjectRequirement>(
    `/api/projects/${encodeURIComponent(projectId)}/requirements`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    });
  invalidateAtlasCache();
  return result;
}
export async function updateProjectRequirement(
  projectId: string,
  requirementId: string,
  input: Partial<Pick<ProjectRequirement, "content" | "recommended_scope" | "recommendation_reason" | "acceptance_conditions" | "reference_ids">>,
) {
  const result = await requestJson<ProjectRequirement>(
    `/api/projects/${encodeURIComponent(projectId)}/requirements/${encodeURIComponent(requirementId)}`, {
      method: "PATCH", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    });
  invalidateAtlasCache();
  return result;
}
export async function confirmProjectRequirement(
  projectId: string,
  requirementId: string,
  input: { scope: ProjectScope; reason: string },
) {
  const result = await requestJson<ProjectRequirement>(
    `/api/projects/${encodeURIComponent(projectId)}/requirements/${encodeURIComponent(requirementId)}/confirm`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    });
  invalidateAtlasCache();
  return result;
}
export async function createProjectDecision(projectId: string, input: {
  statement: string;
  rationale: string;
  reference_ids?: string[];
}) {
  const result = await requestJson<ProjectDecision>(
    `/api/projects/${encodeURIComponent(projectId)}/decisions`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    });
  invalidateAtlasCache();
  return result;
}
export async function createProjectDocument(projectId: string, input: {
  kind: ProjectDocumentKind;
  title: string;
  content: string;
  basis?: DocumentBasis[];
  author?: ProjectDocument["author"];
  change_summary?: string;
}) {
  const result = await requestJson<ProjectDocument>(
    `/api/projects/${encodeURIComponent(projectId)}/documents`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    });
  invalidateAtlasCache();
  return result;
}
export async function addProjectDocumentVersion(
  projectId: string,
  documentId: string,
  input: { content: string; basis?: DocumentBasis[]; expected_current_version: number; author?: ProjectDocument["author"]; change_summary: string },
) {
  const result = await requestJson<ProjectDocument>(
    `/api/projects/${encodeURIComponent(projectId)}/documents/${encodeURIComponent(documentId)}/versions`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    });
  invalidateAtlasCache();
  return result;
}
export async function getProjectDocumentVersions(projectId: string, documentId: string) {
  return fetchJson<ProjectDocumentVersion[]>(
    `/api/projects/${encodeURIComponent(projectId)}/documents/${encodeURIComponent(documentId)}/versions`);
}
export async function getProjectDocumentDiff(projectId: string, documentId: string) {
  return fetchJson<{ document_id: string; from_version: number; to_version: number; diff: string }>(
    `/api/projects/${encodeURIComponent(projectId)}/documents/${encodeURIComponent(documentId)}/diff`);
}
export async function reviewProjectDocument(
  projectId: string,
  documentId: string,
  input: { status: "approved" | "rejected"; note?: string },
) {
  const result = await requestJson<ProjectDocument>(
    `/api/projects/${encodeURIComponent(projectId)}/documents/${encodeURIComponent(documentId)}/review`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    });
  invalidateAtlasCache();
  return result;
}
export async function resolveProjectOpenItem(
  projectId: string,
  input: {
    run_id: string;
    item_kind: ProjectOpenItemKind;
    item_index: number;
    item_key: string;
    status: Exclude<ProjectOpenItemStatus, "open">;
    note?: string;
    convert?: "decision" | "requirement";
  },
) {
  const result = await requestJson<{ item: ProjectOpenItem; decision_id: string | null; requirement_id: string | null }>(
    `/api/projects/${encodeURIComponent(projectId)}/open-items/resolve`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    });
  invalidateAtlasCache();
  return result;
}
export async function exportProject(projectId: string) {
  return requestJson<ProjectExport>(`/api/projects/${encodeURIComponent(projectId)}/export`, {
    method: "POST", headers: { "Content-Type": "application/json" }, body: "{}",
  });
}

export async function listProjectGenerations(projectId: string) {
  return fetchJson<ProjectGenerationRun[]>(
    `/api/projects/${encodeURIComponent(projectId)}/generation-runs`);
}

export async function getProjectGeneration(projectId: string, runId: string) {
  return requestJson<ProjectGenerationRun>(
    `/api/projects/${encodeURIComponent(projectId)}/generation-runs/${encodeURIComponent(runId)}`,
    { method: "GET" });
}

export async function startProjectGeneration(
  projectId: string,
  input: {
    mode: "analysis" | "value" | "documents" | "improvement" | "revision";
    document_kinds?: ProjectDocumentKind[];
    improvement_goal?: string;
    document_id?: string;
    section_heading?: string;
    revision_instruction?: string;
    model?: string;
  },
) {
  return requestJson<ProjectGenerationRun>(
    `/api/projects/${encodeURIComponent(projectId)}/generation-runs`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    });
}

export async function applyProjectGenerationItem(
  projectId: string,
  runId: string,
  input: { item_kind: "requirement" | "document"; index: number; confirm_stale?: boolean },
) {
  const result = await requestJson<{ run: ProjectGenerationRun; created: ProjectRequirement | ProjectDocument }>(
    `/api/projects/${encodeURIComponent(projectId)}/generation-runs/${encodeURIComponent(runId)}/apply`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    });
  invalidateAtlasCache();
  return result;
}

export async function createProjectIteration(projectId: string, input: {
  title: string;
  objective: string;
  input_document_versions: string[];
  requirement_ids: string[];
  activate?: boolean;
}) {
  const result = await requestJson<ProjectIteration>(
    `/api/projects/${encodeURIComponent(projectId)}/iterations`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    });
  invalidateAtlasCache();
  return result;
}

export async function updateProjectIterationStatus(
  projectId: string,
  iterationId: string,
  status: "active" | "completed" | "abandoned",
) {
  const result = await requestJson<ProjectIteration>(
    `/api/projects/${encodeURIComponent(projectId)}/iterations/${encodeURIComponent(iterationId)}/status`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ status }),
    });
  invalidateAtlasCache();
  return result;
}

export async function createProjectTask(projectId: string, input: {
  iteration_id: string;
  kind: ProjectTask["kind"];
  title: string;
  objective: string;
  input_document_versions: string[];
  requirement_ids: string[];
  write_paths: string[];
  verification_commands: string[];
  timeout_seconds?: number;
}) {
  const result = await requestJson<ProjectTask>(
    `/api/projects/${encodeURIComponent(projectId)}/tasks`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    });
  invalidateAtlasCache();
  return result;
}

export async function startProjectExecution(
  projectId: string,
  taskId: string,
  input: { model?: string; transport?: "http" | "cli" } = {},
) {
  const result = await requestJson<ProjectExecution>(
    `/api/projects/${encodeURIComponent(projectId)}/tasks/${encodeURIComponent(taskId)}/executions`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    });
  invalidateAtlasCache();
  return result;
}

export async function getProjectExecution(projectId: string, executionId: string) {
  return requestJson<ProjectExecution>(
    `/api/projects/${encodeURIComponent(projectId)}/executions/${encodeURIComponent(executionId)}`,
    { method: "GET" });
}

export async function stopProjectExecution(projectId: string, executionId: string) {
  const result = await requestJson<ProjectExecution>(
    `/api/projects/${encodeURIComponent(projectId)}/executions/${encodeURIComponent(executionId)}/stop`, {
      method: "POST", headers: { "Content-Type": "application/json" }, body: "{}",
    });
  invalidateAtlasCache();
  return result;
}

export async function continueProjectExecution(
  projectId: string,
  executionId: string,
  instruction: string,
) {
  const result = await requestJson<ProjectExecution>(
    `/api/projects/${encodeURIComponent(projectId)}/executions/${encodeURIComponent(executionId)}/continue`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ instruction }),
    });
  invalidateAtlasCache();
  return result;
}

export async function applyProjectExecutionResult(
  projectId: string,
  executionId: string,
) {
  const result = await requestJson<ProjectExecution>(
    `/api/projects/${encodeURIComponent(projectId)}/executions/${encodeURIComponent(executionId)}/apply`, {
      method: "POST", headers: { "Content-Type": "application/json" }, body: "{}",
    });
  invalidateAtlasCache();
  return result;
}

export async function cleanupProjectExecution(
  projectId: string,
  executionId: string,
) {
  const result = await requestJson<ProjectExecution>(
    `/api/projects/${encodeURIComponent(projectId)}/executions/${encodeURIComponent(executionId)}/cleanup`, {
      method: "POST", headers: { "Content-Type": "application/json" }, body: "{}",
    });
  invalidateAtlasCache();
  return result;
}

export async function replyProjectExecutionPermission(
  projectId: string,
  executionId: string,
  input: { request_id: string; reply: "once" | "always" | "reject"; message?: string },
) {
  return requestJson<ProjectExecution>(
    `/api/projects/${encodeURIComponent(projectId)}/executions/${encodeURIComponent(executionId)}/permission`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    });
}

export async function replyProjectExecutionQuestion(
  projectId: string,
  executionId: string,
  input: { request_id: string; answers?: string[][]; reject?: boolean },
) {
  return requestJson<ProjectExecution>(
    `/api/projects/${encodeURIComponent(projectId)}/executions/${encodeURIComponent(executionId)}/question`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    });
}

export async function rebaseProjectIteration(
  projectId: string,
  iterationId: string,
  input: { note?: string } = {},
) {
  const result = await requestJson<ProjectIteration>(
    `/api/projects/${encodeURIComponent(projectId)}/iterations/${encodeURIComponent(iterationId)}/rebase`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    });
  invalidateAtlasCache();
  return result;
}

export async function recordProjectTaskAcceptance(
  projectId: string,
  taskId: string,
  input: { status: "passed" | "failed" | "waived"; evidence: { kind: string; summary: string }[] },
) {
  const result = await requestJson<ProjectTask>(
    `/api/projects/${encodeURIComponent(projectId)}/tasks/${encodeURIComponent(taskId)}/acceptance`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    });
  invalidateAtlasCache();
  return result;
}
