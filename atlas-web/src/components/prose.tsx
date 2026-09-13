import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { cn } from "@/lib/utils";

export function Prose({ md, className }: { md: string; className?: string }) {
  return (
    <div
      className={cn(
        "prose prose-sm max-w-none text-ink-soft",
        "[&_h1,_h2,_h3,_h4]:font-serif [&_h1,_h2,_h3,_h4]:text-fg",
        "[&_h3]:text-[15px] [&_h4]:text-sm",
        "[&_a]:text-primary [&_a]:underline [&_a]:underline-offset-2",
        "[&_code]:rounded [&_code]:bg-chip [&_code]:px-1 [&_code]:text-[0.85em] [&_code]:text-ink-soft",
        "[&_pre]:bg-bg-elevated [&_pre]:text-fg [&_pre]:shadow-card [&_pre]:rounded-lg",
        "[&_pre_code]:bg-transparent [&_pre_code]:p-0 [&_pre_code]:text-fg",
        "[&_strong]:font-semibold [&_strong]:text-fg",
        "[&_li]:my-1 [&_ul]:my-2 [&_ol]:my-2",
        "[&_blockquote]:border-l-primary [&_blockquote]:font-normal [&_blockquote]:not-italic",
        "[&_table]:text-[13px] [&_th]:bg-chip",
        className,
      )}
    >
      <ReactMarkdown remarkPlugins={[remarkGfm]}>{md}</ReactMarkdown>
    </div>
  );
}
