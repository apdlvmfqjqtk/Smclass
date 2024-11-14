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
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")

# 노트북 페이지 1,2,3dptj
# 만족도 95이상, 금액 1500000이하, 평가수 100이상

for i in range(3):
  url = f"https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=61&p={i+1}"
  browser = webdriver.Chrome(options=options)
  browser.maximize_window()
  browser.get(url)
  soup = BeautifulSoup(browser.page_source,'lxml')
  # 파일 저장하기
  with open(f"c1024/gmarket{i+1}.html",'w',encoding='utf8') as f:
    f.write(soup.prettify())
  browser.get_screenshot_as_file(f"gmarket{i+1}.png")

# i = 0
# # for i in range(3):
# with open(f'c1024/gmarket{i+1}.html','r',encoding='utf8') as f:
#   soup = BeautifulSoup(f,'lxml')
  
# data = soup.select_one("div#section__inner-content-body-container")
# labtops = data.select("div.box__item-container")
# labtop = data.select_one("div.box__item-container")
# # for labtop in labtops:
# money = int(labtop.select_one("strong.text__value").text.replace(",","").strip())
# point = int(labtop.select_one("span.image__awards-points").text.strip()[4:6])
# num = (labtop.select_one("li.list-item list-item__feedback-count").text.strip())
# print(num)