from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.yanolja.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
soup = requests.get(url,headers=headers)

# 브라우저 열기
browser = webdriver.Chrome()
# 창 크기 최대화
browser.maximize_window()
# url입력
browser.get(url)
time.sleep(0.7)
# 검색창 클릭
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/header/section/a[2]/div/div').click()
time.sleep(0.7)
# 날짜 클릭
browser.find_element(By.CLASS_NAME,'SearchInput_calendarButton__3sNMZ').click()
time.sleep(0.7)
# 입실날 선택
browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]').click()
time.sleep(0.7)
# 퇴실날 선택
browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[3]').click()
time.sleep(0.7)
# 확인버튼 클릭
browser.find_element(By.CLASS_NAME,'DateRangePicker_rangePickerConfirmButton__2c41H').click()
time.sleep(0.7)

# 강릉 호텔 입력 후 검색 클릭
elem = browser.find_element(By.CLASS_NAME,'SearchInput_input__342U2')
time.sleep(0.7)
elem.send_keys("강릉 호텔")
time.sleep(0.2)
elem.send_keys(Keys.ENTER)

# 검색 화면 대기
# 화면에 호텔 검색내용이 뜰때까지 대기, 최대 30초
elem = WebDriverWait(browser,30).until(lambda x:x.find_element(By.XPATH,'//*[@id="__next"]/div/main/section/div[2]'))

# 화면을 스크롤해서 내리기 반복
# excute_script() : 자바스크립트 실행 함수
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
  browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(0.7)
  # 페이지가 로딩되면서 길어진 길이를 다시 가져옴
  curr_height = browser.execute_script("return document.body.scrollHeight")
  # 페이지를 스크롤해서 길이가 더 길어졌는지 확인
  if prev_height == curr_height: 
    break

  # 더 길이가 길어졌으면, 이전 길이에 현재 길이를 입력시킴
  prev_height = curr_height


print("스크롤 내리기 완료. ")
soup = BeautifulSoup(browser.page_source,'lxml')
# html데이터 파일로 저장
with open('c1024/yanolja.html','w',encoding='utf8') as f:
  f.write(soup.prettify())


instar = float(input("최소 평점을 입력해주세요.(소수점 한자리까지만 입력가능) : "))
inmonry = int(input("최대 금액을 입력해주세요.(숫자만 입력해주세요.) : "))
input("enter키를 누르면 검색을 시작하겠습니다.")


# html파일 불러와서 soup으로 파싱
with open('c1024/yanolja.html','r',encoding='utf8') as f:
  soup = BeautifulSoup(f,'lxml')


# 평점 4.8이상 금액 15만원 이하만 출력
# 1. 
# 호텔명: 
# 평점
# 금액
# ---------
data = soup.select_one("div.PlaceListBody_listContainer__2qFG1")
rooms = data.select("div.PlaceListItemText_container__fUIgA")
# room = data.select_one("div.PlaceListItemText_container__fUIgA")
f_sc = 0
f_fa = 0
s_fa = 0
s_list = []
i = 0


for room in rooms:
  try:
    rating = float(room.select_one("span.PlaceListScore_rating__3Glxf").text.strip())
    money = int(room.select_one("span.PlacePriceInfoV2_discountPrice__1PuwK").text.replace(',',"").strip())
    if rating >= 4.5 and money <= 150000:  #  instar  inmonry
      print(f"{i+1}.")
      name = room.select_one("strong.PlaceListTitle_text__2511B").text.strip()
      print("호텔명: ",name)
      print(f"평점 : {rating}점")
      print("금액 : {}원".format(money))
      print("-"*60)
      i += 1
      f_sc += 1
      s_list.append([{i+1},name,rating,money])
    else:
      f_fa += 1
  except Exception as e:
    s_fa += 1

# 정렬
s_list.sort(key=lambda x:x[2],reverse=True)
print(s_list[:5])

# 금액 순차정렬
s_list.sort(key=lambda x:x[3])
print(s_list[:5])


print("조건 부합 숙소 개수 : ", f_sc)
print("조건 미달 숙소 개수 : ", f_fa)
print("예약 마감 숙소 개수 : ", s_fa)



# time.sleep(100000)