# 다음 사이트에서 검색창에 '주식정보'를 검색해서 페이지 이동하기

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("https://www.daum.net")

elem =browser.find_element(By.ID,'q')
elem.click()
elem.send_keys("주식정보")
elem.send_keys(Keys.ENTER)

browser.get("http://www.naver.com")
elem = browser.find_element(By.ID,'query')
elem.send_keys("주식정보")
time.sleep(3)
elem.send_keys(Keys.ENTER)

time.sleep(100)













# import time
# import random

# print(random.uniform(1,3))


# # a = [0]*100
# # for i in range(100):
# #   a[i] = i

# b = [i for i in range(100)]
# for i in b:
#   print(i)
#   time.sleep(random.uniform(1,3))