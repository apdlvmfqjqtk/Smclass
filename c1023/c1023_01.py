import os
import requests
from bs4 import BeautifulSoup
import time
import csv

url = "http://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,'lxml')

# 기준점
data = soup.select_one("#contentarea > div.box_type_l > table") # 들고 오려는 데이터들이 포함된 부모 요소 들고오기(기준점)
stocks = data.select("tr") #  들고 오려는 데이터들 list형태로 저장
print(len(stocks))

# list - list 내포를 활용한 list 저장방식
# 1. 상단 타이틀
f = open('c1023/stock.csv','w',encoding='utf-8-sig')
writer = csv.writer(f)
st_list = [ st.text for st in stocks[0].select("th")  ]
writer.writerow(st_list)
# print(st_list) 
# print(len(st_list)) #  상단 타이틀 항목 12개

# 2. 
# print(stocks[1].select("td")) # 항목 1개
# sto_list = [ sto.text.strip().replace('\t','').replace('\n','') for sto in stocks[2].select("td")  ]
# print(sto_list)

# 30개 주식 정보를 csv파일로 저장
stock_list = []
for stock in stocks:
  sts = stock.select("td")
  if len(sts) <= 1: continue
  sto_list = [ st.text.strip().replace("\t","").replace("\n","")  for st in sts ]
  writer.writerow(sto_list)

f.close()
print("완료")

# for stock in stocks:
#   try:
#     sto_list = [ sto.text.strip().replace('\t','').replace('\n','') for sto in stocks[i+1].select("td") ]
#     stock_list.append(sto_list)
#   except:
#     print("빈 데이터")
#     pass
# print(stock_list)

# list 생성
# sts = stocks[0].select("th")     #  'th'값이 리스트 형태로 저장돼있기 때문에 바로 text쓰면 에러가 남(for문으로 꺼내줘야한다)
# st_list = []
# for st in sts:
#   print(st.text)
#   st_list.append(st)
# print(st_list)