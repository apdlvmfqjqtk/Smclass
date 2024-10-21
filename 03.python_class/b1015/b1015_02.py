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

# 학생성적입력 함수선언
def stu_input(stuNo,students):
  while True:
    print("[ 학생성적 입력 ]")
    no = stuNo + 1  # 전역변수더라도 함수 안으로 못가져오기에 매개변수 이용하거나 global로 가져와야 함 (민감한 정보는 매개변수 이용)
    name = input(f"{no}번쨰 학생 이름을 입력하세요. (0. 이전 화면 이동) : ")
    if name == "0":
      print("이전 화면으로 이동합니다.")
      break
    
    # 과목 수가 많은 경우 for문을 이용한 입력이 더 유용함
    score = []
    total = 0
    for i in range(3):
      k = int(input(f"{s_title[i+2]}점수를 입력하세요. : "))
      total += k
      score.append(k)

    # kor = int(input("국어 점수를 입력하세요. : "))
    # eng = int(input("영어 점수를 입력하세요. : "))
    # math = int(input("수학 점수를 입력하세요. : "))
    # total = kor + eng + math

    avg = total/3
    rank = 0

    s = {"no":no, "name":name, "kor":score[0], "eng":score[1], "math":score[2], "total":total, "avg":avg, "rank":rank}
    students.append(s)
    stuNo += 1

    print(f"{name}학생 성적이 저장되었습니다.")
    print()

    print(students)
  return stuNo


# 실제 프로그램 시작 부분 ##
choice = input("원하는 번호를 입력하세요. : ")

if choice == "1":
  stuNo = stu_input(stuNo,students)
  print("현재 학생 번호 : ",stuNo)
  print(students)
  # 기본매개변수 stuNo는 받아줘야하고
  # 복합매개변수 students는 보내기만 해도 된다.


# while True:
#   print("[ 학생성적 입력 ]")
#   no = stuNo + 1
#   name = input(f"{no}번쨰 학생 이름을 입력하세요. (0. 이전 화면 이동) : ")
#   if name == "0":
#     print("이전 화면으로 이동합니다.")
#     break
  
#   # 과목 수가 많은 경우 for문을 이용한 입력이 더 유용함
#   score = []
#   for i in range(3):
#     k = int(input(f"{s_title[i+2]}점수를 입력하세요. : "))
#     total += k
#     score.append(k)

#   # kor = int(input("국어 점수를 입력하세요. : "))
#   # eng = int(input("영어 점수를 입력하세요. : "))
#   # math = int(input("수학 점수를 입력하세요. : "))
#   # total = kor + eng + math

#   avg = total/3
#   rank = 0

#   s = {"no":no, "name":name, "kor":score[0], "eng":score[1], "math":score[2], "total":total, "avg":avg, "rank":rank}
#   students.append(s)
#   stuNo += 1

#   print(f"{name}학생 성적이 저장되었습니다.")
#   print()

#   print(students)