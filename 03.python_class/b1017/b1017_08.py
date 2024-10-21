import datetime
import os

members = []
m_title = ['id','pw','name','nicName','address','money']

####### member.csv파일 불러오기-----------------
f = open('b1017/member.csv','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line:
    break
  # c 리스트 저장
  c = line.strip().split(",")
  c[5] = int(c[5]) #  money
  # members리스트에- 딕셔너리 저장
  members.append(dict(zip(m_title,c)))
f.close
# --------------------------------------

######## cart파일 읽기------------
c_keys = ['cno','id','name','pCode','pName','price','date']
cart = []
cartNo = 0

# isfile - 파일인지아닌지, isdir -디렉토리인지 아닌지, exists - 파일이 존재하는지
if os.path.exists("b1017/cart.txt"):
  if os.path.isfile('b1017/cart.txt'): 
    f = open('b1017/cart.txt','r',encoding='utf-8')
    while True:
      line = f.readline()
      if not line:
        break
      c = line.strip().split(",")
      c[0] = int(c[0])
      c[5] = int(c[5])
      cart.append(dict(zip(c_keys,c)))
    f.close
# --------------------

# 파일 저장해서 불러오기
# csv파일로 저장
product = [
  {"pno":1,"pCode":"t001","pName":"삼성TV","price":2000000,"color":"black"},
  {"pno":2,"pCode":"g001","pName":"LG냉장고","price":3000000,"color":"white"},
  {"pno":3,"pCode":"h001","pName":"하만카돈스피커","price":500000,"color":"gray"},
  {"pno":4,"pCode":"w001","pName":"세탁기","price":1000000,"color":"yellow"}
]
f = open('b1017/product.csv','w',encoding='utf-8')
for p in product:
  f.write(f"{p['pno']},{p['pCode']},{p['pName']},{p['price']},{p['color']}\n")
f.close()

# csv 파일에서 불러오기
pd_info = []
p = []
pd_title = ['pno','pCode','pName','price','color']
f = open('b1017/product.csv','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line:
    break
  p = line.strip().split(",")
  p[0] = int(p[0])
  p[3] = int(p[3])
  pd_info.append(dict(zip(pd_title,p)))
f.close()  

# print(product)
session_info = {}
p_title = ["번호","아이디","이름","코드","상품명","가격","구매일자"]

def singin():
  while True:
    chk = 0
    id = input("아이디를 입력하세요.")
    for idd in members:
      if idd['id'] == id:
        print("이미 존재하는 아이디입니다. 다시 입력해주세요.")
        chk = 1
    if chk == 0:
      pw = input("패스워드를 입력하세요. : ")
      name = input("성함을 입력해주세요. : ")
      nicName = input("별명을 입력해주세요. : ")
      address = input("주소를 입력해주세요(시 단위). : ")
      money = input("보유금액을 입력해주세요. : ")
      sing = [id, pw, name, nicName, address, money]
      members.append(sing)
      print(members)
      break
# ----------------------회원가입

# --로그인----------------------
def login():
  while True:
    chk = 0
    id = input("아이디를 입력하세요.")
    pw = input("패스워드를 입력하세요.")
    for log in members:
      if log['id'] == id and log['pw'] == pw:
        chk = 1
    if chk == 0:
      print("로그인에 실패하였습니다. 다시 시도해주세요.")
    else:
      print(f"{log['name']}님 로그인에 성공하였습니다.")
      return chk
      break

  
### 프로그램 시작 ###
while True:
  print("[ 메인 화면 ]")
  print("1. 로그인")
  print("2. 회원가입")
  print("0. 종료")
  print("-"*30)
  choice = input("원하는 번호를 입력하세요.")
  if choice == "1":
    login()
  elif choice == "2":
    singin()

  elif choice == "0":
    print("프로그램을 종료합니다.")
    break

# 프로그램을 구현하시오.
while True:
  print("           [ SM-SHOP ]")
  print(f"                       닉네임:{session_info['nicName']}님")
  print(f"                       금액 :{session_info['money']:,} 원")
  print("1. 삼성TV - 2,000,000")
  print("2. LG냉장고 - 3,000,000")
  print("3. 하만카돈스피커 - 500,000")
  print("4. 세탁기 - 1,000,000")
  print("7. 내용저장")
  print("8. 구매내역 ")
  print("9. 금액충전 ")
  choice = int(input("구매하려는 상품번호를 입력하세요.>> "))
  # 프로그램 구현