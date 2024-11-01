import oracledb
import datetime

nowYear = datetime.datetime.now().year

def connects():
  user = "ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외 : ", e)
  return conn

# # 회원수 확인
def member_count():
  ## oracledb mem테이블의 count 가져오기
  conn = connects()
  cursor = conn.cursor()
  # # employees 테이블 부서번호 10번
  # sql = "select count(*) no, a.department_id dept, department_name deptname\
  #        from employees a, departments b\
  #        where a.department_id = b.department_id and a.department_id = 50\
  #        group by a.department_id,department_name"
  sql = "select count(*) from mem"
  cursor.execute(sql)
  row = cursor.fetchone()
  cursor.close()  
  # return row
  return row[0]
  

### 회원수 확인값을 리턴하시오.
all_member = member_count()

print("[ 커뮤니티 ]")
# employees
# print(f"현재 회원수 : {all_member[0 ]}, 부서번호: {all_member[1]}, 부서명: {all_member[2]}")
print(f"현재 회원수 : {all_member}")
print()
print("1. 로그인")
print("2. 회원가입")
print("3. 회원정보 수정")
choice = input("원하시는 번호를 입력하세요. >> ")

if choice == "2":
  id = input("아이디를 입력하세요. >>")
  pw = input("패스워드를 입력하세요. >>")
  name = input("이름을 입력하세요. >>")
  birth = input("생년월일을 입력하세요. (예 : 20020312 )>>")
  age = nowYear - int(birth[:4]) # 나이 자동 계산
  gender = input("성별을 입력하세요.(Male, Female) >>")
  hobby = input("취미를 입력하세요. >>")

  my_list = [id,pw,name,age,birth,gender,hobby]

  print(my_list)

  # db접속
  conn = connects()
  cursor = conn.cursor()
  # sql = "insert into mem(id,pw,name,age,birth,gender,hobby) values(:1,:2,:3,:4,:5,:6,:7)"
  # cursor.execute(sql,my_list)
  sql = "insert into mem(id,pw,name,age,birth,gender,hobby) values(:id,:pw,:name,:age,:birth,:gender,:hobby)"
  cursor.execute(sql,id=id,pw=pw,name=name,age=age,birth=birth,gender=gender,hobby=hobby,)
  conn.commit()
  cursor.close()
  print("저장됐습니다.")


if choice == "3":
  # db접속
  conn = connects()
  cursor = conn.cursor()
  id = "aaa"
  sql = "select * from mem where id=:id"
  cursor.execute(sql,id=id)
  row = cursor.fetchone()
  print(f"아이디:{id}, 현재 취미 : {row[6]}")
  hobby = input("수정할 hobby를 입력하세요. >>")
  sql = "update mem set hobby =: hobby where id=:id"
  cursor.execute(sql,id=id,hobby=hobby)
  conn.commit()
  cursor.close()
  print("수정됐습니다.")