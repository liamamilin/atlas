import { useCallback, useEffect, useRef, useState, type FormEvent } from "react";
import {
  AlertTriangle, ArrowUp, Check, ChevronDown, Loader2, Plus, Search,
  Trash2, Wrench,
} from "lucide-react";
import { Link } from "react-router-dom";
import {
  askQuestion,
  createAskThread,
  deleteAskThread,
  getAskThread,
  listAskThreads,
  type AskMessage,
  type AskStatus,
  type AskThread,
  type AskThreadSummary,
} from "@/lib/atlas";
import { Prose } from "@/components/prose";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { useLang, type Lang } from "@/lib/lang";

const POLL_MS = 1500;
const inputClass =
  "w-full resize-none rounded-xl border border-border bg-surface px-3.5 py-3 text-sm outline-none focus:ring-2 focus:ring-primary/35";

function errorText(cause: unknown, lang: Lang) {
  if (cause instanceof Error && cause.message) return cause.message;
  return lang === "zh" ? "请求失败" : "The request failed";
}

function statusText(status: AskStatus | undefined, reason: string | undefined, lang: Lang) {
  const zh = lang === "zh";
  switch (status) {
    case "timeout": return zh ? "超过时间上限，已停止" : "Stopped at the time limit";
    case "token_limit": return zh ? "超过 token 上限，已停止" : "Stopped at the token limit";
    case "turn_limit": return zh ? "超过检索步数上限，已停止" : "Stopped at the step limit";
    case "provider_error": return zh ? `模型调用失败${reason ? `：${reason}` : ""}` : `The model call failed${reason ? `: ${reason}` : ""}`;
    case "no_answer": return zh ? "没有得到回答" : "No answer was produced";
    case "failed": return zh ? `这次提问失败${reason ? `：${reason}` : ""}` : `This question failed${reason ? `: ${reason}` : ""}`;
    default: return "";
  }
}

