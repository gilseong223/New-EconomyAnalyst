# 전처리 과정 'Form Data' 복사해서 사전타입으로 정리
lines = '''pageInfo:bksMain
login_chk:null
LOGIN_SN:null
LOGIN_NAME:null
indexName:news
keyword:양민철 KBS
byLine:
searchScope:1
searchFtr:1
startDate:2019-02-28
endDate:2019-05-30
sortMethod:date
contentLength:100
providerCode:
categoryCode:
incidentCode:
dateCode:
highlighting:true
sessionUSID:
sessionUUID:test
listMode:
categoryTab:
newsId:
filterProviderCode:
filterCategoryCode:
filterIncidentCode:
filterDateCode:
filterAnalysisCode:
startNo:1
resultNumber:1000
topmenuoff:
resultState:
keywordJson:
keywordFilterJson:
realKeyword:
totalCount:
interval:
quotationKeyword1:
quotationKeyword2:
quotationKeyword3:
searchFromUseYN:N
mainTodayPersonYn:
period:3month'''.splitlines()

data = {}
for line in lines:
    key, value = line.split(':', 1)
    if value == 'null':
        value = None
    data[key] = value

import requests
from bs4 import BeautifulSoup
import urllib.request,ssl, json
from urllib.error import HTTPError

result_url = "https://www.bigkinds.or.kr/news/newsResult.do"
response = requests.post(result_url, data=data)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
certifi = ssl.SSLContext()

result = set()

for tag in soup.select('.resultList li h3'):
    doc_id = tag['id'].replace('news_', '')
    doc_url = 'https://www.bigkinds.or.kr/news/detailView.do?docId={}&returnCnt=1'.format(doc_id)
    print(tag.text.strip(), doc_url)
    result.add(tag.text.strip())
    try :
        with urllib.request.urlopen(doc_url, context=certifi) as url:
            data = json.loads(url.read().decode())
            #print(data.get('TITLE'))

            print(data.get('detail').get('CONTENT'))
    except HTTPError:
        print('내용이 없습니다')
        continue

print(result)

for re in result:
    print(re)