import random

# 1,25 사이의 랜덤숫자를 생성해서 출력하시오
# num = int(random.random()*25)+1
# num = random.randint(1, 25)
# 1, 25까지 랜덤숫자를 입력, 중복은 제거하고 출력

# # 중복없이 1-25를 전부 넣으려면
# a_list = []
# while len(a_list) < 25:
#   # for i in range(1):
#     num = random.randint(1, 25)
#     if num not in a_list:
#       a_list.append(num)

# print(a_list)
# print(len(a_list))

# # 1-25까지 랜덤으로 배치
# # sample
# a_list = []
# for i in range(25):
#     a_list.append(i + 1)

# b_list = random.choices(a_list, k=25) #choises는 중복 추출 가능
# print(b_list)


# # random.sample()
# b_list = random.sample(a_list,25) # sample - 범위 리스트에서 25개를 추출함 (중복 추출 안됨)
# print(b_list)
