// Pure assertion helpers shared by the real adapter and synthetic regression fixtures.
function hasId(rows, id) {
  return rows.some(row => row && String(row.id) === String(id));
}

function assertMoveState({ record, recordId, newCategory, oldCategoryRows, newCategoryRows }) {
  const category = record && (record.category ?? record.category_name);
  const name = typeof category === 'string' ? category : category && category.name;
  if (name !== newCategory || !hasId(newCategoryRows, recordId) || hasId(oldCategoryRows, recordId)) {
    throw new Error('move was a no-op or category filters did not reflect the move');
  }
}

function assertFindState({ recordId, categoryControlId, keywordControlId, byCategory, byCombined, byKeyword, keywordMiss }) {
  if (!hasId(byCategory, recordId) || hasId(byCategory, categoryControlId)
      || !hasId(byCombined, recordId) || hasId(byCombined, categoryControlId) || hasId(byCombined, keywordControlId)
      || !hasId(byKeyword, recordId) || !hasId(byKeyword, categoryControlId) || hasId(byKeyword, keywordControlId)
      || hasId(keywordMiss, recordId)) {
    throw new Error('category or keyword filters failed to distinguish target from control/nonmatching rows');
  }
}

function assertExactRecord(record, expected) {
  if (!record || String(record.id) !== String(expected.id) || record.title !== expected.title
      || record.url !== expected.url) {
    throw new Error('record identity, title, or URL differs from the acknowledged record');
  }
  const category = record.category ?? record.category_name;
  const categoryName = typeof category === 'string' ? category : category && category.name;
  if (expected.category !== undefined && categoryName !== expected.category) {
    throw new Error('record category differs from the acknowledged category');
  }
}

function assertAcknowledgedRecords(records, acknowledgements) {
  for (const acknowledged of acknowledgements) {
    const exact = records.filter(record => record && record.title === acknowledged.title && record.url === acknowledged.url);
    if (exact.length !== 1 || String(exact[0].id) !== String(acknowledged.id)) {
      throw new Error(`acknowledged record ${acknowledged.id} is absent, duplicated, or changed`);
    }
  }
}

function rootUrl(appUrl, search = {}) {
  const url = new URL('/', appUrl);
  for (const [key, value] of Object.entries(search)) url.searchParams.set(key, value);
  return url.toString();
}

module.exports = { assertMoveState, assertFindState, assertExactRecord, assertAcknowledgedRecords, rootUrl };
