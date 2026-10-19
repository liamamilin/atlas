import { useCallback, useEffect, useState, type FormEvent } from "react";
import {
  AlertTriangle, Check, CheckCircle2, Cpu, Database, Loader2, Plus, RefreshCw,
  Star, Trash2, X,
} from "lucide-react";
import {
  AtlasApiError,
  deleteModelProvider,
  getModelSettings,
  importOpencodeCredentials,
  listProviderModels,
  saveModelProvider,
  setDefaultModel,
  setEmbeddingEndpoint,
  testModelProvider,
  type ModelProvider,
  type ModelSettings,
  type ProviderTestResult,
} from "@/lib/atlas";
import { ErrorBox, Loading } from "@/components/loaders";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { useLang, type Lang } from "@/lib/lang";

const inputClass =
  "mt-1 h-10 w-full rounded-lg border border-border bg-bg-elevated px-3 text-sm outline-none focus:ring-2 focus:ring-primary/35";

/**
 * A 404 "no route" means the front-end is newer than the running API process:
 * the settings routes exist in the source but the server has not been restarted.
 * Surfacing the raw text sends people looking for a bug in their input.
 */
function actionError(cause: unknown, lang: Lang) {
  if (cause instanceof AtlasApiError) {
    if (cause.status === 404 && /no route/i.test(cause.message)) {
      return lang === "zh"
        ? "后端进程还是旧版本，没有这几个设置接口。请重启本地 API（先停止再启动，直接再点一次图标不会重启已运行的进程），然后刷新本页。"
        : "The backend process is still running older code without these settings routes. Restart the local API (stop it first; launching the app again does not restart a running process), then reload this page.";
    }
    if (cause.message) return cause.message;
  }
  if (cause instanceof Error && cause.message) return cause.message;
  return lang === "zh" ? "操作失败" : "The action failed";
}

type Draft = {
  id: string;
  preset: string;
  name: string;
  base_url: string;
  api_key: string;
  models: string;
};

const EMPTY_DRAFT: Draft = {
  id: "", preset: "", name: "", base_url: "", api_key: "", models: "",
};

