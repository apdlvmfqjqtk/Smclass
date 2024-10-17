import datetime
##### 기본 정보 부분 (DB) #####

# Member 정보 부분---- (member.txt읽어와서 dict로 저장)
member = []
m_keys = ['id','pw','name',"nicName","money","address"]
f = open('member.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line:
    break
  m = line.strip().split(",")
  # print(m)
  m[4] = int(m[4])
  member.append(dict(zip(m_keys,m)))
# print(member)
f.close
# --------------------

# Product 정보 부분---- 상품(나중에는 상품도 txt파일 읽어서 dict 저장)
product = [
  {'pno':'1', 'pCode':'t001', 'pName':'삼성TV', 'price':2000000, 'color':'black'},
  {'pno':'2', 'pCode':'g001', 'pName':'LG냉장고', 'price':3000000, 'color':'white'},
  {'pno':'3', 'pCode':'h001', 'pName':'하만카돈스피커', 'price':500000, 'color':'gray'},
  {'pno':'4', 'pCode':'w001', 'pName':'세탁기', 'price':1000000, 'color':'yellow'}
]
p_title = ['상품번호','상품코드','상품이름','상품가격','상품색깔']
# ---------------------

# Ect 정보 부분(변수)---
session_info = [] # 로그인한 멤버의 정보를 가져오기 위한 list공간 선언
# ----------------------

# cart 정보 부분 -----멤버가 구매한 물건을 cart.txt에 저장하고 나중에 다시 쓰기 위해 불러옴
cart = [] # cart.txt에서 불러온 값 dict로 저장할 list
c_keys = ['cno','id','name','pCode','pName','price'] #나중에 date도 추가
ca = open("cart.txt",'r',encoding="UTF-8")
while True:
  line = ca.readline()
  if not line:
    break
  c = line.strip().split(",")
  # print(c)
  c[0] = int(c[0])
  c[5] = int(c[5])
  cart.append(dict(zip(c_keys,c)))
  # print(cart)
# -------------------



# 함수 선언 부분----
# -------------------


##### 프로그램 시작 부분 #####
# 로그인 부분 -----------------
while True:
  cnt = 0 #비밀번호 / 아이디를 틀렸는지 확인
  inid = input("아이디를 입력해주세요. : ")
  inpw = input("비밀번호를 입력해주세요. : ")
  for m in member:
    if inid == m['id'] and inpw == m['pw']:
      print(f"{m['name']} 계정으로 로그인에 성공하였습니다.")
      session_info = m
      cnt = 1
      break
  if cnt == 0:
    print("로그인에 실패하였습니다. 다시 시도해주세요.")
  else:
    print("로딩 중")
    break #로그인에 성공하고 for문을 break로 나오고 while문도 나오기 위해 break사용
# -----------------------------

# 제품 구매 부분---------------
while True:
  print("[ 상품 구매 페이지 ]")
  print(f"{m['nicName']} 님, 환영합니다.")
  print(f"{m['nicName']} 님의 잔액. : {m['money']:,}원 보유")
  print("1. 상품1 -000원 ")
  print("2. 상품2 -000원 ")
  print("3. 상품3 -000원 ")
  print("4. 상품4 -000원 ")
  print("7. 내용저장 ")
  print("8. 구매내역 ")
  print("9. 잔액충전 ")
  cho = int(input("구매하려는 상품의 번호를 입력하세요."))

  if cho == 1:    # 상품구매 함수 1
    pass
  elif cho == 2:  # 상품구매 함수 2
    pass
  elif cho == 3:  # 상품구매 함수 3
    pass
  elif cho == 4:  # 상품구매 함수 4
    pass
  elif cho == 7:  # 내용저장 함수
    pass
  elif cho == 8:  # 구매내역 함수
    pass
  elif cho == 9:  # 금액충전 함수
    pass
# -----------------------------

# 제품 구매 동작 부분---------------
# ------------------------------