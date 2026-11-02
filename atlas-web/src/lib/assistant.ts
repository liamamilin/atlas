/** Client for the app assistant: one conversation entry that can operate the app. */

export type AssistantStatus =
  | "completed" | "awaiting_confirmation" | "timeout" | "token_limit" | "turn_limit"
  | "provider_error" | "no_answer" | "failed";

export interface AssistantAction {
  id: string;
  method: string;
  path: string;
  query: string;
  body: Record<string, unknown>;
  summary: string;
  risk: "write" | "destructive";
  confirm_text?: string;
}

export interface AssistantMessage {
  id: string;
  role: "user" | "assistant" | "action";
  content?: string;
  created_at: string;
  status?: AssistantStatus;
  error?: string;
  steps?: { index: number; tool: string; summary: string; error: boolean }[];
  navigate?: string | null;
  action?: AssistantAction;
  decision?: "approve" | "reject";
  outcome?: { status: number; ok: boolean; result: unknown } | null;
}

export interface AssistantThread {
  id: string;
  title: string;
  updated_at: string;
  running: boolean;
  pending: AssistantAction | null;
  messages: AssistantMessage[];
}

const BASE = "/api/assistant/threads";

async function request<T>(url: string, init?: RequestInit): Promise<T> {
  const response = await fetch(url, {
    cache: "no-cache", ...init,
    headers: init?.body ? { "Content-Type": "application/json" } : undefined,
  });
  const value = await response.json().catch(() => null) as { error?: string } | null;
  if (!response.ok) throw new Error(value?.error || `请求失败 (${response.status})`);
  return value as T;
}

export const createAssistantThread = () =>
  request<AssistantThread>(BASE, { method: "POST", body: "{}" });

export const getAssistantThread = (id: string) =>
  request<AssistantThread>(`${BASE}/${encodeURIComponent(id)}`);

export const sendAssistantMessage = (id: string, content: string, page: { path: string; title: string }) =>
  request<{ status: string }>(`${BASE}/${encodeURIComponent(id)}/messages`, {
    method: "POST", body: JSON.stringify({ content, page }),
  });

export const decideAssistantAction = (id: string, actionId: string, decision: "approve" | "reject", typed?: string) =>
  request<{ status: string; outcome: AssistantMessage["outcome"] }>(
    `${BASE}/${encodeURIComponent(id)}/actions/${encodeURIComponent(actionId)}`, {
      method: "POST", body: JSON.stringify({ decision, typed }),
    });
