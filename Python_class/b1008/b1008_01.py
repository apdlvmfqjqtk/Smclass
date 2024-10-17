students = []
s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
no = 1

while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")

  if choice == '1':
    print("[ 학생 성적 입력 ]")
    while True:
      print("이전 메뉴로 나가시려면 0을 입력해주세요.")
      name = input(f"{no}번째 학생입니다. 이름을 입력하세요. : ")
      if name == "0":
        break 
      kr = int(input("국어 점수를 입력하세요. : "))
      en = int(input("영어 점수를 입력하세요. : "))
      mt = int(input("수학 점수를 입력하세요. : "))
      tt = kr + en + mt
      av = tt/3
      tp = 0 #등수
      a = [no, name, kr, en, mt, tt, av, tp]
      students.append(a)
      no += 1
      print(a)

  elif choice == '2':
    print("[ 학생 성적 출력]")    

    for st in s_title:
      print(st, end="\t")
    print()
    print('-----'*12)
    for a in students:
      print(f"{a[0]}\t {a[1]}\t {a[2]}\t {a[3]}\t {a[4]}\t {a[5]}\t {a[6]:.2f}\t {a[7]}")


  elif choice == "3":
    print("[ 학생성적 수정 ]")
    name = input("학생 이름을 입력해주세요.")
    cnt = 0
    for n in students:
      if name == n[1]:
        print(f"{name}학생이 있습니다.")
        print("[1. 국어 점수]")
        print("[2. 영어 점수]")
        print("[3. 수학 점수]")
        choice = print("수정하고싶은 부분을 선택해주세요 : ")
        if choice == '1':
          print("지금 점수 : ",a[2])
          a[2] = int(input("변경할 점수를 입랙해주세요. : "))
        elif choice == '2':
          print("지금 점수 : ",a[3])
          a[3] = int(input("변경할 점수를 입랙해주세요. : "))
        elif choice == '3':
          print("지금 점수 : ",a[4])
          a[4] = int(input("변경할 점수를 입랙해주세요. : "))
        elif choice == '0':
          print("수정을 취소합니다.")
          break

        a[5] = a[2]+a[3]+a[4]
        a[6] = a[5]/3
        print(f"{name}성적 변경이 완료되었습니다.")
        cnt += 1
    
    if cnt == 0:
      print("해당 학생은 없습니다.")

  elif choice == "4":
    print("[ 학생성적 검색 ]")
    name = input("학생 이름을 입력해주세요.")
    cnt = 0
    for n in students:
      if name == n[1]:
        print(f"{name}학생이 있습니다.")

        for st in s_title:
          print(st, end="\t")
        print()
        print('-----'*12)
        print(f"\t{a[0]}\t {a[1]}\t {a[2]}\t {a[3]}\t {a[4]}\t {a[5]}\t {a[6]:.2f}\t {a[7]}")
        print()
        cnt += 1
      if cnt == '0':
        print ("찾으시는 학생이 없습니다.")  
  elif choice == "5":
    print("[ 학생성적 삭제 ]")

  elif choice == "6":
    print("[ 등수처리 ]")

  elif choice == "0":
    print("[ 프로그램 종료 ]")
    break