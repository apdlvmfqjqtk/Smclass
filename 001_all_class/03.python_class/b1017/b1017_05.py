# 딕셔너리로 입력
students = []
subject = ['번호','이름','국어','영어','수학','합계','평균','순위']
sub = ['no','name','kor','eng','math','total','avg','rank']

f = open("b1017/students.txt","r",encoding="utf-8")
while True:
  line = f.readline()
  if not line:
    break
  s = line.strip().split(",")

  # 문자는 패스, 정수,실수는 type int, float으로 변경하는 for문
  # ['20', 'cjakubovitsj', '75', '72', '70', '217', '72.3333333333', '1']
  for idx,i in enumerate(s):
    if idx == 1 : continue
    elif idx == 6: s[6] = float(i)
    else: s[idx] = int(i)
  # # for문 없이 작성시.
  # s[0] = int(s[0])
  # s[2] = int(s[2])
  # s[3] = int(s[3])
  # s[4] = int(s[4])
  # s[5] = int(s[5])
  # s[6] = float(s[6])
  # s[6] = int(s[7])
  students.append(dict(zip(sub,s)))
f.close
print(students)
print("프로그램을 종료합니다.")