import oracledb

def connects():
  user="ora_user"
  password="1111"
  dsn="localhost:1521/xe"
  try: 
    conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e:
    print("예외사항 : ", e)
  return conn



### 입력한 달 이상의 입사한 사원을 출력하시오
d_day = int(input("숫자를 입력하세요. >>"))
# d_day = f"0{d_day}"
# d_day = "{:02}".format(d_day)
print(d_day)

conn = connects()
cursor = conn.cursor()

sql = "select hire_date,substr(hire_date,4,2) as hire_date2 from employees\
       where substr(hire_date,4,2) >= :d"
cursor.execute(sql,d=d_day)
rows = cursor.fetchall()
cursor.close()

for row in rows:
  print(row)


print("프로그램 종료")

