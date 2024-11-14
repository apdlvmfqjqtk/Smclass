try:
  print("입력된 숫자", int(input("숫자를 입력하세요. : ")))
except:
  pass



# # try-except : 프로그램 예외를 처리하는 명령어
# # # 오류(error)
# # # 구문 오류   : 프로그램 실행 전에 발생하는 오류
# # print("안녕")
      
# # 런타임 오류 / 예외 : 프로그램 실행 중에 발생하는 오류
# while True:
#   score = 100
#   print("[ 나눗셈 프로그램 ]")
#   nstr = input("숫자만 입력 가능 : ")

#   #숫자가 아닌 것을 입력하면 에러, 0을 입력하면 에러
#   # try에서 에러가 나면 except 처리함. 많이 쓰지는 않고 최대한 if문으로 막고 나머지를 try-except로 막는다.
#   try:
#     num = int(nstr)
#     print("입력된 숫자로 100을 나눔 : ",score/num)
#   except:
#     print("숫자로 변환 안됨")