export function Settings() {
  const { lang } = useLang();
  const [settings, setSettings] = useState<ModelSettings | null>(null);
  const [loading, setLoading] = useState(true);
  const [loadError, setLoadError] = useState<string | null>(null);
  const [error, setError] = useState("");
  const [notice, setNotice] = useState("");
  const [busy, setBusy] = useState("");
  const [editing, setEditing] = useState<Draft | null>(null);
  const [testing, setTesting] = useState<Record<string, ProviderTestResult | "running">>({});
  const [defaultDraft, setDefaultDraft] = useState<{ provider: string; model: string }>({
    provider: "", model: "",
  });
  const [embedding, setEmbedding] = useState({ base_url: "", model: "" });

  const zh = lang === "zh";

  const labels = {
    save: zh ? "保存" : "Save", saving: zh ? "保存中…" : "Saving…",
    saved: zh ? "已保存" : "Saved", cancel: zh ? "取消" : "Cancel",
    del: zh ? "删除" : "Delete", test: zh ? "测试连接" : "Test",
    testing: zh ? "测试中…" : "Testing…", setDefault: zh ? "设为默认" : "Set default",
    default: zh ? "默认" : "Default", noKey: zh ? "未配置凭据" : "No credential",
    apiKeyKeep: zh ? "留空表示保留已保存的凭据" : "Leave blank to keep the saved credential",
    addProvider: zh ? "添加服务" : "Add provider",
    editProvider: zh ? "编辑服务" : "Edit provider",
    keyHint: zh ? "凭据以 0600 权限保存在本机，不会出现在页面返回数据里。" : "Credentials are stored locally with 0600 permissions and never appear in API responses.",
    importBtn: zh ? "从 OpenCode 导入凭据" : "Import from OpenCode",
  };

  const refresh = useCallback(async () => {
    try {
      const value = await getModelSettings();
      setSettings(value);
      setLoadError(null);
      // The default pickers reflect what is *saved*, not what is resolved
      // through an OpenCode credential or environment fallback; the
      // "currently in effect" card above already reports the resolved value.
      const savedProvider = value.default.provider || "";
      const savedItem = value.providers.find((p) => p.id === savedProvider);
      setDefaultDraft({
        provider: savedProvider,
        model: value.default.model || savedItem?.models[0] || "",
      });
      setEmbedding({
        base_url: value.embedding.base_url,
        model: value.embedding.model,
      });
    } catch (cause) {
      setLoadError(actionError(cause, lang));
    } finally {
      setLoading(false);
    }
  }, [lang]);

  useEffect(() => { void refresh(); }, [refresh]);

  const run = async (key: string, fn: () => Promise<void>) => {
    setBusy(key); setError(""); setNotice("");
    try {
      await fn();
    } catch (cause) {
      setError(actionError(cause, lang));
    } finally {
      setBusy("");
    }
  };

  if (loading) return <Loading />;
  if (loadError || !settings) return <ErrorBox message={loadError ?? ""} />;

  const providers = settings.providers;
  const presets = Object.entries(settings.presets);
  const unconsumedPresets = presets.filter(
    ([id]) => !providers.some((p) => p.id === id || p.preset === id));

  const startPreset = (presetId: string) => {
    const preset = settings.presets[presetId];
    setEditing({
      id: presetId,
      preset: presetId,
      name: preset.name,
      base_url: preset.base_url,
      api_key: "",
      models: preset.models.join(", "),
    });
    setError("");
  };

  const submitProvider = (event: FormEvent<HTMLFormElement>, draft: Draft) => {
    event.preventDefault();
    void run("save", async () => {
      await saveModelProvider({
        id: draft.id.trim() || undefined,
        preset: draft.preset || undefined,
        name: draft.name.trim(),
        base_url: draft.base_url.trim(),
        api_key: draft.api_key.trim() ? draft.api_key.trim() : undefined,
        models: draft.models.split(/[,\n]/).map((s) => s.trim()).filter(Boolean),
      });
      setEditing(null);
      setNotice(labels.saved);
      await refresh();
    });
  };

  const onTest = (providerId: string) => {
    setTesting((s) => ({ ...s, [providerId]: "running" }));
    testModelProvider(providerId)
      .then((result) => setTesting((s) => ({ ...s, [providerId]: result })))
      .catch((cause) => setTesting((s) => ({
        ...s,
        [providerId]: {
          id: providerId, ok: false, models: [], model_count: 0,
          error: actionError(cause, lang), code: "client_error", latency_ms: 0,
        },
      })));
  };

  return (
    <main className="mx-auto max-w-5xl px-4 py-10">
      <h1 className="font-serif text-3xl font-medium">{zh ? "设置" : "Settings"}</h1>
      <p className="mt-2 max-w-3xl text-sm leading-6 text-muted">
        {zh
          ? "配置 Atlas 使用的模型服务。凭据只保存在本机，接口不会回传明文。"
          : "Configure the model providers Atlas uses. Credentials stay on this machine and are never returned in plain text."}
      </p>

      {error ? (
        <div role="alert" className="mt-5 flex items-start gap-2 rounded-lg bg-danger/10 p-3 text-sm text-danger">
          <AlertTriangle className="mt-0.5 size-4 shrink-0" />
          <span className="min-w-0 break-words">{error}</span>
        </div>
      ) : null}
      {notice ? (
        <div role="status" className="mt-5 flex items-center gap-2 rounded-lg bg-ok/10 p-3 text-sm text-ok">
          <Check className="size-4 shrink-0" />{notice}
        </div>
      ) : null}

      {/* ---- currently effective ---- */}
      <section className="mt-8 rounded-xl bg-surface p-5 shadow-card">
        <div className="flex items-start gap-3">
          <Cpu className="mt-0.5 size-5 shrink-0 text-primary" />
          <div className="min-w-0 flex-1">
            <h2 className="font-serif text-lg font-medium">{zh ? "当前生效" : "Currently in effect"}</h2>
            {settings.resolved.configured ? (
              <>
                <p className="mt-2 text-sm text-muted">
                  {settings.resolved.provider_name} · <code className="font-mono text-xs">{settings.resolved.model}</code>
                </p>
                <div className="mt-3 flex flex-wrap items-center gap-2">
                  <Badge tone="primary">{sourceLabel(settings.resolved.source, zh)}</Badge>
                  <span className="font-mono text-[11px] text-subtle">{settings.resolved.base_url}</span>
                </div>
              </>
            ) : (
              <EmptyConfigured lang={lang} reason={settings.resolved.reason} />
            )}
            <div className="mt-4 flex flex-wrap gap-2">
              <Button
                size="sm" variant="outline"
                disabled={busy === "import"}
                onClick={() => void run("import", async () => {
                  const result = await importOpencodeCredentials();
                  setNotice(result.count
                    ? (zh ? `已导入 ${result.count} 个服务` : `Imported ${result.count} providers`)
                    : (zh ? "没有找到可导入的凭据" : "No importable credentials found"));
                  await refresh();
                })}
              >
                {busy === "import" ? <Loader2 className="size-4 animate-spin" /> : <RefreshCw className="size-4" />}
                {labels.importBtn}
              </Button>
            </div>
          </div>
        </div>
      </section>

      {/* ---- default selection ---- */}
      <section className="mt-6 rounded-xl bg-surface p-5 shadow-card">
        <h2 className="font-serif text-lg font-medium">{zh ? "默认服务" : "Default provider"}</h2>
        <p className="mt-1 text-xs leading-5 text-subtle">
          {zh
            ? "未指定服务时，Atlas 的模型调用都走这里。"
            : "All Atlas model calls without an explicit provider use this one."}
        </p>
        <div className="mt-4 grid gap-4 sm:grid-cols-[minmax(0,1fr)_minmax(0,1fr)_auto] sm:items-end">
          <label className="block text-sm">
            <span className="text-muted">{zh ? "默认服务" : "Default provider"}</span>
            <select
              className={inputClass}
              value={defaultDraft.provider}
              onChange={(event) => {
                const provider = event.target.value;
                const item = providers.find((p) => p.id === provider);
                setDefaultDraft({
                  provider,
                  model: defaultDraft.model && item?.models.includes(defaultDraft.model)
                    ? defaultDraft.model
                    : (item?.models[0] || ""),
                });
              }}
            >
              <option value="">{zh ? "（未设置）" : "(not set)"}</option>
              {providers.map((p) => <option key={p.id} value={p.id}>{p.name}</option>)}
            </select>
          </label>
          <ModelPicker
            lang={lang}
            providerId={defaultDraft.provider}
            value={defaultDraft.model}
            providers={providers}
            onChange={(model) => setDefaultDraft((s) => ({ ...s, model }))}
          />
          <Button
            disabled={busy === "default" || !defaultDraft.provider}
            onClick={() => void run("default", async () => {
              await setDefaultModel(defaultDraft.provider, defaultDraft.model || null);
              setNotice(labels.saved);
              await refresh();
            })}
          >
            {busy === "default" ? <Loader2 className="size-4 animate-spin" /> : <Star className="size-4" />}
            {labels.setDefault}
          </Button>
        </div>
      </section>

      {/* ---- configured providers ---- */}
      <section className="mt-6">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <h2 className="font-serif text-lg font-medium">
            {zh ? "已配置服务" : "Configured providers"}
          </h2>
          <Button size="sm" variant="outline"
            onClick={() => { setEditing({ ...EMPTY_DRAFT }); setError(""); }}>
            <Plus className="size-4" />{labels.addProvider}
          </Button>
        </div>

        {editing ? (
          <ProviderForm
            lang={lang} draft={editing} presets={settings.presets}
            busy={busy === "save"} onChange={setEditing}
            onCancel={() => setEditing(null)}
            onSubmit={(event) => submitProvider(event, editing)}
            labels={labels} saveError={error}
          />
        ) : null}

        {providers.length === 0 && !editing ? (
          <p className="mt-4 rounded-xl border border-dashed border-border bg-surface p-5 text-sm leading-6 text-muted">
            {zh
              ? "还没有配置模型服务。可以从下方常用服务里选一个，或直接从 OpenCode 导入本机凭据。"
              : "No providers yet. Pick one of the common providers below, or import this machine's OpenCode credentials."}
          </p>
        ) : null}

        <div className="mt-4 grid gap-3">
          {providers.map((provider) => (
            <ProviderRow
              key={provider.id} lang={lang} provider={provider}
              isDefault={settings.default.provider === provider.id}
              result={testing[provider.id]} busy={busy}
              labels={labels}
              onTest={() => onTest(provider.id)}
              onEdit={() => {
                setEditing({
                  id: provider.id, preset: provider.preset, name: provider.name,
                  base_url: provider.base_url, api_key: "",
                  models: provider.models.join(", "),
                });
                setError("");
              }}
              onDelete={() => {
                if (!window.confirm(zh
                  ? `删除服务「${provider.name}」及其保存的凭据？`
                  : `Delete provider "${provider.name}" and its stored credential?`)) return;
                void run(`delete:${provider.id}`, async () => {
                  await deleteModelProvider(provider.id);
                  setNotice(labels.saved);
                  await refresh();
                });
              }}
              onSetDefault={() => void run(`dflt:${provider.id}`, async () => {
                await setDefaultModel(provider.id, provider.models[0] || null);
                setNotice(labels.saved);
                await refresh();
              })}
            />
          ))}
        </div>
      </section>

      {/* ---- presets ---- */}
      {unconsumedPresets.length ? (
        <section className="mt-8">
          <h2 className="font-serif text-lg font-medium">{zh ? "常用服务" : "Common providers"}</h2>
          <p className="mt-1 text-xs text-subtle">
            {zh ? "选一个填入凭据即可，接口地址已预填。" : "Pick one and add a credential; the base URL is prefilled."}
          </p>
          <div className="mt-4 grid gap-2 sm:grid-cols-2 lg:grid-cols-3">
            {unconsumedPresets.map(([id, preset]) => (
              <button
                key={id} type="button" onClick={() => startPreset(id)}
                className="flex items-center justify-between gap-3 rounded-lg bg-surface px-4 py-3 text-left text-sm shadow-card transition-shadow hover:shadow-card-hover"
              >
                <span className="min-w-0">
                  <span className="block truncate font-medium">{preset.name}</span>
                  <span className="mt-0.5 block truncate font-mono text-[10px] text-subtle">{preset.base_url}</span>
                </span>
                <Plus className="size-4 shrink-0 text-primary" />
              </button>
            ))}
          </div>
        </section>
      ) : null}

      {/* ---- embedding ---- */}
      <section className="mt-8 rounded-xl bg-surface p-5 shadow-card">
        <div className="flex items-start gap-3">
          <Database className="mt-0.5 size-5 shrink-0 text-primary" />
          <div className="min-w-0 flex-1">
            <h2 className="font-serif text-lg font-medium">{zh ? "向量检索（Embedding）" : "Embedding"}</h2>
            <p className="mt-1 text-xs leading-5 text-subtle">
              {zh ? "语义检索用。默认使用本机 Ollama 的 bge-m3。" : "Used for semantic search. Defaults to bge-m3 on the local Ollama."}
            </p>
            <div className="mt-4 grid gap-3 sm:grid-cols-[minmax(0,2fr)_minmax(0,1fr)_auto] sm:items-end">
              <label className="block text-sm">
                <span className="text-muted">{zh ? "接口地址（base URL）" : "Base URL"}</span>
                <input className={inputClass} value={embedding.base_url}
                  onChange={(e) => setEmbedding((s) => ({ ...s, base_url: e.target.value }))} />
              </label>
              <label className="block text-sm">
                <span className="text-muted">{zh ? "模型名" : "Model"}</span>
                <input className={inputClass} value={embedding.model}
                  onChange={(e) => setEmbedding((s) => ({ ...s, model: e.target.value }))} />
              </label>
              <Button disabled={busy === "embedding"} variant="outline"
                onClick={() => void run("embedding", async () => {
                  await setEmbeddingEndpoint(embedding);
                  setNotice(labels.saved);
                  await refresh();
                })}>
                {busy === "embedding" ? <Loader2 className="size-4 animate-spin" /> : <Check className="size-4" />}
                {labels.save}
              </Button>
            </div>
          </div>
        </div>
      </section>

      <p className="mt-6 text-xs leading-5 text-subtle">{labels.keyHint}</p>
    </main>
  );
}

