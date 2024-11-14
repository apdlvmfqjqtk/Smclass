# naver 파일 저장. 리솜리조트 파일 저장

import requests

# # url = requests.get("http://www.naver.com")                        # 네이버
# # url = requests.get("http://www.resom.co.kr/resom/main/main.asp")  # 리솜리조트
# # url = requests.get("http://www.coupang.com/")                        # 쿠팡

# url = [
#     "http://www.naver.com",
#     "http://www.resom.co.kr/resom/main/main.asp",
#     "http://www.daum.net",
# ]
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
# }
# for i in range(len(url)):

#     res = requests.get(url[i], headers=headers)
#     res.raise_for_status()  # 에러 발생시 자동 종료.

#     # 파일 저장
#     with open(f"c1021/{i}.html", "w", encoding="utf-8") as f:
#         f.write(res.text)

# print("프로그램 종료!")


url = "http://www.coupang.com"   # 대형 사이트의 경우 
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
print(res.text)
with open("c1021/coo.html", "w", encoding="utf-8") as f:
  f.write(res.text)