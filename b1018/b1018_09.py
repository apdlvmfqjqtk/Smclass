# Student 클래스 생성 후
# 데이터를 직접 입력을 받아, 클래스 선언 후 저장
# 번호(자동부여), 이름, 국어, 영어, 수학, 합계, 평균, 등수
# 클래스 전체 출력
# 클래스 수정

# [ 학생성적 프로그램 ]  
# 1. 성적입력
# 2. 성적출력
# 3. 성적수정

# class 선언
class Student: 
  # class 변수 선언. class내 여러 함수에서 쓰일 학생 목록과 학생 순서를 기록하기 위한 stNo.
  students = []
  cnt = 1

  def __init__(self,name,kr,en,math): #밖에서 가져올 변수는 이름,국어,영어,수학
    self.no = Student.cnt #  class 내 no변수는 Student.stNo값을 가져오겠다
    Student.cnt += 1
    self.name = name
    self.kr = kr
    self.en = en
    self.math = math
    self.total = kr + en + math
    self.avg = (kr + en + math)/3
    Student.students.append(self)
      


# str로 문자로 만들어준 값을 class 내에서 for문으로 출력할 때.
  @classmethod
  def stu_print(cls):
    for s in cls.students:
      print(str(s))

# # student에 들어간 객체에서 출력을 위해 문자만 추출할 때 
  def __str__(self):
    return f'{self.no},{self.name},{self.kr},{self.en},{self.math}'

# for s in Student.students:
#   print(s)
# -------------------------

s1 = Student('임정우',100,90,80)
s2 = Student('임장우',100,90,80)
s3 = Student('임종우',100,90,80)

# 입력받은 이름, 점수 3개를 (name, *score)


Student.stu_print()