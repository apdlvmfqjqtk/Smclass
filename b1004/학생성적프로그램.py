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

    if choice == "1":
        print("[학생 성적 입력]")
        while True:
            name = input(f"{no}번째 학생 이름을 입력하세요. (0.메인 메뉴): ")
            if name == "0":
                break
            kor = int(input("국어 성적을 입력하세요. : "))
            eng = int(input("영어 성적을 입력하세요. : "))
            math = int(input("수학 성적을 입력하세요. : "))
            total = kor + eng + math
            avg = total / 3
            rank = 0
            s = [no, name, kor, eng, math, total, avg, rank]
            students.append(s)
            print(s)

    elif choice == "2":
        print("[학생 성적 출력]")
        print()
        # 상단 항목 출력
        for st in s_title:
            print(st, end="\t")
        print()
        print("-----" * 12)
        # 성적 출력
        for s in students:
            print(
                f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\t"
            )
        print()

    elif choice == "3":
        print("[학생 성적 수정]")
        # 홍길동, 유관순, 이순신
        # 유관순 학생 성적 - 수정하려는
        name = input("수정하려는 학생 이름을 입력하세요. : ")
        # students에서 검색
        count = 0
        for s in students:
            if s[1] == name:
                print(f"{name} 학생을 찾았습니다.")
                print("[ 과목 선택 ]")
                print("1. 국어 점수")
                print("2. 영어 점수")
                print("3. 수학 점수")
                print("0. 수정 취소")
                choice = input("원하는 번호를 입력하세요. : ")
                if choice == "1":
                    print("현재 국어점수 :", s[2])
                    s[2] = int(input("변경 국어 점수 입력 : "))
                elif choice == "2":
                    print("현재 영어점수 :", s[3])
                    s[2] = int(input("변경 영어 점수 입력 : "))
                elif choice == "3":
                    print("현재 수학점수 :", s[4])
                    s[2] = int(input("변경 수학 점수 입력 : "))
                elif choice == "0":
                    print("성적 수정을 취소합니다.")
                    print()
                    count += 1
                    break

                s[5] = s[2] + s[3] + s[4]  # 합계 변경
                s[6] = s[5] / 3  # 평균 변경
                print(f"{name} 학생의 성적이 변경되었습니다.")
                count += 1
        if count == 0:
            print("수정하려는 학생 이름이 없습니다.")
            print()

    elif choice == "4":
        print("[학생 성적 검색]")
        name = input("찾으려는 학생 이름을 입력하세요. : ")
        # students에서 검색
        count = 0
        for s in students:
            if s[1] == name:
                print(f"{name} 학생을 찾았습니다.")
                # 찾은 학생의 데이터 출력
                # 상단 항목 출력
                for st in s_title:
                    print(st, end="\t")
                print()
                print("-----" * 12)
                # 학생 성적 출력
                print(
                    f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\t"
                )
                print()
                count += 1
                break
        if count == 0:
            print("찾고자 하는 학생 이름이 없습니다.")
            print()

    elif choice == "0":
        print("[프로그램 종료]")
        print("프로그램을 종료합니다.")
        break
