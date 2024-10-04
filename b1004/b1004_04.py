# # 두 수를 입력받아 두 수까지의 합계 ex)4,8 = 4,5,6,7,8,9
# r = int(input("첫째 수 : "))
# t = int(input("둘째 수 : "))

# # 함수 이용한 비교
# min_num = min(r,t)
# max_num = max(r,t)
# for a in range(min(r,t),max(r,t)+1):
#   ekq += a
# print(ekq)


# if문 대소비교
# if r > t:
#   a = t
#   b = r
# else:
#   b = t
#   a = r

# # IF문 사용(2)
# if r>t:     # Python만 치환 가능 - 두개 변수 취환
#   r,t = t,r
#   # c = r     # 타 언어는 이렇게 변수 하나를 더 둬야함
#   # r = t
#   # t = c

# ekq = 0
# for a in range(r,t+1):
#   ekq += a
# print("합 : ",ekq)


# # 홀수의 합계를 구하시오
# sum = 0
# for i in range(1 , 100+1):
#   if i%2 != 0:
#     sum += i
# print(sum)
# # 혹은 
# for b in range(1,100+1, 2):
#   sum += b
# print(sum)

# # 1에서 100까지 숫자의 합
# sum = 0
# for i in range(1, 100+1):
#   sum += i
# print("합계 : ",sum)


# # 0: 안녕하세요.
# # 1: 안녕하세요.
# # 2: 안녕하세요.

# for i in range(3):
#   print(f"{i}: 안녕하세요.")
# print("-"*20)
# for _ in range(3):
#   print("안녕하세요.")

# for i in [1, 2, 3]:
#   for j in range(i):
#     print("안녕")
#   print("-"*30)  


# # *****
# # ****
# # ***
# # **
# # *
# 역순 출력
# for i in range(5, 0, -1): # -1씩 감소
#   print("*"* i)




# # for 문을 사용해 서
# # *
# # **
# # ***
# # ****
# # *****
# # 순서대로 출력
# for i in range(1,6):
#   print("*"*i)

# for i in range(1,6):
#   for j in range(5):
#    print('*'*j)

# 일정 수 이상으로 올리기
# for a in range(1, 10, 2):    #시작값, 끝값+1, 중간값
#  for j in range(1,10):
#   print(f"{a} X {j} = {a*j}")



# # 구구단 홀수단만 출력
# for s in range(1,11):
#  if s%2 != 0:
#   print(f"[{s}단]")
#   for g in range(1,11):
#    print(f"{s} X {g} = {s*g}")



#   print(f"[ {i} 단 ]")
#   for j in range(1,9+1):
#     print(f"{i} X {j} = {i*j}")
#   print("-"*13)



# # 1, 2, 5, 7, 9까지 출력
# for i in range(1,10):
#   if i%2 != 0:
#     print(i)



# for a in range(1, 10, 2):    #시작값, 끝값+1, 중간값
#  for j in range(1,10):
#   print(f"{a} X {j} = {a*j}")



# # for문을 이용한 1-11 출력`
# for i in range(1,11):
#   print(i)