students = []
s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]
choice = 0  # 전역변수
stuNo = 0  # 학생번호 생성
chk = 0  # 찾지 못하였을때 결과 출력용
count = 1  # 성적처리에 사용
stuNo = len(students)  # list에 학생이 있으면 그 인원으로 변경이 됨
no = 0
name = ""
kor = 0
eng = 0
math = 0
total = 0
avg = 0
rank = 0  # 성적처리변수

while True:
    print("[ 학생성적 프로그램 ]")
    print("-" * 60)
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
    print("4. 학생성적 검색")
    print("5. 학생성적 삭제")
    print("6. 등수처리")
    print("0. 프로그램 종료")
    print("-" * 60)
    choice = input("원하는 번호를 입력하세요. : ")

    if choice == "1":
        while True:
            print("[ 학생성적 입력 ]")
            # 학생성적 직접 입력
            no = (
                stuNo + 1
            )  # list에 현재 학생 수, 이거로 번호를 넣으면 추후 삭제, 추가할 떄 중복 번호가 생긴다. 고로 이 방법은 XX
            name = input(f"{no}번째 학생 이름을 입력하세요. (0번 : 이전 화면) : ")
            if name == "0":
                print("성적 입력을 취소합니다.")
                print()
                break
            kor = int(input("국어 점수를 입력하세요: "))
            eng = int(input("영어 점수를 입력하세요: "))
            math = int(input("수학 점수를 입력하세요: "))
            total = kor + eng + math
            avg = total / 3
            rank = 0
            students.append([no, name, kor, eng, math, total, avg, rank])
            stuNo += 1  # (학생 수 증가)
            print(f"{name}학생 성적이 저장되었습니다.")
            print()

    elif choice == "2":
        print("                     [ 학생성적 출력 ]")
        # 상단 타이틀 출력
        for title in s_title:
            print(f"{title}\t", end="")
        print()
        # # 위의 3줄과 밑에 3줄은 같은 내용이다.
        # print(
        #     f"{s_title[0]}\t{s_title[1]}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{s_title[6]}\t{s_title[7]}"
        # )
        print("-----" * 12)

        # 학생 성적 출력
        for s in students:
            print(
                f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\t"
            )

    elif choice == "3":
        print("[ 학생성적 수정 ]")
        name = input("찾고자 하는 학생 이름을 입력하세요. : ")
        chk = 0
        for s in students:
            if s[1] == name:
                # 학생 성적 수정
                print(f"{name}학생을 찾았습니다.")
                print()
                print("[수정 과목 선택 ]")
                print("1. 국어 점수")
                print("2. 영어 점수")
                print("3. 수학 점수")
                choice = input("원하는 번호를 입력하세요. : ")
                if choice == "1":
                    print("이전 국어 점수 : {}".format(s[2]))
                    s[2] = int(input("변경 국어 점수 : "))
                elif choice == "2":
                    print("이전 영어 점수 : {}".format(s[3]))
                    s[3] = int(input("변경 영어 점수 : "))
                elif choice == "3":
                    print("이전 수학 점수 : {}".format(s[4]))
                    s[4] = int(input("변경 수학 점수 : "))

                s[5] = s[2] + s[3] + s[4]  # 합계
                s[6] = s[5] / 3  # 평균

                print(f"{name}학생 성적이 수정되었습니다.")
                print()

                # 상단 타이틀 출력
                for title in s_title:
                    print(f"{title}\t", end="")
                print()
                # 위의 3줄과 밑에 3줄은 같은 내용이다.
                print("-----" * 12)
                # 학생 성적 출력
                print(
                    f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\t"
                )
                print()
                chk = 1
        # 모든 학생 비교가 끝난 후, chk 확인.
        if chk == 0:
            print(f"{name}학생이 없습니다. 다시 입력하세요")

        print()
    elif choice == "4":
        print("[ 학생성적 검색 ]")
        name = input("찾고자 하는 학생 이름을 입력하세요. : ")
        chk = 0
        for s in students:
            if s[1] == name:
                # 상단 타이틀 출력
                for title in s_title:
                    print(f"{title}\t", end="")
                print()
                # 위의 3줄과 밑에 3줄은 같은 내용이다.
                print("-----" * 12)
                # 학생 성적 출력
                print(
                    f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\t"
                )
                print()
                chk = 1
        # 모든 학생 비교가 끝난 후, chk 확인.
        if chk == 0:
            print(f"{name}학생이 없습니다. 다시 입력하세요")

    elif choice == "5":
        print("[ 학생 성적 삭제 ]")
        name = input("찾고자 하는 학생 이름을 입력하세요. : ")
        chk = 0
        for idx, s in enumerate(students):
            if s[1] == name:
                chk = 1
                choice = input(
                    f"{name}학생 성적을 삭제하시겠습니까?(삭제시 복구 불가능합니다.)\n 1. 삭제 2. 취소"
                )
                if choice == "1":
                    del students[idx]
                    print(f"{name}학생 성적이 삭제되었습니다.")
                else:
                    print("학생성적 삭제가 취소되었습니다.")
                    break
        # 모든 학생 비교가 끝난 후, chk 확인.
        if chk == 0:
            print(f"{name}학생이 없습니다. 다시 입력하세요")

    elif choice == "6":
        print("[ 등수처리 ]")  # 번외지만 등수 처리, 통계값내기는 리소스를 많이 잡아먹기에 주로 새벽에 몰아서 작업한다.
        for s in students:
         count = 1
         for st in students:
          if s[5] < st [5]:
              count += 1
          s[7] = count # 등수입력
        print("등수 처리가 완료되었습니다.")
        print()

    elif choice == "0":
        print("[ 프로그램 종료 ]")
        print("프로그램을 종료합니다.")
        break
