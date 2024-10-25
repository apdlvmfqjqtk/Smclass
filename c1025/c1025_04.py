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

with open('c1025/mouse1.html','r',encoding='utf8') as f:
  soup = BeautifulSoup(f,'lxml')
data = soup.select_one("div.basicList_list_basis__uNBZx")

# pro_lists = data.select("div.adProduct_item__1zC9h")
# # 광고상품 리스트 4개
# f = open('c1025/nshop.csv','a',encoding='utf-8-sig',newline="")
# writer = csv.writer(f)
# try:
#   for i,pro_list in enumerate(pro_lists):
#   # 제목
#     title = pro_list.select_one("div.adProduct_title__amInq > a").text.strip()
#     print(title)
#     # 가격
#     price = int(pro_list.select_one("div.adProduct_price_area__yA7Ad > strong > span.price > span > em").text.replace(",",''))
#     print(price)

#     # 3. 평점
#     rating = float(pro_list.select_one("div.adProduct_etc_box__UJJ90 > span:nth-child(1) > a > span.adProduct_rating__PaMzh").text)
#     print(rating)
#     # 4. 평가수
#     a_count = int(pro_list.select_one("div.adProduct_etc_box__UJJ90 > span:nth-child(1) > a > em").text.replace(",",""))
#     print(a_count)
#     # 5. 찜 수
#     c_count = int(pro_list.select_one("div.adProduct_etc_box__UJJ90 > span:nth-child(2) > span").text.strip())
#     print(c_count)
#     price("-"*50)
#     writer.writerow([title,price,rating,count,c_count])
# except:
#   print("예외")  
  
pro_lists = data.select("div.product_item__MDtDF")
title = pro_lists[0].select_one("div.product_title__Mmw2K > a")

price = pro_lists[0].select_one("span.price_num__S2p_v>em")



# f.close()

