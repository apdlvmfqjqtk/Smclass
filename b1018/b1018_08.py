# 1. 학생 성적 입력
# 이름, 국, 영, 수 -> 번호, 이름, 국, 영, 수, 합, 평, 등수
# 클래스 1개가 생성이 되고
# # 클래스의 참조변수(__srt__) 출력하기

# 객체선언한 참조변수를 출력하면 주소값이 출력딤
# 참조변수를 출력해서 원하는 데이터를 출력하려면 __str__함수를 사용해야함
# 리턴값. 문자열이어야 함

class Student:
  # 1. 생성자 
  students = []
  
  @classmethod
  def stu_print(cls):
    for s in cls.students:
      print(str(s))

  count = 1    # 클래스 변수
  def __init__(self, name, kor, eng, math):
    self.no =  Student.count    # 클래스 변수   :  클래스명.변수명
    Student.count += 1          # 인스턴스 변수 : 참조변수면. 변수명
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    Student.students.append(self)

  def __str__(self):
    return f'{self.no},{self.name},{self.kor},{self.eng},{self.math}'


# no는 getter를 사용하지 않으면 접근 불가
  def get_no(self):
    return self.no  # return값은 문자여야만 함
  
  def set_no(self,no):
    if no<0: raise("0이하는 입력을 할 수 있습니다.")
    self.no = no


s1 = Student('홍길',100,80,40)
print(s1)
s2 = Student('유관',100,80,40)
print(s2)
s3 = Student('이순',100,80,40)
print(s3)
s4 = Student('강감',100,80,40)
print("-"*50)

# Student.stu_print()
# Student.students
for s in Student.students:
  print(s)

# A변수가 없을때랑 private지정시켰을때 뜨는 에러 메시지가 똑같다.
# s_ti = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
# s_enti = ['no', 'name', 'kor', 'eng', 'math', 'total', 'avg', 'rank']
# tst = []
# while True:
#   print("1. 성적 입력")
#   print("2. 성적 출력")
#   ch = input("번호 선택 : ")

#   if ch == "1":
#     print('성적 입력')
#     name = input("이름 : ") 
#     for i in range(2,5):
#       tst.append(int(input(f"{s_ti[i]} 점수입력 : ")))
#   elif ch == "2":
#     pass




#   elif ch == "0":
#     print("끝")
#     break
# print("종료")



# # class Student:
# #   # 1. 생성자 정의가 없음
# #   # 기본 생성자

# #   # 변수는 3종류
# #   # 1. 지역변수 : 함수 내에 선언된 변수, 함수가 종료되면 사라짐.
# #   # 2. 인스턴스 변수: 객체 선언할 때 만들어짐. 각각의 객체마다 변수가 생성됨. (self선언)
# #   #   -참조변수명.변수명
# #   # 3. 클래스 변수: 객체가 선언되지 않아도 만들어짐. 모든 객체가 공통으로 사용.
# #   #   -클래스명.변수명

# #   # 함수는 2종류가 있음
# #   # 1. 인스턴스 함수: 객체선언할 때 만들어짐. 각각의 객체마다 함수가 생성됨.
# #   #   -참조변수명.함수명
# #   # 2. 클래스 함수: 객체가 선언되지 않아도 만들어짐. 모든 객체가 공통으로 사용함.
# #   #   -클래스명.함수명
# #   # @classmethod  #클래스 함수 사용하려면 써야함

# #   kor = 100  #클래스변수 - 클래스명.변수면
# #   # 함수에 self는 무조건 들어가야함
# #   def __init__(self, no, name, kor):
# #     self.no = no  # 인스턴스 변수 - 참조변수명.변수명
# #     self.name = name
# #     self.kor = kor
# # # 객체선언
# # # 참조변수명 = 클래스명()
# # print("최초 : ",Student.kor)

# # s1 = Student(10)
# # print(s1.no)
# # Student.kor = 50

# # s2 = Student(20)
# # print(s2.no)

# # print("최종 : ",Student.kor)