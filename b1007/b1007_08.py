# speeDDo 500원
# 보안필요
import random

a_list = [0]*24 + [1]
random.shuffle(a_list)
# print(a_list)

l_list = []
for l in range(0, len(a_list),5):
  l_list.append(a_list[l:l+5])

# print(l_list)

ll_list = [
  ["로또", "로또", "로또", "로또", "로또", ],
  ["로또", "로또", "로또", "로또", "로또", ],
  ["로또", "로또", "로또", "로또", "로또", ],
  ["로또", "로또", "로또", "로또", "로또", ],
  ["로또", "로또", "로또", "로또", "로또", ]
]


while True:
  money = int(input("얼마를 거시겠습니까(배당 10배)"))
  print("                   [ 스피또 ]")
  print("\t0\t1\t2\t3\t4")
  print("-"*50)
  for i in range(5):
    print(i,'|',end="\t")
    for j in range(5):
      print(ll_list[i][j], end="\t")
    print()

  input("긁을 좌표를 입력해주세요 (0.0) : ")