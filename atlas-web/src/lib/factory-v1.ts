import { AtlasApiError } from "@/lib/atlas";

export type V1Segment = "G1" | "T08";
export type V1AdmissionPolicy = "ready-only-v1" | "reviewed-draft-v1";

export interface V1Application {
  app_id: string;
  slug?: string | null;
  name: string;
  status?: string;
  catalog_status?: string;
  source_identity?: { kind?: string; repository?: string };
  [key: string]: unknown;
}

export interface V1Case {
  case_id: string;
  revision: number;
  app_id: string;
  digest: string;
  evidence_digest?: string;
  research?: { summary?: string; unknowns?: string[] };
  observations?: V1Observation[];
  scenario_links?: { scenario_id: string; scenario_revision: number; [key: string]: unknown }[];
  source_snapshots?: { repository?: string; commit_sha?: string; digest?: string; file_manifest_digest?: string; files?: Record<string, string>; [key: string]: unknown }[];
  templates?: Record<string, unknown>[];
  created_at?: string;
}

export interface V1Observation {
  evidence_id: string;
  kind: "documentation" | "code_observation" | "inference" | "runtime_verification" | string;
  summary?: string;
  content?: string;
  statement?: string;
  observation_status?: string;
  status?: string;
  outcome?: string;
  unknowns?: string[];
  location?: { path?: string; line_start?: number; line_end?: number; depends_on?: string[] };
  digest?: string;
  reviews?: { outcome: string; reviewer?: string; reviewer_kind?: string; created_at?: string }[];
  [key: string]: unknown;
}

export interface V1Scenario {
  id: string;
  leaf: string;
  leaf_name?: string;
  name: string;
  status: "ready" | "draft" | "archived" | string;
  revision: number;
  reviews?: { current?: boolean; outcome?: string; scenario_revision?: number }[];
  [key: string]: unknown;
}

export interface V1Plan {
  id?: string;
  plan_id?: string;
  plan_digest?: string;
  digest?: string;
  state?: string;
  status?: string;
  batch?: { state?: string; [key: string]: unknown };
  seeds?: unknown[];
  items?: unknown[];
  scenarios?: unknown[];
  excluded?: unknown[];
  budget?: Record<string, unknown>;
  report?: Record<string, unknown>;
  [key: string]: unknown;
}

export async function factoryV1Request<T>(route: string, body?: unknown, signal?: AbortSignal): Promise<T> {
  const response = await fetch(`/api/factory/v1/${route}`, {
    method: body === undefined ? "GET" : "POST", cache: "no-store", signal,
    ...(body !== undefined ? { headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) } : {}),
  });
  const value = await response.json().catch(() => null) as { error?: string; code?: string } | null;
  if (!response.ok) throw new AtlasApiError(response.status, value?.error || "Factory V1 request failed", value?.code);
  return value as T;
}

export function unwrapPlan(value: unknown): V1Plan {
  if (value && typeof value === "object" && "plan" in value) return (value as { plan: V1Plan }).plan;
  return value as V1Plan;
}

export function planId(plan: V1Plan) { return plan.plan_id || plan.id || ""; }
export function planDigest(plan: V1Plan) { return plan.plan_digest || plan.digest || ""; }
export function isTerminalPlan(plan: V1Plan) {
  return ["completed", "failed", "cancelled", "blocked", "needs_attention"].includes(plan.state || plan.status || "");
}

export function displayUnknown(value: unknown, zh: boolean) {
  return value === null || value === undefined || value === "" ? (zh ? "未知" : "Unknown") : String(value);
}
