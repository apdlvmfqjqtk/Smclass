import oracledb

# oracle과 연결 (보통 예외처리해야함 (오라클 문제로 내 컴이 에러가 날 시 면책이 가능하기 때문))
# sql developer 연결
conn = oracledb.connect(user="ora_user", password="1111", dsn="localhost:1521/xe")
# 연결확인
print(conn.version)

# # sql실행창 오픈
# cursor = conn.cursor()
# sql = "select count(*) from member"
# cursor.execute(sql)
# # 1개 데이터 검색된 내용 호출
# count1 = cursor.fetchone()
# print("개수 :", count1)

# 여러 개의 데이터 검색된 내용 호출
cursor = conn.cursor()
sql = "select * from member"
cursor.execute(sql)
# 1개 데이터 검색된 내용 호출
rows = cursor.fetchall()
# print(rows)
for i,row in enumerate(rows):
  i += 1
  print(f"ID: {row[0]}, PW: {row[1]}, NAME: {row[2]}, EMAIL: {row[3]}, PHONE: {row[4]}, GENDER: {row[5]}, HOBBY: {row[6]}, MDATE: {row[7]}")




# 항상 마지막에는 close() 해 줘야함
conn.close()