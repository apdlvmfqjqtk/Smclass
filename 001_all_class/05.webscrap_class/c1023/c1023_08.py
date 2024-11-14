from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random

url = "http://flight.naver.com/"
browser = webdriver.Chrome()
browser.maximize_window() # 창 크기 최대화
browser.get(url)
time.sleep(1)
# 1.  출발공항 서울로 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]/b').click()
browser.find_element(By.CLASS_NAME,"autocomplete_input__qbYlb").send_keys("김포")
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li[2]/a/b').click()
time.sleep(1)
# 2.  도착공항 제주로 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]/b').click()
browser.find_element(By.CLASS_NAME,"autocomplete_input__qbYlb").send_keys("제주")
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[3]/div[2]/section/ul/li/a/b').click()
time.sleep(1)
# 3.  가는날, 날짜 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]').click()
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/button/b').click()
time.sleep(1)

# 4.  오는날, 날짜 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[2]').click()
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[7]/button').click()
time.sleep(1)

# 5.  인원 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[3]/button').click()
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]').click()
time.sleep(1)

# 6.  항공권 검색 클릭
browser.find_element(By.CLASS_NAME,'searchBox_txt__jQZGF').click()
browser.find_element(By.CLASS_NAME,'searchBox_txt__jQZGF').click()
time.sleep(1)
# # 검색창 대기
# time.sleep(7)

# 화면 대기 함수
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 화면 대기
# 화면에 찾으려고 하는 <html>요소가 있는지 확인
# 브라우저는 최대 30초까지 기다리고. 그 전에 내가 찾으려는 데이터가 나온다면 그 데이터를 출력 
elem = WebDriverWait(browser,30).until(EC.presence_of_all_elements_located(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div[2]'))

# 화면 스크롤 내리기
# 현재 스크롤 높이 검색
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이 : ", prev_height)
while True:

  # 스크롤 내리기
  browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(2)  #스크롤 내리고 다른 정보가 추가될 때 까지 대기
  curr_height = browser.execute_script("return document.body.scrollHeight")
  if prev_height == curr_height:
    break

  prev_height = curr_height
  print("현재 높이 :", curr_height)



# 데이터 가져와서 처리
# BeautifulSoup 데이터 처리
# 웹 스크래핑
suop = BeautifulSoup(browser.page_source,'lxml')
with open('flight.html','w',encoding='utf8') as f:
  f.write(suop.prettify())

input("enter키를 누르면 프로그램이 종료됩니다.")
browser.quit()




time.sleep(100000)

# # 네이버 -> 네이버항공권
# url = "http://www.naver.com/"
# browser = webdriver.Chrome()
# browser.get(url)
# elem = browser.find_element(By.ID,'query')
# elem.send_keys("네이버 항공권")
# elem.send_keys(Keys.ENTER)


# # 네이버 항공권 선택
# browser.find_element(By.CLASS_NAME,'link_name').click()

# time.sleep(100)