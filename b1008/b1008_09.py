# students 리스트 타입
students = [
  {"no":1, "name":"홍길동", "kor":100, "eng":100, "math":99, "total":299,"avg":99.67, "rank":0},
  {"no":2, "name":"유관순", "kor":80, "eng":80, "math":85, "total":245,"avg":81.67, "rank":0},
  {"no":3, "name":"이순신", "kor":90, "eng":90, "math":91, "total":271,"avg":90.33, "rank":0},
  {"no":4, "name":"강감찬", "kor":60, "eng":65, "math":67, "total":192,"avg":64.00, "rank":0},
  {"no":5, "name":"김구", "kor":100, "eng":100, "math":84, "total":284,"avg":94.67, "rank":0}
]
no = len(students) + 1
s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

# 학생성적프로그램
while True:
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
  if choice == "2":
    print("[ 학생성적 출력 ]")
    for st in s_title:
      print(st, end="\t")
      print()
      print('-----'*12)
      for a in students:
        print(f"{a['no']}\t {a['name']}\t {a['kor']}\t {a['eng']}\t {a['math']}\t {a['total']}\t {a['avg']:.2f}\t {a['rank']}")
  elif choice == '7':
    while True:
      print("[ 학생성적 정렬 ]")
      print("1. 이름으로 순차정렬")
      print("2. 이름으로 역순정렬")
      print("3. 합계로 순차정렬")
      print("4. 합계로 역순정렬")
      print("5. 번호로 순차정렬")
      print("0. 이전페이지 이동")
      print("-"*40)
      choice = input("원하는 번호를 입력하세요.")

      if choice == "1":
        students.sort(key=lambda x:x['name'])
      elif choice == "2":
        students.sort(key=lambda x:x['name'], reverse=True)
      elif choice == "0":
        print("이전 페이지로 이동합니다")
        break

      print("정렬이 완료되었습니다.")









# students = []
# # 학생성적 입력부분을 구현하시오.
# # dict타입으로 입력을 할 것
# # 번호 이름 국어 영어 수학 합계 평균 등수 
# # 입력이 완료되면 출력이 바로 되도록 할것

# no = 1
# while True:
#   print("학생성적처리")
#   print("1. 성적입력")
#   print("1. 성적출력")
#   choice = input("번호입력")
#   if choice == "1":
#     print("[ 성적 입력 ]")
#     name = input("이름을 입력하세요 : ")
#     kor = int(input("국어점수를 입력하세요 : "))
#     eng = int(input("영어점수를 입력하세요 : "))
#     math = int(input("수학점수를 입력하세요 : "))
#     total = kor +eng +math
#     avg = total /3