import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv



# 웹스크래핑 시작
# url = f"https://search.daum.net/search?w=tot&q={syear}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
# browser = webdriver.Chrome()
# # 이동하려는 주소 입력
# browser.get(url)
# time.sleep(3)
# soup = BeautifulSoup(browser.page_source,"lxml")
# # html 파일 저장하기
# with open(f'Smclass/d1107/screen{syear}.html','w',encoding='utf-8') as f:
#   f.write(soup.prettify())

s_list = []
for syear in range(2020,2024):
  with open(f'Smclass/d1107/screen{syear}.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')
    print(f"{syear}년도 ----------------------")
    # 기준점
    data = soup.select_one("#mor_history_id_0 > div > div.flipsnap_view > div > div:nth-child(1) > c-flicking-item > c-layout > div > c-list-doc > ul")
    screens = data.select("li")
    for i,screen in enumerate(screens):
      print(f"{i+1}. ------------------")
      s_img = screen.select_one(".wrap_thumb img")['src']
      title = screen.select_one(".tit-g.clamp-g").text.strip()
      number = int(screen.select_one(".conts-desc.clamp-g").text.strip()[3:-2].replace(",",""))
      sdate = screen.select_one(".conts-subdesc.clamp-g").text.strip()[:-1]
      s_list.append([title,number,sdate])
      # 파일 저장
      # 파일 저장을 하지 않고 s_list에 모든 데이터를 담아서 뒤에서 모두 저장

  # 파일저장
topTitle = ['제목','관객수','날짜']
  # f.write('제목,관객수,날짜\n')  # 1번만 글 저장
with open('Smclass/d1107/screens.txt','w',encoding="utf-8") as f:
  f.write(s_list)

print("프로그램 완료")

















# a_list = ['서울의 봄','100','2024-11-07']

# with open('Smclass/d1107/s.txt','w',encoding='utf-8') as f:
#   f.write('제목','관객수','날짜')
#   for i in range(10):
#     f.write(f'{a_list[0]},{a_list[2]},{a_list[2]}\n')


# # with open('Smclass/d1107/s.txt','w',encoding='utf-8') as f:
# #   a_title = ['제목','관객수','날짜']
# #   f.write(','.join(a_title)+'\n')
# #   for i in range(10):
# #     f.write(','.join(a_list)+'\n')

# print("프로그램 완료")