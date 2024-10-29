import oracledb
## sql developer 실행과 똑같다.
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')

## sql 창이 열림
cursor = conn.cursor()

# sql 작성, 실행
num = input("숫자를 입력하세요. >>")
num2 = input("숫자를 입력하세요. >>")
num3 = input("숫자를 입력하세요. >>")
n_list = [num,num2,num3]
n_list.sp


# # 10, 20, 30 검색해서 출력
# sql = "select * from students where no in (:no1, :no2, :no3)"
# cursor.execute(sql,no1=num,no2=num,no3=num)

# list 값으로 전달
# execute뒤에는 dict,list,tuple만 가능
# sql = "select * from students where no in (:1, :2, :3)"
# cursor.execute(sql,n_list)

# # execute함수 : 변수 추가
# sql = "select * from students where no >= no"
# cursor.execute(sql,no=num)

# # 문자열함수 f사용
# sql = f"select * from students where no >={num}"
# cursor.execute(sql)

# 데이터 가져오기 - fetchone(): 1개 가져오기, fetchmany(): 정해진 수 만큼 가져오기, fetchall(): 모든 데이터 가져오기
rows = cursor.fetchall()

titles = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수', '등록일']

for title in titles:
  print(title,end='\t')
print()
print("-"*80)


for row in rows:
  for i,r in enumerate(row):
    if i == 1:
      print(f"{r:10s}",end='\t')
      continue
    if i == 6:
      print(f"{r:.2f}",end='\t')
      continue
    if i == 8:
      # strftime()함수 : 날짜포맷함수 %Y = 2024, %y = 24
      print(r.strftime("%Y-%m-%d"),end='\t')
      continue
    print(r,end='\t')
  print()

conn.close()