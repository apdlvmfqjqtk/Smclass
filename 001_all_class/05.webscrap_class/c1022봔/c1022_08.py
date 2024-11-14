import os
import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

# print(res.text)
soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())

#  제목, 금액, 평점, 평가수
# 기준점
data = soup.select_one("#productList")

# 금액이 90만원 이상이면서 평점 4.5이상, 평가수 500명 이상일때만 출력
lists = data.select("li")
n_lists = []
f = open("c1022/coupang.txt","w",encoding='utf8')

for i in range(len(lists)):
  n_list = [] # 제목, 금액, 평점, 평가수, 링크, 이미지
  print(i)
  try:
    price = int(lists[i].select_one("strong.price-value").text.replace(",",""))
    rating = float(lists[i].select_one("em.rating").text)
    num = int(lists[i].select_one("span.rating-total-count").text[1:-1])
    if price >= 900000 and rating >= 4.5 and num >= 500:
      n_list = ""
      print("링크 : ","https://www.coupang.com"+lists[i].select_one("a")["href"])
      print("제목 : ",lists[i].select_one("div.name").text)
      print("금액 : ", price)
      print("평점 : ", rating)
      # print("평점 : ", lists[0].select_one("em.rating").text)
      print("평가수 : ", num)
      # print("평가수 : ", lists[i].select_one("span.rating-total-count").text)
      print("이미지 : ","https:/"+lists[i].select_one("dt.image>img")['src'][1:])
      print("--"*50)
    else: 
      print("스킵")
      pass
    n_list.append
  except Exception as e:
    print("에러 : ", e)
    pass
  f.write(','.join(n_list)+'\n')
  n_lists.append(n_list)
f.close()


































# # 금액이 90만원 이상이면서 평점 4.5이상, 평가수 500명 이상일때만 출력
# lists = data.select("li")
# print("링크 : ","https://www.coupang.com"+lists[0].select_one("a")["href"])
# print("제목 : ",lists[0].select_one("div.name").text)
# price = int(lists[0].select_one("strong.price-value").text.replace(",",""))
# print("금액 : ", price)
# rating = float(lists[0].select_one("em.rating").text)
# print("평점 : ", rating)
# # print("평점 : ", lists[0].select_one("em.rating").text)
# num = int(lists[0].select_one("span.rating-total-count").text[1:-1])
# print("평가 : ", num)
# print("평가수 : ", lists[0].select_one("span.rating-total-count").text)
# # print("이미지 : ", )