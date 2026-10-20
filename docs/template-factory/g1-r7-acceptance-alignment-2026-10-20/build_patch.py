"""Deterministic, host-prepared R7 deltas. Never writes original job material."""
from pathlib import Path
from copy import deepcopy
import difflib
import hashlib
import json

HERE = Path(__file__).resolve().parent
OLD = HERE.parent / 'g1-r6-source-alignment-2026-10-20/candidate-attempt-1-not-frozen'
OUT = HERE / 'prepared-programs'
patch = {'spec_changes': [], 'file_plan_changes': [], 'case_design_changes': [], 'program_changes': []}


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def replace_program(path, spans):
    before = (OLD / path).read_text()
    after = before
    for span in spans:
        assert after.count(span['old']) == 1, (path, span['old'][:80])
        after = after.replace(span['old'], span['new'], 1)
    dest = OUT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(after)
    patch['program_changes'].append({'path': path, 'mode': 'replace', 'patch': spans})
    (HERE / (Path(path).name + '.diff')).write_text(''.join(difflib.unified_diff(
        before.splitlines(True), after.splitlines(True), fromfile='R6/' + path, tofile='R7/' + path)))


JSON_POSITIVE = '''        # Independent JSON positive: not an HTML-created record read through JSON.
        before_json_ids = _record_ids(_fetch_bookmarks(client, recorder, 'a02-json-before-create'))
        json_boundary = f'https://atlas-a02-json-{token}/original?keep=1'
        positive = client.post_json('/api/bookmarks', {
            'url': json_boundary, 'title': f'A02 JSON {token}',
            'description': f'A02 JSON positive {token}',
        })
        recorder.expect_status(positive, 201, aid='a02-json-boundary-create-status')
        json_id = _record_id(_extract_record(_safe_json(positive)))
        recorder.check('a02-json-boundary-new-id', bool(json_id) and json_id not in before_json_ids,
                       f'独立 JSON POST 返回新的非空 id={json_id!r}')
        if json_id:
            saved = _get_record(client, recorder, json_id, 'a02-json-boundary')
            recorder.check('a02-json-boundary-readback',
                           _record_id(saved) == json_id and _record_url(saved) == json_boundary,
                           '独立 GET 读回同一 id 与精确原始 URL')
            listed_positive = _fetch_bookmarks(client, recorder, 'a02-json-positive')
            recorder.check('a02-json-boundary-listed', any(
                _record_id(item) == json_id and _record_url(item) == json_boundary
                for item in listed_positive), '列表包含同一 JSON 创建记录与原始 URL')
'''

