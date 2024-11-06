# 인기영화 웹스크래핑
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui

url = "https://search.daum.net/search?w=tot&q=2023%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# 셀레니움으로 긁어와서 파일 저장
for i in range(4):
  soup = BeautifulSoup(browser.page_source,'lxml')
  with open(f'C:/workspace/smclass/d1106/movies{i+1}.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())
  time.sleep(random.randint(2,5))
  if i == 3:
    break
  else:
    browser.find_element(By.XPATH,f'//*[@id="morColl"]/div/c-container/div[2]/c-carousel/div/ul/li[{i+3}]/a').click()
    time.sleep(random.randint(2,5))
  print(f"{i+1}번째 페이지 저장 완료")

f = open("C:/workspace/smclass/d1106/movielist.csv",'a',encoding='utf-8-sig',newline="")
writer = csv.writer(f)
writer.writerow(['제목', '관객수', '개봉일'])

for i in range(4):
  with open(f'C:/workspace/smclass/d1106/movies{i+1}.html','r',encoding='utf8') as f:
    soup = BeautifulSoup(f,'lxml')

  data = soup.select_one("div.pdt2") #  기준점:영화박스
  moives = data.select("div.c-item-content")
  # movie = data.select_one("div.c-item-content")
  # print(movies)
  m_list = []
  for movie in moives:
    try:
      title = movie.select_one("strong.tit-g").text.strip()
      people = movie.select_one("p.conts-desc").text.strip()[3:][:-2]
      if ',' in people:
        peop = int(people.replace(',',''))*10000
      else:
        peop = int(people)*10000
      openday = movie.select_one("span.conts-subdesc").text.strip()[:-1]
    except Exception as e:
      print("정보 부족 :", e)
    print(title, peop, openday)
    m_list.append([title, peop, openday])
    writer.writerow([title, peop, openday])



print(m_list)