class Student:
  # 인스턴스 변수 - 객체선언을 하면 변수는 개별적으로 선언
  count =  0 # 클래스 변수 - 모든 객체가 동일한 변수를 사용
  students = [] # 클래스 리스트

  # 클래스함수 선언
  @classmethod
  # 클래스 함수
  def stu_print(cls):
    for s in cls.students:
      print(str(s))
  
  
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
    # 클래스 리스트에 추가
    Student.students.append(self)

  # 객체를 문자열로 리턴하는 함수 - return은 항상 문자열이 돼야한다.
  def __str__(self):
    return f'{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}'

  def print(self):
    return {"no":self.no,"name":self.name,"kor":self.kor,"eng":self.eng,"math":self.math,"total":self.total,"avg":self.avg,"rank":self.rank,}

##### 프로그램 시작



# ##### 프로그램 시작 #####
# s1 = Student()
# s1.students
# s2 = Student()
# s1.students

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']
s_t = ['no', 'name', 'kor', 'eng', 'math', 'total', 'avg', 'rank']

while True:
  print("[ 학생성적 프로그램 ]")
  print("1. 학생성적 입력")
  print("2. 학생성적 출력")
  print("3. 홍길동, 유관순 비교 ")
  choice = input("원하는 번호를 입력하세요. : ")

  if choice == "1":
    print("[ 학생성적 입력 ]")
    name = input("이름을 입력하세요. : ")
    score = []
    for i in range(2,5):
      score.append(int(input(f"{s_title[i]}점수를 입력하세요. : ")))
    Student(name, *score) #class를 저장

    # 클래스 변수 접근 방법
    for s in Student.students:
      print(s)

    #인스턴스변수 참조변수.변수명, 참조변수명.함수명
    # 클래스변수 클래스명.변수명, 클래스명.함수명
    # s1 = Student(name, *score)   #  전개연산자
    # s1 = Student(name,  score[0],score[1],score[2]) 윗줄이랑 같은내용

  elif choice == "2":
    print("[ 학생성적 출력 ]")
    print(*s_title,sep='\t')
    print('-'*70)
    Student.stu_print() #클래스함수 호출
      # print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
  elif choice == "3":   # 홍길동 학생의 합계, 유관순 학생의 합계 대소비교
    s1 = Student("홍길동", 100, 100, 90)
    s2 = Student("유관순", 90, 100, 90)










s1 = Student("홍길동",100,100,99)
print(s1)    # 0x000 -> __str___저장된 형태로 출력

# # students리스트에 딕셔너리로 저장
# students = []
# s1 = Student("홍길동",100,100,99)
# print(s1.print())
# students.append(s1.print())
# s2 = Student("유관순",99,99,98)
# print(s2.print())
# students.append(s2.print())
# print(students)

# s1 = Student("홍길동", 100, 100, 99)
# print(s1.name)
# print("s1.count : ",s1.count) #1
# s2 = Student("유관순", 90, 90, 99)
# print(s2.name)
# print("s1.count : ",s1.count) #2
# print("s2.count : ",s2.count) #2