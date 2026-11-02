import { useCallback, useEffect, useRef, useState, type FormEvent } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { ArrowUp, Check, Loader2, Plus, Sparkles, X } from "lucide-react";
import { Prose } from "@/components/prose";
import { Button } from "@/components/ui/button";
import {
  createAssistantThread, decideAssistantAction, getAssistantThread, sendAssistantMessage,
  type AssistantAction, type AssistantMessage, type AssistantThread,
} from "@/lib/assistant";
import { invalidateAtlasCache } from "@/lib/atlas";
import { useLang } from "@/lib/lang";

const STORAGE_KEY = "atlas.assistant.thread";
const POLL_MS = 1200;

function stored(): string {
  try { return localStorage.getItem(STORAGE_KEY) || ""; } catch { return ""; }
}
function store(id: string) {
  try { if (id) localStorage.setItem(STORAGE_KEY, id); else localStorage.removeItem(STORAGE_KEY); } catch { /* optional */ }
}

const SUGGESTIONS: [string, string][] = [
  ["找一个星标最多的开源笔记应用", "Find the most-starred open-source notes app"],
  ["列出我的项目和它们的进度", "List my projects and their progress"],
  ["密码管理器有哪些开源项目？", "Which open-source password managers exist?"],
  ["打开模型设置", "Open the model settings"],
];

const STATUS_TEXT: Record<string, [string, string]> = {
  timeout: ["超过时间上限，已停止", "Stopped at the time limit"],
  token_limit: ["超过用量上限，已停止", "Stopped at the usage limit"],
  turn_limit: ["步骤太多，已停止", "Stopped at the step limit"],
  provider_error: ["模型调用失败", "The model call failed"],
  no_answer: ["没有得到回答", "No answer was produced"],
  failed: ["这次处理失败", "This request failed"],
};