function sourceLabel(source: string | undefined, zh: boolean) {
  if (source === "environment") return zh ? "来自环境变量" : "From environment";
  if (source === "opencode") return zh ? "来自 OpenCode 凭据" : "From OpenCode credentials";
  return zh ? "来自设置" : "From settings";
}

function EmptyConfigured({ lang, reason }: { lang: Lang; reason?: string }) {
  const zh = lang === "zh";
  return (
    <div className="mt-2">
      <p className="text-sm font-medium text-warn">{zh ? "尚未配置" : "Not configured"}</p>
      {reason ? <p className="mt-1 text-xs leading-5 text-muted">{reason}</p> : null}
    </div>
  );
}

function ModelPicker({
  lang, providerId, value, providers, onChange,
}: {
  lang: Lang; providerId: string; value: string;
  providers: ModelProvider[]; onChange: (model: string) => void;
}) {
  const zh = lang === "zh";
  const [listed, setListed] = useState<string[] | null>(null);
  const [loading, setLoading] = useState(false);
  const item = providers.find((p) => p.id === providerId);
  const options = listed ?? item?.models ?? [];

  if (!providerId) {
    return (
      <label className="block text-sm">
        <span className="text-muted">{zh ? "默认模型" : "Default model"}</span>
        <input className={inputClass} disabled value="" placeholder="—" />
      </label>
    );
  }
  return (
    <label className="block text-sm">
      <span className="flex items-center justify-between gap-2 text-muted">
        <span>{zh ? "默认模型" : "Default model"}</span>
        <button type="button" className="text-[11px] text-primary hover:underline"
          disabled={loading}
          onClick={() => {
            setLoading(true);
            listProviderModels(providerId)
              .then((r) => setListed(r.models))
              .catch(() => setListed([]))
              .finally(() => setLoading(false));
          }}>
          {loading ? (zh ? "读取中…" : "Loading…") : (zh ? "查看全部模型" : "Load all models")}
        </button>
      </span>
      <input className={inputClass} list={`models-${providerId}`} value={value}
        placeholder={zh ? "输入或选择一个模型" : "Type or pick a model"}
        onChange={(e) => onChange(e.target.value)} />
      <datalist id={`models-${providerId}`}>
        {options.map((m) => <option key={m} value={m} />)}
      </datalist>
    </label>
  );
}

