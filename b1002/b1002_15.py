import random

ct = 0
rn = random.randint(1,100)
tr = 1
for a in range(10):
  tn = int(input(f"숫자를 입력해주세요 {tr} 번째 도전입니다. : "))
  if tn < rn:
    print("더 큰 수를 입력하세요.",9-a,"번 남았습니다.")
    tr += 1
  elif tn > rn:
    print("더 작은 수를 입력하세요.",9-a,"번 남았습니다.")
    tr += 1
  else:
    print("정답입니다.")
    ct += 1
    break

if ct == 0:
  print("기회 소진! 정답 :",rn)