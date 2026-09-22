import { useMemo } from "react";
import tutorialMd from "../../../TUTORIAL.md?raw";
import { Prose } from "@/components/prose";
import { useLang, t } from "@/lib/lang";

/**
 * The tutorial is authored as repo Markdown. Relative links such as `README.md`
 * have no route in the web app, so render the path as inline code instead.
 */
function forWeb(md: string) {
  return md
    .replace(/^# .*\n/, "")
    .replace(/\[([^\]]+)\]\((?!https?:\/\/|#|mailto:)([^)]+)\)/g, (_match, _label, href: string) => `\`${href}\``);
}

export function Tutorial() {
  const { lang } = useLang();
  const md = useMemo(() => forWeb(tutorialMd), []);
  return (
    <main className="mx-auto max-w-3xl px-4 py-10">
      <h1 className="font-serif text-3xl font-medium">{t("tutorial", lang)}</h1>
      <div className="mt-8">
        <Prose md={md} />
      </div>
    </main>
  );
}
