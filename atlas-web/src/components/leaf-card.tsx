import { Link } from "react-router-dom";
import type { SectionData } from "@/lib/atlas";
import { stripMd } from "@/lib/utils";
import { useLang } from "@/lib/lang";

export function LeafCard({ leaf }: { leaf: SectionData["leaves"][number] & { l0_zh?: string; dc_zh?: string } }) {
  const { lang } = useLang();
  return (
    <Link
      to={`/types/${leaf.slug}`}
      className="block rounded-lg bg-surface p-4 shadow-card transition-shadow hover:shadow-card-hover"
    >
      <div className="flex items-baseline gap-2">
        <h3 className="text-[15px] font-medium leading-snug">{lang === "zh" ? (leaf.name_zh || leaf.name) : leaf.name}</h3>
        {lang === "zh" && leaf.name_zh && leaf.name_zh !== leaf.name ? (
          <span className="truncate text-xs text-subtle">{leaf.name}</span>
        ) : null}
      </div>
      {leaf.l0 ? <p className="mt-1.5 line-clamp-2 text-[13px] leading-relaxed text-muted">{stripMd(lang === "zh" ? leaf.l0_zh || leaf.l0 : leaf.l0)}</p> : null}
    </Link>
  );
}
