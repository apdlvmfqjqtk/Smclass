import random

# 1-100까지 
# 입력한 숫자가 랜덤숫자보다 크면 입력한 숫자가 큽니다.
# 입력한 숫자가 랜덤숫자보다 작으면 입력한 숫자가 작습니다 출력.
# 총 10번 시도
# 정답입니다.프로그램 종료

# for문 사용
# tf = 0
# rdn = random.randint(1,100)
# for a in range (10):
#   trn = int(input("숫자를 입력하세요 : "))
#   if rdn < trn:
#     print("더 작은 수를 입력하세요.",9-a,'번 남았습니다.')
#   elif rdn > trn:
#     print("더 큰 수를 입력하세요",9-a,'번 남았습니다.')
#   else:
#     print("정답입니다. 프로그램을 종료합니다.")
#     tf +=1
#     break

# if tf == 0 : 
#   print("실패했습니다. 프로그램을 종료합니다.")


# # while 문 사용
# i = 0
# tf = 0
# rdn = random.randint(1,100)
# while i<10:
#   ttrn = int(input("숫자를 입력하세요 : "))
#   if rdn < ttrn:
#     print("더 작은 수를 입력하세요")
#   elif rdn > ttrn:
#     print("더 큰 수를 입력하세요")
#   else:
#     print("정답입니다. 프로그램을 종료합니다.")
#     tf += 1
#     break
#   i += 1

# if tf == 0 : 
#   print("실패했습니다. 프로그램을 종료합니다.") 



# # @@@@@@@@@@@@@@@@@@@@강사님 버전@@@@@@@@@@@@
# # while문
# rnum = random.randint(1,100) #이 수를 while문 안에 넣는다면 식이 돌떄마다 값이 변경됨으로 while문 밖에 있어야 한다.
# cnt = 0 #10번 모두 실패했을 때 메시지를 출력하기 위한 카운드 변수
# i = 0       #초기값 
# while i<10: #조건식
#   ipnum = int(input("숫자를 입력하세요."))
#   # 랜덤 숫자와 다르게 입력 숫자를 while 밖에 두면 입력한 값 고정으로 10번 돌아가기에 while문 안에 넣어줘야 한다(10번 시도할 수 있게)
#   # 또한 입력되는 숫자는 str타입이기에 int를 넣어줌으로서 에러가 생기지 않게 한다.
#   # 비교 구문
#   if rnum < ipnum:
#     print("더 작은 수를 입력해주세요.")
#   elif rnum > ipnum:
#     print("더 큰 수를 입력해주세요.")
#   else:
#     print("정답.")
#     cnt += 1
#     break
#   i += 1    #증감식

# #10번 도전을 모두 실패할 경우
# if cnt == 0:
#   print("도전에 실패하셨습니다. 정답 :",rnum)


# for문 일때
cnt = 0
rn = random.randint(1,100)
for i in range(10):
# 여기까지가 while문과 다른 점이고 나머지는 모두 같다.
  ipnum = int(input("숫자를 입력하세요."))
  # 비교 구문
  if rn < ipnum:
    print("더 작은 수를 입력해주세요.")
  elif rn > ipnum:
    print("더 큰 수를 입력해주세요.")
  else:
    print("정답.")
    cnt += 1
    break

#10번 도전을 모두 실패할 경우
if cnt == 0:
  print("도전에 실패하셨습니다. 정답 :",rn)