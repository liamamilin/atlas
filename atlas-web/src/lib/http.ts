/** Bounded requests; writes are never retried automatically. */
export async function fetchWithTimeout(url: string, init: RequestInit = {}, timeoutMs = 20_000) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    const response = await fetch(url, { ...init, signal: controller.signal });
    // Consume the body within the same deadline, including stalled responses.
    const body = await response.text();
    let value: unknown;
    try { value = JSON.parse(body); }
    catch { throw new Error(`服务返回了无效响应 / Invalid service response (${response.status})`); }
    if (!response.ok) {
      const error = value as { error?: string };
      throw new Error(error?.error || `请求失败 / Request failed (${response.status})`);
    }
    return value;
  } catch (error) {
    if (controller.signal.aborted) throw new Error("请求超时，请重试 / Request timed out. Please retry.");
    throw error;
  } finally { clearTimeout(timer); }
}
