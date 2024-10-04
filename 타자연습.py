# # 1~100 랜덤숫자 맞추기
# # for 문 사용해서 작성
# import random
# cnt = 0
# rn = random.randint(1,100)
# for n in range(10):
#   tn = int(input(f"숫자를 입력하세요,{n+1}번째 도전입니다. : "))
#   if tn > rn:
#     print("더 낮은 숫자를 입력해주세요.")
#   elif tn < rn:
#      print("더 높은 숫자를 입력해주세요.")
#   else:
#     cnt += 1
#     print("정답입니다.")
#     print("프로그램을 종료합니다.")

# if cnt == 0:
#   print("실패입니다. 정답은",rn,"입니다.")
#   print("프로그램을 종료합니다.")


# while문 사용해서 작성
import random
cnt = 0
rn = random.randint(1,100)
i = 0
while i < 10:
  tn = int(input(f"숫자를 입력하세요, {i+1}번째 도전입니다. : "))
  if tn > rn:
    print("더 낮은 수를 입력하세요")
  elif tn < rn:
    print("더 높은 수를 입력하세요")
  else:
    cnt += 1
    print("정답입니다. 축하드립니다.")
    break
  i += 1

if cnt == 0:
  print(f"실패하였습다. 정답은 {rn}입니다.")