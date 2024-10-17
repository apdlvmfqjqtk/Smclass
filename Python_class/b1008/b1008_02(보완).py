# [0, 3, 6, 9, 12, ...]
aArr = []
for i in range(20):
  aArr.append(3*i)
print(aArr)

# 4,5 2차원 리스트
a_list = []
for i in range(4):
  a = []
  for j in range(5):
    a.append(aArr[5*i+j])
    # a.append(aArr[j]+5*3*i)
  a_list.append(a)

print(a_list)


# # [4, 5] 2차원 리스트 제작
# a_list = []

# for i in range(4):
#   a = []
#   for j in range(5):
#     a.append(5*3*i+(3*j))
#   a_list.append(a)
# print(a_list)

# # 제작한 2차원 list 사각형으로 형태변형
# for i in range(4):
#   for j in range(5):
#     print(a_list[i][j],end="\t")


# ## 여기 보완필
