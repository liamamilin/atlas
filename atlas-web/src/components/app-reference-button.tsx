import { useState } from "react";
import { BookmarkPlus, CheckCircle2 } from "lucide-react";
import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { saveProjectReference } from "@/lib/atlas";
import { useLang } from "@/lib/lang";
import { useCurrentProjectId } from "@/lib/project-selection";

export function AppReferenceButton({ slug }: { slug: string }) {
  const { lang } = useLang();
  const [projectId] = useCurrentProjectId();
  const [saving, setSaving] = useState(false);
  const [state, setState] = useState<{ saved: boolean; message: string } | null>(null);

  if (!projectId) {
    return (
      <Link to="/projects" className="text-xs text-primary hover:underline">
        {lang === "zh" ? "选择项目后收藏" : "Select a project to save"}
      </Link>
    );
  }

  const collect = async () => {
    setSaving(true);
    setState(null);
    try {
      await saveProjectReference(projectId, { kind: "app", slug, read_status: "read" });
      setState({ saved: true, message: lang === "zh" ? "已收藏目录资料" : "Catalog record saved" });
    } catch (cause) {
      if (String(cause).includes("already saved")) {
        setState({ saved: true, message: lang === "zh" ? "已收藏此版本" : "This version is already saved" });
      } else {
        setState({ saved: false, message: String(cause) });
      }
    } finally {
      setSaving(false);
    }
  };

  if (state?.saved) {
    return <span className="flex items-center gap-1 text-xs text-ok"><CheckCircle2 className="size-3.5" />{state.message}</span>;
  }
  return (
    <div>
      <Button size="sm" variant="outline" onClick={collect} disabled={saving}>
        <BookmarkPlus className="size-3.5" />
        {saving ? (lang === "zh" ? "收藏中…" : "Saving…") : (lang === "zh" ? "收藏目录资料" : "Save catalog record")}
      </Button>
      {state ? <p className="mt-1 max-w-64 text-xs text-danger">{state.message}</p> : null}
    </div>
  );
}
