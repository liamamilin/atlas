import { useEffect, useState } from "react";
import { Button } from "@/components/ui/button";
import { useLang } from "@/lib/lang";
import { fetchWithTimeout } from "@/lib/http";

type GitHubStatus = { configured: boolean; source: "local" | "environment" | "none" };
type Probe = { limits: { core: { remaining: number; limit: number }; search: { remaining: number; limit: number } } };

async function request<T>(path = "", body?: unknown): Promise<T> {
  return await fetchWithTimeout(`/api/settings/github${path}`, body === undefined ? undefined : {
    method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body),
  }) as T;
}

export function GitHubSettings() {
  const { lang } = useLang(); const zh = lang === "zh";
  const [status, setStatus] = useState<GitHubStatus | null>(null);
  const [token, setToken] = useState("");
  const [busy, setBusy] = useState(false);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");
  const [probe, setProbe] = useState<Probe | null>(null);
  useEffect(() => { void request<GitHubStatus>().then(setStatus).catch(e => setError(String(e.message))); }, []);
  async function act(action: "save" | "remove" | "test") {
    setBusy(true); setError(""); setMessage(""); setProbe(null);
    try {
      if (action === "test") setProbe(await request<Probe>("/test", {}));
      else {
        setStatus(await request<GitHubStatus>("", action === "remove" ? { remove: true } : { token }));
        setToken("");
        setMessage(zh ? "GitHub 设置已保存，后续采集立即使用。" : "Saved. Subsequent requests use this setting immediately.");
      }
    } catch (e) { setError(e instanceof Error ? e.message : "GitHub settings unavailable"); }
    finally { setBusy(false); }
  }
  return <section id="github" className="mt-8 scroll-mt-36 rounded-xl bg-surface p-5 shadow-card" aria-label="GitHub Token">
    <h2 className="font-serif text-lg font-medium">GitHub Token</h2>
    <p className="mt-2 text-sm text-muted">{zh ? "用于搜索公开项目、读取 README、官方文档与许可证，提高采集额度。" : "Used to search public projects and read their official documentation and licenses."}</p>
    <p className="mt-2 text-xs text-muted">{status ? (status.configured ? (zh ? `已配置 · ${status.source === "local" ? "本机保存" : "环境变量"}` : `Configured · ${status.source}`) : (zh ? "未配置 · 使用公开匿名额度" : "Not configured · public anonymous quota")) : (zh ? "读取配置状态…" : "Loading status…")}</p>
    <form className="mt-4" onSubmit={e => { e.preventDefault(); void act("save"); }}>
      <label className="block text-sm">{zh ? "GitHub 访问令牌" : "GitHub access token"}
        <input type="password" autoComplete="new-password" spellCheck={false} value={token} onChange={e => setToken(e.target.value)} placeholder={zh ? "留空保留已保存的 Token" : "Leave blank to keep the saved token"} className="mt-1 h-10 w-full rounded-lg border border-border bg-bg-elevated px-3 text-sm" />
      </label>
      <p className="mt-2 text-xs leading-5 text-subtle">{zh ? "建议使用仅访问公开仓库的 fine-grained Token，设置有效期。凭据以 0600 权限保存在本机，接口不回传明文，不进入模型输入。" : "Use a fine-grained token for public repositories with an expiry date. Stored locally with 0600 permissions; never returned or sent to the model."}</p>
      <div className="mt-3 flex flex-wrap gap-2">
        <Button type="submit" disabled={busy}>{zh ? "保存 GitHub Token" : "Save GitHub token"}</Button>
        <Button type="button" variant="outline" disabled={busy || !status} onClick={() => void act("test")}>{zh ? "测试 GitHub 连接" : "Test GitHub connection"}</Button>
        {status?.source === "local" && <Button type="button" variant="outline" disabled={busy} onClick={() => void act("remove")}>{zh ? "清除已保存 Token" : "Clear saved token"}</Button>}
      </div>
    </form>
    {message && <p role="status" className="mt-3 text-sm text-primary">{message}</p>}
    {probe && <p role="status" className="mt-3 text-sm text-primary">{zh ? "连接成功" : "Connected"} · REST {probe.limits.core.remaining}/{probe.limits.core.limit} · Search {probe.limits.search.remaining}/{probe.limits.search.limit}</p>}
    {error && <p role="alert" className="mt-3 break-words text-sm text-danger">{error}</p>}
  </section>;
}
