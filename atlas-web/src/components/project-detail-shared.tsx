import { AtlasApiError } from "@/lib/atlas";
import type { ProjectDocumentKind, ProjectScope } from "@/lib/atlas";

export const DOCUMENT_KINDS: { value: ProjectDocumentKind; zh: string; en: string }[] = [
  { value: "analysis", zh: "调研与分析", en: "Research & analysis" },
  { value: "value-analysis", zh: "价值分析", en: "Value analysis" },
  { value: "product-requirements", zh: "产品需求", en: "Product requirements" },
  { value: "interaction", zh: "交互与页面", en: "Interaction & screens" },
  { value: "technical-plan", zh: "技术方案", en: "Technical plan" },
  { value: "development-plan", zh: "开发规划", en: "Development plan" },
  { value: "acceptance-plan", zh: "验收方案", en: "Acceptance plan" },
  { value: "current-state", zh: "项目现状与变更", en: "Current state & changes" },
];

export const DOCUMENT_BUNDLE_KINDS = DOCUMENT_KINDS.filter(
  (item) => item.value !== "current-state" && item.value !== "value-analysis",
);
export const CORE_DOCUMENT_BUNDLE: ProjectDocumentKind[] = [
  "product-requirements", "technical-plan", "development-plan", "acceptance-plan",
];
export const FULL_DOCUMENT_BUNDLE: ProjectDocumentKind[] = [
  "analysis", "product-requirements", "interaction", "technical-plan",
  "development-plan", "acceptance-plan",
];

export const inputClass = "mt-1.5 h-11 w-full rounded-md border border-border bg-bg-elevated px-3 outline-none focus:ring-2 focus:ring-primary/35";

export function actionError(cause: unknown, lang: "zh" | "en") {
  if (cause instanceof AtlasApiError) {
    const byCode: Record<string, { zh: string; en: string }> = {
      conflict: {
        zh: "当前状态已变化，请刷新后重试。",
        en: "The current state changed. Refresh and try again.",
      },
      not_found: {
        zh: "目标记录不存在，可能已被删除或已更新。",
        en: "The target record no longer exists or was updated.",
      },
      invalid_request: {
        zh: "请求内容不完整或已过期，请检查后重试。",
        en: "The request is incomplete or stale. Check it and try again.",
      },
      provider_unavailable: {
        zh: "provider 暂时不可用，请检查环境后重试。",
        en: "The provider is unavailable. Check the environment and try again.",
      },
      provider_model_unavailable: {
        zh: "当前 provider 模型不可用，请选择已确认的模型。",
        en: "The selected provider model is unavailable. Choose a confirmed model.",
      },
    };
    const mapped = byCode[cause.code];
    if (mapped) return mapped[lang];
    if (cause.retryable || cause.status === 503) {
      return lang === "zh" ? "服务暂时不可用，请稍后重试。" : "The service is temporarily unavailable. Try again later.";
    }
  }
  const raw = cause instanceof Error ? cause.message : String(cause || "");
  const status = raw.match(/(?:^|\b)(?:HTTP|status\s*)?([45]\d{2})\b/i)?.[1];
  if (status === "409") return lang === "zh" ? "当前状态已变化，请刷新后重试。" : "The current state changed. Refresh and try again.";
  if (status === "404") return lang === "zh" ? "目标记录不存在，可能已被删除或已更新。" : "The target record no longer exists or was updated.";
  if (status === "400") return lang === "zh" ? "请求内容不完整或已过期，请检查后重试。" : "The request is incomplete or stale. Check it and try again.";
  if (status === "503") {
    const detail = raw.replace(/^\s*503\s+/i, "").trim();
    return lang === "zh"
      ? (detail ? `执行服务暂时不可用：${detail}` : "执行服务暂时不可用，请检查 OpenCode 环境后重试。")
      : (detail ? `The execution service is unavailable: ${detail}` : "The execution service is unavailable. Check the OpenCode environment and try again.");
  }
  return lang === "zh" ? "操作未完成，请稍后重试。" : "The action could not be completed. Please try again.";
}

export function scopeLabel(scope: ProjectScope | null, lang: "zh" | "en") {
  if (!scope) return lang === "zh" ? "无" : "None";
  const labels = { current: { zh: "本版", en: "Current" }, later: { zh: "以后", en: "Later" }, excluded: { zh: "不做", en: "Excluded" } };
  return labels[scope][lang];
}

export function documentKind(kind: ProjectDocumentKind, lang: "zh" | "en") {
  const item = DOCUMENT_KINDS.find((candidate) => candidate.value === kind);
  return item ? (lang === "zh" ? item.zh : item.en) : kind;
}

export function generationMode(mode: string, lang: "zh" | "en") {
  const labels: Record<string, { zh: string; en: string }> = {
    analysis: { zh: "资料分析", en: "Source analysis" },
    value: { zh: "价值分析", en: "Value analysis" },
    documents: { zh: "文档生成", en: "Document generation" },
    improvement: { zh: "改进方案", en: "Improvement plan" },
  };
  return labels[mode]?.[lang] || mode.replaceAll("_", " ");
}

export function runStatus(status: string, lang: "zh" | "en") {
  const labels: Record<string, { zh: string; en: string }> = {
    queued: { zh: "排队中", en: "Queued" },
    running: { zh: "运行中", en: "Running" },
    completed: { zh: "已完成", en: "Completed" },
    failed: { zh: "失败", en: "Failed" },
    canceled: { zh: "已取消", en: "Canceled" },
    stopped: { zh: "已停止", en: "Stopped" },
  };
  return labels[status]?.[lang] || status;
}

export function sameKinds(left: ProjectDocumentKind[], right: ProjectDocumentKind[]) {
  return left.length === right.length && left.every((item) => right.includes(item));
}

export function lines(value: string) {
  return value.split("\n").map((item) => item.trim()).filter(Boolean);
}

export function ChangePaths({ title, paths }: { title: string; paths: string[] }) {
  return <div className="mt-3"><p className="text-xs font-medium">{title} · {paths.length}</p>{paths.length ? <div className="mt-1 max-h-28 overflow-auto rounded bg-bg-elevated px-3 py-2 font-mono text-[11px] leading-5 text-muted">{paths.map((path) => <div key={path}>{path}</div>)}</div> : <p className="mt-1 text-xs text-subtle">—</p>}</div>;
}

export function TechnicalMeta({ label, value, inline = false }: { label: string; value?: string | null; inline?: boolean }) {
  if (!value) return null;
  return <details className={`${inline ? "inline-block ml-2 align-middle" : "inline-block"} text-[10px] text-subtle`}><summary className="cursor-pointer">{label}</summary><code className="mt-1 block max-w-full break-all rounded bg-chip px-1.5 py-0.5 font-mono">{value}</code></details>;
}

export function TechnicalError({ message, lang }: { message?: string | null; lang: "zh" | "en" }) {
  if (!message) return null;
  return <details className="mt-2 text-[11px] text-danger"><summary className="cursor-pointer">{lang === "zh" ? "查看技术详情" : "View technical details"}</summary><pre className="mt-2 max-h-40 overflow-auto whitespace-pre-wrap rounded bg-bg-elevated p-2 font-mono">{message}</pre></details>;
}

export function TextArea({ label, value, onChange, required, rows = 3 }: { label: string; value: string; onChange: (value: string) => void; required?: boolean; rows?: number }) {
  return <label className="block text-sm"><span className="text-muted">{label}</span><textarea required={required} rows={rows} value={value} onChange={(event) => onChange(event.target.value)} className={`${inputClass} h-auto py-2.5`} /></label>;
}
