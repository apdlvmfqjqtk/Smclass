subject = ["국어","영어"]
score = []
while True:
  print("1. 과목추가")
  print("0. 종료")
  choice = input("원하는 번호를 입력해주세요 : ")
  if choice == "1":
    s_input = input("과목을 추가하세요. : ")
    subject.append(s_input)
  elif choice == "0":
    print("종료")
    break


for i in range(len(subject)):
  score.append(int(input(f"{subject[i]}점수를 입력하세요.")))

sum = 0
for i in range(len(subject)):
  print(f"{subject[i]} : ",score[i])
  sum += score[i]
print("합계 : ",sum)













# # 함수 선언
# def output(subject):
#   # 출력함수 선언
#   print('과목')
#   print('-'*20)
#   for s in subject:
#     print(s)


# while True:
#   print("[ 과목 생성 프로그램 ]")
#   s_input = input("원하는 과목을 입력하세요. : ")
#   # list - append(리스트에 변수 추가)
#   subject.append(s_input)
#   # 출력함수 호출
#   output(subject)




# a = 10
# b = 20
# c = 30

# # a에 함수써서 a+b+c 출력
# def abc(a,b,c):
#   a = a+b+c
#   print(a)


# abc(a,b,c)
# print(a)



# a = 10
# b = 20
# sum = 0

# # 함수선언
# def add(a,b):
#   return a+b
# # 함수호출
# sum = add(a,b)
# print("a,b합계 : ",sum)






# a = 10  #  전역변수

# # 함수 선언. 파이썬도 위에서 아래로 읽어가기에 함수 호출보다 위에서 함수 선언해야 함.
# def func(a):
#   print("함수 내 a값 : ",a)
#   a += 50
#   return a
#   # global a  # 전역변수를 가져옴
#   # a = 50  # 지역함수 : 함수를 종료하면 모두 제거됨

# # 함수 호출
# a = func(a)
# print("함수 밖 a값 : ",a)