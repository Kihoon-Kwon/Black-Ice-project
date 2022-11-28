import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

while True:
    header = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8' 
    }
    
    response = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EB%82%A0%EC%94%A8", headers=header)
    
    contents = BeautifulSoup(response.content, 'html.parser')
    
    temps = contents.find('div',"_today")
    time.sleep(5)
    print(time.strftime('--> 현재 날짜 시간 : %Y년%m월%d일 %H:%M:%S'))
    print('--> 오늘 경기도 날씨 : ', temps.get_text() )