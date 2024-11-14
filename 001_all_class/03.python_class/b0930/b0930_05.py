# 두 수를 입력받아 더하기, 빼기, 곱하기, 나누기를 출력하시오.
# 에러가 나지 않도록 안전하게 코드를 짜고 생각을 하는것이 중요 (에러 = 서버따운 = 위기)
anum = input("첫번째 수를 입력하세요.")
bnum = input("두번째 수를 입력하세요")
print(type(anum), type(bnum))
aa = int(anum)
bb = int(bnum)
print(type(aa), type(bb))
sksnrl = aa / bb
print(type(sksnrl))

print(
    "더하기: {},빼기: {},곱하기: {},나누기: {}".format(
        aa + bb, aa - bb, aa * bb, aa / bb
    )
)
print(type(aa+bb))
print(type(aa-bb))
print(type(aa*bb))
print(type(aa/bb)) #Python은 나누기 하면 float형으로 적용됨.

a = 0
for i in range(1, 11): # 1~10까지
  a += i
# a = a + i
print(a)
b = (10>100)
print(b) # False
print(type(b))
c = (10<100)
print(c) # True
# 함수
d = 10 # 전역변수
def add():
  print(10 + 9)
  e = 20 # 지역변수