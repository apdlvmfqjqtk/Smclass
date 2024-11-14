# list1 = [52,273,32,72,100]

# try:
#   n_input = int(input("리스트 순번에 있는 값 출력 : "))
#   print(f"리스트의 {n_input}번쨰의 값 : {list1[n_input]}")
# except ValueError as e:
#   print("값을 잘못 입력하셨습니다.", type(e), e)
# except IndexError as e:
#   print("번호가 리스트 범위를 벗어났습니다.", type(e), e)
# except Exception as e:
#   print("모든 예외처리의 부모")
#   # # Exception는 밑의 두 에러를 전부 긁어오기 때문에 자세한 에러를 알 수 없음
#   # # 또한 Exception을 위에 두면 모든 에러를 받아 처리하기에 밑에 넣어야한다
#   # # 혹시 모를 에러를 대비해 exception만은 작성 필요
#   # print("값을 잘못 입력하셨습니다.")
#   # print("번호가 리스트 범위를 벗어났습니다.")
#   pass
# finally:
#   # print(type(e))
#   # print("e : ",e)
#   pass

# try - except - else = finally
# Exception : 모든 예외의 부모, 예외처리에서 마지막에 위치해야 함
# as e : e 변수는 예외에 대한 설명문, type(e):예외객체
# 리스트의 범위 밖 호출 에러 : IndexError
# 입력된 값의 변환 에러 : ValueError
# raise 키워드 : 강제예외 발생

print("프로그램 시작")
print("1")
print("2")
try:
  print("3")
  print("4")
  raise NotImplementedError("프로그램을 구현해야 함.") #프로그램이 구현되어 있지 않음
  # print(10/0) # 강제에러
  print("5")
except Exception as e:
  print(e)
  print("6")
  print("7")
finally:
  print("8")
  print("9")
print("10")
print("프로그램 종료")

