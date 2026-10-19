// Atlas-authored reference. No third-party source is copied.
export function normalizeBookmarkUrl(value) {
  if (typeof value !== 'string') throw new Error('validation');
  let url;
  try { url = new URL(value.trim()); } catch { throw new Error('validation'); }
  if (!['http:', 'https:'].includes(url.protocol) || !url.hostname || url.username || url.password) throw new Error('validation');
  return url.href;
}
