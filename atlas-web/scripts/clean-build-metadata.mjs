import { readdir, unlink } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const webRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const roots = [path.join(webRoot, "public"), path.join(webRoot, "dist")];

async function removeFinderMetadata(directory) {
  let entries;
  try {
    entries = await readdir(directory, { withFileTypes: true });
  } catch (error) {
    if (error?.code === "ENOENT") return;
    throw error;
  }
  for (const entry of entries) {
    const entryPath = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      await removeFinderMetadata(entryPath);
    } else if (entry.isFile() && entry.name === ".DS_Store") {
      await unlink(entryPath);
    }
  }
}

for (const root of roots) {
  await removeFinderMetadata(root);
}
