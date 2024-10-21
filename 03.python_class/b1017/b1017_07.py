# members 리스트 딕셔너리 저장
members = []
m_title = ['id','pw','name','nicName','address','money']

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

# # members 출력
# print(members)

while True:
  print("1. 회원등록")
  print("2. 회원검색")
  choice = input("원하는 번호를 입력하세요. : ")
  if choice == "1":
    id = input("ID를 입력하세요. : ")
    flag = 0
    for m in members:
      if m['id'] == id:
        print(f"{id}: 동일한 아이디가 존재합니다. 다시 입력해주세요.")
        flag = 1
        break
    if flag == 1:
      continue
    else:
      print(f"{id} 은(는) 사용 가능한 ID입니다.")
      print()
    pw = input("PW를 입력하세요. : ")
    name = input("이름을 입력하세요.")
    nicName = input("닉네임을 입력하세요.")
    address = input("주소 입력하세요.")
    money = int(input("보유금액을 입력하세요"))
    m_list = ['id','pw','name','nicName','address','money']
    members.append(dict(zip(m_title,m_list)))

    print(f"{id}님 회원가입이 완료되었습니다.")
    print(m_list)
    print("-"*50)
    print(members)
  #회원 검색
  elif choice == "2":
    search = input("검색할 회원 이름을 입력하세요. ")
    flag = 0
    mm = []
    for m in members:
      if m['name'].find(search) != -1:
        print("검색한 멤버를 찾았습니다.")
        mm.append(m)
        flag = 1

    if flag == 0:
      print("검색한 회원을 찾지 못했습니다.")
    else:
      pass





# 아이디 검색
# members 리스트에서
# 입력된 문자로 검색된 데이터를 모두 출력하시오
# (a가 들어간 아이디를 출력)