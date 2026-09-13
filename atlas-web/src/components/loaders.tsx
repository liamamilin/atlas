import { useEffect, useState } from "react";
import type { ReactNode } from "react";

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

export function Loading({ children = "加载中…" }: { children?: ReactNode }) {
  return <div className="py-16 text-center text-sm text-subtle">{children}</div>;
}

export function ErrorBox({ message }: { message: string }) {
  return (
    <div className="mx-auto mt-12 max-w-xl rounded-xl bg-surface p-6 text-center shadow-card">
      <p className="text-sm text-danger">加载失败：{message}</p>
    </div>
  );
}
