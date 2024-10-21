import requests
from bs4 import BeautifulSoup

url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')
# # 찾고자 하는 text가 한번에 찾아지지 않으면 위에 서부터 찾아가면 된다.
# print(soup.find("div",{"id":"bestPrdList"}).find("h3").text)

# 1-28위 제목 가격 출력
lists = soup.find("div",{"id":"bestPrdList"})
for i in lists:
  prod = lists.find("ul",{"class":"cfix"})
  pnpp = prod.find("div",{"class":"pname"})
  pname = pnpp.p.text
  pprice = pnpp.find("span",{"class":"price_detail"})

  print(pname)
  print(pprice.text)

# print(soup.find("div",{"id":"bestPrdList"}).find("div",{"class":"pname"}).p.text)
# print(soup.find("div",{"id":"bestPrdList"}).find("span",{"class":"price_detail"}).text)


# # 제목 출력 
# print(soup.find("div",{"id":"bestPrdList"}).find("div",{"class":"pname"}).p.text)

