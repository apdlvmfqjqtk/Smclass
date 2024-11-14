a = ['20', 'cjakubovitsj', '75', '72', '70', '217', '72.3333333333', '1']
b = ['20', '75', '72', '70', '217', '72.3333333333', '1']
t_title = ['no','name','kor','eng','math','total','avg','rank']
c = []
students = []

def f_float(value):
  if value.isdigit(): # 정수인지 / 실수&문자열인지로 구분
    return int(value)     # 정수일 때 정수로 변환 후 리턴
  else:
    try:
      return float(value) # 실수일 때 실수로 변환 후 리턴
    except:
      return value        # 문자열일 때 문자열 그대로 변환 후 리턴

# 문자열, 정수, 실수 구성
for idx, value in enumerate(a):
  c = []
  c.append(f_float(value))

# students 리스트에 딕셔너리로 저장
students.append(dict(zip(t_title,c)))
print(c)

print(students)

# 숫자로만 구성 - 정수실수
for idx,value in enumerate(b):
  if value.isdigit(): # 정수면 true, 실수면 false
    print(f"{idx}번째 {type(int(value))}")
  else:
    print(f"{idx}번째 {type(float(value))}")






# # try-except 구문을 이용해 정수, 실수를 구분하는 함수
# def t_float(n):
#   try:
#     int(n)
#     return True
#   except:
#     return False

# # 문자인지 아닌지 구분
# for idx,i in enumerate(a):
#   if i.isdigit():
#     print(f"{idx}번째 {i}는 숫자입니다.")
#   else:
#     print(f"{idx}번째 {i}는 문자입니다.")

# # 정수로 변경
# for i in b:
#   if t_float(i): 
#     i = int(i)
#   else:
#     i = float(i)
#   c.append(i)
# print(c)

# # b의 리스트 전부 float후 c
# # b의 형태가 모두 숫자 -> float
# for i in b:
#   c.append(float(i))
# print(c)