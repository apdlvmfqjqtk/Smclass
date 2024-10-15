# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수

# 메뉴출력함수 시작
def title_program():
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("7. 학생성적정렬")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")
  return choice
# --------------------

# 1. 학생 성적 입력 함수 선언
def stu_input(stuNo):
  while True:
    no = stuNo + 1
    score = []
    print(f"{no}번째 학생 성적 입력")
    # for문 활용한 성적 변수 선언
    for i in range(3):
      num = int(input(f"{s_title[i+2]} 점수를 입력하세요"))
      total += num
      avg = total/3
      rank = 0
      score.append(num)
    # 새로 입력한 데이터 dict 형태로 변환
    s = {"no":no, "name":name, "kor":score[0], "eng":score[1], "math":score[2], "total":no, "avg":avg, "rank":rank, }
    students.append(s)
    stuNo += 1
    print(f"{name}학생 성적이 입력되었습니다.")





# 프로그램 시작
while True:
  title_program()
  if choice == "1":
    stu_input(stuNo)
  elif choice == "2":
    pass
  elif choice == "3":
    pass
  elif choice == "4":
    pass
  elif choice == "5":
    pass
  elif choice == "6":
    pass
  elif choice == "7":
    pass
  elif choice == "0":
    print("0. 프로그램 종료")
    print("프로그램을 종료합니다.")
    break











# print(sArr)

# # s = "11"
# # print(str.isdigit(s)) # 문자열이 숫자여이면 true, 아니면 false
# # ss = "a"
# # print(str.isdigit(ss) 



# print(sArr)


# stu_1 = "6, 홍길자, 100, 100, 100, 300, 100.0, 0"
# key_1 = ["no", "name", "kor", "eng", "math", "total", "avg", "rank",]
# sArr = stu_1.split(",")
# sArr[0] = 
# print(sArr)

# # 딕셔너리 생성 방법
# dict_1 = {"no":int(sArr[0]), "name":sArr[1], "name":int(sArr[2]), }
# print(dict_1)
# # zip
# dict_list = dict(zip(key_1,sArr))
# print(dict_list)