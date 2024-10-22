import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')
with open("c1022/melo.html","w",encoding="utf8") as f:
  f.write(soup.prettify())
# print(soup.prettify())
# 순위, 사진링크주소, 제목,  가수명 들고오기

chart = soup.select_one("#frm > div > table > tbody")
lists = chart.select("tr")
# print(lists[0].select_one("span.rank").text)
# print(lists[0].select_one("#lst50 > td:nth-child(4) > div > a > img"))

for list in lists:
  print(list.text.strip(),end="\t")
  print("-"*80)
# sing = lists[0].select("span")
