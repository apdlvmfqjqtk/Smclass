# 2차원 리스트
#for문을 2번 작성해 1,25까지 [5,5] 리스트 생성
a_list = []
for i in range(0,5):
  a = []
  for j in range(0,5):
    a.append(5*i + (j+1))
  a_list.append(a)

print(a_list)
# # 1차원(선, 학생), 2차원(면, 반), 3차원(큐브, 학년)개념, 그러나 3차원은 잘안씀. 최대한 2차원 선에서 끝내도록함
# a_list = []
# for i in range(9):
#   a_list.append(i+1)
# print(a_list)


# b_list = []
# for i in range(9):
#   b =[]
#   if(a_list[i]%4) == 0: #1, 2, 3, 4, 5, 6
#     b.append(a_list[i])

# print(b_list)


# # # [3, 3]리스트 / [1, 2, 3], [4, 5, 6], [7, 8, 9]
# # 1-9 for문 이용해 2차원형태로 집어넣기
# a_list = []
# for i in range(0,3):
#   a = []
#   for j in range(0,3):
#     y = 3*i + (j+1)
#     a.append(y)
#   a_list.append(a)
# print(a_list)

# # 1-9까지 for문 이용해 리스트 추가하시오
# b_list = []
# for i in range(1, 10):
#   b_list.append(i)
#   print(b_list)

# # 2차원 리스트
# a_list = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9, 10, 11, 12]
# ]

# # 2차원 리스트 -> for문을 2번 사용
# for i in a_list:
#   print(i)
#   for j in i:
#     print(j)