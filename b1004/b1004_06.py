a_list = ["홍길동", "유관순", "이순신"]
# '님'자 붙이기
a_list = [a + "님" for a in a_list]
print(a_list)


# a_list = [1, 2, 3, 4, 5]
# # b_list = [1*1, 2*2, 3*3, 4*4, 5*5]

# print(a_list)
# # list의 값을 변경해 list에 저장
# # for idx,a in enumerate(a_list):
# #   a_list[idx] = a**2

# # list에 값을 변경해 list에 저장 - list 내포 / 한 줄 for문
# a_list = [a**2 for a in a_list]

# print(a_list)


# # list 값 변경
# print(a_list)
# a_list[1] = 100
# print(a_list)

# # list 슬라이싱 0부터 4 앞까지(3까지)
# print(a_list[0:4])

# # list 범위보다 넘어서 출력할 시, 에러 없이 출력은 되지만 범위까지만 출력이 됨(범위가 0:7이라면 0~7만.)
# print(a_list[0:10])

# # 없는 list 위치에 값 수정시 에러 발생함
# a_list[5] = 1000
# print(a_list)

# # 없는 list 위치 출력시 에러
# print(a_list[10])


# # enumerate() 함수
# a_list = ['홍길동', '유관순', '이순신', '강감찬', '김구', '김유신', '홍길자']

# # for문으로 출력
# for a in a_list:
#   print(a)

# # enumerate()함수 - index번호를 출력 index, value
# for i,a in enumerate(a_list):
#   print(f"{i+1}:{a}")

# print(a_list)