/** A global assistant drawer: ask in words, approve each change it proposes. */
export function AssistantPanel({ onDataChanged }: { onDataChanged: () => void }) {
  const { lang } = useLang(); const zh = lang === "zh";
  const location = useLocation();
  const navigate = useNavigate();
  const [open, setOpen] = useState(false);
  const [thread, setThread] = useState<AssistantThread | null>(null);
  const [text, setText] = useState("");
  const [error, setError] = useState("");
  const [sending, setSending] = useState(false);
  const handled = useRef(new Set<string>());
  const bottom = useRef<HTMLDivElement>(null);
  const input = useRef<HTMLTextAreaElement>(null);

  const remember = useCallback((next: AssistantThread, initial = false) => {
    for (const message of next.messages) {
      if (handled.current.has(message.id)) continue;
      handled.current.add(message.id);
      if (initial) continue;
      if (message.role === "assistant" && message.navigate) navigate(message.navigate);
    }
    setThread(next);
  }, [navigate]);

  // Restore the last conversation the first time the drawer opens.
  useEffect(() => {
    if (!open || thread) return;
    const id = stored();
    if (!id) return;
    getAssistantThread(id).then(next => remember(next, true)).catch(() => store(""));
  }, [open, thread, remember]);

  useEffect(() => {
    if (!thread?.running) return;
    const timer = setInterval(() => {
      getAssistantThread(thread.id).then(next => remember(next)).catch(() => undefined);
    }, POLL_MS);
    return () => clearInterval(timer);
  }, [thread?.id, thread?.running, remember]);

  useEffect(() => { bottom.current?.scrollIntoView({ block: "end" }); }, [thread?.messages.length, thread?.pending?.id, thread?.running]);
  useEffect(() => { if (open) input.current?.focus(); }, [open]);

  useEffect(() => {
    const onKey = (event: KeyboardEvent) => {
      if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") { event.preventDefault(); setOpen(value => !value); }
      else if (event.key === "Escape" && open) setOpen(false);
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [open]);

  async function send(content: string) {
    const value = content.trim();
    if (!value || sending || thread?.running) return;
    setSending(true); setError("");
    try {
      let current = thread;
      if (!current) { current = await createAssistantThread(); store(current.id); }
      await sendAssistantMessage(current.id, value, { path: location.pathname + location.search, title: document.title });
      setText("");
      remember(await getAssistantThread(current.id));
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : String(cause));
    } finally { setSending(false); }
  }

  async function decide(action: AssistantAction, decision: "approve" | "reject", typed?: string) {
    if (!thread) return;
    setError("");
    try {
      const result = await decideAssistantAction(thread.id, action.id, decision, typed);
      if (result.outcome?.ok) { invalidateAtlasCache(); onDataChanged(); }
      remember(await getAssistantThread(thread.id));
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : String(cause));
    }
  }

  function reset() { setThread(null); store(""); setError(""); setText(""); input.current?.focus(); }

  function submit(event: FormEvent) { event.preventDefault(); void send(text); }

  const busy = sending || Boolean(thread?.running);
  return <>
    {!open && <button type="button" onClick={() => setOpen(true)} aria-label={zh ? "打开应用助手" : "Open the assistant"} title={zh ? "应用助手（⌘K）" : "Assistant (⌘K)"}
      className="fixed bottom-5 right-5 z-30 inline-flex h-12 items-center gap-2 rounded-full bg-primary px-4 text-sm font-medium text-primary-fg shadow-lg hover:opacity-90">
      <Sparkles className="size-4" aria-hidden="true" />{zh ? "助手" : "Assistant"}
    </button>}
    {open && <aside role="dialog" aria-label={zh ? "应用助手" : "Assistant"}
      className="fixed inset-0 z-40 flex flex-col border-border bg-bg-elevated shadow-2xl sm:inset-y-0 sm:left-auto sm:right-0 sm:w-[420px] sm:border-l">
      <header className="flex items-center justify-between gap-2 border-b border-border px-4 py-3">
        <div className="min-w-0">
          <h2 className="font-serif text-lg font-medium">{zh ? "应用助手" : "Assistant"}</h2>
          <p className="truncate text-xs text-muted">{zh ? "用一句话操作应用；每次修改都会先请你确认" : "Operate the app in words; every change asks you first"}</p>
        </div>
        <div className="flex shrink-0 items-center gap-1">
          <button type="button" onClick={reset} disabled={busy} aria-label={zh ? "新对话" : "New conversation"} title={zh ? "新对话" : "New conversation"} className="flex size-9 items-center justify-center rounded-lg text-muted hover:bg-chip disabled:opacity-40"><Plus className="size-4" /></button>
          <button type="button" onClick={() => setOpen(false)} aria-label={zh ? "关闭助手" : "Close the assistant"} className="flex size-9 items-center justify-center rounded-lg text-muted hover:bg-chip"><X className="size-4" /></button>
        </div>
      </header>
      <div className="min-h-0 flex-1 overflow-y-auto px-4 py-4" aria-live="polite">
        {!thread?.messages.length && <div className="text-sm text-muted">
          <p>{zh ? "可以让我查找类型和开源项目、管理项目的需求与文档、启动生成或执行，或者打开任意页面。" : "Ask me to find types and projects, manage project requirements and documents, start generation or execution, or open any page."}</p>
          <div className="mt-4 flex flex-wrap gap-2">{SUGGESTIONS.map(([zhText, enText]) => <button key={zhText} type="button" onClick={() => void send(zh ? zhText : enText)} className="rounded-full border border-border bg-surface px-3 py-1.5 text-xs text-fg hover:border-primary hover:text-primary">{zh ? zhText : enText}</button>)}</div>
        </div>}
        <ol className="space-y-4">{thread?.messages.map(message => <li key={message.id}><MessageView message={message} zh={zh} /></li>)}</ol>
        {thread?.running && <p role="status" className="mt-4 inline-flex items-center gap-2 text-sm text-muted"><Loader2 className="size-4 animate-spin" />{zh ? "正在处理…" : "Working…"}</p>}
        {thread?.pending && !thread.running && <PendingCard key={thread.pending.id} action={thread.pending} zh={zh} onDecide={decide} />}
        <div ref={bottom} />
      </div>
      {error && <p role="alert" className="border-t border-border px-4 py-2 text-xs text-danger">{error}</p>}
      <form onSubmit={submit} className="flex items-end gap-2 border-t border-border p-3">
        <textarea ref={input} rows={2} value={text} onChange={e => setText(e.target.value)} aria-label={zh ? "给助手的消息" : "Message to the assistant"}
          placeholder={zh ? "例如：给「个人知识管理」项目新增一条需求" : "e.g. Add a requirement to my notes project"}
          onKeyDown={e => { if (e.key === "Enter" && !e.shiftKey && !e.nativeEvent.isComposing) { e.preventDefault(); void send(text); } }}
          className="min-h-11 flex-1 resize-none rounded-xl border border-border bg-surface px-3 py-2.5 text-sm outline-none focus:ring-2 focus:ring-primary/35" />
        <Button type="submit" disabled={busy || !text.trim()} aria-label={zh ? "发送" : "Send"} className="size-11 shrink-0 p-0">{busy ? <Loader2 className="size-4 animate-spin" /> : <ArrowUp className="size-4" />}</Button>
      </form>
    </aside>}
  </>;
}

