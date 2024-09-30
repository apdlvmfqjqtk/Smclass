# # #  python 변수의 종류 bool(논리형) int(정수형) float(실수형) str(문자형)
# # name,kor,eng,math,total,avg 출력
# input으로 입력을 받아
# 홍길동, 100, 100, 99, 합계, 평균을 1줄에 출력
name = input("이름을 입력하세요.")
kor = input("국어 점수를 입력하세요.")
eng = input("영어 점수를 입력하세요.")
math = input("수학 점수를 입력하세요.")
total = int(kor) + int(eng) + int(math) #문자열에서 정수형으로 타입 변경
avg = total / 3

#format버전
print(
    "이름 : {}  국어 : {}  영어 : {}  수학 : {}  합계 : {}  평균 : {:.2f}".format(
        name, kor, eng, math, total, avg
    )
)
# f함수 버전
print(f"이름 : {name}, 국어 : {kor}, 영어 : {eng}, 수학 : {math}, 합계 : {total}, 평균 : {avg:.2f}")

# a = "100"
# b = "200"
# print(type(a))
# print(type(b))

# print(a + b)  # 문자연결연산자 100200
# print(int(a) + int(b))  # 타입 변경
# name = "홍길동"
# # print(int(name)) #문자를 숫자로 변경 못함. 문자인 숫자는 변경 가능
# c = "3.14"
# print(int(float(c)))  # 실수형으로 변경 후 정수형으로 변경
# # print(int(c)) #문자실수형은 정수로 바로 변경이 불가능
# print(str(c))  # 실수형을 문자열로 변경

# d = "True"
# print(bool(d)) #문자불형을 불형으로 변경

# #타입 변경 - str, int, float, bool (웹에서 입력받는 모든 데이터가 문자형이기에 변경이 필요한것)


# name = "홍길동"
# print(type(name))

# level = "3레벨"
# print(type(level))

# n = 3.14
# print(type(n))

# num = 100
# print(type(num)) # True, Flase 대문자로 넣어야 함

# a_bool = True
# print(type(a_bool))

# var1 = 100
# var2 = var1
# var3 = var2
# var4 = var3
# print(var4)

# v4 = v3 = v2 = v1 = 10
# print(v4)
