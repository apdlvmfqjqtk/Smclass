import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  #  에러 시 종료

# print(res.text)  #  타입: str

# 태그를 활용한 검색 방법
# find, find_all -> select, select_all


soup = BeautifulSoup(res.text,'lxml')
# print(soup.find("h2",{"class":"rankingnews_tit"}))
# print(soup.select_one("h2.rankingnews_tit").text)
# print(soup.select_one("div#header"))


# select_one, select 사용
data = soup.select_one("#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking")
news = data.select("div.rankingnews_box")
print(len(news))

for i in news:
  print(i)
  print("-"*50)
  
# print("언론사 : ",news.select_one("strong.rankingnews_name").text)
# news_lists = news.select_one("ul.rankingnews_list>li")
# for idx,news_list in enumerate(news_lists):
#   print(f"{idx+1} : ", news_list.select_one("div.list_content>a").text)




# 내꺼
# print(soup.select_one("strong.rankingnews_name").text)
# cont = soup.select_one("ul.rankingnews_list")
# print(len(cont))
# for i in cont:
#   print(cont.select_one("a").text)

# # html, csss파싱이 돼 이쁘게 출력
# print(soup.prettify()) 

