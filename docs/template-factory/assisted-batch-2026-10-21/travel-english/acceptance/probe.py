"""Frozen course journey; only on a disposable test-owned instance. Not run yet."""
import argparse,json,urllib.request,urllib.error,uuid
from pathlib import Path

def call(base,path,data=None,status=200):
 req=urllib.request.Request(base+path,None if data is None else json.dumps(data).encode(),{'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(req) as r:code=r.status;value=json.load(r)
 except urllib.error.HTTPError as e:code=e.code;value=json.load(e)
 assert code==status,(code,value)
 return value
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--base-url',required=True);p.add_argument('--case',choices=['A01','A02','A03'],required=True);a=p.parse_args();b=a.base_url
 lessons=json.loads(Path(__file__).with_name('COURSE.json').read_text());course=call(b,'/api/course');assert [l['id'] for l in course['lessons']]==[l['id'] for l in lessons]
 assert course['progress']['mastered_count']==0
 call(b,'/api/lessons/hotel',status=409)
 for lesson in lessons:
  actual=call(b,'/api/lessons/'+lesson['id']);assert [q['id'] for q in actual['questions']]==[q['id'] for q in lesson['questions']]
  for q in lesson['questions']:
   before=call(b,'/api/course')['progress']
   wrong=call(b,'/api/answers',{'question_id':q['id'],'answer':'definitely wrong','submission_id':uuid.uuid4().hex});assert wrong['correct'] is False
   assert call(b,'/api/course')['progress']==before and q['id'] in call(b,'/api/course')['mistakes']
   call(b,'/api/answers',{'question_id':q['id'],'answer':'','submission_id':uuid.uuid4().hex},400)
   payload={'question_id':q['id'],'answer':'  '+q['accepted'][0].swapcase()+'  ','submission_id':uuid.uuid4().hex}
   answer=call(b,'/api/answers',payload);assert answer['correct'] is True
   assert call(b,'/api/answers',payload)==answer
   assert call(b,'/api/course')['progress']['mastered_count']==before['mastered_count']+1
   assert q['id'] not in call(b,'/api/course')['mistakes']
   call(b,'/api/answers',{**payload,'answer':'changed'},409)
 call(b,'/api/lessons/unknown',status=404)
 final=call(b,'/api/course');assert final['progress']['mastered_count']==9 and len(final['progress']['completed_lessons'])==3
 print(json.dumps({'case':a.case,'status':'http_passed','remaining':'Browser refresh and same-data-dir process restart still require separate evidence. This program is not runtime evidence until executed.'}))
