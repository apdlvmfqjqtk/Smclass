import requests
from bs4 import BeautifulSoup

url = "http://finance.naver.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  #  에러 시 종료

soup = BeautifulSoup(res.text,'lxml')

# 기준점
data = soup.select_one("#container > div.aside > div > div.aside_area.aside_popular")

# 인기검색종목
print(f"[ {data.select_one("span").text} ]")
sum = 0
# 1, 2, 3, 4, 5위
pops = data.select("tbody>tr")
# print("개수 : ", len(pops))
for pop in pops:
  print("사명 : ", pop.select_one("th>a").text)
  print("주가 : ", pop.select_one("td").text)
  a = int((pop.select_one("td").text).replace(",",""))
  sum += a
  # next_sibling : 형제 관계, find_next_sibling : 형제 관계 중 검색
  # print("변동 : ", pop.select_one("td").find_next_sibling("td"))
  sps = pop.select_one("td").find_next_sibling("td").select("span")
  tit = ['변동','변동액']
  for idx,sp in enumerate(sps):
    print(tit[idx],":",sp.text.strip())
  print("-"*80)

print(f"합계 : {sum:,}")
  # print("변동1 : ", pop.select_one("td").find_next_sibling("td").select_one("span").text)
  # print("변동2. : ", pop.select_one("td").find_next_sibling("td").select_one("span").next.next.next.strip())

  # # 내꺼
  # print(pop.select_one("th").text)
  # print(pop.select_one("tr>td").text)