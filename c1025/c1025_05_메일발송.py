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
import smtplib
from email.mime.text import MIMEText

smtpName = "smtp.naver.com"
smtpPort = 587

# 자신의 네이버메일주소,id, pw, 받는사람이메일주소
sendEmail = ""
pw = ""
recvEmail = ""

title = "제목, 파이썬 이메일보내기 안내"
content = """\
  파이썬에서 text 이메일을 보냅니다.
  여러줄 쓰기 형태로 보냅니다.
  네이버 smtp서버를 사용해서 보냅니다.
  """

# 설정
msg = MIMEText(content)
msg['Subject'] = title
msg['From'] = sendEmail
msg['To'] = recvEmail
print("msg 데이터 : ",msg.as_string())

s = smtplib.SMTP(smtpName,smtpPort)
s.starttls()
s.login(sendEmail,pw)
s.sendmail(sendEmail,recvEmail,msg.as_string())
s.quit()

# 메일 발송 완료
print("메일을 발송했습니다.")