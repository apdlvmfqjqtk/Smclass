# 시작은 0으로 시작, 0부터 0씩 증가하면서 10번 실행
for i in range(10):
  print(i)

# 5부터 10이전까지 실행(총 5번(5,6,7,8,9))
for x in range(5,10):
  print(x)

print("-"*50)
a_list = [1, 2, 3, 4, 5]
for k in a_list:
  print(k)

# Python - 문자열(str), 정수형(int), 실수형(float), 논리형(bool)
# list type
b_list = [3, 5, 9, 10, 20, 3, 3, 10, 5, 20]
for m in b_list:
  print(m)

# 딕셔너리 타입 - {} : json타입과 모양이 같음. 키와 값{}(key,value)
dic = {
  "번호" :1,
  "이름" :"홍길동", 
  "국어" :100,
  "영어" :100,
  "수학" :99
}
print(dic["번호"])

for n in dic:   ## dic에서 key값을 n에 넣어줌
  print(n)      ## key값이 출력이 됨.
  print(dic[n]) ## key값의 value값이 출력이 됨
# list 길이 - len()
print(len(b_list))

# list 안 해당하는 숫자가 몇개인지 확인 - count
print(b_list.count(5))

# list 형태에 추가하는 방법 - append, tnsert, extend([2,3] / 여러개 동시추가)
# list 형태에 삭제하는 방법 - del, remove, clear(모두 삭제)
