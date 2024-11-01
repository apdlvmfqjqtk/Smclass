# 학생성적 프로그램
# 1. 학생성적 입력
# 2. 학생성적 출력
# 3. 학생성적 검색
# students table 사용
# 번호는 students_seq 생성해서 입력
# 김유신 99 98 96 합계 평균 등수 입력일

import oracledb

def connects():
  user="ora_user"
  password = '1111'
  dsn = "localhost:1521/xe"
  try:
    conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e:
    print("예외처리 : ", e)
  return conn

print("[ 학생성적 프로그램 ]")
print("1. 학생성적 입력")
print("2. 학생성적 출력")
print("3. 학생성적 검색")

choice = input("원하시는 번호를 입력해주세요.")

if choice == "1":
  print("[ 학생성적 입력 ]")
  print
  name = input("이름을 입력하세요. >>")
  kor = int(input("국어 점수를 입력하세요. >>"))
  eng = int(input("영어 점수를 입력하세요. >>"))
  math = int(input("수학 점수를 입력하세요. >>"))
  total = kor+eng+math
  avg = (kor+eng+math)/3
  rank = 0
  s_list = [name, kor, eng, math, total, avg, rank]
    # db접속
  conn = connects()
  cursor = conn.cursor()
  # sql = "inser
  sql = "insert into students (no,name,kor,eng,math,total,avg,rank,sdate) values(stu_seq.nextval,:1,:2,:3,:4,:5,:6,:7,sysdate)"
  cursor.execute(sql,s_list)
  conn.commit()
  cursor.close()
  print("저장됐습니다.")

elif choice == "2":
  print("[ 학생성적 출력 ]")
  conn = connects()
  cursor = conn.cursor()
  sql = "select * from students"
  cursor.execute(sql)
  conn.commit()
  rows = cursor.fetchall()
  cursor.close()
  for row in rows:
    print(row)


elif choice == "3":
  print("[ 학생성적 검색 ]")
  name = input("찾으려는 학생 이름을 입력해주세요. >>")
  # db접속
  try: 
    conn = connects()
    cursor = conn.cursor()
    sql = "select * from students where name=:name"
    cursor.execute(sql,name=name)
    conn.commit()
    row = cursor.fetchone()
    cursor.close()
    print(f"검색하신 {name}학생 정보입니다. : {row}")
  except Exception as e:
    print(f"{name}학생을 찾지 못하였습니다. 이름이 없거나 잘못 입력하셨습니다.")
    print(e)


# # db접속
# conn = connects()
# cursor = conn.cursor()
# # sql = "insert into mem(id,pw,name,age,birth,gender,hobby) values(:1,:2,:3,:4,:5,:6,:7)"
# # cursor.execute(sql,my_list)
# sql = "insert into mem(id,pw,name,age,birth,gender,hobby) values(:id,:pw,:name,:age,:birth,:gender,:hobby)"
# cursor.execute(sql,id=id,pw=pw,name=name,age=age,birth=birth,gender=gender,hobby=hobby,)
# conn.commit()
# cursor.close()
# print("저장됐습니다.")