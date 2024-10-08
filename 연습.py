# 3 X 3 리스트를 만들고 좌표값을 지정하면 꽝인지 결과인지 도출, 이후 그 결과를 기록한다.

import random  # random 함수 사용을 위한 함수 선언

lotto = [0]*6 + [1]*3  #꽝과 당첨을 구분할 0과 1 list 선언.
random.shuffle(lotto) #0과 1을 무작위로 섞어준다.(shuffle)
# print(lotto) 

a_list = [   # 단순 스피또를 만드는데 9~ 17번까지의 과정이 필수는 아님, (수업 때)a_list를 2차원 list로 나타내는 걸 먼저 했고 
  [0, 1, 0], # 그 위에 로또를 위한 변수 셔플을 집어넣었기에 보다 복잡하게 그리는 것
  [1, 0, 0],
  [0, 0, 1]
]

for i in range(3):   # a_list의 기존 좌표에 lotto list값 집어넣는 식 
  for j in range(3): # a*x + y 식으로 a*a 배열에서 1,2,3,4,5,6...a** 표현 가능
    a_list[i][j] = lotto[3*i + j]

# print(a_list)

aa_list = [  #  당첨값(1)을 알면 안되니 겉에 보일 list값.(외형만 aa_list를 보이고 실제 동작은 a_list에서 작동)
  ['로또', '로또', '로또'],
  ['로또', '로또', '로또'],
  ['로또', '로또', '로또']
]

while True:  # 여러 번 시도할 수 있게 while True 사용(무한반복)
  money = int(input("베팅할 금액을 입력하세요 : "))  #당첨금 계산을 위한 int적용

  print(" [스피또]") #제목, 디자인 요소
  print("\t0\t1\t2") #  좌표. 좌표값을 알 수 있게 하는 디자인요소
  print("-"*30) #디자인
  for i in range(3):
    print(i, '|', end="\t")  #  y값 알수 있게 삽입(세로칸)
    for j in range(3):
      print(aa_list[i][j], end="\t")
      print