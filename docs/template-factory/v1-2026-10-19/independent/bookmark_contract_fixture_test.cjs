// Synthetic malformed-product snapshots for bookmark acceptance helper logic.
// These are regression fixtures only, never downstream app evidence.
const assert = require('node:assert/strict');
const checks = require('./bookmark_contract_checks.cjs');

const target = { id: 'target-1', title: 'Acceptance token-1', url: 'http://fixture/original', category: 'Destination' };
const categoryControl = { id: 'control-1', title: 'Cross-category token-1 control', url: 'http://fixture/second', category: 'Control' };
const keywordControl = { id: 'keyword-control-1', title: 'Unrelated keyword control', url: 'http://fixture/keyword', category: 'Destination' };

assert.equal(checks.rootUrl('http://127.0.0.1:8000/', { category: 'a b', q: 'x' }),
  'http://127.0.0.1:8000/?category=a+b&q=x');
assert.equal(checks.rootUrl('http://127.0.0.1:8000', { category: 'a b', q: 'x' }),
  'http://127.0.0.1:8000/?category=a+b&q=x');

checks.assertMoveState({ record: target, recordId: target.id, newCategory: 'Destination',
  oldCategoryRows: [], newCategoryRows: [target] });
assert.throws(() => checks.assertMoveState({ record: { ...target, category: '待购' }, recordId: target.id,
  newCategory: 'Destination', oldCategoryRows: [target], newCategoryRows: [target] }), /no-op|filters/);

checks.assertFindState({ recordId: target.id, categoryControlId: categoryControl.id, keywordControlId: keywordControl.id,
  byCategory: [target, keywordControl], byCombined: [target], byKeyword: [target, categoryControl], keywordMiss: [] });
// A query-only implementation must fail: the same-keyword control is in another category.
assert.throws(() => checks.assertFindState({ recordId: target.id, categoryControlId: categoryControl.id, keywordControlId: keywordControl.id,
  byCategory: [target, keywordControl], byCombined: [target, categoryControl], byKeyword: [target, categoryControl], keywordMiss: [] }), /filters/);
assert.throws(() => checks.assertFindState({ recordId: target.id, categoryControlId: categoryControl.id, keywordControlId: keywordControl.id,
  byCategory: [target, categoryControl, keywordControl], byCombined: [target], byKeyword: [target], keywordMiss: [] }), /filters/);
assert.throws(() => checks.assertFindState({ recordId: target.id, categoryControlId: categoryControl.id, keywordControlId: keywordControl.id,
  byCategory: [target, keywordControl], byCombined: [target, keywordControl], byKeyword: [target], keywordMiss: [] }), /filters/);
assert.throws(() => checks.assertFindState({ recordId: target.id, categoryControlId: categoryControl.id, keywordControlId: keywordControl.id,
  byCategory: [target, keywordControl], byCombined: [target], byKeyword: [target], keywordMiss: [target] }), /filters/);

checks.assertExactRecord(target, target);
assert.throws(() => checks.assertExactRecord({ ...target, url: 'http://fixture/changed' }, target), /differs/);
assert.throws(() => checks.assertExactRecord({ ...target, category: '待购' }, target), /category/);
const ack = { id: 'ack-1', title: 'parallel-1', url: 'https://parallel-1.example/' };
checks.assertAcknowledgedRecords([ack], [ack]);
assert.throws(() => checks.assertAcknowledgedRecords([], [ack]), /absent/);
assert.throws(() => checks.assertAcknowledgedRecords([{ ...ack, id: 'different-id' }], [ack]), /changed/);
assert.throws(() => checks.assertAcknowledgedRecords([ack], [ack, { id: 'ack-2', title: 'parallel-2', url: 'https://parallel-2.example/' }]), /ack-2/);

console.log('synthetic move/filter/persistence/concurrency and slash-normalization fixtures passed');