library = (OLD / 'acceptance/p0_library.py').read_text()
old_a11 = library[library.index('def _case_a11('):library.index('\n\n_HANDLERS =')]
base_a11 = old_a11.replace('def _case_a11(', 'def _case_a11_base(').replace("'a11-", "'a11-base-")
new_a11 = '''def _case_a11(args, recorder):
    # The base deployment may already contain records. Only fresh proves first init.
    if not recorder.check('a11-fresh-required-flags', bool(args.app_root and args.data_dir),
                          'A11 必须绑定实际冻结 app_root 与测试者 data_dir'):
        return
    _case_a11_base(args, recorder)
    proc = None
    client = None
    try:
        proc = common.launch_app(args.app_root, args.data_dir, 0, fresh=True)
        recorder.check('a11-fresh-owned-source',
                       os.path.realpath(proc.app_root) == os.path.realpath(args.app_root),
                       'fresh 实例来自同一冻结交付源码')
        client = common.HttpClient(proc.base_url)
        health = client.get('/api/health')
        recorder.expect_status(health, 200, aid='a11-fresh-health-status')
        recorder.check('a11-fresh-health-json', isinstance(_safe_json(health), dict),
                       'fresh 健康检查返回 JSON 对象')
        # No business write precedes these unfiltered observations.
        for name, params in (('active', None), ('including-trash', {'include_trashed': '1'})):
            records = _fetch_bookmarks(client, recorder, f'a11-fresh-{name}', params)
            recorder.check(f'a11-fresh-{name}-empty', records == [],
                           f'未过滤全库 {name} 记录数={len(records)}，首次初始化必须为0')
        categories = _fetch_categories(client, recorder, 'a11-fresh')
        ids = []
        for index, preset in enumerate(common.PRESET_CATEGORIES, 1):
            matches = [item for item in categories if isinstance(item, dict) and item.get('name') == preset]
            recorder.check(f'a11-fresh-preset-{index}', len(matches) == 1,
                           f'首次初始化准确存在预置分类 {preset!r}')
            if len(matches) == 1:
                item = matches[0]
                cid = item.get('id')
                legal = isinstance(cid, (str, int)) and not isinstance(cid, bool) and bool(str(cid).strip())
                recorder.check(f'a11-fresh-preset-{index}-id', legal, f'分类 ID={cid!r}')
                recorder.check(f'a11-fresh-preset-{index}-count', item.get('count') == 0,
                               f'预置分类活动记录 count={item.get("count")!r}')
                ids.append(str(cid))
        recorder.check('a11-fresh-preset-unique-ids', len(ids) == 4 and len(set(ids)) == 4,
                       '四个预置分类 ID 各自唯一')
        page = client.get('/', accept='text/html')
        recorder.expect_status(page, 200, aid='a11-fresh-home-status')
        recorder.check('a11-fresh-home-content-type', 'text/html' in page.content_type.lower(),
                       '未过滤首页是 HTML')
        doc = _parse_html(page.text)
        form = doc.save_form()
        recorder.check('a11-fresh-save-form', form is not None and
                       _action_path(form.action) == '/bookmarks/new' and form.has_name('url'),
                       '未过滤首页具备保存表单与 URL 字段')
        recorder.check('a11-fresh-category-entry', any(
            a.testid == 'category-manager' and _action_path(a.href) == '/categories'
            for a in doc.anchors), '未过滤首页有分类管理入口')
        recorder.check('a11-fresh-list-container', _has_list_container(doc), '未过滤首页有列表容器')
        recorder.check('a11-fresh-no-record-rows', not doc.rows, '首次初始化未过滤首页没有记录行')
        recorder.check('a11-fresh-explicit-empty-state', bool(_empty_state_marker(doc)),
                       '首次初始化未过滤首页有明确空状态')
    finally:
        try:
            if client is not None:
                client.close()
        finally:
            if proc is not None:
                try:
                    common.stop_app(proc)
                except Exception as exc:
                    recorder.check('a11-fresh-cleanup', False, f'清理异常：{exc}')
                recorder.check('a11-fresh-process-stopped', proc.poll() is not None,
                               '本用例拥有的 fresh 子进程已结束')
'''
replace_program('acceptance/p0_library.py', [
    {'old': "        before = _fetch_bookmarks(client, recorder, 'a02-before')", 'new': JSON_POSITIVE + "        before = _fetch_bookmarks(client, recorder, 'a02-before')"},
    {'old': old_a11, 'new': base_a11 + '\n\n' + new_a11.rstrip()},
    {'old': '    args = common.parse_case_args(argv)\n    recorder = common.Recorder(args.case)',
     'new': '''    try:
        args = common.parse_case_args(argv)
    except SystemExit as exc:
        raw_args = list(sys.argv[1:] if argv is None else argv)
        requested_a11 = '--case=A11' in raw_args or any(
            value == '--case' and index + 1 < len(raw_args) and raw_args[index + 1] == 'A11'
            for index, value in enumerate(raw_args))
        if not exc.code or not requested_a11:
            raise
        failed = common.Recorder('A11')
        failed.check('a11-fresh-arguments', False, 'A11 参数无效；详见 stderr，不降级或跳过')
        return failed.finish('A11')
    recorder = common.Recorder(args.case)'''},
])

