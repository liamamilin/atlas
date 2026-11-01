import { useEffect, useState } from "react";

const CURRENT_PROJECT = "atlas-current-project";
const CHANGE_EVENT = "atlas-current-project-change";
let sessionProjectId: string | null = null;

export function getCurrentProjectId() {
  if (sessionProjectId !== null) return sessionProjectId;
  try { return localStorage.getItem(CURRENT_PROJECT) || ""; }
  catch { return ""; }
}

export function setCurrentProjectId(projectId: string) {
  sessionProjectId = projectId;
  try {
    if (projectId) localStorage.setItem(CURRENT_PROJECT, projectId);
    else localStorage.removeItem(CURRENT_PROJECT);
    sessionProjectId = null;
  } catch { /* Keep project selection usable for this session. */ }
  window.dispatchEvent(new CustomEvent(CHANGE_EVENT, { detail: projectId }));
}

export function useCurrentProjectId() {
  const [projectId, setProjectId] = useState(getCurrentProjectId);
  useEffect(() => {
    const sync = () => setProjectId(getCurrentProjectId());
    window.addEventListener("storage", sync);
    window.addEventListener(CHANGE_EVENT, sync);
    return () => {
      window.removeEventListener("storage", sync);
      window.removeEventListener(CHANGE_EVENT, sync);
    };
  }, []);
  return [projectId, setCurrentProjectId] as const;
}
