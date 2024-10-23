from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random

# 자동 로그인 장치 

url = "http://www.naver.com"
# 크롬브라우저 열기
browser = webdriver.Chrome()
# 네이버 페이지 이동
browser.get(url)
# 로그인버튼 선택
elem = browser.find_element(By.CLASS_NAME,"MyView-module__link_login___HpHMW")
# 로그인버튼 클릭
elem.click()
time.sleep(random.randint(2,5))



# 1. JS사용 (매크로감지 덜당함)
# 자바스크립트 호출방법
id = ""
pw = ""
input_js = 'document.getElementById("loginId--1").value="{id}";\
  document.getElementById("password--2").value = "{pw}";'.format(id="", pw='')
browser.execute_script(input_js)
time.sleep(random.randint(2,5))
# 로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME,"btn_login")
elem.click()
# # 브라우저 등록안함
# elem = browser.find_element(By.ID,"new.dontsave")
# elem.click()

# 완료
time.sleep(100)

# -----------------------------
# 2. selenium 사용
# # id값을 입력
# elem = browser.find_element(By.ID,"id")
# elem.send_keys("onulee") # 본인 아이디 입력
# time.sleep(random.randint(2,5))
# # pw값을 입력
# elem = browser.find_element(By.ID,"pw")
# elem.send_keys("1111") # 본인 패스워드 입력
# time.sleep(random.randint(2,5))
# 로그인 버튼 클릭
# elem = browser.find_element(By.CLASS_NAME,"btn_login")
# elem.click()

# 완료
time.sleep(100)