#!/usr/bin/env python3
"""Local-only weekly dinner planner. Run without installation or dependencies."""
import argparse
from http.server import ThreadingHTTPServer
from pathlib import Path
import re
from urllib.parse import urlencode
from store import Store, week, iso_date
from views import render
from web_support import Handler as BaseHandler, Error


def form_int(value, code='invalid_servings'):
    if not isinstance(value,str) or not re.fullmatch(r'[0-9]+',value):
        raise Error(code,'请填写 1–20 的整数人数。' if code=='invalid_servings' else '请选择存在的菜谱或计划。',400 if code=='invalid_servings' else 404)
    return int(value)


class Handler(BaseHandler):
    @property
    def store(self):
        return self.server.store

    def dispatch(self, method):
        if method == 'GET':
            if self.route == '/api/health':
                return self.json(200,{'status':'ok','application':'meal-plan-trial'})
            if self.route in ('/api/state','/api/shopping'):
                state = self.store.state(self.query.get('start'),self.query.get('end'))
                return self.json(200,state if self.route=='/api/state' else state['shopping'])
            if self.route == '/':
                return self.send(200,render(self.store,self.query))
            raise Error('not_found','页面不存在。',404)
        is_api = self.route.startswith('/api/')
        route = self.route[4:] if is_api else self.route
        if route not in ('/recipes','/plans','/plans/update','/plans/toggle'):
            raise Error('not_found','操作不存在。',404)
        data = dict(self.data)
        if not is_api:
            if route=='/recipes':
                data['base_servings'] = form_int(data.get('base_servings'))
                ingredients = []
                for line in data.get('ingredients','').splitlines():
                    if not line.strip():
                        continue
                    parts = [part.strip() for part in line.split('|')]
                    if len(parts)!=3:
                        raise Error('invalid_ingredient','食材每行需填写：名称|单位|数量。')
                    ingredients.append(dict(zip(('name','unit','quantity'),parts)))
                data['ingredients'] = ingredients
            else:
                for field in ('id','recipe_id'):
                    if field in data:
                        data[field] = form_int(data[field],'not_found')
                if route!='/plans/toggle':
                    data['servings'] = form_int(data.get('servings'))
        if route=='/recipes':
            result,status,message = self.store.recipe(data),201,'recipe'
        elif route=='/plans':
            result,status,message = self.store.plan(data),201,'plan'
        else:
            result,status,message = self.store.change(data,route.endswith('toggle')),200,('toggle' if route.endswith('toggle') else 'update')
        if is_api:
            return self.json(status,result)
        if route=='/plans':
            start,end = week(iso_date(result['date']))
        else:
            from store import date_range
            try:
                start,end = date_range(data.get('start'),data.get('end'))
            except Error:
                start,end = week()
        self.redirect('/?'+urlencode({'start':start,'end':end,'saved':message}))

    def error_page(self,error):
        query = dict(self.query)
        for key in ('start','end'):
            if key in self.data:
                query[key] = self.data[key]
        return render(self.store,query,self.data,error,self.route)


def main():
    parser = argparse.ArgumentParser(description='本机一周晚餐计划（仅 Python 标准库）')
    parser.add_argument('--port',type=int,default=5277)
    parser.add_argument('--data-dir',type=Path,default=Path(__file__).resolve().parents[1]/'data')
    parser.add_argument('--demo',action='store_true',help='仅新数据库首次创建演示菜谱和计划')
    args = parser.parse_args()
    if not 1024 <= args.port <= 65535:
        parser.error('--port 必须为 1024–65535')
    store = Store(args.data_dir/'meal-plan.sqlite3',demo=args.demo)
    server = ThreadingHTTPServer(('127.0.0.1',args.port),Handler)
    server.store = store
    print(f'一周晚餐 http://127.0.0.1:{args.port} · 数据目录 {args.data_dir.resolve()}',flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__=='__main__':
    main()
