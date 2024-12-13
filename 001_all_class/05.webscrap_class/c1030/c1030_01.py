import oracledb
import random
# 이메일 발송 관련
import smtplib
from email.mime.text import MIMEText
# 이메일 첨부파일 추가
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 이메일 기본 설정
smtpName = "smtp.naver.com"
smtpPort = 587

# 자신의 네이버메일주소,id, pw, 받는사람이메일주소
sendEmail = "보내는 이메일 주소"
pw = "보내는 이메일의 비번"
recvEmail = "받는 사람의 이메일 주소"

def connects():
  user="ora_user"
  password = '1111'
  dsn = "localhost:1521/xe"
  try:
    conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e:
    print("예외발생 : ", e)
  return conn

while True:
  print("[ 커뮤니티 ]")
  print("1. 로그인")
  print("2. 비밀번호 찾기")
  print("3. 회원가입")
  print("0. 프로그램 종료")
  print("-"*30)
  choice = input("원하는 번호를 입력하세요. >>")

  if choice == "1":
    print("[ 로그인 ]")
    user_id = input("아이디를 입력하세요. >>")
    user_pw = input("패스워드를 입력하세요. >>")
    # db 접속
    conn = connects()
    cursor = conn.cursor()
    sql = "select * from member where id=:id and pw=:pw"
    cursor.execute(sql,id=user_id,pw=user_pw)
    row = cursor.fetchone()
    # print(row)
    if row != None:
      print(f"로그인에 성공하였습니다. {row[2]}님 환영합니다.")
    else:
      print("아이디 또는 패스워드가 일치하지 않습니다. 다시 입력해주세요.")
    cursor.close()

    # 오라클 DB에 접속해서 member 테이블에서 검색해서 가져옴


    # if user_id == 'aaa' and user_pw == '1111':
    #   print("로그인 성공")
    # else:
    #   print("로그인 실패")
    #   continue
  elif choice == "2":
    print("[ 비밀번호 찾기 ]")
    search = input("해당 아이디를 입력하세요. >>")
    # 입력한 아이디가 있는지 확인
    conn = connects()
    cursor = conn.cursor()
    sql = "select * from member where id=:id"
    cursor.execute(sql,id=search)
    row = cursor.fetchone()
    print(row)
    if row != None:
      print("아이디가 존재합니다. 임시비밀번호를 발급합니다.")
      # 1. 임시 비밀번호를 생성해서
      # 2. 이메일로 보낸다.
      # 3. 아이디에 비밀번호를 임시 비밀번호로 수정합니다.
      # 4. 임시번호로 로그인을 했을 경우 로그인 성공이 나타나도록 하시오

      # 1. 임시 비밀번호 생성
      a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
      a = random.randrange(0,100000000)  # 0~9999
      ran_num = f"{a:08}"
      print(ran_num)
      

      # 메일 발송
      title = "임시 비밀번호 입니다"
      content = f"""\
        파이썬에서 임시 비밀번호를 보냅니다.
        {ran_num}
        해당 번호로 로그인하시면 됩니다.
        """
      msg = MIMEText(content)
      msg['Subject'] = title
      msg['From'] = sendEmail
      msg['To'] = recvEmail

      s = smtplib.SMTP(smtpName,smtpPort)
      s.starttls()
      s.login(sendEmail,pw)
      s.sendmail(sendEmail,recvEmail,msg.as_string())
      s.quit()
      print("메일 발송 완료")

      # de에 임시 비번 저장
      # conn = connects()
      # cursor = conn.cursor()
      # sql = "alter table member modify pw VARCHAR2(:qqqx)"
      # cursor.execute(sql,qqqx=str(len(ran_num)))
      sql = "update member set pw=:pw where id=:id"
      cursor.execute(sql,id=search,pw=ran_num)
      conn.commit()

      print("파일이 수정됐습니다.")
      cursor.close()
      print("발급받은 비밀번호로 로그인을 진행해 주세요")
      

    else:
      print("아이디가 존재하지 않습니다.")
  elif choice == "3":
    pass
  elif choice == "0":
    print("프로그램을 종료합니다.")
    break