import os
from dotenv import load_dotenv

load_dotenv()
SERVICE_KEY = os.getenv('CITY_DATA')


URL = f'http://openapi.seoul.go.kr:8088/{SERVICE_KEY}/json/tbLnOpendataRtmsV/1/100/' 
# json자리에 xml등 넣을 수 있음
# 맨 뒤에 100: 데이터 수 (주의: 한 번에 1000개까지밖에 안 됨)



import requests
import json
import pandas as pd

req = requests.get(URL)
req.status_code     # 200, req만 입력해도 Response 200나오긴 함


content = req.json()
# content   # 정상 처리되었다고 하고 데이터 쭉 
result = pd.DataFrame(content['tbLnOpendataRtmsV']['row'])    #content 안의 tbLn~은 key값. 그 뒤에 row만 찾음 (content 주석 풀면 보일 것)
result


URL

URL1 = URL.replace('json', 'xml')
URL1