EXCLUSIONS = '''        # Tokens occur only in excluded fields of this target, never in allowed ones.
        for label, token_value in (('url-path', path_only), ('url-query', query_only), ('category-name', cat_a)):
            allowed_text = ' '.join((title_a, host_token + '.atlas-acceptance.example', desc_a)).lower()
            recorder.check(f'a07-{label}-isolated-token', token_value.lower() not in allowed_text,
                           '负例 token 不在目标记录 title/hostname/description')
            for scoped in (False, True):
                aid = f'a07-excludes-{label}-' + ('category' if scoped else 'all')
                params = {'q': token_value}
                if scoped:
                    params['category'] = cat_a
                results = _search(client, recorder, aid + '-json', params)
                recorder.check(aid + '-json-target-absent', id_a not in _record_ids(results),
                               'JSON 不因 URL path/query 或分类名而命中目标记录')
                html = _html_search(client, recorder, aid + '-html', search_form,
                                    cat_a if scoped else '', token_value)
                recorder.check(aid + '-html-target-absent', id_a not in _row_ids(html),
                               '实际搜索表单的记录行不因排除字段命中；不检查页面回显')
        # These positive controls also prove both entry points do not return always-empty.
        for label, positive_token in (('title', shared), ('hostname', host_token), ('description', desc_token)):
            positive_doc = _html_search(client, recorder, f'a07-html-positive-{label}',
                                        search_form, cat_a, positive_token.upper())
            recorder.check(f'a07-html-positive-{label}-hit', id_a in _row_ids(positive_doc),
                           '允许字段经真实 HTML 搜索表单仍命中同一记录')
'''
replace_program('acceptance/p0_find_open.py', [
    {'old': "        url_a = f'https://{host_token}.atlas-acceptance.example/notes/{uuid.uuid4().hex[:10]}'", 'new': "        path_only = f'pathonly{uuid.uuid4().hex[:12]}'\n        query_only = f'queryonly{uuid.uuid4().hex[:12]}'\n        url_a = f'https://{host_token}.atlas-acceptance.example/{path_only}?q={query_only}'"},
    {'old': "        doc_empty = _html_search(client, recorder, 'a07-html-empty', search_form, cat_a, unmatched)", 'new': EXCLUSIONS + "        doc_empty = _html_search(client, recorder, 'a07-html-empty', search_form, cat_a, unmatched)"},
])

runner = (OLD / 'acceptance/runner.json').read_text()
obj = json.loads(runner)
old_args = obj['cases']['A11']['args']
new_args = ['--case', '{case_id}', '--base-url', '{base_url}', '--app-root', '{app_root}', '--data-dir', '{data_dir}']
obj['cases']['A11']['args'] = new_args
# Only the A11 stanza is changed, preserving every other byte/order.
start = runner.index('"A11"')
end = runner.index(']', start) + 1
stanza = runner[start:end]
new_stanza = stanza[:-1].rstrip() + ',\n        "--app-root",\n        "{app_root}",\n        "--data-dir",\n        "{data_dir}"\n      ]'
assert json.loads(runner[:start] + new_stanza + runner[end:]) == obj
replace_program('acceptance/runner.json', [{'old': stanza, 'new': new_stanza}])

