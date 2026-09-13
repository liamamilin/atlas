import { Routes, Route, useParams } from "react-router-dom";
import { AppShell } from "@/components/app-shell";
import { Home } from "@/routes/home";
import { Browse } from "@/routes/browse";
import { Leaf } from "@/routes/leaf";
import { Search } from "@/routes/search";
import { Apps } from "@/routes/apps";
import { Drafts, DraftDetailPage } from "@/routes/drafts";
import { Projects } from "@/routes/projects";
import { ProjectDetail } from "@/routes/project-detail";

export default function App() {
  return (
    <Routes>
      <Route element={<AppShell />}>
        <Route path="/" element={<Home />} />
        <Route path="/browse" element={<Browse />} />
        <Route path="/types/:slug" element={<Leaf />} />
        <Route path="/search" element={<Search />} />
        <Route path="/apps" element={<Apps />} />
        <Route path="/drafts" element={<Drafts />} />
        <Route path="/drafts/:slug" element={<DraftDetailRoute />} />
        <Route path="/projects" element={<Projects />} />
        <Route path="/projects/:projectId" element={<ProjectDetail />} />
        <Route path="*" element={<Home />} />
      </Route>
    </Routes>
  );
}

function DraftDetailRoute() {
  const { slug } = useParams();
  return slug ? <DraftDetailPage slug={slug} /> : <Home />;
}
