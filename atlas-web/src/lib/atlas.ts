const cache = new Map<string, Promise<unknown>>();

export function fetchJson<T>(url: string): Promise<T> {
  let p = cache.get(url);
  if (!p) {
    p = fetch(url).then((r) => {
      if (!r.ok) throw new Error(`${r.status} ${url}`);
      return r.json() as Promise<T>;
    });
    cache.set(url, p);
  }
  return p as Promise<T>;
}

export interface LeafIndexItem {
  slug: string;
  name: string;
  name_zh: string;
  sec: string;
  dc: string;
  dc_zh?: string;
}

export interface SubSection {
  id: string;
  name: string;
  name_zh?: string;
  path: string;
}

export interface L0 {
  id: string;
  name: string;
  name_zh?: string;
  subs: SubSection[];
}

export interface Meta {
  leafCount: number;
  sectionCount: number;
  l0Count: number;
  appCount: number;
  l0s: L0s[];
  leafIndex: LeafIndexItem[];
}
type L0s = L0;

export interface SectionData {
  id: string;
  name: string;
  name_zh?: string;
  path: string;
  leaves: { slug: string; name: string; name_zh: string; l0: string; l0_zh?: string }[];
}

export interface LeafDetail {
  slug: string;
  name: string;
  name_zh: string;
  aliases_zh: string[];
  section_id: string;
  section_name: string;
  section_name_zh?: string;
  overview: string;
  overview_zh?: string;
  dc: string;
  dc_zh?: string;
  how: string;
  how_zh?: string;
  rules: string;
  rules_zh?: string;
  variants: string;
  variants_zh?: string;
  products: string;
  products_zh?: string;
  relations: { to: string; toName: string; kind: string; distinction: string; distinction_zh?: string }[];
  apps: { slug: string; name: string }[];
}

export interface AppEntry {
  slug: string;
  name: string;
  vendor: string;
  tagline: string;
  tasks: string[];
  leaf: string;
  leafName: string;
}

export const REL_KIND_ZH: Record<string, string> = {
  adjacent: "相邻",
  related: "相关",
  sibling: "同类",
  other: "其他",
  upstream: "上游",
  downstream: "下游",
  overlaps: "交叠",
  contrasts: "对照",
  variant_of: "变体",
  capability_of: "内嵌能力",
  component_of: "组件",
  parent_of: "父类",
  child_of: "子类",
  specializes: "特化",
  generalizes: "泛化",
  enabled_by: "依托",
};

export async function getMeta() {
  return fetchJson<Meta>("/data/meta.json");
}
export async function getSection(id: string) {
  return fetchJson<SectionData>(`/data/sections/${id}.json`);
}
export async function getLeaf(slug: string) {
  return fetchJson<LeafDetail>(`/data/leaves/${slug}.json`);
}
export async function getApps() {
  return fetchJson<AppEntry[]>("/data/apps.json");
}
