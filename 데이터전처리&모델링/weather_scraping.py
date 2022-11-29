from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import sys
import pandas as pd
import numpy as np
import schedule
import time
import datetime
import MySQLdb

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(chrome_path)

group = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(2) > div > div > div:nth-child(3) > div > div > div > div.graph_inner._hourly_weather > ul'
humid_group = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(2) > div > div > div:nth-child(6) > div > div > div > div.climate_box > div.graph_wrap > ul'
counties = ['가평군','고양시','과천시','광명시','광주시','구리시','군포시','김포시','남양주시','동두천시','부천시','성남시','수원시','시흥시','안산시','안성시','안양시','양주시','양평군','여주시','연천군','오산시','용인시','의왕시','의정부시','이천시','파주시','평택시','포천시','하남시','화성시']
dataset_total = [] # 습도 제외 나머지 데이터
humidity_list = [] # 습도만 따로 리스트로 만들어서 나중에 병합

today_and_tommorow = []
now = datetime.datetime.now()
after_1day = datetime.timedelta(days=1)
after_2day = datetime.timedelta(days=2)

for i in range(60):
    if i<23-now.hour:
        today_and_tommorow.append(now.strftime('%Y-%m-%d'))
    elif i>=23-now.hour and i<47-now.hour:
        today_and_tommorow.append((now+after_1day).strftime('%Y-%m-%d'))
    else:
        today_and_tommorow.append((now+after_2day).strftime('%Y-%m-%d'))

user_name = input("유저명을 입력하세요: ")
password = input("비밀번호를 입력하세요: ")
host_name = input("호스트명을 입력하세요: ")
db_name = input("DB명을 입력하세요: ")

conn = MySQLdb.connect(
    user=user_name,
    passwd=password,
    host=host_name,
    db=db_name
)

# 웹 크롤링 실행하는 extract 함수
def extract():
    for county in counties:
        url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=경기도+'+county+'+날씨'
        driver.get(url)
        total_list = driver.find_elements(By.CSS_SELECTOR,group+'>li')
        total_length = len(total_list)
        for i in range(1,61):
            time = driver.find_element(By.CSS_SELECTOR, group+'> li:nth-child('+str(i)+') > dl > dt > em')

            temperature = driver.find_element(By.CSS_SELECTOR, group+'> li:nth-child('+str(i)+') > dl > dd.degree_point > div > div > span')
            temp_text = temperature.text.split('\n')
            temperature = temp_text[0]

            weather = driver.find_element(By.CSS_SELECTOR, group+'> li:nth-child('+str(i)+') > dl > dd.weather_box > i > span')
            dataset_total.append([today_and_tommorow[i-1], county, time.text, temperature, weather.text])

        humid_btn = driver.find_element(By.CSS_SELECTOR,'#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(2) > div > div > div.sub_tab > div > ul > li:nth-child(4) > a > span')
        humid_btn.click()

        humid_list = driver.find_elements(By.CSS_SELECTOR,humid_group+'>li')
        humid_length = len(humid_list)
        for k in range(1,61):
            humidity = driver.find_element(By.CSS_SELECTOR,humid_group+'> li:nth-child('+str(k)+') > div > span > span')
            humidity_list.append(humidity.text)

#프로그램을 종료 및 csv 저장, DB 저장하는 exit_and_save 함수
def exit_and_save():
    print("function exit")
    driver.quit()
    time.sleep(1)
    columns = ['날짜','지역','일시','기온(°C)','기상상태']
    pd_data = pd.DataFrame(dataset_total, columns=columns)
    pd_data['습도(%)'] = humidity_list
    pd_data.replace(['내일','모레'],['00시','00시'],inplace=True) # 00시 데이터 부분이 내일이나 모레라고 표기되어 있어서 변경
    pd_data.to_csv('./weather_scraping.csv',encoding='cp949')
    val_list = pd_data.values.tolist()
    cursor = conn.cursor()
    cursor.execute("drop table if exists crawldata_before")
    cursor.execute("create table crawldata_before(date text, county text, time text, temperature text, weather text, humidity text)")
    for k in range(len(val_list)):
        data = list(pd_data.iloc[k])
        cursor.execute(f"INSERT INTO crawldata_before VALUES(\"{data[0]}\",\"{data[1]}\",\"{data[2]}\",\"{data[3]}\",\"{data[4]}\",\"{data[5]}\")")
    conn.commit()
    conn.close()

    # 일시 값 숫자만 남기기
    time_h = pd_data['일시'].values.tolist()
    h_time = []
    for i in time_h:
        h = i[0:2]
        h_time.append(int(h))    
    pd_data['일시'] = h_time

    # 기상상태 값 수치화
    weather = pd_data['기상상태'].values.tolist()
    weather_n = []
    for w in weather:
        if (w == "눈") or (w=="비"):
            w=1.342
            weather_n.append(w)
        elif w=="안개":
            w=2
            weather_n.append(w)
        else:
            w=1
            weather_n.append(w)        
    pd_data['기상상태'] = weather_n
    
    pd_data.to_csv('./weather_scraping2.csv',encoding='cp949')
    val_list = pd_data.values.tolist()
    cursor = conn.cursor()
    cursor.execute("drop table if exists crawldata")
    cursor.execute("create table crawldata(date text, county text, time text, temperature text, weather text, humidity text)")
    for k in range(len(val_list)):
        data = list(pd_data.iloc[k])
        cursor.execute(f"INSERT INTO crawldata VALUES(\"{data[0]}\",\"{data[1]}\",\"{data[2]}\",\"{data[3]}\",\"{data[4]}\",\"{data[5]}\")")
    conn.commit()
    conn.close()
    sys.exit()

time1 = input("시간을 입력하세요: ") # XX:OO시 형태로 입력, 시간 입력할 때 현재 시간보다 약 2분 뒤로 입력하는 것을 권장
time2 = input("시간을 입력하세요: ") # ex) 현재 시간이 10시 49분이면 time1에 10:51, time2에 10:52 입력    

# 23시 XX분에 프로그램 실행하면 00시 날씨 데이터부터 받기 시작한다. 너무 늦게 받으면 00시 데이터가 받아지지 않을 수 있다. 
schedule.every().day.at(time1).do(extract) # extract 함수 실행
schedule.every().day.at(time2).do(exit_and_save) # 가평군부터 화성시까지 루프 1번은 돌고 프로그램 종료하는 exit_and_save함수

#무한 루프를 돌면서 스케쥴을 유지한다.
while True:
    schedule.run_pending()
    time.sleep(1)

# 이 밑으로는 코딩해도 while문 무한루프 때문에 실행 안됩니다. 추가로 이어서 작업하려면 exit_and_save함수 안에 이어서 작성할 것