export function Ask() {
  const { lang } = useLang();
  const zh = lang === "zh";
  const [threads, setThreads] = useState<AskThreadSummary[]>([]);
  const [thread, setThread] = useState<AskThread | null>(null);
  const [question, setQuestion] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [showList, setShowList] = useState(false);
  const bottomRef = useRef<HTMLDivElement | null>(null);
  const threadIdRef = useRef<string>("");

  const loadThreads = useCallback(async () => {
    try {
      setThreads(await listAskThreads());
    } catch {
      /* the thread list is secondary; a failure must not block asking */
    }
  }, []);

  const openThread = useCallback(async (id: string) => {
    threadIdRef.current = id;
    try {
      setThread(await getAskThread(id));
      setError("");
    } catch (cause) {
      setError(errorText(cause, lang));
    }
  }, [lang]);

  useEffect(() => { void loadThreads(); }, [loadThreads]);
  useEffect(() => { threadIdRef.current = thread?.id ?? ""; }, [thread?.id]);

  // Poll only while a run is in flight; a completed thread needs no traffic.
  useEffect(() => {
    if (!thread?.running) return;
    let alive = true;
    const timer = window.setInterval(() => {
      const id = threadIdRef.current;
      if (!id) return;
      getAskThread(id)
        .then((next) => {
          if (!alive) return;
          setThread(next);
          if (!next.running) void loadThreads();
        })
        .catch(() => { /* keep the last good state; the next tick retries */ });
    }, POLL_MS);
    return () => { alive = false; window.clearInterval(timer); };
  }, [thread?.running, loadThreads]);

  useEffect(() => {
    if (thread?.running) bottomRef.current?.scrollIntoView({ block: "end" });
  }, [thread?.messages.length, thread?.running]);

  const startNew = async () => {
    setBusy(true); setError("");
    try {
      const created = await createAskThread();
      setThread(created);
      threadIdRef.current = created.id;
      setShowList(false);
      await loadThreads();
    } catch (cause) {
      setError(errorText(cause, lang));
    } finally {
      setBusy(false);
    }
  };

  const submit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const text = question.trim();
    if (!text || busy || thread?.running) return;
    void (async () => {
      setBusy(true); setError("");
      try {
        let id = threadIdRef.current;
        if (!id) {
          const created = await createAskThread(text.slice(0, 60));
          id = created.id;
          threadIdRef.current = id;
        }
        await askQuestion(id, text);
        setQuestion("");
        setThread(await getAskThread(id));
        await loadThreads();
      } catch (cause) {
        setError(errorText(cause, lang));
      } finally {
        setBusy(false);
      }
    })();
  };

  const onDelete = (id: string) => {
    if (!window.confirm(zh ? "删除这段对话？" : "Delete this conversation?")) return;
    void (async () => {
      try {
        await deleteAskThread(id);
        if (threadIdRef.current === id) {
          setThread(null);
          threadIdRef.current = "";
        }
        await loadThreads();
      } catch (cause) {
        setError(errorText(cause, lang));
      }
    })();
  };

  const resolved = thread?.model;
  const modelReady = resolved ? resolved.configured : true;

  return (
    <main className="mx-auto flex min-h-[calc(100dvh-8rem)] max-w-3xl flex-col px-4 py-8">
      <header className="flex flex-wrap items-center justify-between gap-3">
        <div className="min-w-0">
          <h1 className="font-serif text-3xl font-medium">{zh ? "对话 Atlas" : "Ask Atlas"}</h1>
          <p className="mt-1 text-sm text-muted">
            {zh
              ? "用自然语言查询类型知识；回答只用本页实际检索到的资料，并给出类型链接。"
              : "Query type knowledge in natural language. Answers are grounded in what this page retrieved, with links to the types used."}
          </p>
        </div>
        <div className="flex shrink-0 gap-2">
          <Button size="sm" variant="outline" onClick={() => setShowList((v) => !v)}>
            <ChevronDown className={`size-4 transition-transform ${showList ? "rotate-180" : ""}`} />
            {zh ? "历史" : "History"}
            {threads.length ? <span className="text-subtle">{threads.length}</span> : null}
          </Button>
          <Button size="sm" onClick={() => void startNew()} disabled={busy}>
            <Plus className="size-4" />{zh ? "新对话" : "New"}
          </Button>
        </div>
      </header>

      {showList ? (
        <section className="mt-4 rounded-xl bg-surface p-2 shadow-card">
          {threads.length === 0 ? (
            <p className="px-3 py-4 text-sm text-muted">{zh ? "还没有对话。" : "No conversations yet."}</p>
          ) : (
            <ul className="max-h-72 overflow-auto">
              {threads.map((item) => (
                <li key={item.id} className="flex items-center gap-2">
                  <button
                    type="button"
                    onClick={() => { void openThread(item.id); setShowList(false); }}
                    className={`min-w-0 flex-1 rounded-lg px-3 py-2 text-left text-sm hover:bg-chip ${threadIdRef.current === item.id ? "bg-chip" : ""}`}
                  >
                    <span className="flex items-center gap-2">
                      <span className="min-w-0 truncate font-medium">
                        {item.title || (zh ? "（未命名）" : "(untitled)")}
                      </span>
                      {item.running ? <Badge tone="primary">{zh ? "进行中" : "running"}</Badge> : null}
                    </span>
                    <span className="mt-0.5 block truncate text-[11px] text-subtle">
                      {item.message_count} {zh ? "条消息" : "messages"} · {item.updated_at}
                    </span>
                  </button>
                  <button
                    type="button"
                    aria-label={zh ? "删除对话" : "Delete conversation"}
                    onClick={() => onDelete(item.id)}
                    className="rounded-md p-2 text-subtle hover:bg-danger/10 hover:text-danger"
                  >
                    <Trash2 className="size-4" />
                  </button>
                </li>
              ))}
            </ul>
          )}
        </section>
      ) : null}

      {!modelReady ? (
        <div role="status" className="mt-5 flex items-start gap-2 rounded-lg bg-warn/10 p-3 text-sm text-warn">
          <AlertTriangle className="mt-0.5 size-4 shrink-0" />
          <span className="min-w-0 flex-1">
            {zh
              ? "还没有配置模型服务。先去「设置」配置一个可用的 provider，再回来提问。"
              : "No model provider is configured. Add one in Settings, then come back to ask."}
            {resolved?.reason ? <span className="mt-1 block text-xs opacity-80">{resolved.reason}</span> : null}
            <Link to="/settings" className="mt-2 inline-block font-medium underline">
              {zh ? "去设置" : "Open settings"}
            </Link>
          </span>
        </div>
      ) : null}

      {error ? (
        <div role="alert" className="mt-5 flex items-start gap-2 rounded-lg bg-danger/10 p-3 text-sm text-danger">
          <AlertTriangle className="mt-0.5 size-4 shrink-0" />
          <span className="min-w-0 break-words">{error}</span>
        </div>
      ) : null}

      <div className="mt-6 min-h-0 flex-1 space-y-5">
        {thread ? thread.messages.map((message) => (
          <Message key={message.id} lang={lang} message={message} />
        )) : (
          <EmptyState lang={lang} onPick={(text) => setQuestion(text)} />
        )}
        {thread?.running ? (
          <p role="status" className="flex items-center gap-2 text-sm text-subtle">
            <Loader2 className="size-4 animate-spin" />
            {zh ? "正在检索并回答…" : "Searching and answering…"}
          </p>
        ) : null}
        <div ref={bottomRef} />
      </div>

      <form onSubmit={submit} className="sticky bottom-0 mt-6 bg-bg/95 pt-3 backdrop-blur">
        <div className="flex items-end gap-2">
          <textarea
            value={question}
            onChange={(event) => setQuestion(event.target.value)}
            onKeyDown={(event) => {
              if (event.key === "Enter" && !event.shiftKey) {
                event.preventDefault();
                event.currentTarget.form?.requestSubmit();
              }
            }}
            rows={2}
            placeholder={zh ? "问点什么，例如：看板类和任务管理类有什么区别？" : "Ask something, e.g. how do kanban and task management types differ?"}
            className={inputClass}
            disabled={busy || Boolean(thread?.running)}
          />
          <Button
            type="submit"
            size="icon"
            aria-label={zh ? "提问" : "Ask"}
            disabled={busy || Boolean(thread?.running) || !question.trim()}
          >
            {busy || thread?.running
              ? <Loader2 className="size-4 animate-spin" />
              : <ArrowUp className="size-4" />}
          </Button>
        </div>
        <p className="mt-2 text-[11px] leading-5 text-subtle">
          {zh
            ? "本页只读：只能检索和阅读类型资料，不会修改语料、项目或文件。Enter 发送，Shift+Enter 换行。"
            : "Read-only: this page searches and reads type material, and never modifies the corpus, projects, or files. Enter to send, Shift+Enter for a newline."}
        </p>
      </form>
    </main>
  );
}

