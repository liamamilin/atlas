"""Isolated real HTTP notebook checks, fixed before application implementation."""
import argparse
import json
from pathlib import Path
import secrets
import socket
import subprocess
import sys
import tempfile
import time
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def request(base,path,data=None):
    req=Request(base+path,data=None if data is None else json.dumps(data).encode(),headers={'Content-Type':'application/json'})
    try:
        with urlopen(req,timeout=10) as response:return response.status,json.load(response)
    except HTTPError as error:return error.code,json.load(error)


def journey(base):
    token='meeting-'+secrets.token_hex(6)
    status,a=request(base,'/api/projects',{'name':token+'-A'});assert status==201
    status,b=request(base,'/api/projects',{'name':token+'-B'});assert status==201
    body='决策 '+token+'\n|行动|负责人|\n|---|---|\n|发布候选|小林|\n<script>literal text</script>'
    status,note=request(base,'/api/notes',{'title':'Z-'+token,'body':body});assert status==201
    identifier=note['id'];assert note['body']==body
    status,note=request(base,'/api/notes/move',{'id':identifier,'project_id':a['id']});assert status==200
    assert note['project_id']==a['id']
    def state(**query):
        status,value=request(base,'/api/state?'+urlencode(query));assert status==200;return value
    assert identifier in [n['id'] for n in state(project=a['id'])['notes']]
    assert identifier not in [n['id'] for n in state(project=b['id'])['notes']]
    revision=note['revision'];newbody=body+'\n最终通过，保留原文 & 引号 "。'
    status,note=request(base,'/api/notes/update',{'id':identifier,'revision':revision,'project_id':a['id'],'title':'Z-'+token,'body':newbody});assert status==200 and note['body']==newbody
    assert request(base,'/api/notes/update',{'id':identifier,'revision':revision,'project_id':a['id'],'title':'stale','body':'must not overwrite'})[0]==409
    assert request(base,'/api/notes/update',{'id':identifier,'revision':note['revision'],'project_id':a['id'],'title':'empty','body':''})[0]==400
    assert request(base,'/api/notes/'+identifier)[1]['body']==newbody
    assert request(base,'/api/notes',{'title':'A-'+token,'body':'Other '+token,'project_id':a['id']})[0]==201
    assert request(base,'/api/notes/pin',{'id':identifier})[0]==200
    assert state(project=a['id'],sort='title')['notes'][0]['id']==identifier
    assert request(base,'/api/notes/archive',{'id':identifier})[0]==200
    assert identifier not in [n['id'] for n in state()['notes']]
    assert identifier in [n['id'] for n in state(q=token)['notes']]
    assert request(base,'/api/notes/trash',{'id':identifier})[0]==200
    assert identifier not in [n['id'] for n in state(q=token)['notes']]
    assert identifier in [n['id'] for n in state(view='trash')['notes']]
    status,note=request(base,'/api/notes/restore',{'id':identifier});assert status==200
    assert note['project_id']==a['id'] and note['archived']==1 and note['pinned']==1 and note['body']==newbody
    assert state(q='absent-'+token)['notes']==[]
    return token,state(q=token),request(base,'/api/notes/'+identifier)[1]


def restart(base,root):
    assert request(base,'/api/health')[0]==200
    with tempfile.TemporaryDirectory(prefix='notes-restart-') as tmp:
        with socket.socket() as sock:sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
        url=f'http://127.0.0.1:{port}';command=[sys.executable,str(Path(root)/'app/serve.py'),'--port',str(port),'--data-dir',tmp]
        def start():
            proc=subprocess.Popen(command,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            for _ in range(100):
                try:
                    if request(url,'/api/health')[0]==200:return proc
                except OSError:pass
                time.sleep(.05)
            proc.terminate();proc.wait();raise RuntimeError('not ready')
        proc=start()
        try:token,before,note=journey(url)
        finally:proc.terminate();proc.wait(timeout=10)
        proc=start()
        try:
            assert request(url,'/api/state?'+urlencode({'q':token}))[1]==before
            assert request(url,'/api/notes/'+note['id'])[1]==note
        finally:proc.terminate();proc.wait(timeout=10)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--base-url',required=True);parser.add_argument('--case',choices=['N01','N02','N03','N04'],required=True);parser.add_argument('--app-root');args=parser.parse_args()
    try:
        if args.case=='N04':
            if not args.app_root:raise ValueError('N04 requires --app-root')
            restart(args.base_url,args.app_root)
        else:journey(args.base_url)
    except Exception as error:
        print(json.dumps({'case':args.case,'status':'failed','error':str(error),'browser_verified':False}));return 1
    print(json.dumps({'case':args.case,'status':'passed','scope':'real HTTP and owned restart only; not browser proof'}));return 0

if __name__=='__main__':sys.exit(main())
