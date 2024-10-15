# 함수 - 기본매개변수, 가변매개변수, 키워드 매개변수

# 함수 - 가변매개변수, 키워드 매개변수 동시 사용할 경우
def plus(*n,k=10):  # 가변형 매개변수가 먼저, 다음으로 키워드 매개변수를 사용해야 함
  print("k : ",k)
  for i in  n:
    print(i)

plus(1, 2, 3, 4, 5, k=50)

# print(1, 2, 3, 4, 5,sep="",end="\t")
# print(1)


# # 3. 함수 - 키워드매개변수
# def plus(k=10, m=5):
#   print("k =", k)
#   print("m =", m)

# plus(m=1,k=2)  # 매개변수 개수가 일치하지 않으면 에러가 남, 그러나 키워드 매개변수는 상관없음



# # 2. 함수 - 가변매개변수 (개수랑 상관없이 모든걸 다 받을 수 있다.)
# def plus(a,*n1):  # 기본매개변수과 가변매개를 같이 쓴다면 기본매개변수를 앞에 둬야 한다.
#   print(a)
#   for i in n1:
#     print(i)
#   print(type(n1))

# plus(1, 2, 3, 4, 5, 6, 7, 8)



# # 1. 함수 - 기본매개변수
# def plus(n1,n2):
#     sum = n1 + n2
#     print("합계 : ",sum)

# # 함수 호출 - 매개변수 개수가 맞지 않으면 에러가 남
# plus(10,20) 


# # # 구구단 (함수)
# # 함수 선언
# def calc(st,end):
#     for i in range(st, end + 1):
#         print(f"[{i} 단]")
#         for j in range(1, 10):
#             print(f"{i} X {j} = {i*j}")

# # ----------
# # 2-9단
# st = 2
# end = 9

# calc(2,9) # 함수 정의(함수 호출)

# # 구구단 (for문)
# for i in range(st, end + 1):
#     print(f"[{i} 단]")
#     for j in range(1, 10):
#         print(f"{i} X {j} = {i*j}")

# # 3-7단
# calc(3,7)


# st = 3
# end = 7
# for i in range(st, end + 1):
#     print(f"[{i} 단]")
#     for j in range(1, 10):
#         print(f"{i} X {j} = {i*j}")

# # 5-9단
# calc(5,9)


# st = 5
# end = 9
# for i in range(st, end + 1):
#     print(f"[{i} 단]")
#     for j in range(1, 10):
#         print(f"{i} X {j} = {i*j}")

# # 여러 방식을 나타낼 때 for문과 달리 함수는 한번 정해 두어 소스 코드를 아낄 수 있다.