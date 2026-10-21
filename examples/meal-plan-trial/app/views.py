"""Explicit Chinese HTML forms; all user values pass through h()."""
from datetime import timedelta, date
from urllib.parse import urlencode
from web_support import h, options, page, Error
from store import week, date_range, iso_date, quantity_text

MESSAGES = {'recipe':'菜谱已保存，可以安排晚餐了。','plan':'晚餐已安排，已切换到该日期所在周。',
            'update':'用餐人数已保存，采购清单已重新计算。','toggle':'计划状态已更新，采购清单已重新计算。'}


def render(store, query, values=None, error=None, route=''):
    values = values or {}
    raw_start, raw_end = query.get('start'), query.get('end')
    try:
        start, end = date_range(raw_start, raw_end)
    except Error as range_error:
        start, end = week()
        error = error or range_error
    state = store.state(start,end)
    def hidden():
        return f'<input type="hidden" name="start" value="{h(start)}"><input type="hidden" name="end" value="{h(end)}">'
    def val(key, default=''):
        return h(values.get(key, default))
    def nav(offset):
        return '/?' + urlencode({'start':(iso_date(start)+timedelta(days=offset)).isoformat(),
                                'end':(iso_date(end)+timedelta(days=offset)).isoformat()})
    notice = (f'<div class="notice error" role="alert"><strong>未保存：</strong>{h(error.message)} <span class="muted">输入已保留，请检查后重试。</span></div>' if error else
              f'<div class="notice" role="status">{h(MESSAGES[query["saved"]])}</div>' if query.get('saved') in MESSAGES else '')
    range_form = f'''<section class="panel"><div class="row"><h2>查看 7 天内的晚餐</h2><a href="/">回到本周</a></div>
    <form method="get" action="/" class="inline"><div class="field"><label for="start">开始日期</label><input id="start" name="start" type="date" value="{h(raw_start if raw_start is not None else start)}" required></div>
    <div class="field"><label for="end">结束日期</label><input id="end" name="end" type="date" value="{h(raw_end if raw_end is not None else end)}" required></div><button type="submit">查看计划</button></form>
    <div class="row" style="margin-top:14px"><a href="{h(nav(-7))}">← 前 7 天</a><span class="muted">范围包含起止日期，最多 7 天</span><a href="{h(nav(7))}">后 7 天 →</a></div></section>'''
    rows = []
    by_date = {p['date']:p for p in state['plans']}
    for offset in range((iso_date(end)-iso_date(start)).days+1):
        day = iso_date(start)+timedelta(days=offset)
        p = by_date.get(day.isoformat())
        day_label = f'{h(day.isoformat())}<br><span class="muted">周{["一","二","三","四","五","六","日"][day.weekday()]}</span>'
        if not p:
            rows.append(f'<tr><td>{day_label}</td><td colspan="3" class="muted">尚未安排 · 在下方选择日期和菜谱</td></tr>')
            continue
        current = values.get('servings') if route=='/plans/update' and str(values.get('id'))==str(p['id']) else p['servings']
        rows.append(f'''<tr><td>{day_label}</td><td><strong>{h(p['recipe_name'])}</strong><br><span class="pill">{"已安排" if p['active'] else "已暂停 · 不计采购"}</span></td>
        <td><form action="/plans/update" method="post" class="inline">{hidden()}<input type="hidden" name="id" value="{p['id']}"><div class="field"><label for="servings-{p['id']}">用餐人数</label><input class="small-input" id="servings-{p['id']}" name="servings" type="number" min="1" max="20" step="1" value="{h(current)}" required></div><button type="submit" aria-label="保存{h(p['date'])}人数">保存人数</button></form></td>
        <td><form action="/plans/toggle" method="post">{hidden()}<input type="hidden" name="id" value="{p['id']}"><button type="submit" aria-label="{'暂停' if p['active'] else '恢复'}{h(p['date'])}计划">{'暂停计划' if p['active'] else '恢复计划'}</button></form></td></tr>''')
    plan_fields = values if route=='/plans' else {}
    plan_options = options([(r['id'],f"{r['name']}（基准 {r['base_servings']} 人）") for r in state['recipes']],plan_fields.get('recipe_id',''))
    add_plan = f'''<h3>安排一顿晚餐</h3><form action="/plans" method="post">{hidden()}<div class="inline">
    <div class="field"><label for="plan-date">晚餐日期</label><input id="plan-date" name="date" type="date" value="{h(plan_fields.get('date',max(start,min(date.today().isoformat(),end))))}" required></div>
    <div class="field"><label for="plan-recipe">选择菜谱</label><select id="plan-recipe" name="recipe_id" required><option value="">请选择菜谱</option>{plan_options}</select></div>
    <div class="field"><label for="plan-servings">用餐人数（1–20）</label><input id="plan-servings" name="servings" type="number" min="1" max="20" step="1" value="{h(plan_fields.get('servings','2'))}" required></div><button class="primary" type="submit" {'disabled' if not state['recipes'] else ''}>保存晚餐</button></div>
    <p class="muted">每日期一份晚餐。已存在的计划请修改人数或恢复；选择其他日期后，会显示该日期所在周。</p></form>'''
    plans_panel = f'<section class="panel"><h2>晚餐日历</h2><div class="table-wrap"><table><thead><tr><th>日期</th><th>菜谱 / 状态</th><th>人数</th><th>操作</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>{add_plan}</section>'
    shopping = state['shopping']
    shopping_rows = ''.join(f'<tr><td>{h(i["name"])}</td><td class="amount"><strong>{h(quantity_text(i["quantity_minor"]))}</strong> {h(i["unit"])}</td></tr>' for i in shopping['items'])
    shopping_panel = f'''<section class="panel"><h2>合并采购清单</h2><p class="muted">{h(start)} 至 {h(end)}<br>来自 {shopping['plan_count']} 顿有效晚餐，暂停计划不计入。</p>
    {'<table><thead><tr><th>食材</th><th class="amount">估算数量</th></tr></thead><tbody>'+shopping_rows+'</tbody></table>' if shopping_rows else '<div class="empty">还没有采购项<br>先登记菜谱，再安排晚餐</div>'}
    <p class="muted">同名同单位合并；不同单位分开列出。每顿按人数换算并保留两位小数，再合计。</p><p class="muted">这是份数估算，并非营养建议或真实购买订单。</p></section>'''
    recipe_values = values if route=='/recipes' else {}
    recipe_form = f'''<section class="panel"><h2>登记菜谱</h2><p class="muted">保存后菜谱不可修改。食材数量按基准人数填写。</p><form action="/recipes" method="post">{hidden()}
    <div class="inline"><div class="field"><label for="recipe-name">菜谱名称</label><input id="recipe-name" name="name" value="{h(recipe_values.get('name',''))}" placeholder="例如：番茄炒蛋" required></div>
    <div class="field"><label for="base-servings">基准人数（1–20）</label><input id="base-servings" name="base_servings" type="number" min="1" max="20" step="1" value="{h(recipe_values.get('base_servings','2'))}" required></div></div>
    <div class="field" style="margin-top:14px"><label for="ingredients">食材清单：每行 名称|单位|数量</label><textarea id="ingredients" name="ingredients" rows="5" placeholder="番茄|g|300&#10;鸡蛋|个|2" aria-describedby="ingredient-help" required>{h(recipe_values.get('ingredients',''))}</textarea><div id="ingredient-help" class="muted">单位只填 g、ml 或 个；数量大于 0，最多两位小数。同名同单位每份菜谱只写一行。</div></div><button class="primary" type="submit">保存菜谱</button></form></section>'''
    recipe_cards = ''.join(f'<article class="note-card"><div class="row"><strong>{h(r["name"])}</strong><span class="pill">基准 {r["base_servings"]} 人</span></div><p class="muted">'+ ' · '.join(f'{h(i["name"])} {h(i["quantity"])} {h(i["unit"])}' for i in r['ingredients'])+'</p></article>' for r in state['recipes'])
    library = f'<section class="panel"><h2>我的菜谱 · {len(state["recipes"])} 份</h2>{recipe_cards or "<div class=empty>登记第一份菜谱，开始规划一周晚餐。</div>"}</section>'
    metrics = f'''<div class="cards"><div class="metric"><small>有效晚餐</small><strong>{shopping['plan_count']} <small>顿</small></strong><small>当前日期范围</small></div><div class="metric"><small>已暂停</small><strong>{len(state['plans'])-shopping['plan_count']} <small>顿</small></strong><small>随时可以恢复</small></div><div class="metric"><small>合并采购项</small><strong>{len(shopping['items'])} <small>项</small></strong><small>按名称和单位计算</small></div><div class="metric"><small>已保存菜谱</small><strong>{len(state['recipes'])} <small>份</small></strong><small>保存在本机</small></div></div>'''
    return page('一周晚餐','安排晚餐，采购刚刚好',f'<p class="muted">为自己或两个人，提前想好每天吃什么。</p>{notice}{metrics}{range_form}<div class="grid"><div>{plans_panel}{recipe_form}{library}</div><aside>{shopping_panel}<div class="panel"><h2>从一份菜谱开始</h2><p class="muted">① 登记基准人数和食材<br>② 选择日期，安排晚餐人数<br>③ 查看清单，调整或暂停计划</p></div></aside></div>')