function MessageView({ message, zh }: { message: AssistantMessage; zh: boolean }) {
  if (message.role === "user") return <div className="ml-8 rounded-xl bg-primary/[0.08] px-3.5 py-2.5 text-sm whitespace-pre-wrap">{message.content}</div>;
  if (message.role === "action") {
    const action = message.action!;
    const done = message.decision === "approve";
    return <p className={`flex items-start gap-2 text-xs ${done && message.outcome?.ok ? "text-ok" : "text-muted"}`}>
      {done ? <Check className="mt-0.5 size-3.5 shrink-0" /> : <X className="mt-0.5 size-3.5 shrink-0" />}
      <span>{done ? (message.outcome?.ok ? (zh ? "已执行：" : "Done: ") : (zh ? `执行失败（${message.outcome?.status}）：` : `Failed (${message.outcome?.status}): `)) : (zh ? "已取消：" : "Cancelled: ")}{action.summary}</span>
    </p>;
  }
  const failure = message.status && message.status !== "completed" && message.status !== "awaiting_confirmation" ? STATUS_TEXT[message.status] : undefined;
  return <div className="text-sm">
    {message.content && <Prose md={message.content} />}
    {failure && <p className="mt-1 text-xs text-danger">{zh ? failure[0] : failure[1]}{message.error ? `：${message.error}` : ""}</p>}
    {!!message.steps?.length && <details className="mt-2 text-xs text-muted">
      <summary className="cursor-pointer select-none">{zh ? `${message.steps.length} 个步骤` : `${message.steps.length} steps`}</summary>
      <ol className="mt-1 space-y-0.5 border-l border-border pl-3 font-mono">{message.steps.map(step => <li key={step.index} className={step.error ? "text-danger" : ""}>{step.summary}</li>)}</ol>
    </details>}
  </div>;
}

function PendingCard({ action, zh, onDecide }: { action: AssistantAction; zh: boolean; onDecide: (action: AssistantAction, decision: "approve" | "reject", typed?: string) => Promise<void> }) {
  const [typed, setTyped] = useState("");
  const [busy, setBusy] = useState(false);
  const destructive = action.risk === "destructive";
  const ready = !destructive || typed.trim() === action.confirm_text;
  const body = Object.keys(action.body || {}).length ? JSON.stringify(action.body, null, 1) : "";
  async function run(decision: "approve" | "reject") {
    setBusy(true);
    try { await onDecide(action, decision, destructive ? typed : undefined); } finally { setBusy(false); }
  }
  return <section aria-label={zh ? "待确认的操作" : "Action to confirm"} className={`mt-4 rounded-xl border p-3.5 ${destructive ? "border-danger/50 bg-danger/[0.04]" : "border-primary/40 bg-surface"}`}>
    <p className="text-xs font-medium text-muted">{destructive ? (zh ? "危险操作，需要确认" : "Destructive action") : (zh ? "需要你确认" : "Needs your approval")}</p>
    <p className="mt-1 text-sm font-medium">{action.summary}</p>
    <p className="mt-1 break-all font-mono text-xs text-subtle">{action.method} {action.path}{action.query ? `?${action.query}` : ""}</p>
    {body && <pre className="mt-2 max-h-40 overflow-auto rounded-lg bg-chip/60 p-2 text-xs">{body}</pre>}
    {destructive && <label className="mt-3 block text-xs text-muted">{zh ? "输入 " : "Type "}<code className="font-mono text-fg">{action.confirm_text}</code>{zh ? " 以确认" : " to confirm"}
      <input value={typed} onChange={e => setTyped(e.target.value)} className="mt-1 block h-10 w-full rounded-lg border border-border bg-surface px-3 font-mono text-sm" /></label>}
    <div className="mt-3 flex gap-2">
      <Button type="button" size="sm" disabled={busy || !ready} onClick={() => void run("approve")} className={destructive ? "bg-danger" : undefined}>{zh ? "执行" : "Run"}</Button>
      <Button type="button" size="sm" variant="outline" disabled={busy} onClick={() => void run("reject")}>{zh ? "取消" : "Cancel"}</Button>
    </div>
  </section>;
}
