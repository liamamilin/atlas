"""Meal planning storage and exact per-plan quantity calculation (stdlib only)."""
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP, localcontext
import json
import re
import sqlite3
from web_support import Error, connect


def servings(value):
    if type(value) is not int or not 1 <= value <= 20:
        raise Error('invalid_servings', '用餐人数和基准人数必须是 1–20 的整数。')
    return value


def name(value, code='invalid_name'):
    if not isinstance(value, str) or not value.strip():
        raise Error(code, '名称不能为空，请填写清晰的名称。')
    return value.strip()


def iso_date(value):
    try:
        if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
            raise ValueError()
        return date.fromisoformat(value)
    except ValueError:
        raise Error('invalid_date', '日期无效，请使用 YYYY-MM-DD 格式和真实日期。') from None


def week(day=None):
    day = day or date.today()
    start = day - timedelta(days=day.weekday())
    return start.isoformat(), (start + timedelta(days=6)).isoformat()


def date_range(start=None, end=None):
    if start is None and end is None:
        return week()
    try:
        a, b = iso_date(start), iso_date(end)
    except Error:
        raise Error('invalid_range', '请选择真实的起止日期，范围为 1–7 天。') from None
    if not 0 <= (b - a).days <= 6:
        raise Error('invalid_range', '起止日期范围必须为 1–7 天（含首尾）。')
    return a.isoformat(), b.isoformat()


def identifier(value):
    if type(value) is not int or value < 1:
        raise Error('not_found', '没有找到对应的菜谱或计划。', 404)
    return value


def quantity_minor(value):
    if not isinstance(value, str) or not re.fullmatch(r'[0-9]+(?:\.[0-9]{1,2})?', value):
        raise Error('invalid_quantity', '食材数量必须是正十进制数字，最多两位小数。')
    whole, _, fraction = value.partition('.')
    result = int(whole) * 100 + int((fraction + '00')[:2])
    if result <= 0:
        raise Error('invalid_quantity', '食材数量必须大于零。')
    return result


def quantity_text(minor):
    return f'{minor // 100}.{minor % 100:02d}'.rstrip('0').rstrip('.')


def scaled_minor(minor, count, base):
    with localcontext() as context:
        context.prec = max(28, len(str(minor)) + 10)
        return int((Decimal(minor) * count / base).quantize(Decimal('1'), rounding=ROUND_HALF_UP))