readme = (OLD / 'acceptance/README.md').read_text()
new_readme = readme.replace('| `--app-root` | A01、A05、A09 |', '| `--app-root` | A01、A05、A09、A11 |').replace('| `--data-dir` | A01、A05、A09、A14 |', '| `--data-dir` | A01、A05、A09、A11、A14 |')
new_readme = new_readme.replace('A01/A05/A09 还必须带', 'A01/A05/A09/A11 还必须带')
new_readme = new_readme.replace('| A11 | `p0_library.py` | ["--case","A11","--base-url","{base_url}"] |', '| A11 | `p0_library.py` | ["--case","A11","--base-url","{base_url}","--app-root","{app_root}","--data-dir","{data_dir}"] |')
new_readme = new_readme.replace('p0_library.py --case A11 --base-url "$BASE_URL"', 'p0_library.py --case A11 --base-url "$BASE_URL" --app-root "$APP_ROOT" --data-dir "$DATA_DIR"')
new_readme = new_readme.replace('同时保留 JSON API 的同等断言。', 'JSON API 保留已有非法名称、重复名称及默认分类保护断言；不宣称成功 JSON rename/delete 已覆盖。')
new_readme = new_readme.replace('单标签主机是接受策略，不要求点域名。', '另用独立唯一单标签 hostname URL 经 JSON POST 保存，断言 201、新 id、独立 GET/列表中同一 id 与原始 URL；非法输入的 before 快照在两条合法创建后取得。单标签主机是接受策略，不要求点域名。')
new_readme = new_readme.replace('category+q 叠加，无匹配返回 200 空数组。 |', 'category+q 叠加，无匹配返回 200 空数组；仅存在 URL path、URL query 或分类名的唯一 token 经 JSON 与实际 HTML 搜索表单查询不得命中目标记录，以 id/行集合判断而非页面回显，保留允许字段的正向控制。 |')
new_readme = new_readme.replace('用不存在的归类过滤得到明确空状态。 |', '用不存在的归类过滤得到明确空状态（a11-base-*，仅当前部署入口）。另必须使用同一冻结 app_root 与 data_dir 创建 fresh=True 的新隔离实例，业务写入前证明 health、未过滤全库含软删除均为空、四预置分类合法唯一 ID/count=0、未过滤首页表单/URL/分类入口/列表/明确空态且无记录行（a11-fresh-*）；finally 关闭 client 并停止拥有的进程、确认退出，缺参数/启动失败/清理失败不得通过。这不证明 base_url 被清空或同容器重启。 |')
new_readme += '\nA11 单独使用 common.launch_app(app_root, data_dir, 0, fresh=True)：每次新建 instances/<uuid>，不传旧 instance_dir、不删除已有数据；其首启证据属于 A11 自己，不借用 A01 receipt。实际 G1 必须绑定交付应用源码，准备 fixture 不能替代真实 P0。\n'
# Spans remain exact and reconstruct the full README from immutable R6 bytes.
replace_program('acceptance/README.md', [{'old': readme, 'new': new_readme}])

plan = json.loads((HERE / 'r6-plan.json').read_text())
effective = deepcopy(plan)
spec = effective['spec']


def spec_change(path, old, new):
    patch['spec_changes'].append({'path': path, 'old': deepcopy(old), 'new': deepcopy(new)})


for row in spec['features']:
    if row['id'] == 'F01':
        old = deepcopy(row['acceptance']); row['acceptance'].append('A12')
        spec_change(['features', 'F01', 'acceptance'], old, row['acceptance'])
for row in spec['acceptance']:
    if row['id'] == 'A12':
        old = deepcopy(row['features']); row['features'].insert(0, 'F01')
        spec_change(['acceptance', 'A12', 'features'], old, row['features'])
cov = spec['contract_coverage']
branches = cov['error_contract']['branches']
save_ids = [b['id'] for b in branches if b['operation'] == 'bookmark_save']
for branch in branches:
    if branch['id'] in save_ids:
        old = branch['feature_ids']; branch['feature_ids'] = ['F01', 'F10']
        spec_change(['contract_coverage', 'error_contract', 'branches', branch['id'], 'feature_ids'], old, branch['feature_ids'])
old_schema = cov['error_contract']['schema']
cov['error_contract']['schema'] = 'atlas.bookmark-error-contract.v2'
spec_change(['contract_coverage', 'error_contract', 'schema'], old_schema, cov['error_contract']['schema'])
for row in cov['features']:
    fid = row['feature_id']
    if fid == 'F01':
        old = deepcopy(row['acceptance_ids']); row['acceptance_ids'].append('A12')
        spec_change(['contract_coverage', 'features', fid, 'acceptance_ids'], old, row['acceptance_ids'])
    if fid in ('F01', 'F04'):
        old = deepcopy(row.get('error_branch_ids'))
        row['error_branch_ids'] = [b['id'] for b in branches if fid in b['feature_ids']]
        spec_change(['contract_coverage', 'features', fid, 'error_branch_ids'], old, row['error_branch_ids'])
    updates = {}
    if fid == 'F02':
        updates = {'recovery': '重试保存；仅首次初始化数据库时事务创建四个预置归类。后续启动保留已持久化的分类变更，不复活用户已删除或重命名的非默认分类；默认「未整理」仍遵守既有保护与初始化合同。', 'success_state': '记录的 category_id 为默认「未整理」，可在 /?category=未整理 看到；首次初始化时“未整理”“待购”“家居改造”“以后看看”均可见，之后显示真实持久化的用户分类状态。'}
    if fid == 'F11':
        updates = {'success_state': row['success_state'] + ' A11 自身区分 base_url 当前部署入口与绑定同一冻结 app_root 的 fresh 新实例，后者独立证明首启预置及未过滤真空库；不宣称 base_url 被清空或同容器重启。'}
    for key, value in updates.items():
        spec_change(['contract_coverage', 'features', fid, key], row[key], value); row[key] = value
