import { useEffect, useState } from "react";
import type { ReactNode } from "react";
import { useLang, t } from "@/lib/lang";

export function useAsync<T>(fn: () => Promise<T>, deps: unknown[]): { data: T | null; error: string | null; loading: boolean } {
  const [state, setState] = useState<{ data: T | null; error: string | null; loading: boolean }>({
    data: null,
    error: null,
    loading: true,
  });
  useEffect(() => {
    let alive = true;
    setState((s) => ({ data: s.data, error: null, loading: true }));
    fn().then(
      (data) => alive && setState({ data, error: null, loading: false }),
      (e) => alive && setState({ data: null, error: String(e), loading: false }),
    );
    return () => {
      alive = false;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps);
  return state as { data: T | null; error: string | null; loading: boolean };
}

export function Loading({ children }: { children?: ReactNode }) {
  const { lang } = useLang();
  return <div role="status" aria-live="polite" className="py-16 text-center text-sm text-subtle">{children ?? t("loading", lang)}</div>;
}

export function ErrorBox({ message }: { message: string }) {
  const { lang } = useLang();
  return (
    <div role="alert" className="mx-auto mt-12 max-w-xl rounded-xl bg-surface p-6 text-center shadow-card">
      <p className="text-sm font-medium text-danger">{t("loadFailed", lang)}</p>
      {message ? (
        <details className="mt-3 text-left">
          <summary className="cursor-pointer text-xs text-muted hover:text-fg">{t("errorDetails", lang)}</summary>
          <pre className="mt-2 max-h-40 overflow-auto whitespace-pre-wrap break-words rounded-md bg-bg-elevated p-3 font-mono text-[11px] leading-5 text-subtle">{message}</pre>
        </details>
      ) : null}
      <p className="mt-3 text-xs leading-5 text-subtle">{t("retryHint", lang)}</p>
      <button type="button" className="mt-4 rounded-md bg-primary px-3 py-2 text-xs font-medium text-white hover:opacity-90" onClick={() => window.location.reload()}>
        {t("retry", lang)}
      </button>
    </div>
  );
}