class Store:
    def __init__(self, path, demo=False):
        self.path = path
        fresh = not path.exists()
        path.parent.mkdir(parents=True, exist_ok=True)
        with connect(path) as con:
            con.executescript('''
            CREATE TABLE IF NOT EXISTS recipes(
              id INTEGER PRIMARY KEY, name TEXT NOT NULL,
              base_servings INTEGER NOT NULL CHECK(base_servings BETWEEN 1 AND 20),
              ingredients TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS plans(
              id INTEGER PRIMARY KEY, date TEXT UNIQUE NOT NULL,
              recipe_id INTEGER NOT NULL REFERENCES recipes(id),
              servings INTEGER NOT NULL CHECK(servings BETWEEN 1 AND 20),
              active INTEGER NOT NULL DEFAULT 1 CHECK(active IN(0,1)));
            ''')
        if fresh and demo:
            recipe = self.recipe({'name':'番茄炒蛋','base_servings':2,'ingredients':[
                {'name':'番茄','unit':'g','quantity':'300'}, {'name':'鸡蛋','unit':'个','quantity':'2'}]})
            start, _ = week()
            self.plan({'date':start,'recipe_id':recipe['id'],'servings':2})
            self.plan({'date':(iso_date(start)+timedelta(days=1)).isoformat(),'recipe_id':recipe['id'],'servings':4})

    @staticmethod
    def recipe_out(row):
        return {'id':row['id'],'name':row['name'],'base_servings':row['base_servings'],
                'ingredients':[{'name':i['name'],'unit':i['unit'],'quantity':quantity_text(i['quantity_minor'])}
                               for i in json.loads(row['ingredients'])]}

    def recipe(self, data):
        title, base = name(data.get('name')), servings(data.get('base_servings'))
        ingredients = data.get('ingredients')
        if not isinstance(ingredients, list) or not ingredients:
            raise Error('invalid_ingredient', '请至少登记一行食材：名称|单位|数量。')
        prepared, seen = [], set()
        for item in ingredients:
            if not isinstance(item, dict):
                raise Error('invalid_ingredient', '每项食材必须包含名称、单位和数量。')
            label = name(item.get('name'), 'invalid_ingredient')
            unit = item.get('unit')
            if unit not in ('g','ml','个'):
                raise Error('invalid_ingredient', '食材单位仅支持 g、ml、个。')
            key = (label.casefold(), unit)
            if key in seen:
                raise Error('invalid_ingredient', '同一菜谱内同名同单位食材只能出现一次。')
            seen.add(key)
            prepared.append({'name':label,'unit':unit,'quantity_minor':quantity_minor(item.get('quantity'))})
        with connect(self.path) as con:
            cursor = con.execute('INSERT INTO recipes(name,base_servings,ingredients) VALUES(?,?,?)',
                                 (title,base,json.dumps(prepared,ensure_ascii=False)))
            return self.recipe_out(con.execute('SELECT * FROM recipes WHERE id=?',(cursor.lastrowid,)).fetchone())

    def plan(self, data):
        day = iso_date(data.get('date')).isoformat()
        recipe_id, count = identifier(data.get('recipe_id')), servings(data.get('servings'))
        with connect(self.path) as con:
            if not con.execute('SELECT 1 FROM recipes WHERE id=?',(recipe_id,)).fetchone():
                raise Error('not_found','菜谱不存在，请重新选择。',404)
            try:
                cursor = con.execute('INSERT INTO plans(date,recipe_id,servings) VALUES(?,?,?)',(day,recipe_id,count))
            except sqlite3.IntegrityError:
                raise Error('already_exists','该日期已有晚餐计划，请修改人数或恢复原计划。',409) from None
            return dict(con.execute('SELECT * FROM plans WHERE id=?',(cursor.lastrowid,)).fetchone())

    def change(self, data, toggle=False):
        plan_id = identifier(data.get('id'))
        count = None if toggle else servings(data.get('servings'))
        with connect(self.path) as con:
            if not con.execute('SELECT 1 FROM plans WHERE id=?',(plan_id,)).fetchone():
                raise Error('not_found','晚餐计划不存在。',404)
            if toggle:
                con.execute('UPDATE plans SET active=1-active WHERE id=?',(plan_id,))
            else:
                con.execute('UPDATE plans SET servings=? WHERE id=?',(count,plan_id))
            return dict(con.execute('SELECT * FROM plans WHERE id=?',(plan_id,)).fetchone())

    def state(self, start=None, end=None):
        start, end = date_range(start,end)
        with connect(self.path) as con:
            recipes = [self.recipe_out(row) for row in con.execute('SELECT * FROM recipes ORDER BY id')]
            rows = list(con.execute('''SELECT p.*, r.name recipe_name, r.base_servings, r.ingredients
                FROM plans p JOIN recipes r ON r.id=p.recipe_id WHERE p.date BETWEEN ? AND ? ORDER BY p.date,p.id''',(start,end)))
        plans, totals, count = [], {}, 0
        for row in rows:
            plans.append({key:row[key] for key in ('id','date','recipe_id','servings','active','recipe_name')})
            if not row['active']:
                continue
            count += 1
            for item in json.loads(row['ingredients']):
                key = (item['name'].strip().casefold(),item['unit'])
                if key not in totals:
                    totals[key] = {'name':item['name'].strip(),'unit':item['unit'],'quantity_minor':0}
                totals[key]['quantity_minor'] += scaled_minor(item['quantity_minor'],row['servings'],row['base_servings'])
        return {'recipes':recipes,'plans':plans,'shopping':{'items':[totals[key] for key in sorted(totals)],'plan_count':count}}
