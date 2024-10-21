students = []

while True:
    print("[ 학생 성적 프로그램 ]")
    print("------" * 10)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("------" * 10)
    choice = input("원하는 번호를 입력해주세요. (0.종료): ")

    if choice == "1":
      print("[학생 성적 입력]")
      no = 1
      while True:
        n = input("이름을 입력하세요.(0. 상위 메뉴 이동): ")
        if n == "0":
          break
        k = int(input("국어 점수를 입력하세요 : "))
        e = int(input("영어 점수를 입력하세요 : "))
        m = int(input("수학 점수를 입력하세요 : "))
        t = k + e + m
        a = (k + e + m) / 3
        r = 0
        print(
            f"번호: {no}, 이름: {n}, 국어: {k}, 영어: {e}, 수학: {m}\ 합계: {t}, 평균: {a:.2f}"
        )
        s = [no, n, k, e, m, t, a, r]
        students.append(s)
        no += 1

    elif choice == "2":
      print("[학생 성적 출력]")
      print()
      # 출력
      s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

      # 상단 출력
      for s in s_title:
        print(s, end="\t") # 끝을 enter키가 아닌tab키를 쳐서 늘려라
      print() ; print("-----"*12)

      # 학생 성적 출력
      for s in students: 
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
      print()
    elif choice == "3":
      print("[학생 성적 수정]")
    elif choice == "0":
      print("[ 프로그램 종료]")
      print("프로그램을 종료합니다.")
      break

# # 이름, 국어, 영어, 수학 -> 번호 이름 국어 영어 수학 합계 평균
# # 이름에 0 입력시 프로그램을 종료합니다 출력.

# no = 1
# while True:
#   n = input("이름을 입력하세요.\n프로그램 종료는 0을 입력하세요. : ")
#   if n == "0":
#       break
#   k = int(input("국어 점수를 입력하세요 : "))
#   e = int(input("영어 점수를 입력하세요 : "))
#   m = int(input("수학 점수를 입력하세요 : "))
#   t = k + e + m
#   a = (k + e + m) / 3
#   print(
#       f"번호: {no}, 이름: {n}, 국어: {k}, 영어: {e}, 수학: {m}\ 합계: {t}, 평균: {a:.2f}"
#   )
#   s = [no, n, k, e, m, t, a]
#   s_list.append(s)
#   no += 1

# print(s_list)
# # print("프로그램을 종료합니다.")
