# css나 js같이 파이썬 함수도 모듈(함수의 집합체)을 만들고 import로 불러와서 사용하면 된다
# import S_func  
from S_func import *  # *: 모든 함수를 들고 와라. 별표 말고 하나 지정해서 들고 오기도 가능함.



# ----------프로그램 시작 --------------
# 학생성적프로그램
# 실제 제공되는 코드는 밑의 코드.
# 구조가 어떻게 이루어지는지 모르니 보안상으로도 우수.
while True:
  choice = title_program()         # 메뉴 출력 함수 호출
  if choice == "1":
    stuNo = stu_input(stuNo)       # 학생 성적 입력 함수 호출
  elif choice == "2":
    stu_output(students)   # 학생 성적 출력 함수 호출
  elif choice == "3":
    stu_update(students)   # 학생 성적 수정 함수 호출
  elif choice == "4":
    stu_select(students)   # 학생 성적 검색 함수 호출
  elif choice == "5":
    stu_delete(students)   # 학생 성적 삭제 함수 호출
  elif choice == "6":
    stu_rank(students)
  elif choice == "7":
    stu_sort(students)     #  학생 성적 정렬 함수 호출

  elif choice == "0":
    print("[ 프로그램 종료 ]")
    print("프로그램을 종료합니다.")
    break
# 학생성적 입력부분을 구현하시오.
# dict타입으로 입력을 할것
# 번호,이름,국어,영어,수학,합계,평균,등수
# 입력이 완료되면 출력이 바로 되도록 하시오.