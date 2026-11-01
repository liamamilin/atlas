import { fetchWithTimeout } from "./http";

export const PKM_LEAF = "personal-knowledge-management-application";

export type Evidence = { source_url: string; immutable_url: string; source_sha256: string; excerpt: string; source_kind?: string; verification?: "quote_matched" | "source_based" | "inferred" };
export type RepositorySource = { kind: string; url: string; immutable_url?: string; path?: string; blob_sha?: string; sha256?: string; retrieved_at: string };
export type LicenseStatus = "open_source" | "source_available" | "pending";
export type RepositoryProject = {
  repository_id: number; name: string; full_name: string; github_url: string;
  leaves?: string[];
  positioning: string; summary: string; summary_evidence: Evidence; scope: string; scope_evidence: Evidence;
  positioning_evidence?: Evidence; generation_method?: string;
  features: { text: string; evidence: Evidence }[]; languages: string[]; archived: boolean;
  license: { spdx: string | null; detected_spdx: string | null; status: LicenseStatus; note: string; source: RepositorySource | null; reviewed_at?: string; restriction_evidence?: Evidence };
  matches: { scenario_id: string; reason: string; evidence: Evidence; applicability?: "direct" | "conditional" | "unverified"; conditions?: string[] }[];
  sources: RepositorySource[]; checked_at: string; favorite: boolean; editorial_method: string;
  quality_review?: { reason: string; reviewed_at: string };
  completeness?: "complete" | "partial"; missing_fields?: string[]; collection_notes?: string[]; project_type?: string;
};
export type CatalogRun = {
  id: string; status: "running" | "completed" | "partial" | "failed" | "interrupted" | "paused_model";
  leaf?: string;
  created: number; updated: number; unchanged: number; failed: number; processed: number; total?: number;
  started_at: string; finished_at?: string; errors: { repo?: string; error: string }[];
  mode?: string; phase?: string; model_calls?: number; discovered?: number; rejected?: number;
  gaps?: { scenario: string; projects: number; target: number }[];
  candidate_counts?: Record<string, number>;
  document_fetches?: number; document_cache_hits?: number;
};
export type RepositoryCatalogData = {
  leaf: string; pilot_leaf: string;
  scenarios: { id: string; name: string; description: string; project_count: number; leaf?: string; leaf_name?: string }[];
  supported_leaves: { slug: string; name: string; mode: "curated" | "automatic"; project_count?: number }[];
  stats?: { projects: number; scenarios: number; leaves: number; favorites: number };
  pagination?: { total: number; offset: number; limit: number | null; has_more: boolean };
  projects: RepositoryProject[]; latest_run: CatalogRun | null;
  discovery?: { total: number; counts: Record<string, number>; items: { repository_id: number; leaf: string; full_name: string; github_url: string; status: string; reason: string }[] };
};

async function request<T>(path: string, body?: unknown): Promise<T> {
  return await fetchWithTimeout(`/api/oss/${path}`, body === undefined ? undefined : {
    method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body),
  }) as T;
}

export function getRepositoryCatalog(filters: Record<string, string> = {}) {
  return request<RepositoryCatalogData>(`catalog?${new URLSearchParams(filters)}`);
}
export const refreshRepositoryCatalog = (leaf = PKM_LEAF) => request<CatalogRun>("refresh", { leaf });
export const getCatalogRun = (id: string) => request<CatalogRun>(`runs/${encodeURIComponent(id)}`);
export const favoriteRepository = (id: number, favorite: boolean) => request(`projects/${id}/favorite`, { favorite });

export type BatchJob = {
  id: string; status: "running" | "retry_wait" | "interrupted" | "completed" | "partial" | "paused_model" | "awaiting_acceptance";
  leaves: string[]; processed: number; total: number; current_leaf?: string; prepared: string[];
  targets: Record<string, { repository_id: number; full_name: string; status: string; reason?: string }[]>;
  errors: { leaf?: string; error: string }[]; existing_only: boolean;
  pause_reason?: string;
  auto_recovery?: boolean;
  scope?: "first_round";
  first_round_limit?: number;
  completed_leaves?: string[];
  deferred_total?: number;
  candidate_totals?: Record<string, number>;
  pilot?: { size: number; status: "pending" | "awaiting_acceptance" | "passed" | "not_required" };
  recovery?: { next_retry_at?: string; cycles?: number; consecutive_failures?: number; last_error?: string };
};
export const listBatchJobs = () => request<{ jobs: BatchJob[] }>("batches");
export const startBatchJob = (leaves: string[], existing_only: boolean, first_round_limit?: number) =>
  request<BatchJob>("batches", { leaves, existing_only, ...(first_round_limit === undefined ? {} : { first_round_limit }) });
export const resumeBatchJob = (id: string) => request<BatchJob>(`batches/${encodeURIComponent(id)}/resume`, {});
