students = []
s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]  # 전역변수
no = 1
while True:
    print("[ 학생 성적 프로그램 ]")
    print("------" * 10)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 학생 성적 검색")
    print("5. 학생 성적 삭제")
    print("6. 등수 처리")
    print("0. 프로그램 종료")
    print("------" * 10)
    choice = input("원하는 번호를 입력해주세요. (0.종료): ")
    # 1,2,3,4,0
    if choice == "1":
        print("[학생 성적 입력]")
        while True:
            n = input(f"{no}번째 학생 이름을 입력하세요(0. 메인메뉴) : ")
            if n == "0":
                print("메인메뉴로 이동합니다.")
                break
            k = int(input("국어 성적 입력 : "))
            e = int(input("영어 성적 입력 : "))
            m = int(input("수학 성적 입력 : "))
            t = k + e + m
            a = t / 3
            r = 0
            s = [no, n, k, e, m, t, a, r]
            students.append(s)
            print(s)
            no += 1
    elif choice == "2":
        print("[학생 성적 출력]")
        print()
        for st in s_title:
            print(st, end="\t")
        print()
        print("-----" * 12)
        for s in students:
            print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
        print()

    elif choice == "3":
        print("[학생 성적 수정]")
        count = 0
        name = input("수정하려는 학생 이름을 입력해주세요. : ")
        for s in students:
            if s[1] == name:
                  print(f"{name}학생을 찾았습니다.")
                  print("[과목 선택]")
                  print("1. 국어 점수")
                  print("2. 영어 점수")
                  print("3. 수학 점수")
                  print("0. 수정 취소")
                  cn = input("원하는 번호를 입력하세요 : ")
                  if cn == "1":
                      print("현재 국어 점수 : ",s[2])
                      s[2] = int(input("국어 점수 입력 : "))
                  elif cn == "2":
                      print("현재 영어 점수 : ",s[3])
                      s[3] = int(input("영어 점수 입력 : "))
                  elif cn == "3":
                      print("현재 수학 점수 : ",s[4])
                      s[4] = int(input("수학 점수 입력 : "))
                  elif cn == "0":
                      count += 1
                      print("메인화면으로 돌아갑니다.")
                      break
                  s[5] = s[2] + s[3] + s[4]
                  s[6] = s[5]/3
                  print(f"{name}학생 성적 변경")
                  count += 1
        if count == 0:
            print("수정하려는 학생이 없습니다.")
            print()



    elif choice == "4":
        print("[학생 성적 검색]")
        count = 0
        nm = input("찾으려는 학생 이름을 입력하세요.: ")
        for n in students:
            if n[1] == nm:
                print(f"{nm}학생을 찾았습니다.")
                for st in s_title:
                    print(st, end="\t")
                print()
                print("------" * 12)
                print(
                    f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}"
                )
                print()
                count += 1
                break
        if count == 0:
            print("찾으려는 학생 이름이 없습니다.")
            print()

    elif choice == "0":
        print("[프로그램 종료]")
        print("프로그램을 종료합니다.")
        break
