import random  ## 랜덤 수를 출력하기 위해서는 import 선언 필수

# 1~100까지 수 중 하나 출력(100 포함)   (b1002_random 참고)
random.randint(1,100)

# # 10번 도전으로 입력수가 크면 '작은수 입력', 입력수가 작으면 '큰 수 입력'
# # 10번의 도전을 모두 소진하면 '10번 도전에 실패했습니다. 랜덤숫자는 n번이다.'
# # 10번 도전안에 성공했으면 '도전에 성공했습니다. 랜덤숫자 n번'

# # for 문으로 작성
rn = random.randint(1,100)
sf = 0
for a in range(10):
  tn = int(input(f"숫자를 입력해주세요. {a + 1}번째 도전입니다. : "))
  if tn > rn:
    print("더 작은 수를 입력해주세요")
  elif tn < rn:
    print("더 큰 수를 입력해주세요.")
  else:
    sf += 1
    print(f"성공하셨습니다. 정답은{rn}입니다.")
    break
if sf == 0:
 print(f"10번 도전에 실패하였습니다. 정답은{rn}입니다.")



# while문으로 작성
i = 0
tf = 0
rn = random.randint(1,100)
while i < 10:
  tn = int(input(f"숫자를 입력. {i + 1}번째 시도 : "))
  if tn > rn:
    print("더 작은 수 입력")
  elif tn < rn:
    print("더 큰 수 입력")
  else:
    print(f"성공. 정답은 {rn}.")
    tf += 1
    break
  i += 1

if tf == 0:
  print(f"10번 모두 소진. 정답은 {rn}")