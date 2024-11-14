# 오라클 db에는 타입 결정
# 문자형(숫자만) 타입+ 숫자와 사칙연산 됨.
# 파이썬에서 호출한 타입의 결과값이 어떻게 되는지 확인

import oracledb

def connects():
  user = "ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외 : ", e)
  return conn

conn = connects()
cursor = conn.cursor()
# sql : "select no,to_char(kor,'1000000'),to_char(kor,'1,000,000') from chartable2 ;"
# sql = "select * from chartable"
cursor.execure(sql)
rows = cursor.fetchall()

for row in rows:
  print(f"두 수의 합 : {row[1]+row[2]}" )   # 오라클에서는 계산이 가능하지맍만 oracle의 병우 별
  print(row)
  
  conn.close()