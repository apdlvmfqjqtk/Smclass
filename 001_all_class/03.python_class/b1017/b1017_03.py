# try - except
# try에 에러가 발생하면 except 실행
# try - except - else
# else는 try구문에 에러가 없으면 실행

# try - except - finally
# try 에러가 발생해도, 발생하지 않아도 무조건 finally 실행

numbers = [52,273,32,103,90,10,275,1,2,1,2,12]
# a = "12351200"
# print(a.find("1"))
try:
  print(numbers.index(52))
  print(numbers.index(1))
  print(numbers.index(3))
  print(numbers.index(32))
  print(numbers.index(90))
except Exception as e: #  Exception as e - 에러 알려줌(가장 상위개념) (하위는 vlaue error, index error등)
  print("찾는 번호가 없습니다.",e)





# f = open('b1017/a.txt','w',encoding='utf-8')
# try:
#   f.write("안녕하세요.1\n")
#   f.write("안녕하세요.2\n")
#   f.write("안녕하세요.3\n")
#   f.write({"a":1})
#   f.write("안녕하세요.4")
# except Exception as e:
#   print(e)
# finally:
#   f.close()





# print('파일 open')
# try:
#   print('글쓰기 1')
#   print('글쓰기 2')
#   print('글쓰기 3')
#   # print('str -> 딕셔너리 입력 4')
#   print('글쓰기 5')
#   print('글쓰기 6')
# except:
#   print("잘못된 타입이 들어왔습니다.")
# finally:
#   print("파일 close")
# # 파일을 열면 에러가 상관없이 닫아야 하기에 finally이용하는것이 이득
# print("프로그램을 종료하겠습니다.")




# print("1")
# try:  # try구문에 에러가 발생해야 except를 실행시킴
#   print("2")
#   print(3/0)
#   print("3")
#   print("4")
# except:
#   print("5")
#   print("6")
# else:
#   print("프로그램 에러가 발생하지 않으면 실행")
# finally:
#   print("finally 실행됨")
# print('7')
# print('8')



# list_a = [1, 2, 3, 4, 5, '홍길동',6 , 7, 8]
# list_b = []
# # 숫자에 *2를 하는 프로그램 구현
# try:
#   for a in list_a:
#     list_b.append(a**2)
# except Exception as e:
#   print(e)
# print(list_b)



# n_str = input("반지름을 입력하세요.")
# try:
#   num = int(n_str)
#   # 원의 넓이, 원의 둘레
#   print("원의 넓이 : ", (num**2)*3.14)
#   print("원의 둘레 : ", 2*num*3.14)
# except Exception as e :
#   print("정수가 아닙니다. 정수를 입력하세요.",e)



# # 예외처리 : try - except 구문을 사용해 처리
# # 에러가 일어날 수 있는 부분에만 집어넣어야 한다.

# print("프로그램 시작")
# print(list_a)

# try:
#   # print("프로그램 시작)   # 구문 오류 - 프로그램이 실행하기 전에 오류
#   print(list_a)           # 런타임 오류 - 프로그램이 실행되는 도중에 오류

# except:
#   print("에러가 발생되었습니다.")

# print("프로그램 종료")