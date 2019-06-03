from bs4 import BeautifulSoup
import urllib.request as MYURL

api = 'http://asp1.krx.co.kr/servlet/krx.asp.XMLSiseEng?code=018260'

response = MYURL.urlopen(api)
juga = BeautifulSoup(response, 'html.parser')

print(juga.find('dailystock')['day_date'])
print(juga.find('tbl_stockinfo')['jongname'])