# 크롤링 - 웹상에 있는 컨텐츠 수집하는 작업(자동화 가능)
# api에서 정보를 긁어오기도 함

import requests
# res = requests.get("http://www.google.com") #html 소스를 가져옴.
res = requests.get("http://www.naver.com") #html 소스를 가져옴.
# res = requests.get("http://www.melon.com/") #html 소스를 가져옴.
res.raise_for_status() #  에러시 자동 종료

# requests 정보를 가져올 시 제이쿼리, 자바스크립트, 외부 페이지, react, vue...등은 가져오지 못함, 비동기식으로 잗

print("총 문자 길이 : ",len(res.text))
# print(res.text) # html 소스 출력

# # 웹 소스코드 파일 저장 (f.close 필수)
# f = open("a.html","w",encoding="utf-8")
# f.write(res.text)
# f.close

# f.close 생략해도 폴더가 자동으로 닫힘
with open("c1021/naver.html","w",encoding="utf-8") as f:
  f.write(res.text)



# # 이 코드로도 확인은 가능하나 코드가 김
# # if res.status_code == 200:
# #   print(res.text)
# # else:
# #   print("접근할 수 없습니다.")

# print("응답코드 : ", res.status_code)  # 200
# # 멜론과 구글 똑같이 url로 웹스크래핑을 시도하지만 멜론은 406에러가 뜬다.

# print(res.text)