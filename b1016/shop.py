import datetime
member = []
m_keys = ['id','pw','name','nicName','money','address']

# member.txt에서 파일 읽기를 해 와서 member안에 dict로 저장시키기
f = open('member.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line:
    break
  m = line.strip().split(",")
  m[4] = int(m[4])
  member.append(dict(zip(m_keys,m)))
# --------------------------------------

# cart.txt에서 파일 읽기를 해 와서 member안에 dict로 저장시키기
c_keys = ['cno','id','name','pCode','pName','price','date']
cart = []
f = open('cart.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line:
    break
  c = line.strip().split(",")
  c[0] = int(c[0])
  c[5] = int(c[5])
  cart.append(dict(zip(c_keys,c)))
# --------------------------------------

# 상품 정보
product = [
  {'pno':'1', 'pCode':'t001', 'pName':'삼성TV', 'price':2000000, 'color':'black'},
  {'pno':'2', 'pCode':'g001', 'pName':'LG냉장고', 'price':3000000, 'color':'white'},
  {'pno':'3', 'pCode':'h001', 'pName':'하만카돈스피커', 'price':500000, 'color':'gray'},
  {'pno':'4', 'pCode':'w001', 'pName':'세탁기', 'price':1000000, 'color':'yellow'}
]

cartNo = 0
cart = []
session_info = []
p_title = ['번호', '아이디', '이름', '상품코드', '상품명', '가격', '구매일자']

### 함수 선언 ###
def buy(choice, cartNo):
  if session_info['money'] < 2000000:
    print('잔액이 부족합니다.')
    # 로그인 정보 - session_info
  else:
    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d %h:%m:%s")
    c = {'cno':cartNo+1, 'id':session_info['id'], 'name':session_info['name'], 'pCode':product[choice-1]['pCode'], 'pName':product[choice-1]['pName'], 'price':product[choice-1]['price'],"date":today} #이런식으로 작성하면 함수로 빼낼 수 없음
    print(f"{product[choice-1]['pName']} 을(를) 구매하셨습니다.")
    print("구매 내역에 등록합니다.")
    print()
    session_info['money'] -= product[choice-1]['price']
    cart.append(c)
    print("구매 내역 : ",cart)
  cartNo += 1
  return cartNo
# ----------------------

# 구매내역 출력 함수
def buy_output():
  print("[ 구매내역 출력 ]")
  print(f"{p_title[0]}\t{p_title[1]}\t{p_title[2]}\t{p_title[3]}\t{p_title[4]:10s}\t{p_title[5]}\t{p_title[6]}")
  print("-"*50)
  sum = 0
  for l in cart:
    sum += l['price']
    print(f"{l['cno']}\t{l['id']}\t{l['name']}\t{l['pCode']}\t{l['pName']:10s}\t{l['price']}\t{l['date']}")
  
  print(f"총 구매 금액 : {sum}")
  print(f"총 구매 건수 : {len(cart)}")
# -------------------

# 잔액 충전 함수 선언
def money_plus():
  print("[ 금액 충전 ]")
  print(f'현재 잔액 : {session_info['money']:,} 원 입니다.')
  plusm = int(input('충전하실 금액을 입력하세요. : '))
  if plusm < 0:
    print("0보다 작은 금액은 입력할 수 없습니다.")
  else:
    session_info['money'] += plusm
    print(f"충전 후 잔액 : {session_info['money']:,} 원 입니다.")
# ------------------------

# 잔액 저장 함수 선언
def buy_save():
  f = open('member.txt','w',encoding='utf-8')
  for m in member:
    f.write(f"{m['id']}, {m['pw']}, {m['name']}, {m['nicName']}, {m['money']}, {m['address']}\n")
  f.close()
  f = open('member.txt','w',encoding='utf-8')
  for c in cart:
    f.write(f"{c['cno']}, {c['id']}, {c['name']}, {c['pCode']}, {c['pName']}, {c['price']}, {c['color']}\n")
  f.close()
  print("내용 저장이 완료되었습니다.")
  print()
# -----------------------------



### 프로그램 시작 ###
# 로그인 화면
while True:
  # 로그인이 되어 있을 때에만 물건 구매 가능하도록 설정
  input_id = input("아이디를 입력하세요.")
  input_pw = input("패스워드를 입력하세요.")

  # 푸후 DB에서 가져와 비교함
  flag = 0
  for i in member:
    if input_id == i['id'] and input_pw == i['pw']:
      print(f"{i['name']} 님, SM SHOP에 오신 것을 환영합니다.")
      session_info = i  #실개발에선 정보를 통으로 집어넣지는 않음(보안)
      flag = 1
      break
  if flag == 0:
    print("아이디 또는 패스워드가 일치하지 않습니다.")
  else:
    break

# 제품 구매
while True:
  print("                  [ SM-SHOP ]")
  print(f"         닉네임 {session_info['nicName']} 님, 반갑습니다.")
  print(f"           보유액: {session_info['money']:,}원")
  print("1. 삼성TV          - 2,000,000원")
  print("2. LG냉장고        - 3,000,000원")
  print("3. 하만카돈 스피커 - 50,000원")
  print("4. 세탁기          - 1,000,000원")
  print("7. 내용저장")
  print("8. 구매내역")
  print("9. 금액충전")
  choice = int(input("구매하려는 상품 번호를 입력하세요. : "))

  if choice == 1:
    cartNo = buy(choice, cartNo)         # 상품 구매함수 호출
  elif choice == 2:
    cartNo = buy(choice, cartNo)         # 상품 구매함수 호출
  elif choice == 3:
    cartNo = buy(choice, cartNo)         # 상품 구매함수 호출
  elif choice == 4:
    cartNo = buy(choice, cartNo)         # 상품 구매함수 호출
  elif choice == 7:
    buy_save()                           # 내용 저장 함수 호출
  elif choice == 8:
    buy_output()
  elif choice == 9:
    money_plus()
      
  # c = {'cno':cartNo+1, 'id':session_info['id'], 'name':session_info['name'], 'pCode':product[choice-1]['pCode'], 'pName':product[choice-1]['pName'], 'price':product[choice-1]['price']} #이런식으로 작성하면 함수로 빼낼 수 없음