old = spec['architecture_markdown']
new = old.replace('A01/A05/A09 另需 `--app-root` 与 `--data-dir`，A14 需 `--data-dir`。', 'A01/A05/A09 另需 `--app-root` 与 `--data-dir` 做既有重启检查；A11 也必需二者，用同一冻结源码的 fresh 新实例独立证明首次初始化/未过滤空库，base_url 只观察当前部署入口，两组在 A11 输出中区分；A14 仍仅需 `--data-dir`。A11 不属于同容器重启证明。')
assert new != old
spec_change(['architecture_markdown'], old, new); spec['architecture_markdown'] = new

for row in effective['file_plan']:
    old = deepcopy(row)
    row['reuse'] = row['path'] not in {r['path'] for r in patch['program_changes']}
    if row['path'] == 'acceptance/p0_library.py':
        row['purpose'] += ' R7：A02 新增独立 JSON POST 单标签 hostname 的201/新id/GET与列表精确读回，保留HTML正向及双入口负向；A11 必需 --app-root/--data-dir，base当前入口与同冻结源码fresh新实例首启/全库含软删为空/四预置count0分别断言，finally确认进程退出。A01/A03不变。'
    elif row['path'] == 'acceptance/p0_find_open.py':
        row['purpose'] += ' R7：A07 增加只在URL path/query或分类名的唯一token，JSON与真实HTML搜索表单均按记录ID排除，并保留允许字段正向控制；A08原断言不变。'
    elif row['path'] == 'acceptance/p0_organize.py':
        row['purpose'] = row['purpose'].replace('同时保留 JSON API 的同等断言。', 'JSON API 保留已有非法名称、重复名称及默认分类保护断言，不宣称成功 JSON rename/delete 已覆盖。')
    elif row['path'] == 'acceptance/README.md':
        row['purpose'] += ' R7说明A02双入口正向、A07排除字段与正负控制、A11必需app_root/data_dir及两组观察/进程清理；修正A04 JSON覆盖描述，保留未运行和网络/浏览器证据边界。'
    elif row['path'] == 'acceptance/runner.json':
        row['purpose'] = row['purpose'].replace('保持固定字节不变且位于最后', '仅增加A11的app_root/data_dir绑定且位于最后').replace('A01、A05、A09 绑定', 'A01、A05、A09、A11 绑定').replace('A10–A13', 'A10、A12–A13')
    if old != row:
        patch['file_plan_changes'].append({'path': row['path'], 'old': old, 'new': deepcopy(row)})

choices = json.loads((HERE / 'r6-choices.json').read_text())
new_choices = deepcopy(choices)
auth = (HERE / 'authorization/ATLAS_G1_R7_ACCEPTANCE_ALIGNMENT_CODEX_INSTRUCTIONS.txt').read_text()
for prefix, label in [('F11:', 'F11'), ('A deliberate save', 'record lifecycle')]:
    row = next(c for c in new_choices if c['capability'].startswith(prefix))
    identity = row['capability']
    for field in ('capability', 'reason'):
        marker = f'{label} {field} 替换为：\n'
        value = auth.split(marker, 1)[1].split('\n\n', 1)[0].strip()
        patch['case_design_changes'].append({'choice_id': identity, 'path': [field], 'old': row[field], 'new': value})
        row[field] = value

write_json(HERE / 'patch.json', patch)
write_json(HERE / 'effective-plan-preview.json', effective)
write_json(HERE / 'effective-choices-preview.json', new_choices)
for path in [r['path'] for r in plan['file_plan'] if r['path'] not in {c['path'] for c in patch['program_changes']}]:
    target = OUT / path; target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes((OLD / path).read_bytes())
print('prepared four byte replacements, five exact reuses; spec deltas', len(patch['spec_changes']))
