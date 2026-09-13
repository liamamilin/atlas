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
  | "product-requirements"
  | "interaction"
  | "technical-plan"
  | "development-plan"
  | "acceptance-plan"
  | "current-state";

export interface DocumentBasis {
  kind?: "reference" | "requirement" | "decision" | "document_version";
  id?: string;
  source?: string;
  version?: string | number;
  fingerprint?: string;
}

export interface DocumentReview {
  status: "current" | "needs_review";
  reasons: { kind: "requirement_changed" | "upstream_document_changed"; id: string; document_id?: string }[];
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
}

export interface ProjectExport {
  project_id: string;
  directory: string;
  archive: string;
  archive_sha256: string;
  manifest: {
    schema: number;
    counts: Record<string, number>;
    unresolved_requirement_ids: string[];
    documents_needing_review: string[];
  };
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
export async function exportProject(projectId: string) {
  return requestJson<ProjectExport>(`/api/projects/${encodeURIComponent(projectId)}/export`, {
    method: "POST", headers: { "Content-Type": "application/json" }, body: "{}",
  });
}
