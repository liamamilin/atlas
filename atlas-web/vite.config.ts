import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import { fileURLToPath, URL } from "node:url";

export default defineConfig({
  plugins: [tailwindcss(), react()],
  resolve: {
    alias: { "@": fileURLToPath(new URL("./src", import.meta.url)) },
  },
  server: {
    // TUTORIAL.md lives one level above the atlas-web root and is imported with `?raw`.
    fs: { allow: [".."] },
    proxy: {
      "/api": process.env.ATLAS_API_TARGET || "http://localhost:5199",
    },
  },
});
