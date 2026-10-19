import { createContext, useContext, useEffect, useState, type ReactNode } from "react";

export type Lang = "zh" | "en";

const LangCtx = createContext<{ lang: Lang; setLang: (l: Lang) => void }>({
  lang: "zh",
  setLang: () => {},
});

export function LangProvider({ children }: { children: ReactNode }) {
  const [lang, setLangState] = useState<Lang>(() =>
    (localStorage.getItem("atlas-lang") as Lang) || "zh",
  );
  const setLang = (l: Lang) => {
    setLangState(l);
    localStorage.setItem("atlas-lang", l);
  };
  useEffect(() => {
    document.documentElement.lang = lang === "zh" ? "zh-CN" : "en";
  }, [lang]);
  return <LangCtx.Provider value={{ lang, setLang }}>{children}</LangCtx.Provider>;
}

export function useLang() {
  return useContext(LangCtx);
}

/** Pick bilingual field pair: prefer lang-specific value, fall back to the other. */
export function pick(lang: Lang, zh: string | undefined | null, en: string | undefined | null) {
  if (lang === "zh") return (zh && zh.trim()) || en || "";
  return (en && en.trim()) || zh || "";
}

export const T = {
  appName: { zh: "应用图谱", en: "Application Atlas" },
  home: { zh: "首页", en: "Home" },
  browse: { zh: "浏览类型", en: "Browse Types" },
  apps: { zh: "应用实证", en: "Case Studies" },
  projects: { zh: "项目", en: "Projects" },
  tutorial: { zh: "使用教程", en: "Tutorial" },
  projectsTitle: { zh: "项目工作台", en: "Project Workspace" },
  projectsP: {
    zh: "从一个简短目标开始，保存新想法或已有项目的工作上下文。",
    en: "Start with a short objective and preserve the context for a new idea or an existing project.",
  },
  projectNew: { zh: "创建项目", en: "Create project" },
  projectName: { zh: "项目名称", en: "Project name" },
  projectObjective: { zh: "目标", en: "Objective" },
  projectWorkspace: { zh: "本地工作区路径（新想法可留空）", en: "Local workspace path (optional for a new idea)" },
  projectMode: { zh: "项目类型", en: "Project type" },
  projectModeNew: { zh: "新想法", en: "New idea" },
  projectModeExisting: { zh: "已有项目改进", en: "Existing project" },
  projectCreate: { zh: "创建并进入工作区", en: "Create and open workspace" },
  projectCreating: { zh: "保存中…", en: "Saving…" },
  projectCurrent: { zh: "当前项目", en: "Current project" },
  projectSelect: { zh: "切换到此项目", en: "Select project" },
  projectsEmpty: { zh: "还没有项目。创建后会保存在本地项目库。", en: "No projects yet. New projects are kept in the local project store." },
  browseTitle: { zh: "浏览类型树", en: "Browse the Type Tree" },
  searchPlaceholder: {
    zh: "搜索软件类型或产品，例如：任务管理、看板、Notion、SIEM",
    en: "Search a software type or product, e.g. task management, kanban, Notion, SIEM",
  },
  searchLabel: { zh: "搜索类型或应用", en: "Search types or applications" },
  searchBtn: { zh: "开始搜索", en: "Start searching" },
  browseAll: { zh: "浏览全部 29 个领域", en: "Browse all 29 domains" },
  heroLead: {
    zh: "1805 种软件应用类型，按「它到底管什么」重新整理。",
    en: "1,805 software application types, organized around what each kind of software actually manages.",
  },
  heroP: {
    zh: "看清一种软件解决什么问题、如何工作、有哪些变体、与什么软件容易混淆，再找到这一类型下真正存在的产品。",
    en: "Understand what a type solves, how it works, how it varies, and what it is easily confused with, then explore the real products that exist within it.",
  },
  heroTitle: {
    zh: "软件世界很大，但不是没有边界",
    en: "Software is vast, but it is not without boundaries",
  },
  heroKicker: { zh: "软件应用类型百科", en: "An encyclopedia of software application types" },
  byDomain: { zh: "按领域浏览", en: "Browse by Domain" },
  byDomainP: { zh: "29 个顶级域，每个域下按子域组织类型。", en: "29 top-level domains, each organizing types into sub-domains." },
  domains: { zh: "个顶级域", en: " top-level domains" },
  subs: { zh: "个子域", en: " sub-domains" },
  types: { zh: "个类型", en: " types" },
  leafCount: { zh: "应用类型叶子", en: "Application types" },
  secCount: { zh: "子域导航节点", en: "Sub-domain nodes" },
  appCount: { zh: "已归位的真实产品", en: "Real products classified" },
  definingCore: { zh: "定义核心 · Defining Core", en: "Defining Core" },
  enOriginal: { zh: "英文原文", en: "English original" },
  overview: { zh: "概览", en: "Overview" },
  howItWorks: { zh: "工作结构", en: "How It Works" },
  rules: { zh: "重要规则", en: "Important Rules" },
  variants: { zh: "变体谱系", en: "Variants" },
  realProducts: { zh: "该类型下的真实产品", en: "Real products of this type" },
  corpusProducts: { zh: "代表产品（语料记录）", en: "Representative products (from corpus)" },
  neighbors: { zh: "与相邻类型的关系", en: "Relations to Neighboring Types" },
  typeTree: { zh: "类型树", en: "Type Tree" },
  browseP: {
    zh: "{l0} 个顶级域 · {sec} 个子域 · {leaf} 个类型。点开子域查看全部类型。",
    en: "{l0} top-level domains · {sec} sub-domains · {leaf} types. Open a sub-domain to see its types.",
  },
  loading: { zh: "加载中…", en: "Loading…" },
  loadTypes: { zh: "加载类型中…", en: "Loading types…" },
  loadFailed: { zh: "加载失败", en: "Failed to load" },
  errorDetails: { zh: "查看错误详情", en: "View error details" },
  retryHint: { zh: "请刷新页面重试；如果问题持续存在，请检查本地服务。", en: "Refresh to try again; if the problem persists, check the local service." },
  retry: { zh: "重新加载", en: "Reload" },
  sourceUnavailable: { zh: "正式资料暂时不可用", en: "Canonical source unavailable" },
  notExist: { zh: "类型不存在", en: "Type not found" },
  sources: { zh: "资料来源", en: "Sources" },
  searchTitle: { zh: "搜索「{q}」", en: 'Search "{q}"' },
  searchHits: {
    zh: "{n} 个匹配类型（M1 为名称/别名/定义文本匹配，语义检索见 MCP 工具）",
    en: "{n} matching types (M1 matches names/aliases/defining text; semantic search available via MCP tools)",
  },
  searchNone: { zh: "没有匹配的类型或应用", en: "No matching types or applications" },
  appsTitle: { zh: "应用实证", en: "Case Studies" },
  appsP: {
    zh: "{n} 个真实软件产品，经 atlas 分类管线自动归位到类型图谱中。每个产品卡片可跳转到它所属的类型页（含分界逻辑）。",
    en: "{n} real software products, automatically classified into atlas types. Each card links to its type page (with boundary logic).",
  },
  classified: { zh: "atlas 归类", en: "atlas classification" },
  unclassified: { zh: "未归类", en: "Unclassified" },
  footer: {
    zh: "Application Atlas · {n} 软件应用类型 · 由语料自动生成 · v1.1 方法论",
    en: "Application Atlas · {n} software application types · generated from the corpus · v1.1 methodology",
  },
  headerNote: { zh: "{n} 类型 · 数据来自 atlas 语料", en: "{n} types · data from the atlas corpus" },
  aliasesLabel: { zh: "别名", en: "Aliases" },
  drafts: { zh: "草稿", en: "Drafts" },
  draftsTitle: { zh: "草稿叶", en: "Draft Leaves" },
  draftsP: {
    zh: "新建类型的产房：草稿不进正式语料，可随时编辑；归类前必须通过查重。",
    en: "Nursery for new types: drafts stay out of the corpus, editable anytime; dedup is required before promotion.",
  },
  draftsEmpty: { zh: "暂无草稿", en: "No drafts yet" },
  draftNew: { zh: "新建叶", en: "New Leaf" },
  draftNameEn: { zh: "英文名（可不填，模型起名）", en: "Name in English (optional — model names it)" },
  draftNameZh: { zh: "中文名（可不填，模型生成）", en: "Name in Chinese (optional)" },
  draftDesc: { zh: "一句话想法（与链接二选一）", en: "One-line thesis (or a link, either one)" },
  draftDescPh: {
    zh: "例：单机命令行复式记账工具（ledger/hledger 一类：纯文本账本、无 GUI）",
    en: "e.g. single-machine CLI double-entry bookkeeping (ledger/hledger style: plain-text ledger, no GUI)",
  },
  draftLink: { zh: "调研起点链接（与想法二选一）", en: "Research starting link (or a thesis, either one)" },
  draftForce: { zh: "与语料高相似时仍强制创建", en: "Force create despite high similarity" },
  draftCreate: { zh: "创建（引擎生成完整叶子）", en: "Create (engine writes full leaf)" },
  draftCreating: { zh: "生成中…", en: "Generating…" },
  draftGenBanner: {
    zh: "引擎正在调研并撰写正文（约几分钟），以下信号实时刷新；生成期间可以离开页面。",
    en: "The engine is researching and writing the body (takes minutes); signals below update live. Safe to leave.",
  },
  genResearch: { zh: "调研笔记", en: "Research notes" },
  genBody: { zh: "正文已写", en: "Body so far" },
  genSection: { zh: "当前小节", en: "Writing" },
  genUpdated: { zh: "更新于", en: "updated" },
  genLog: { zh: "引擎最近动作", en: "Recent engine actions" },
  genNamedLabel: { zh: "调研定名", en: "Named after research" },
  genNamedHint: {
    zh: "草稿 id 仍是临时 wip-slug；入库时自动改为正式 slug。",
    en: "The draft id is still a temporary wip-slug; it becomes the formal slug on promotion.",
  },
  dupChip: {
    zh: "查重拦截 · 未成叶",
    en: "Dedupe stop · no leaf",
  },
  draftCreateHint: {
    zh: "想法和链接至少填一个；名称可全部留空由模型起名。创建后由写作引擎按语料方法论生成完整叶子（约几分钟），生成期间可关闭页面。",
    en: "Fill in a thesis or a link (at least one); names may be left blank for the model. A writing engine drafts the full leaf (takes minutes). Safe to leave the page.",
  },
  draftSaved: { zh: "已保存", en: "Saved" },
  draftSave: { zh: "保存", en: "Save" },
  draftDelete: { zh: "删除", en: "Delete" },
  draftDelConfirm: { zh: "删除这片草稿（正文+边界发现+日志）？", en: "Delete this draft (body + boundary findings + log)?" },
  draftDedupe: { zh: "查重", en: "Dedupe" },
  draftDeduped: { zh: "查重完成，已刷新", en: "Dedupe done, refreshed" },
  draftCollision: { zh: "语料最近邻（相似度）", en: "Nearest corpus neighbors (similarity)" },
  draftBody: { zh: "叶子正文", en: "Leaf body" },
  draftResearch: { zh: "边界发现 / Boundary Findings", en: "Boundary Findings" },
  draftResearchZh: { zh: "中文对照已生成", en: "Chinese preview available" },
  draftVerdict: { zh: "查重裁决（需人工确认）", en: "Dedup verdict (human confirms)" },
  draftNoVerdict: { zh: "尚未查重：点上方「查重」获取向量近邻与 LLM 裁决", en: "Not deduped yet: run dedupe above for vector neighbors + LLM verdict" },
  draftPromote: { zh: "确认归类入库", en: "Confirm & promote" },
  draftPromoting: { zh: "入库中…", en: "Promoting…" },
  draftPromoted: { zh: "已入库", en: "Promoted" },
  draftPromoteLocked: { zh: "正文检查未通过或当前状态不允许，修正正文后才能入库", en: "Content checks are not clean or the current status blocks promotion; fix the body first" },
  draftActionNew: { zh: "归入子域", en: "New leaf in sub-domain" },
  draftActionMerge: { zh: "并入现有叶（记别名）", en: "Merge into existing leaf (alias)" },
  draftPickSection: { zh: "选择子域…", en: "Pick a sub-domain…" },
  draftViewZh: { zh: "中文对照", en: "中文" },
  draftTranslate: { zh: "生成中文对照", en: "Generate Chinese preview" },
  draftTranslating: { zh: "翻译中，约一分钟后刷新页面查看", en: "Translating — refresh in about a minute" },
  settings: { zh: "设置", en: "Settings" },
  ask: { zh: "对话", en: "Ask" },
  askTitle: { zh: "对话 Atlas", en: "Ask Atlas" },
  askP: {
    zh: "用自然语言查询 Atlas 的类型知识。回答只用本页实际检索到的资料，并给出类型链接。",
    en: "Query Atlas type knowledge in natural language. Answers are grounded only in what this page actually retrieved, with links to the types used.",
  },
  askPlaceholder: { zh: "问点什么，例如：看板类和任务管理类有什么区别？", en: "Ask something, e.g. how do kanban and task management types differ?" },
  askSend: { zh: "提问", en: "Ask" },
  askSending: { zh: "提问中…", en: "Asking…" },
  askThinking: { zh: "正在检索并回答…", en: "Searching and answering…" },
  askNewThread: { zh: "新对话", en: "New conversation" },
  askThreads: { zh: "历史对话", en: "Conversations" },
  askNoThreads: { zh: "还没有对话。", en: "No conversations yet." },
  askEmpty: {
    zh: "从一个问题开始。Atlas 会先检索类型语料，再基于检索结果回答，并在末尾列出引用的类型。",
    en: "Start with a question. Atlas searches the type corpus first, answers from what it found, and lists the types it cited.",
  },
  askSteps: { zh: "检索过程", en: "Retrieval steps" },
  askStepsCount: { zh: "{n} 步", en: "{n} steps" },
  askCitations: { zh: "引用类型", en: "Cited types" },
  askUsage: { zh: "用量", en: "Usage" },
  askUsageTokens: { zh: "{n} tokens", en: "{n} tokens" },
  askUsageUnknown: { zh: "用量未知", en: "Usage unknown" },
  askDelete: { zh: "删除", en: "Delete" },
  askDeleteConfirm: { zh: "删除这段对话？", en: "Delete this conversation?" },
  askStatusTimeout: { zh: "超过时间上限，已停止（未完成的检索已丢弃）", en: "Stopped at the time limit (partial work discarded)" },
  askStatusTokenLimit: { zh: "超过 token 上限，已停止", en: "Stopped at the token limit" },
  askStatusTurnLimit: { zh: "超过检索步数上限，已停止", en: "Stopped at the step limit" },
  askStatusProviderError: { zh: "模型调用失败", en: "The model call failed" },
  askStatusNoAnswer: { zh: "没有得到回答", en: "No answer was produced" },
  askStatusFailed: { zh: "这次提问失败", en: "This question failed" },
  askNotConfigured: {
    zh: "还没有配置模型服务。先去「设置」配置一个可用的 provider，再回来提问。",
    en: "No model provider is configured. Add one in Settings, then come back to ask.",
  },
  askGoSettings: { zh: "去设置", en: "Open settings" },
  askReadOnlyNote: {
    zh: "本页只读：只能检索和阅读类型资料，不会修改语料、项目或文件。",
    en: "This page is read-only: it can search and read type material, and never modifies the corpus, projects, or files.",
  },
  askExample1: { zh: "看板类和任务管理类有什么区别？", en: "How do kanban and task management types differ?" },
  askExample2: { zh: "有哪些和电子表格相关的类型？", en: "Which types relate to spreadsheets?" },
  askExample3: { zh: "CRM 和销售管道管理是同一个类型吗？", en: "Are CRM and sales pipeline management the same type?" },
  askStepError: { zh: "失败", en: "failed" },
  settingsTitle: { zh: "设置", en: "Settings" },
  settingsP: {
    zh: "配置 Atlas 使用的模型服务。凭据只保存在本机，接口不会回传明文。",
    en: "Configure the model providers Atlas uses. Credentials stay on this machine and are never returned in plain text.",
  },
  settingsModel: { zh: "模型服务", en: "Model providers" },
  settingsModelP: {
    zh: "Atlas 的问答、分类、查重和文档生成都通过这里的默认服务调用。",
    en: "Atlas question answering, classification, dedupe, and document generation all use the default provider set here.",
  },
  settingsResolved: { zh: "当前生效", en: "Currently in effect" },
  settingsNotConfigured: { zh: "尚未配置", en: "Not configured" },
  settingsSourceConfig: { zh: "来自设置", en: "From settings" },
  settingsSourceEnv: { zh: "来自环境变量", en: "From environment" },
  settingsSourceOpencode: { zh: "来自 OpenCode 凭据", en: "From OpenCode credentials" },
  settingsImport: { zh: "从 OpenCode 导入凭据", en: "Import from OpenCode" },
  settingsImporting: { zh: "导入中…", en: "Importing…" },
  settingsImported: { zh: "已导入 {n} 个服务", en: "Imported {n} providers" },
  settingsImportedNone: { zh: "没有找到可导入的凭据", en: "No importable credentials found" },
  settingsAddProvider: { zh: "添加服务", en: "Add provider" },
  settingsEditProvider: { zh: "编辑服务", en: "Edit provider" },
  settingsProviders: { zh: "已配置服务", en: "Configured providers" },
  settingsProvidersEmpty: {
    zh: "还没有配置模型服务。可以从下方常用服务里选一个，或直接从 OpenCode 导入本机凭据。",
    en: "No providers yet. Pick one of the common providers below, or import this machine's OpenCode credentials.",
  },
  settingsPreset: { zh: "常用服务", en: "Provider" },
  settingsPresetCustom: { zh: "自定义（手动填写地址）", en: "Custom (enter a base URL)" },
  settingsName: { zh: "显示名称", en: "Display name" },
  settingsBaseUrl: { zh: "接口地址（base URL）", en: "Base URL" },
  settingsApiKey: { zh: "API Key", en: "API key" },
  settingsApiKeyKeep: {
    zh: "留空表示保留已保存的凭据",
    en: "Leave blank to keep the saved credential",
  },
  settingsApiKeyStored: { zh: "已保存：{masked}", en: "Saved: {masked}" },
  settingsModels: { zh: "模型（逗号或换行分隔）", en: "Models (comma or newline separated)" },
  settingsSave: { zh: "保存", en: "Save" },
  settingsSaving: { zh: "保存中…", en: "Saving…" },
  settingsSaved: { zh: "已保存", en: "Saved" },
  settingsCancel: { zh: "取消", en: "Cancel" },
  settingsDelete: { zh: "删除", en: "Delete" },
  settingsDeleteConfirm: {
    zh: "删除服务「{name}」及其保存的凭据？",
    en: "Delete provider \"{name}\" and its stored credential?",
  },
  settingsTest: { zh: "测试连接", en: "Test" },
  settingsTesting: { zh: "测试中…", en: "Testing…" },
  settingsTestOk: { zh: "连接正常 · {n} 个模型 · {ms}ms", en: "Connected · {n} models · {ms}ms" },
  settingsTestFail: { zh: "连接失败", en: "Connection failed" },
  settingsSetDefault: { zh: "设为默认", en: "Set default" },
  settingsDefault: { zh: "默认", en: "Default" },
  settingsDefaultProvider: { zh: "默认服务", en: "Default provider" },
  settingsDefaultModel: { zh: "默认模型", en: "Default model" },
  settingsNoKey: { zh: "未配置凭据", en: "No credential" },
  settingsEmbedding: { zh: "向量检索（Embedding）", en: "Embedding" },
  settingsEmbeddingP: {
    zh: "语义检索用。默认使用本机 Ollama 的 bge-m3。",
    en: "Used for semantic search. Defaults to bge-m3 on the local Ollama.",
  },
  settingsEmbeddingModel: { zh: "模型名", en: "Model" },
  settingsLoadFailed: { zh: "无法读取设置", en: "Could not load settings" },
  settingsMoreModels: { zh: "查看全部模型", en: "Load all models" },
  settingsLoadingModels: { zh: "读取中…", en: "Loading…" },
  settingsKeyHint: {
    zh: "凭据以 0600 权限保存在本机，不会出现在页面返回数据里。",
    en: "Credentials are stored locally with 0600 permissions and never appear in API responses.",
  },
} as const;

export function t(key: keyof typeof T, lang: Lang, vars?: Record<string, string | number>) {
  let s: string = T[key][lang] || T[key].zh;
  if (vars) for (const [k, v] of Object.entries(vars)) s = s.replace(`{${k}}`, String(v));
  return s;
}
