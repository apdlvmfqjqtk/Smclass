import random
import oracledb
import smtplib
from email.mime.text import MIMEText

## DB연결 함수 선언
def connects():
  user="ora_user"
  password = '1111'
  dsn = "localhost:1521/xe"
  try:
    conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e:
    print("예외처리 : ", e)
  return conn


## 시작화면 함수선언
def screen():
  # 로그인이 안돼있는 상태
  print("[ 커뮤니티 ]")
  print("1. 로그인")
  print("2. 비밀번호 찾기")
  print("3. 회원가입")
  print("4. 프로그램 종료")
  choice = input("번호를 입력해주세요. >>")
  return choice

# 1. 로그인 함수 선언
def memLogin():
  user_id = input("아이디를 입력하세요. >>")
  user_pw = input("패스워드를 를 입력하세요. >>")
  # db접속
  conn = connects()
  cursor = conn.cursor()
  sql = "select * from member where id=:id and pw=:pw"
  cursor.execute(sql,id=user_id,pw=user_pw)
  row = cursor.fetchone()
  cursor.close()
  if row == None:
    print("아이디 또는 패스워드가 일치하지 않습니다. 다시 입력하세요.")
    return
  # 이후 프로그램
  print(f"{row[2]}님, 환영합니다.")
  print()



## 랜덤 비밀번호 생성 함수 선언
def random_pw():
  a = random.randrange(0,10000) # 0-9999
  ran_num = f"{a:04}"
  print("랜덤번호 : ",ran_num)
  return ran_num


# 메일 발송 함수선언
def emailSend(email):
  # email 발송
  smtpName = 'smtp.naver.com'
  smtpPort = 587

  sendEmail = 'tjdwkwnsla1@naver.com'
  pw = 'ECF8JTXMDJEL'
  recvEmail = email

  title = '[메일발송] 임시번호 안내'

  ran_num = random_pw()

  # 설정 
  content = f'임시비밀번호 {ran_num}'
  print(content)
  msg = MIMEText(content)
  msg['Subject'] = title
  msg['From'] = sendEmail
  msg['To'] = recvEmail

  # 서버이름, 서버포트
  s = smtplib.SMTP(smtpName,smtpPort)
  s.starttls()
  s.login(sendEmail,pw)
  s.sendmail(sendEmail,recvEmail,msg.as_string())
  s.quit()

  # 메일 발송완료
  print("메일이 발송되었습니다.")
  return ran_num

  # 비밀번호찾기 함수선언
def searh_pw():
  user_id = input("아이디를 입력하세요. >>")
  # db접속
  conn = connects()
  cursor = conn.cursor()
  sql = "select * from member where id=:id"
  cursor.execute(sql,id=user_id)
  row = cursor.fetchone()

  if row == None:
    print("아이디가 존재하지 않습니다. 다시 입력해주세요")
    return

  input(f"{row[0]}아이디가 존재합니다. 메일을 보내려면 엔터를 입력하세요. >>")
  print("이메일 :",row[3])

  # ##이메일발송함수 호출
  ran_num = emailSend(row[3])

  # 임시비밀번호를 update
  sql = 'update member set pw=:pw where id=:id'
  cursor.execute(sql, pw=ran_num, id=user_id)
  conn.commit()