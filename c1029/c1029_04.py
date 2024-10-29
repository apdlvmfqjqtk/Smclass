import oracledb

def connections():
  try:
    conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
    print("DB연결 : ",conn.version)
  except Exception as e:
    print("예외 발생 : ", e)
  return conn

# 함수 호출
conn = connections()
cursor = conn.cursor()


# num1 = input("첫번째 숫자를 입력하세요")
# num2 = input("두번째 숫자를 입력하세요")
# # 월급 4000 - 8000 출력
# sql = "select * from employees where salary >= 4000 and salary <= 8000 OD"
# cursor.execute(sql)

# # 검색한 단어
# search = input("검색할 단어를 입력하세요. >>")
# search = '%'+search+'%'
# # employees테이블. emp_name a가 포함돼있는 row를 모두 출력하시오
# sql = "select * from employees where emp_name like :search"
# cursor.execute(sql,search=search)
# # 번호순서
# # sql = "select * from employees where employee_id>=:1"
# # cursor.execute(sql,[search])




sql = "select * from employees"
cursor.execute(sql)

title = ['employee_id', 'emp_name', 'salary']
a_list = [] # dict타입으로 변경해서 저장하시오
rows = cursor.fetchall()
for row in rows:
  a_list.append(dict(zip(title,row)))

# 딕셔너리로 바꾸는 이유는 후에 데이터 분석을 할 때 2차원 데이터로 만들기 쉽게 하기 위하여 만듬

conn.close()