# 파일 이어 쓰기 (a)

while True:
  no = input("번호를 입력하세요. : ")
  if no == "0": break
  name = input("이름을 입력하세요. : ")
  kor = int(input("국어 점수를 입력하세요. : "))
  eng = int(input("영어 점수를 입력하세요. : "))
  math = int(input("수학 점수를 입력하세요. : "))
  total = kor + eng + math
  avg = total/3
  rank = 0

  # csv파일 형태
  data = f"{no}, {name}, {kor}, {eng}, {math}, {total}, {avg:.2f}, {rank}\n"
  f = open('a.txt','a',encoding='utf-8')
  f.write(data)
  f.close()