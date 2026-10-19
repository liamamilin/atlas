import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import App, { RouteErrorPage } from "./app";
import { LangProvider } from "@/lib/lang";
import "./styles.css";

const router = createBrowserRouter([{
  path: "*",
  element: <App />,
  errorElement: <RouteErrorPage />,
}]);

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <LangProvider>
      <RouterProvider router={router} />
    </LangProvider>
  </StrictMode>,
);
