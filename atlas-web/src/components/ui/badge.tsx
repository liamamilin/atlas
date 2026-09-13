import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@/lib/utils";

const badgeVariants = cva(
  "inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium tracking-wide",
  {
    variants: {
      tone: {
        default: "bg-chip text-ink-soft",
        primary: "bg-primary text-primary-fg",
        ok: "bg-ok/12 text-ok",
        warn: "bg-warn/12 text-warn",
        danger: "bg-danger/12 text-danger",
        outline: "shadow-card bg-surface text-muted",
      },
    },
    defaultVariants: { tone: "default" },
  },
);

export function Badge({
  className,
  tone,
  ...props
}: React.HTMLAttributes<HTMLSpanElement> & VariantProps<typeof badgeVariants>) {
  return <span className={cn(badgeVariants({ tone }), className)} {...props} />;
}
