import { useEffect, useState } from "react";

const CURRENT_PROJECT = "atlas-current-project";
const CHANGE_EVENT = "atlas-current-project-change";

export function getCurrentProjectId() {
  return localStorage.getItem(CURRENT_PROJECT) || "";
}

export function setCurrentProjectId(projectId: string) {
  if (projectId) localStorage.setItem(CURRENT_PROJECT, projectId);
  else localStorage.removeItem(CURRENT_PROJECT);
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
