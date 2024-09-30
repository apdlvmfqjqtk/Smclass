# stu_data = ["홍길동", 100, 100, 100, 99]
# for s in stu_data :
#   print(s)

stu_title = ["번호", "이름", "국어", "영어", "수학", "과학", "합계", "평균"]
stu_datas = [
    [1, "유관순", 100, 100, 100, 99],
    [2, "이순신", 100, 99, 98, 99],
    [3, "김구", 80, 100, 90, 99],
]
print("                     [학생성적 프로그램]")
# print(
#     "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
#         stu_title[0],
#         stu_title[1],
#         stu_title[2],
#         stu_title[3],
#         stu_title[4],
#         stu_title[5],
#         stu_title[6],
#         stu_title[7]
#     )
# )
# print("-"*60)

for s_t in stu_title:
    # 기본 설정(아무것도 적지 않았읗 시.)은 end='\n'로 적용되지만 end=' '를 넣음으로 스페이스로 바뀜
    print("{}".format(s_t), end="\t")
print()
print("-" * 60)


for s in stu_datas:
    print(
        "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
            s[0],
            s[1],
            s[2],
            s[3],
            s[4],
            s[5],
            s[2] + s[3] + s[4] + s[5],
            ((s[2] + s[3] + s[4] + s[5]) / 4)
        )
    )
    ## 학번, 이름, 국어, 영어, 수학, 과학, 합계, 평균


# #이순신의 평균을 출력하시오
# print("{} 평균 : {}".format(stu_datas[1][0], (stu_datas[1][1]+stu_datas[1][2]+stu_datas[1][3]+stu_datas[1][4])/4))

# 학생 이름 : 홍길동
# 국어 : 100
# 영어 : 100
# 수학 : 100
# 과학 : 99
# 합계 :
# 평균 :
# print("학생 이름 : {}".format(stu_data[0]))
# print("국어 : {}".format(stu_data[1]))
# print("영어 : {}".format(stu_data[2]))
# print("수학 : {}".format(stu_data[3]))
# print("과학 : {}".format(stu_data[4]))
# print("합계 : {}".format(stu_data[1] + stu_data[2] + stu_data[3] + stu_data[4]))
# print("평균 : {}".format((stu_data[1] + stu_data[2] + stu_data[3] + stu_data[4]) / 4))


# # # 한번에 2개 길이를 입력받아 삼각형의 넓이, 직사각형의 넓이를 구하시오
# length = input("2개 길이를 입력하세요.")
# print(length.split(" ")) # 2개의 리스트로 나눠짐 (js에선 배열이라 불림)
# l_list = length.split(" ")
# print("삼각형 넓이 : {}".format(float(l_list[0])*float(l_list[1])*0.5))
# print("사각형 넓이 : {}".format(float(l_list[0])*float(l_list[1])))

# # 2개 길이를 입력받아 삼각형의 넓이, 직사각형의 넓이를 구하시오
# width = float(input("가로를 입력하시오."))
# height=  float(input("세로를 입력하세요."))
# triangle = (width * height)* 0.5
# oblong = width * height
# print(triangle)
# print(oblong)


# # 원의 넓이 : 3.14* r**
# # 반지름 입력받아 넓이구하기
# r = float(input("반지름을 입력하시오"))
# area = r ** 2 * 3.14
# print(area)
# print("원의 넓이 : {:.1f}".format(area))


##### 약식 #####
# 자바처럼 +=, -=, /=, *= // 등등 가능하지만 증가연산자(i++, i--)사용은 불가함
# 또한 스위치(switch) 문 사용 불가
###복합대입연산자 +=, -=, *=, /=, //=(몫), %=(나머지), **(거듭제곱)=
# a = 10
# a += 5 ; print(a)
# a -= 5 ; print(a)
# a *= 5 ; print(a)
# a /= 5 ; print(a)
# a //= 5 ; print(a)
# a %= 5 ; print(a)
# a **= 5 ; print(a)

# ### 숫자를 문자열로 변환 ##
# # 문자열 + 숫자 = 불가능
# a = 100
# b = 10
# print(str(a)+str(b))

# 문자형 숫자 변환
# a = "100"
# b = "10.5"
# c = "안녕"
# print(float(a)) #정수형 문자열 -> 정수타입, 실수타입 변경 가능
# print(int(b))   #실수형 문자열 -> 실수타입 변경 가능
# print(float(c)) #글자는 숫자형 타입으로 변경 불가
# aa = 10
# bb = 5

##우선순위 ##
# 코드 계산 순서도 사칙연산을 따른다.

### 코드를 한줄로 쓸 때
# a = 5; b = 3 # 한줄로 쓸때 ; 표현 넣어주면 됨
# s1, s2, s3 = 1, 2, 3
# c, d = 10, 20
# # / % // **
# print("{}, {}, {}, {}".format(a/b, a%b, a//b, a**b))
