import { useCallback, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { RefreshCw } from "lucide-react";
import { fetchWithTimeout } from "@/lib/http";
import { useLang } from "@/lib/lang";

export function ServiceStatus() {
  const { lang } = useLang(); const zh = lang === "zh";
  const [status, setStatus] = useState<"checking" | "online" | "offline">("checking");
  const [checking, setChecking] = useState(false);
  const check = useCallback(async () => {
    setChecking(true);
    try {
      const result = await fetchWithTimeout("/api/health", {}, 5000) as { ok?: boolean };
      setStatus(result.ok ? "online" : "offline");
    } catch { setStatus("offline"); }
    finally { setChecking(false); }
  }, []);
  useEffect(() => {
    void check();
    const visible = () => { if (document.visibilityState === "visible") void check(); };
    const timer = setInterval(visible, 60_000);
    document.addEventListener("visibilitychange", visible);
    window.addEventListener("online", visible);
    return () => { clearInterval(timer); document.removeEventListener("visibilitychange", visible); window.removeEventListener("online", visible); };
  }, [check]);
  if (status !== "offline") return null;
  return <div role="status" className="border-b border-warn/20 bg-warn/5">
    <div className="mx-auto flex max-w-6xl flex-wrap items-center gap-x-4 gap-y-2 px-4 py-3 text-xs leading-5 text-warn">
      <p className="flex-1 basis-64">{zh ? "本地服务暂时无法连接。分类资料仍可阅读；项目库、收藏和设置需要服务恢复。" : "The local service is unavailable. Taxonomy pages remain readable; repositories, favorites and settings need the service."}</p>
      <button className="inline-flex min-h-9 items-center gap-1.5 font-medium disabled:opacity-50" disabled={checking} onClick={() => void check()}><RefreshCw className={`size-3.5 ${checking ? "animate-spin" : ""}`} />{zh ? "重新检查" : "Check again"}</button>
      <Link className="underline underline-offset-4" to="/guide#service">{zh ? "启动与排查" : "Connection help"}</Link>
    </div>
  </div>;
}
