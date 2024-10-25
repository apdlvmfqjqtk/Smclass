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
with open("c1025/newses.csv",'rb') as f:
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
