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
# 이메일 발송 관련
import smtplib
from email.mime.text import MIMEText
# 이메일 첨부파일 추가
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


url = "https://news.naver.com/main/ranking/popularDay.naver"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(3)


# 모든 언론사 싹 긁어오기
  # 무선 마우스 창 내려서 정보를 모두 가져온 후 파일에 저장
prev_height = browser.execute_script("return document.body.scrollHeight")
# 스크롤 내리기 반복문
while True:
  browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(2)
  curr_height = browser.execute_script("return document.body.scrollHeight")
  try:
    browser.find_element(By.XPATH,'//*[@id="wrap"]/div[4]/button').click()
    time.sleep(2)
  except:
    print("드래그 끝")
  if prev_height == curr_height:
    break
  prev_height = curr_height
  print("스크롤 완료")

soup = BeautifulSoup(browser.page_source,'lxml')
with open(f'c1025/newsrank.html','w',encoding='utf-8') as f:
  f.write(soup.prettify())

with open(f"c1025/newsrank.html",'r',encoding='utf8') as f:
  soup = BeautifulSoup(f,'lxml')

data = soup.select_one("div.rankingnews_box_wrap")
boxes = data.select("div.rankingnews_box")
box = data.select_one("div.rankingnews_box")


f = open("c1025/news.csv",'a',encoding='utf-8-sig',newline="")
writer = csv.writer(f)
for box in boxes:
  titles = box.select("div.list_content>a")
  brodcast = box.select_one("strong.rankingnews_name").text.strip()
  # writer(brodcast)/
  writer.writerow([brodcast,])
  print("언론사 : ",brodcast)

  for i,title in enumerate(titles):
    no = (i+1)
    title = box.select_one(f"li:nth-child({i+1}) > div > a").text.strip()
    hour = box.select_one(f"li:nth-child({i+1}) > div > span").text.strip()
    print(f"{no}번째 뉴스 : {title}. 작성일 : {hour}")
    writer.writerow([no,title,hour])
  print("-"*80)  

f.close()

# 메일보내기
smtpName = "smtp.naver.com"
smtpPort = 587

# 자신의 네이버메일주소,id, pw, 받는사람이메일주소
sendEmail = ""
pw = ""
recvEmail = ""

title = "파이썬이메일보내기"
content = "파일첨부"

msg = MIMEMultipart()
msg["Subject"] = title
msg["from"] = sendEmail
msg["To"] = recvEmail
msg.attach(MIMEText(content))

# 파일 첨부
with open("c1025/news.csv",'rb') as f:
  attachment = MIMEApplication(f.read())  # 파일첨부
  attachment.add_header('Content-Disposition','attachment',filename="mouses.csv")
  msg.attach(attachment)

s = smtplib.SMTP(smtpName,smtpPort)
s.starttls() #  보안인증
s.login(sendEmail,pw)
s.sendmail(sendEmail,recvEmail,msg.as_string())
print("msg : ")
print(msg.as_string())
s.quit()

print("메일 발송 완료")
