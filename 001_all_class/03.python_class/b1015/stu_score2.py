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

# 0.메뉴 출력 함수 선언
def title_program():
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생 성적 입력")
  print("2. 학생 성적 출력")
  print("3. 학생 성적 수정")
  print("4. 학생 성적 검색")
  print("5. 학생 성적 삭제")
  print("6. 학생 등수 처리")    # 보통 DB영역
  print("7. 학생 성적 정렬")    # 보통 DB영역
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
    total = 0
    name = input(f"{no}번째 학생 이름을 입력하세요 (0번은 뒤로가기) : ")
    if name == "0":
      print("[ 이전 화면 이동 ]")
      break
    # for문 활용한 성적 변수 선언
    for i in range(3):
      num = int(input(f"{s_title[i+2]} 점수를 입력하세요. : "))
      total += num
      avg = total/3
      rank = 0
      score.append(num)
    # 새로 입력한 데이터 dict 형태로 변환
    s = {"no":no, "name":name, "kor":score[0], "eng":score[1], "math":score[2], "total":total, "avg":avg, "rank":rank, }
    students.append(s)
    stuNo += 1
    print(f"{name} 학생 성적이 입력되었습니다.")
    
    return stuNo
# ---------------------------------------------------------------

# 2. 학생 성적 출력 함수 선언
def stu_output(students):
  print("[ 학생 성적 출력 ]")
  print()
  # 상단 제목 출력(번호, 이름, 성적...)
  for st in s_title:
    print(st,end="\t")
  print()  
  print("-"*60)  

  # 하단 내용 출력(1, 홍길동, 100....)
  for s in students:
    print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
  print()
# -----------------------------------------------------------------

# 3. 학생 성적 수정 함수 선언
def stu_search(students):
  print("[ 학생 성적 검색 ]")
  while True:
    name = input("수정하려는 학생 이름을 정확히 입력해주세요. (0.이전 메뉴): ")
    if name == "0":
      break
    for s in students:
      if name == s['name']:
        print(f"{name} 학생이 있습니다.")
        print()
        print("[수정 과목 선택]")
        print("1. 국어 성적")
        print("2. 영어 성적")
        print("3. 수학 성적")
        choice = input("수정하려는 과목을 선택해주세요. (0.이전 메뉴): ")
        if choice == "1":
          print("이전 국어 점수 : ",{s['kor']})
          s['kor'] = input("변경 국어 점수 : ")
        elif choice == "2":
          print("이전 국어 점수 : ",{s['kor']})
          s['kor'] = input("변경 국어 점수 : ")
        elif choice == "3":
          print("이전 국어 점수 : ",{s['kor']})
          s['kor'] = input("변경 국어 점수 : ")
# ----------------------------



# 프로그램 시작
while True:
  choice = title_program()
  if choice == "1":
    stu_input(stuNo)
  elif choice == "2":
    stu_output(students)
  elif choice == "3":
    stu_search(students)
  elif choice == "4":
    pass
  elif choice == "5":
    pass
  elif choice == "6":
    pass


  elif choice == "7":
    while True:
      print("[ 학생성적 정렬 ]")
      print("1. 이름 순차정렬")
      print("2. 이름 역순정렬")
      print("3. 합계 순차정렬")
      print("4. 합계 역순정렬")
      print("5. 번호 순차정렬")
      print("0. 이전페이지 이동")
      print("-"*40)
      choice = input("원하는 번호를 입력하세요.>> ")
      if choice == "1":
        students.sort(key=lambda x:x['name'])
      elif choice == "2":
        students.sort(key=lambda x:x['name'],reverse=True)
      elif choice == "0":
        print("이전페이지로 이동합니다.")
        break
      print("정렬이 완료되었습니다.")
  elif choice == "0":
    print("[ 프로그램 종료 ]")
    print("프로그램을 종료합니다.")
    break









# stu = "6, 홍길자, 100, 100, 100, 300, 100.0, 0" # 파일에 저장하는 형태
# sArr = stu.split(",")

# for i,s in enumerate(sArr):
#   if str.isdigit(s):   # int타입 변경이 가능하나
#     sArr[i] = int(s)
# sArr[6] = float(sArr[6])

# students.append(sArr)

# students     