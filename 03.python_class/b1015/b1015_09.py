# def selfcall() :
#   print("하", end='')
#   selfcall()
# selfcall()

# # 4 * 3 * 2 * 1
# # 재귀함수를 쓰기보단 for문이 속도가 더 빠름.
# result = 1
# for i in range(1,5):
#   result *= i
# print(result)

# # 퀴즈
# a = [1, 2, 3, 4, 5]
# # a리스트에 전부 10을 더해서 리스트에 담아 출력하시오.
# # 리스트 내포, map람다식 사용
# # 리스트 내포 식
# b = [i+10 for i in a]
# print(b)

# # 람다식
# # map - list에 동일한 형태를 적용시킬때
# b = list(map(lambda i:i+10, a))
# print(b)


# def func(v1, v2):
#   return v1*v2
# lambda v1, v2: v1*v2


# a = [1, 2, 3, 4]
# b = [10, 20, 30, 40]
# # 위의 두 리스트를
# # aArr = [11, 22, 33, 44] 출력
# ---------------------------------
# #람다식
# # map(lambda 매개변수1, 매개변수2,:리턴값, 복합자료형1, 복합자료형2)
# aArr = list(map(lambda i,j:i+j,a,b))
# print(aArr)
# ---------------------------
# # 리스트 내포
# aArr = [i+j for i,j in zip(a,b)]
# print(aArr)
# -----------------------------
# # 기본함수사용
# aArr = []
# def func(a,b):
#   for i,j in zip(a,b):
#     aArr.append(i+j)
#   return aArr
# print(func(a,b))
# ------------------------------------
# # 리스트를 하나 보내는 경우
# aArr = []
# def func(a):
#   for i in a:
#     aArr.append(i*i)
#     return aArr
# print(func(a))
# ---------------------------------


# # zip함수 : 2개의 리스트를 1개로 변경
# a = [1, 2, 3, 4]
# b = [10, 20, 30, 40]
# print(list(zip(a,b)))   # 튜플 형태로 들어감
# print(dict(zip(a,b)))   # 딕셔너리 형태로 들어감


# filter(함수, 반복 가능한 자료형) - 리스트, 튜플, 딕셔너리
# filter 함수 사용 방법
# def func(v):
#   if v%2 == 0: 
#     return True 
#   else:
#     return False
# # aArr 값 중에 2의 배수인 경우에만 리턴
# aArr = [1, 2, 3, 4]
# bArr = list(filter(func,aArr))
# print(aArr)


# # 필터 함수 람다식 변경
# aArr = [1, 2, 3, 4]
# bArr = list(filter(lambda x:x%2==0,aArr))
# print(bArr)


# # # 기본 함수 사용 방법
# def func(v):
#   if v%2 == 0:
#     return v
# aArr = [1, 2, 3, 4]
# bArr = []
# for i in aArr:
#   if func(i) != None:
#     bArr.append(func(i))
# print(bArr)


# def func(v):
#   return v*2
# lambda v:v*2 #  람다는 한 줄만 가능
# # map 함수
# # map(함수,리스트) : 리스트의 내용을 1개씩 함수에 전달해서 결과값을 리스트로 저장
# aArr = [1, 2, 3, 4]
# # bArr = list(map(func, aArr)) #aArr을 하나씩 함수에 던지고 그 값을 bArr에 기록하는게 map함수 (map 타입으로 넘겨주기에 list로 변경해줘야 한다)
# # print(bArr)

# bArr = list(map(lambda x:x*2,aArr))  #  함수의 줄임 (함수를 따로 만들지 않아도 됨.)
# print(bArr)


# # 리스트 내포
# aArr = [1, 2, 3, 4]
# print(aArr)
# bArr = [ a*2 for a in aArr]
# print(bArr)


# # 기본적인 함수 사용
# print(func(2))

# aArr = [1, 2, 3, 4]
# print(aArr)

# bArr = []
# for a in aArr:
#   bArr.append(func(a))

# print(bArr)
