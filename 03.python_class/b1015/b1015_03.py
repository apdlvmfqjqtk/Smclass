# return의 사용이유

# 복합매개변수 값 전달 - list, dict, return 필요 없음
def plus(a):
  # return해주는 이유는 함수 내에 새로운 변수들은 함수를 벗어나면 사라지기 때문임
  a += 10
  print("지역변수 a : ",a)  # 20
  return a # return 필요

a = 10   #  전역변수
a = plus(a)  # 함수를 돌려 나온 a값을 변수 a에 전달해야만 변경이 됨
print("전역변수 a : ",a) #  10



# return a # return 하고 변수값에 넣어줘야 함수에서 수정한 값이 나옴 or global 사용(기본매개변수인경우)
# 복합매개변수인 경우 return을 하지 않아도 함수에서 수정한 값이 나옴. (list, dict)



# # 복합매개변수 값 전달 - list, dict, return 필요 없음
# def plus(a):
#   a[0] = 100
#   a[1] = 200
#   print("지역변수 a : ",a)

# a = [10,20]  #  전역변수
# plus(a)
# print("전역변수 a : ",a)