function EmptyState({ lang, onPick }: { lang: Lang; onPick: (text: string) => void }) {
  const zh = lang === "zh";
  const examples = zh
    ? ["看板类和任务管理类有什么区别？", "有哪些和电子表格相关的类型？", "CRM 和销售管道管理是同一个类型吗？"]
    : ["How do kanban and task management types differ?",
       "Which types relate to spreadsheets?",
       "Are CRM and sales pipeline management the same type?"];
  return (
    <div className="rounded-xl border border-dashed border-border bg-surface p-6">
      <p className="text-sm font-medium">{zh ? "从一个问题开始" : "Start with a question"}</p>
      <p className="mt-2 text-sm leading-6 text-muted">
        {zh
          ? "Atlas 会先检索类型语料，再基于检索结果回答，并在末尾列出引用的类型。"
          : "Atlas searches the type corpus first, answers from what it found, and lists the types it cited."}
      </p>
      <div className="mt-4 flex flex-wrap gap-2">
        {examples.map((text) => (
          <button
            key={text}
            type="button"
            onClick={() => onPick(text)}
            className="rounded-full bg-chip px-3 py-1.5 text-xs text-ink-soft transition-colors hover:bg-border"
          >
            {text}
          </button>
        ))}
      </div>
    </div>
  );
}

