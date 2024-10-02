# if - else
# if - elfe - else

# 100~98 A+
# 97~94 A
# 93~90 A-
# 89~88 B+
# 87~84 B
# 83~80 B-
#70 C
# 60 D
# 60미만 F


g = int(input("성적을 입력하세요."))
s = "";
if 90<=g:
  s = "A"
  if 98<=g:
    s += "+"
  elif 90<=g<=93:
    s += "-"
# //ㅇㅣ런식으로 if문구문 줄이기도가능...


if 101>g>97:
  print("A+")
elif g>93:
  print("A")
elif g>89:
  print("A-")
elif g>87:
  print("B+")
elif g>83:
  print("A")
elif g>79:
  print("B-")
elif g>77:
  print("C+")
elif g>73:
  print("C")
elif g>69:
  print("C-")
elif g>67:
  print("D+")
elif g>63:
  print("D")
elif g>59:
  print("D-")
else:
  print("F")

# #3,4,5 봄 5,7,8 여름 9,10,11 가을 12,1,2 겨울
# mon = int(input("월을 입력하세요."))
# if 3<= mon <=5 :
#   print("봄")
# elif 6<= mon <=8 :
#   print("여름")
# elif 9<= mon <=11 :
#   print("가을")
# elif mon == 12 or 1<= mon <=2 :
#   print("겨울")
# else:
#   ("잘못 입력하셨습니다.")


# # 입력한 수가 10이하 또는 100이상일때 정답입니다. 오답입니다.
# num = int(input("수 기입"))
# if num <=10 or num >=100:
#   print("정답")
# else:
#   print("오답")


# # 입력수가 1이상 10이하 정답
# num = int(input("숫자입력"))
# if num >= 1 and num <=10:
#   print("정답")
# else:
#   print("오답")
# # python만 가능한 구문
# if num <= num <=10:
#   print("정답")
# else:
#   print("오답")


#  # 짝홀구문
# num = float(input("숫자를 입력해주세요"))
# if num % 2 == 0:
#     print("짝")
# else:
#     print("홀")
