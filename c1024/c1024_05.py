from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui

# url = "https://new.land.naver.com/complexes?ms=37.4592802,126.8930386,17&a=APT:PRE:ABYG:JGC&e=RETAIL"


# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)

# time.sleep(1)
# pyautogui.moveTo(1280,570)
# time.sleep(1)
# pyautogui.moveTo(1280,485)
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(100,750)
# time.sleep(1)

# prev_height= browser.execute_script("return articleListArea.scrollHeight")
# print("화면높이:", prev_height)
# while True:
#   # browser.execute_script("window.scroll(0,articleListArea.scrollHeight)")
#   pyautogui.scroll(-prev_height)
#   time.sleep(0.5)
#   curr_height = browser.execute_script("return articleListArea.scrollHeight")
#   if prev_height == curr_height: break
#   prev_height = curr_height
#   print("높이", prev_height)

# # all_height = browser.execute_script("return document.body.scrollHeight")
# # print("전체높이 : ",all_height)
# # print("-"*50)
# soup = BeautifulSoup(browser.page_source,'lxml')
# data = soup.select_one("#complexOverviewList > div.list_contents > div.item_area > div")
# with open("c1024/naver.html",'w',encoding='utf8') as f:
#   f.write(soup.prettify())

with open("c1024/naver.html",'r',encoding='utf8') as f:
  soup = BeautifulSoup(f,'lxml')
data = soup.select_one("#complexOverviewList > div.list_contents > div.item_area > div")
# if문을 이용한 억 변환은..서비스 종료다.

# real_p = 0
# 전세 최저가 매매 최저가 5개씩
houses = data.select("div.item_inner")
# house = data.select_one("div.item_inner")



# spec[1][:-3]
# print(spec)

# print("전/매:", hp_type)
# print("집값", h_price)
ah = []
lh = []

# 슬래쉬 (/) 로 나누고 뒤에 글자만 지우고 숫자만 남기고 가격 나누기 평방제곱미터해서 1m2당 가격 출력하기

def num_chg(h_price):
  b=h_price.split('억')
  f_num = int(b[0])*100000000
  if b[1].strip() != '':
    s_num = int(b[1].strip().replace(",",""))*10000
  else:
    s_num = 0
  price = f_num+s_num
  return price

def spec_chg(spec):
  spec_a = spec.split(",")
  spec_b = spec_a[0].split("/")
  spec_c = int(spec_b[1][:-2])
  return spec_c

for idx,house in enumerate(houses):
  print(f"{idx+1}.")
  hp_type = house.select_one("span.type").text.strip()
  if hp_type == "월세": 
    print("월세라 건너뛰었음")
    print("-"*100)
    continue
  h_name = house.select_one("div.item_title").text.strip()
  h_price = house.select_one("span.price").text.strip().strip().replace(",","")
  spec = house.select_one("div.info_area > p:nth-child(1) > span").text.strip()

  hp = num_chg(h_price)
  spec = spec_chg(spec)
  if hp_type == "매매":
   ah.append([h_name, hp_type, hp]) 
  else:
   lh.append([h_name, hp_type, hp]) 
  print("이름 : ", h_name)
  print("유형 : ", hp_type)
  print("가격 : ", h_price)
  print("평수 : ", spec,"m**2")
  print("-"*100)


ah.sort(key=lambda x:x[2])
lh.sort(key=lambda x:x[2])

print("매매 최저가 5개 : ", ah[:5])
print("전세 : 최저가 5개", lh[:5])






# input("엔터")