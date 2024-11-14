import requests
from bs4 import BeautifulSoup  #  html이라는 형태의 소스 코드를 명령어가 들어갈 수 있도록 바꿔줌

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

with open("c1021/1.html","w",encoding="UTF-8") as f:
  f.write(res.text)

# html, css 정보를 가진 소스로 변경
soup = BeautifulSoup(res.text,"lxml") # str -> html태그, css태그 사용될 수 있는 형태로 변경됨

# BeautifulSoup 사용
# 태그 출력, 태그 글자 출력
print(soup.title)                       # title 태그
print(soup.title.text)                  # title 태그 문자 - text, get_text()
print("없는 태그 : ", soup.titletitle)  # 없는 태그 입력 시 None으로 출력해줌
# print("없는 태그 : ", soup.titletitle.get_text())  # 없는 태그 입력 시 에러 발생
print(soup.a)                           # a태그의 첫번째 것을 가져옴
print(soup.a.next)                      # a태그의 다음 태그 들고옴 (다음 a태그가 아님)
# 태그 속성 출력
print(soup.a.attrs)                     # 태그의 속성값을 가져옴 : dict 형태
print(soup.a["href"])                   # a태그의 href속성값을 가져옴

# 특정 정보 출력
# print(soup.find("div",attrs={"id":"header"}))
print(soup.find("div",{"id":"header"}))                   # div 태그 중에 id가 header인것 찾아줘
print(soup.find("h2",{"class":"rankingnews_tit"}).text)   # h2태그에 있는 class가 rankingbews_tit의 text를 출력해줘
print(len(soup.find_all("div")))                          # 모든 div태그를 검색해줘
print(type(soup.find_all("div"))) # ResultSet :객체의 리스트

# # soup.prettify() 정보 저장
# with open("c1021/2.html","w",encoding="utf8") as f:
#   # soup.prettify() : 소스가 정리되어 저장됨
#   f.write(soup.prettify())

print("완료")

# print(res.text)