function ProviderRow({
  lang, provider, isDefault, result, busy, labels, onTest, onEdit, onDelete, onSetDefault,
}: {
  lang: Lang; provider: ModelProvider; isDefault: boolean;
  result?: ProviderTestResult | "running"; busy: string; labels: Record<string, string>;
  onTest: () => void; onEdit: () => void; onDelete: () => void; onSetDefault: () => void;
}) {
  const zh = lang === "zh";
  return (
    <article className="rounded-xl bg-surface p-4 shadow-card">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div className="min-w-0 flex-1">
          <div className="flex flex-wrap items-center gap-2">
            <h3 className="font-medium">{provider.name}</h3>
            {isDefault ? <Badge tone="primary">{labels.default}</Badge> : null}
            {provider.has_key
              ? <Badge tone="ok">{provider.key_masked}</Badge>
              : <Badge tone="warn">{labels.noKey}</Badge>}
          </div>
          <p className="mt-1 break-all font-mono text-[11px] text-subtle">{provider.base_url}</p>
          {provider.models.length ? (
            <p className="mt-1 text-[11px] text-subtle">
              {provider.models.length} {zh ? "个模型" : "models"} · {provider.models.slice(0, 4).join(", ")}
            </p>
          ) : null}
        </div>
        <div className="flex shrink-0 flex-wrap gap-1.5">
          <Button size="sm" variant="outline" onClick={onTest}
            disabled={result === "running" || !provider.has_key}>
            {result === "running" ? <Loader2 className="size-3.5 animate-spin" /> : <RefreshCw className="size-3.5" />}
            {result === "running" ? labels.testing : labels.test}
          </Button>
          {!isDefault ? (
            <Button size="sm" variant="ghost" onClick={onSetDefault} disabled={busy === `dflt:${provider.id}`}>
              <Star className="size-3.5" />{labels.setDefault}
            </Button>
          ) : null}
          <Button size="sm" variant="ghost" onClick={onEdit}>{zh ? "编辑" : "Edit"}</Button>
          <Button size="sm" variant="ghost" onClick={onDelete}
            disabled={busy === `delete:${provider.id}`}
            className="text-danger hover:bg-danger/10">
            <Trash2 className="size-3.5" />{labels.del}
          </Button>
        </div>
      </div>
      {result && result !== "running" ? (
        <div className={`mt-3 flex items-start gap-2 rounded-lg p-2.5 text-xs ${result.ok ? "bg-ok/10 text-ok" : "bg-danger/10 text-danger"}`}>
          {result.ok ? <CheckCircle2 className="mt-0.5 size-3.5 shrink-0" /> : <X className="mt-0.5 size-3.5 shrink-0" />}
          <span className="min-w-0 break-words">
            {result.ok
              ? (zh
                ? `连接正常 · ${result.model_count} 个模型 · ${result.latency_ms}ms`
                : `Connected · ${result.model_count} models · ${result.latency_ms}ms`)
              : (result.error || (zh ? "连接失败" : "Connection failed"))}
          </span>
        </div>
      ) : null}
    </article>
  );
}

