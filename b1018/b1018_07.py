class Student:
  # 인스턴스 변수 - 객체선언을 하면 변수는 개별적으로 선언
  count =  0 # 클래스 변수 - 모든 객체가 동일한 변수를 사용

  def __init__(self, name, kor, eng, math):
    Student.count += 1
    self.no = Student.count  #  클래스변수 - 공용으로 사용
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor + eng + math
    self.avg = (kor + eng + math) / 3
    self.rank = 0

  # == : 호출되는 함수
  # 같냐
  def __eq__(self, value):  #self : 현재 자신의 객체, value : 비교할 다른 객체
    return self.total == value.total
    # 다르냐
  def __ne__(self, value):  #self : 현재 자신의 객체, value : 비교할 다른 객체
    return self.total != value.total
    # 크냐
  def __gt__(self, value):  #self : 현재 자신의 객체, value : 비교할 다른 객체
    return self.total > value.total
    # 크거나 같냐
  def __ge__(self, value):  #self : 현재 자신의 객체, value : 비교할 다른 객체
    return self.total >= value.total
    # 작냐
  def __lt__(self, value):  #self : 현재 자신의 객체, value : 비교할 다른 객체
    return self.total < value.total
    # 작거나 같냐
  def __le__(self, value):  #self : 현재 자신의 객체, value : 비교할 다른 객체
    return self.total <= value.total

s1 = Student("홍길동",100,100,100)  #300
s2 = Student("유관순",90,100,100)   #290

if (300>299):
  print("참입니다.")
else:
  print("거짓입니다.")

if(s1 > s2):  #항목 중에 어떤 것으로 비교
  print('참입니다.')
else:
  print('거짓입니다.')
















# a = [1, 2, 3]
# print(*a)  #전개연산자

# s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']

# print(*s_title,sep='\t')
# # 위 구문이 바로 밑 구문이랑 똑같이 출력된다.
# print(f"{s_title[0]}\t{s_title[1]}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{s_title[6]}\t{s_title[7]}")