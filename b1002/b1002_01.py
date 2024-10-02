# 문자열

# 문자열 숫자
a = "123"
print(type(a))        #str
print(type(int(a)))   #int
print(type(float(a))) #float

b="12.3"
# print(type(int(b)))  # 에러 - 소수점이 있는 문자열 수는 float으로 변환해야함
print(type(float(b)))  # floar

#문자열연결연산자
s1 = "안녕"
s2 = "안녕하세요"
print(s1+s2)
print(a+b) # 문자열 연결연산자
# print(a*b) # 문자열은 -, *, / 안됨

# 문자열 *2 문자열 반복연산자
print("안녕"*10)
print("-."* 40)

#문자열 슬라이싱 
str1 = "안녕하세요. 반갑습니다."  #문자열을 하나의 리스트 형태로 봄
print(str1[0])  #넣은 번호에 해당되는 문자를 출력
print(str1[7]) #문자 사이 스페이스도 한칸으로 인식함
print(str1[2:5]) # 2:5를 넣었으면 2~4까지의 문자를 출력
print(str1[:5]) # [처음: 숫자앞까지]
print(str1[2:]) # [위치: 끝까지]
print(str1[1:10:2]) # [위치: 숫자 앞까지: 2씩]
print(str1[::-1]) # [처음부터:끝까지:역순으로]

# [] - 배열 : 배열은 한번 범위가 정해지면 수정 불가능 : C, JAVA
# [] - 리스트 : 범위 상관없음.


c = 12.3
print(type(int(c)))   # 실수는 int타입으로 변경 가능.
print(int(c))         # float







# input_str = input("글자를 입력하세요.")

# # 문자가 입력되지 않았을 때

# if input_str != "": # 빈공백이 아니냐? (!는 부정형)
#     print("입력문자 :", input_str)
#     print("프로그램이 종료됩니다.")
# else:
#     print("글자를 입력하셔야 합니다.")
# # JS와 다르게 들여쓰기로 괄호를 대체함.