function ProviderForm({
  lang, draft, presets, busy, onChange, onCancel, onSubmit, labels, saveError,
}: {
  lang: Lang; draft: Draft; presets: ModelSettings["presets"]; busy: boolean;
  onChange: (draft: Draft) => void; onCancel: () => void;
  onSubmit: (event: FormEvent<HTMLFormElement>) => void;
  labels: Record<string, string>; saveError?: string;
}) {
  const zh = lang === "zh";
  const set = (patch: Partial<Draft>) => onChange({ ...draft, ...patch });
  return (
    <form onSubmit={onSubmit} className="mt-4 rounded-xl bg-surface p-5 shadow-card">
      <h3 className="font-medium">{draft.id ? labels.editProvider : labels.addProvider}</h3>
      <div className="mt-4 grid gap-4 sm:grid-cols-2">
        <label className="block text-sm">
          <span className="text-muted">{zh ? "常用服务" : "Provider"}</span>
          <select className={inputClass} value={draft.preset}
            onChange={(e) => {
              const preset = presets[e.target.value];
              set({
                preset: e.target.value,
                id: e.target.value || draft.id,
                name: preset?.name || draft.name,
                base_url: preset?.base_url || "",
                models: (preset?.models || []).join(", "),
              });
            }}>
            <option value="">{zh ? "自定义（手动填写地址）" : "Custom (enter a base URL)"}</option>
            {Object.entries(presets).map(([id, p]) => (
              <option key={id} value={id}>{p.name}</option>
            ))}
          </select>
        </label>
        <label className="block text-sm">
          <span className="text-muted">{zh ? "显示名称" : "Display name"}</span>
          <input className={inputClass} value={draft.name} required
            onChange={(e) => set({ name: e.target.value })} />
        </label>
        <label className="block text-sm sm:col-span-2">
          <span className="text-muted">{zh ? "接口地址（base URL）" : "Base URL"}</span>
          <input className={inputClass} value={draft.base_url} required
            placeholder="https://api.example.com/v1"
            onChange={(e) => set({ base_url: e.target.value })} />
        </label>
        <label className="block text-sm sm:col-span-2">
          <span className="text-muted">{zh ? "API Key" : "API key"}</span>
          <input className={inputClass} type="password" value={draft.api_key}
            autoComplete="off" placeholder={zh ? "留空表示保留已保存的凭据" : "Leave blank to keep the saved credential"}
            onChange={(e) => set({ api_key: e.target.value })} />
          <span className="mt-1 block text-[11px] text-subtle">{labels.apiKeyKeep}</span>
        </label>
        <label className="block text-sm sm:col-span-2">
          <span className="text-muted">{zh ? "模型（逗号或换行分隔）" : "Models (comma or newline separated)"}</span>
          <textarea className={`${inputClass} h-20 py-2 font-mono text-xs`} value={draft.models}
            placeholder="deepseek-v4.1-flash, glm-5.3-flash"
            onChange={(e) => set({ models: e.target.value })} />
        </label>
      </div>
      {saveError ? (
        <div role="alert" className="mt-4 flex items-start gap-2 rounded-lg bg-danger/10 p-3 text-sm text-danger">
          <AlertTriangle className="mt-0.5 size-4 shrink-0" />
          <span className="min-w-0 break-words">{saveError}</span>
        </div>
      ) : null}
      <div className="mt-4 flex gap-2">
        <Button type="submit" disabled={busy}>
          {busy ? <Loader2 className="size-4 animate-spin" /> : <Check className="size-4" />}
          {busy ? labels.saving : labels.save}
        </Button>
        <Button type="button" variant="outline" onClick={onCancel} disabled={busy}>{labels.cancel}</Button>
      </div>
    </form>
  );
}
