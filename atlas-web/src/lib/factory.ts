import { AtlasApiError } from "@/lib/atlas";

export interface Scenario {
  id: string; leaf: string; leaf_name: string; name: string; audience: string;
  objective: string; workflow: string[]; acceptance: string[];
  status: "draft" | "ready" | "archived"; revision: number; updated_at: string;
  reviews?: ScenarioReview[];
  review_jobs?: {id: string; state: string; error: string | null; scenario_revision: number; current: boolean}[];
}
export interface ScenarioReview {
  id: string; scenario_id: string; scenario_revision: number; job_id: string;
  outcome: "passed" | "needs_changes" | "rejected"; summary: string; current: boolean;
  checks: {dimension: string; outcome: string; reason: string}[];
  leaf_quotes: string[]; related_scenario_ids: string[]; suggestions: string[];
  leaf_evidence?: {start_line: number; end_line: number}[];
  peer_scenarios: {id: string; name: string; revision: number}[];
  model: string; created_at: string; scope: string;
}
export function scenarioReviewState(scenario: Scenario) {
  const reviews = scenario.reviews || [];
  const current = reviews.find(review => review.current);
  const latestJob = scenario.review_jobs?.find(job => job.current);
  const pending = latestJob && ["queued", "running"].includes(latestJob.state);
  const failed = latestJob && ["failed", "interrupted", "cancelled"].includes(latestJob.state);
  const status = pending ? latestJob.state : failed ? "failed" : current?.outcome || (reviews.length ? "outdated" : "unreviewed");
  return {current, latestJob, pending: !!pending, failed: !!failed, status,
    action: pending ? latestJob.state : failed ? "retry" : reviews.length || scenario.review_jobs?.length ? "again" : "first"};
}

export interface FactoryConfig {
  name: string; model: string; concurrency: number; timeout: number; repair_attempts: number;
  language?: "zh" | "en";
  cognition_guidance?: string;
  acceptance_protocol?: "atlas.acceptance-runner.v1";
  kind: "blueprint-production" | "cognitive-review" | "blueprint-import" | "blueprint-runtime" | "production" | "scenarios" | "scenario-review" | "harness-review" | "runtime-verification";
}
export interface FactoryJob {
  id: string; batch_id: string; kind: string; state: string; stage: string; attempt: number;
  error: string | null; updated_at: string;
  generation_result?: { count: number; reason: string; scenario_ids: string[] };
  snapshot: { leaf: {slug: string; name: string; name_zh: string}; scenario: Scenario | null; config: FactoryConfig };
  events?: {seq: number; at: string; attempt: number; stage: string; message: string}[];
  design_reviews?: {stage:string;outcome:string;summary:string;scope:string;checks:{dimension:string;outcome:string;files:string[];reason:string}[];suggestions:string[]}[];
}
export interface FactoryBatch { id: string; state: string; config: FactoryConfig; created_at: string; jobs: FactoryJob[] }
export interface FactoryStatus {
  cli: { available: boolean; version: string | null; models: string[]; models_error?: string };
  runtime: { available: boolean; message?: string; version?: string };
}
export interface FactoryArtifact {
  artifact_type?: "product-blueprint" | "runnable-starter";
  id: string; job_id: string; leaf: string; scenario_name: string; scenario_revision: number;
  scenario_id?:string;
  digest: string; level: string; state: string; created_at: string;
  manifest: { name: string; description: string; render_files?: string[]; version?: string; feature_count?: number; decision_count?: number; phase_count?: number; acceptance_count?: number; phases?: {id:string;title:string}[] };
  provenance: { repository?: string; commit?: string; license?: string; model?: string; change_summary?: string; origin?: string; package_digest?: string; note?: string; shared_case_refs?: {case_id:string;revision:number;digest:string;app_id:string}[]; imported_snapshot?: {digest:string;archive_sha256:string;provenance:Record<string,unknown>} };
  formal_checks: {project_name?: string; passed: boolean; scope: string}[];
  acceptance_jobs?: {id: string; kind: string; state: string; stage: string; updated_at: string}[];
  runtime_acceptance?: {supported:boolean;reason:string|null;protocol:"atlas.acceptance-runner.v1";result_schema:"atlas.acceptance-result.v1";network:"none"};
  acceptances: {id: string; job_id: string; digest: string; method: string; outcome: string; scope: string; summary?: string; error?: string; failure?:string; protocol_note?: string; startup?: {status:string;reason?:string;error?:string;output?:string;captured_output?:{stdout?:string;stderr?:string};readiness?:{status?:string;passed?:boolean;output?:string;error?:string;exit_code?:number}}; case_results?: {id?:string;case_id?:string;status:string;reason?:string;error?:string;output?:string;assertions?:{id:string;passed:boolean;detail:string}[]|null}[]; cleanup?: {status:string;reason?:string;error?:string;errors?:string[]}; checks?: {dimension:string;outcome:string;files:string[];reason:string}[]; suggestions?: string[]; reports?: unknown[]; created_at: string}[];
  reports: {project_name: string; passed: boolean; environment: {platform: string; image: string}}[];
  review?: {note: string; at: string}; preview_path?: string;
}

export async function factoryRequest<T>(route: string, body?: unknown, signal?: AbortSignal): Promise<T> {
  const response = await fetch(`/api/factory/${route}`, {
    method: body === undefined ? "GET" : "POST", cache: "no-store", signal,
    ...(body !== undefined ? {headers: {"Content-Type": "application/json"}, body: JSON.stringify(body)} : {}),
  });
  const value = await response.json().catch(() => null);
  if (!response.ok) throw new AtlasApiError(response.status, value?.error || "Factory request failed", value?.code);
  return value as T;
}
