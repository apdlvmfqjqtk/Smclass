import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

print(soup.title)           # 제일 먼저 찾아지는 것을 출력
print(soup.find("title"))   # 특정 위치의 태그를 출력
print(soup.find("div",{"class":"rankingnews_box_wrap"}))
newLists = soup.find("div",{"class":"rankingnews_box_wrap"}).find_all("div",{"class":"rankingnews_box"})
print("여러개 개수 확인 : ", len(newLists))

for newList in newLists:
  print(newList.find("strong",{"class":"rankingnews_name"}))

# # find : 1개 검색
# rankingnews_wrap = soup.find("div",{"rankingnews_box_wrap"})
# # find_all : 여러개 검색
# rankingnews_boxes = rankingnews_wrap.find_all("div",{"class":"rankingnews_box"})
# print(len(rankingnews_boxes))
# # print(rankingnews_boxes.find("strong",{"class":"rankingnews_name"})) 오답

# print(len(soup.find_all("div",{"class":"rankingnews_box"})))