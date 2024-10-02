import random

aArr = []
# 0-9까지 10개의 랜덤 숫자 추출해서 aArr에 10번 추가
# 같은 숫자가 있으면 제외하고 입력
# for a in range(10):
#     r_num = random.randint(0, 9)
#     if r_num not in aArr:
#         aArr.append(r_num)

# print(aArr)

i = 0
while i<10: # i가 10일때 종료
  r_num = random.randint(0, 9)
  if r_num not in aArr:
    aArr.append(r_num) 
    i += 1

print("aArr 개수 : ",len(aArr))
print(aArr)