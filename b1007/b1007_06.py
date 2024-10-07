import random

#25개 1차원 list

# 25개 중 1을 5개, 나머지를 0
a_list = [0]*20 + [1]*5
random.shuffle(a_list)
print(a_list)
# 일단 1차원 배열을 랜덤으로 넣음

b_list = []
for i in range(5):
  a = []
  for j in range(5):
    a.append(a_list[5*i+j])   #  5*i+j는 for문을 돌면서 0, 1, 2, 3, 4, 5..출력 a_list에 있는 5개를 list에 추가
  b_list.append(a)            # a리스트를 b_list에 추가 
print(b_list)

# [5,5] 배열로 출력
for i in range(5):
  for j in range(5):
    print(b_list[i][j], end = "\t")
  print()

num = input("좌표를 입력하세요. (0,0) : ")
num2 = num.split(",")
print = (f"{num} 좌표값 : {b_list[int(num2[0])][int(num[1])]}")


# # 2. [5,5] 2차원리스트에 a_list의 값을 입력한 후 출력하시오.
#  #####폐기
# b_list = []
# for a in range(5):
#   d = []
#   for c in range(5):
# d.append(a_list[5*a+(c)])    ##<<<폐기코드
#   b_list.append(d)
# print(b_list)

# 0: 20개, 1: 5개 생성
# a_list = []
# for i in range(25):
#   if i < 5:
#     a_list.append(1)
#   else:
#     a_list.append(0)

