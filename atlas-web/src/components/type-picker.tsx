import { useEffect, useId, useMemo, useRef, useState } from "react";
import { X } from "lucide-react";
import { useLang } from "@/lib/lang";

export type TypeOption = { slug: string; name: string; count: number };

const LIMIT = 50;

// Exact slug or name first, then names that start with the keyword.
function rank(item: TypeOption, keyword: string) {
  const name = item.name.toLowerCase();
  return item.slug === keyword || name === keyword ? 0 : name.startsWith(keyword) ? 1 : 2;
}

/** Searchable type filter: the taxonomy has ~1,800 types, too many for a native select. */
export function TypePicker({ options, value, onChange }: { options: TypeOption[]; value: string; onChange: (slug: string) => void }) {
  const { lang } = useLang(); const zh = lang === "zh";
  const id = useId();
  const listId = `${id}-list`;
  const selected = options.find(item => item.slug === value);
  const [text, setText] = useState("");
  const [open, setOpen] = useState(false);
  const [active, setActive] = useState(0);
  const root = useRef<HTMLDivElement>(null);
  const input = useRef<HTMLInputElement>(null);
  const label = selected ? selected.name : value;
  useEffect(() => { if (!open) setText(""); }, [open, value]);
  useEffect(() => {
    if (!open) return;
    const close = (event: PointerEvent) => { if (!root.current?.contains(event.target as Node)) setOpen(false); };
    document.addEventListener("pointerdown", close);
    return () => document.removeEventListener("pointerdown", close);
  }, [open]);
  const matches = useMemo(() => {
    const keyword = text.trim().toLowerCase();
    const found = keyword
      ? options.filter(item => item.name.toLowerCase().includes(keyword) || item.slug.includes(keyword))
        .sort((a, b) => rank(a, keyword) - rank(b, keyword) || b.count - a.count)
      : [...options].sort((a, b) => b.count - a.count);
    return found.slice(0, LIMIT);
  }, [options, text]);
  useEffect(() => setActive(0), [text]);
  function choose(slug: string) {
    onChange(slug); setOpen(false); input.current?.blur();
  }
  return <div ref={root} className="relative mt-1">
    <input ref={input} role="combobox" aria-expanded={open} aria-controls={listId} aria-autocomplete="list"
      aria-activedescendant={open && matches[active] ? `${id}-${matches[active].slug}` : undefined}
      aria-label={zh ? "软件类型" : "Type"}
      className="block h-11 w-full rounded-lg border border-border bg-surface px-3 pr-9 text-sm text-fg placeholder:text-fg"
      value={open ? text : ""} placeholder={open ? (zh ? "输入名称筛选类型" : "Filter types by name") : label || (zh ? "全部类型" : "All types")}
      onFocus={() => setOpen(true)} onChange={e => { setText(e.target.value); setOpen(true); }}
      onKeyDown={e => {
        if (e.key === "ArrowDown") { e.preventDefault(); setOpen(true); setActive(i => Math.min(i + 1, matches.length - 1)); }
        else if (e.key === "ArrowUp") { e.preventDefault(); setActive(i => Math.max(i - 1, 0)); }
        else if (e.key === "Enter" && open) { e.preventDefault(); if (matches[active]) choose(matches[active].slug); }
        else if (e.key === "Escape") { setOpen(false); input.current?.blur(); }
      }} />
    {value && !open && <button type="button" aria-label={zh ? "清除类型筛选" : "Clear type filter"} className="absolute right-1 top-1/2 flex size-9 -translate-y-1/2 items-center justify-center rounded-md text-muted hover:text-primary" onClick={() => choose("")}><X className="size-4" /></button>}
    {open && <ul id={listId} role="listbox" aria-label={zh ? "软件类型" : "Types"} className="absolute z-20 mt-1 max-h-80 w-full min-w-64 overflow-y-auto rounded-lg border border-border bg-surface py-1 text-sm shadow-lg">
      {!text && <li id={`${id}-all`} role="option" aria-selected={!value} className="cursor-pointer px-3 py-2 text-muted hover:bg-chip" onPointerDown={e => e.preventDefault()} onClick={() => choose("")}>{zh ? "全部类型" : "All types"}</li>}
      {matches.map((item, index) => <li key={item.slug} id={`${id}-${item.slug}`} role="option" aria-selected={item.slug === value}
        className={`flex cursor-pointer items-baseline justify-between gap-3 px-3 py-2 ${index === active ? "bg-chip" : ""} ${item.slug === value ? "font-medium text-primary" : ""}`}
        onPointerDown={e => e.preventDefault()} onMouseEnter={() => setActive(index)} onClick={() => choose(item.slug)}>
        <span className="min-w-0 truncate">{item.name}</span><span className="shrink-0 text-xs tabular-nums text-subtle">{item.count}</span>
      </li>)}
      {!matches.length && <li className="px-3 py-2 text-muted">{zh ? "没有匹配的类型" : "No matching types"}</li>}
      {!text && options.length > LIMIT && <li className="px-3 py-2 text-xs text-subtle">{zh ? `按项目数显示前 ${LIMIT} 个，输入名称查找全部 ${options.length} 个类型` : `Top ${LIMIT} by projects; type to search all ${options.length}`}</li>}
    </ul>}
  </div>;
}
