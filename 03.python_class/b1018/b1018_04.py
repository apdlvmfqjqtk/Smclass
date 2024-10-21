class Circle:
  def __init__(self,length):
    self.__length = length  # __변수 : 변수에 직접적으로 접근 제한
  
  # 원의 넓이
  def get_area(self):
    return 3.14*self.__length**2
  def get_circum(self):
    return 3.14 * 2 * self.__length

c1 = Circle(int(input("반지름을 입력하세요.")))

c1.length = 7  #  (여기서 변수를 지정하더라도 c1은 내가 입력한 값으로 계산해줌)
print("넓이 : ", c1.get_area())
print("둘레 : ", c1.get_circum())


c2 = Circle(int(input("반지름을 입력하세요.")))
print("넓이 : ", c2.get_area())
print("둘레 : ", c2.get_circum())




# # 절차적인 형태의 프로그램 구현
# # 반지름을 입력받아 원의 둘레와 넓이를 출력하시오
# r = int(input("반지름을 입력해주세요. : "))
# length = r*2*3.14
# asd = (r**2)*3.14
# print(length)
# print(asd)