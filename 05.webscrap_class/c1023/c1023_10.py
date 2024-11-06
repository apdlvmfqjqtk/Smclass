# 금액 5만원이하
# 김포제주 5만원이하 :15개
# 제주김포 5만원이하 30개
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random





url = "https://flight.naver.com/flights/domestic/GMP-CJU-20241106/CJU-GMP-20241109?adult=2&child=0&infant=0&fareType=YC&selectedFlight="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')
with open("flight.html","w",encoding="utf8") as f:
  f.write(soup.prettify())

print(soup)