function Message({ lang, message }: { lang: Lang; message: AskMessage }) {
  const zh = lang === "zh";
  if (message.role === "user") {
    return (
      <div className="flex justify-end">
        <div className="max-w-[85%] whitespace-pre-wrap break-words rounded-2xl bg-primary px-4 py-2.5 text-sm text-primary-fg">
          {message.content}
        </div>
      </div>
    );
  }

  const reason = statusText(message.status, message.error, lang);
  const failed = message.status && message.status !== "completed";
  const steps = message.steps ?? [];
  const citations = message.citations ?? [];

  return (
    <article className="rounded-2xl bg-surface p-4 shadow-card">
      {steps.length ? <Steps lang={lang} steps={steps} /> : null}

      {message.content ? (
        <div className="mt-3">
          <Prose md={message.content} />
        </div>
      ) : null}

      {reason ? (
        <p className={`mt-3 flex items-start gap-2 rounded-lg p-2.5 text-xs ${failed ? "bg-warn/10 text-warn" : "bg-chip text-muted"}`}>
          <AlertTriangle className="mt-0.5 size-3.5 shrink-0" />
          <span className="min-w-0 break-words">{reason}</span>
        </p>
      ) : null}

      {citations.length ? (
        <section className="mt-3 border-t border-border pt-3">
          <p className="text-[11px] font-medium tracking-wide text-subtle">
            {zh ? "引用类型" : "Cited types"}
          </p>
          <div className="mt-2 flex flex-wrap gap-1.5">
            {citations.map((item) => (
              <Link
                key={item.slug}
                to={`/types/${item.slug}`}
                className="inline-flex items-center gap-1.5 rounded-full bg-chip px-2.5 py-1 text-xs text-ink-soft transition-colors hover:bg-border"
              >
                <span className="font-medium">{item.name_zh || item.slug}</span>
                <code className="font-mono text-[10px] text-subtle">{item.slug}</code>
              </Link>
            ))}
          </div>
        </section>
      ) : null}

      <Usage lang={lang} usage={message.usage} />
    </article>
  );
}

function Steps({ lang, steps }: { lang: Lang; steps: NonNullable<AskMessage["steps"]> }) {
  const zh = lang === "zh";
  const [open, setOpen] = useState(false);
  const failed = steps.filter((step) => step.error).length;
  return (
    <details
      className="rounded-lg bg-bg-elevated p-2.5"
      open={open}
      onToggle={(event) => setOpen((event.target as HTMLDetailsElement).open)}
    >
      <summary className="flex cursor-pointer items-center gap-2 text-xs text-muted">
        <Wrench className="size-3.5 shrink-0" />
        <span className="font-medium">{zh ? "检索过程" : "Retrieval steps"}</span>
        <span className="text-subtle">
          {steps.length} {zh ? "步" : "steps"}
        </span>
        {failed ? <Badge tone="warn">{failed} {zh ? "失败" : "failed"}</Badge> : null}
      </summary>
      <ol className="mt-2 space-y-1.5">
        {steps.map((step) => (
          <li key={step.index} className="flex items-start gap-2 text-xs">
            <span className="mt-1 w-4 shrink-0 text-right font-mono text-[10px] text-subtle">{step.index}</span>
            {step.error
              ? <AlertTriangle className="mt-0.5 size-3.5 shrink-0 text-warn" />
              : <Check className="mt-0.5 size-3.5 shrink-0 text-ok" />}
            <span className="min-w-0 flex-1">
              <code className="font-mono text-[11px] text-primary">{step.tool}</code>
              <span className="ml-2 break-words text-muted">{step.summary}</span>
            </span>
          </li>
        ))}
      </ol>
    </details>
  );
}

function Usage({ lang, usage }: { lang: Lang; usage: AskMessage["usage"] }) {
  if (!usage) return null;
  const zh = lang === "zh";
  const tokens = usage.total_tokens;
  return (
    <p className="mt-3 flex items-center gap-1.5 text-[11px] text-subtle">
      <Search className="size-3" />
      {typeof tokens === "number"
        ? `${tokens.toLocaleString()} tokens`
        : (zh ? "用量未知" : "usage unknown")}
      {usage.cost === null ? <span>· {zh ? "费用未知" : "cost unknown"}</span> : null}
    </p>
  );
}
