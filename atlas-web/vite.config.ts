import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import { fileURLToPath, URL } from "node:url";

const webRoot = fileURLToPath(new URL(".", import.meta.url));
const tutorialPath = fileURLToPath(new URL("../TUTORIAL.md", import.meta.url));
const apiProxy = { "/api": process.env.ATLAS_API_TARGET || "http://127.0.0.1:5199" };

export default defineConfig({
  plugins: [tailwindcss(), react()],
  resolve: {
    alias: { "@": fileURLToPath(new URL("./src", import.meta.url)) },
  },
  server: {
    // Only the parent tutorial file is intentionally exposed to Vite's dev server.
    fs: { allow: [webRoot, tutorialPath] },
    proxy: apiProxy,
  },
  preview: {
    proxy: apiProxy,
  },
});
