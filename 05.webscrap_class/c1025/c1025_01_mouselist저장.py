from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui


# 제목, 금액, 평점, 평가수, 찜. 1-5페이지
# 평점 4.8이상, 평가수 1000명 이상인 상품은 csv파일로 저장하고 출력


# 네이버에서 네이버 쇼핑으로 검색해 이동 및 무선 마우스 검색해 출력
url = "https://www.naver.com/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# 검색창에 '네이버 쇼핑' 입력 및 엔터
elem = browser.find_element(By.ID,"query")
elem.click()
time.sleep(1)
elem.send_keys("네이버 쇼핑")
elem.send_keys(Keys.ENTER)

# 네이버 쇼핑 클릭해 이동
time.sleep(3)
browser.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div/div/div[1]/div/div[2]/a').click()

# 쇼핑 화면 검색창이 뜰 때까지 기다렸다가 검색창에 '무선 마우스' 검색하기
# 최대 30초 동안 네이버 쇼핑 검색창이 뜨는지 대기하기

# 새로 열린 탭으로 selenium을 옮김
browser.switch_to.window(browser.window_handles[1])

WebDriverWait(browser,30).until(lambda x:x.find_element(By.CLASS_NAME,'_searchInput_search_text_3CUDs'))
# print(browser.window_handles)
# browser.to_swi
elem = browser.find_element(By.CLASS_NAME,'_searchInput_search_text_3CUDs')
elem.click()
time.sleep(1)
elem.send_keys("무선 마우스")
time.sleep(1)
elem.send_keys(Keys.ENTER)
time.sleep(random.randint(2,4))


url = browser.current_url
for i in range(5):
# --------------------------------------------------
  # 무선 마우스 창 내려서 정보를 모두 가져온 후 파일에 저장
  prev_height = browser.execute_script("return document.body.scrollHeight")
  # 스크롤 내리기 반복문
  while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
      break
    prev_height = curr_height
    print("스크롤 완료")

  soup = BeautifulSoup(browser.page_source,'lxml')
  with open(f'c1025/mouse{i+1}.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())
  time.sleep(random.randint(2,5))
  if i+1 == 5:
    break
  browser.find_element(By.XPATH,f'//*[@id="content"]/div[1]/div[4]/div/a[{i+1}]').click()
  time.sleep(random.randint(2,5))
  print(url)
print("1-5페이지 저장 완료")
# time.sleep(1000)
# -------------------------------------


# 리뷰 수 숫자로 바꾸는 함수
def rivint(e):
  if '만' in e:
    num = e.replace("만","").replace(".","")
    end = int(num)*1000
    return end
  elif ',' in e:
    num = e.replace(",","")
    end = int(num)
    return end
  else:
    end = int(e)
    return end
# ----------------------

item_list = []
f = open("c1025/mouses.csv",'a',encoding='utf-8-sig',newline="")
writer = csv.writer(f)


with open(f"c1025/mouse{i+1}.html",'r',encoding='utf8') as f:
  soup = BeautifulSoup(f,'lxml')
data = soup.select_one("div.basicList_list_basis__uNBZx")
items = data.select("div.adProduct_item__1zC9h")
# #### html파일 불러와서 마우스 정보 출력 (이름, 금액, 평점, 평가수, 찜) 총 5가지
# 광고 상품들 저장





# 광고가 아닌 상품들 저장
for i in range(5):
  with open(f"c1025/mouse{i+1}.html",'r',encoding='utf8') as f:
    soup = BeautifulSoup(f,'lxml')
  data = soup.select_one("div.basicList_list_basis__uNBZx")
  items = data.select("div.product_item__MDtDF")
  # item = data.select_one("div.product_item__MDtDF")


  for idx,item in enumerate(items):
    try:
      name = item.select_one("div.product_title__Mmw2K > a").text.strip()
      cost = int(item.select_one("span.price_num__S2p_v").text.strip().replace(",","")[:-1])
      star = float(item.select_one("span.product_grade__IzyU3").text.replace("별점","").strip())
      riveiw = item.select_one("div.product_etc_box__ElfVA > a > em").text.strip()[1:-1].strip()
      zzim = item.select_one("span.product_etc__LGVaW").text.replace("찜","").strip().replace(",","")

      intr = rivint(riveiw)
      print('번호 : ', idx+1)
      print("이름 : ", name)
      print("금액 : ", cost)
      print("평점 : ", star)
      print("평가수 : ", intr)
      print("찜 수 : ", zzim)
      print("-"*60)
      writer.writerow([name,cost,star,intr,zzim])
    except Exception as e:
      print("정보 부족으로 패스")
      print(e)
      print("-"*60) 


time.sleep(1000)



# # # 1.상단타이틀. csv파일로 저장
# # f = open('c1023/stock.csv','w',encoding='utf-8-sig',newline="")
# # writer = csv.writer(f)
# # m_list = [ st.text  for st in stocks[0].select("th") ]
# # writer.writerow(m_list)