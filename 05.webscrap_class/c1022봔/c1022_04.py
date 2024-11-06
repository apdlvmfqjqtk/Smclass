import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)

soup = BeautifulSoup(res.text,'lxml')
with open("c1022/mon.txt","w",encoding="utf8") as f:
  f.write(res.text)

chart = soup.select_one("table.type_5")
tits = chart.tr
# print(tits.text)  #   제목
# print("-"*100)
# print(tits.find_next_siblings("tr")) 내용
conts = tits.find_next_siblings("tr")
for cont in conts:
  # print(cont.text.strip())
  print("-"*100)
  for c in cont:
    print(c.text.strip())
# tits = soup.select("tr.type1>th")

# for tit in tits:
#   print(tit.text,end="\t")
# print()
# print("-"*100)

