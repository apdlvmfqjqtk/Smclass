member = [
  {"id":"aaa","pw":"1111",'name':'홍길동','nicName':'길동스','money':100000000,'address':'서울특별시'},
  {"id":"bbb","pw":"2222",'name':'유관순','nicName':'관순스','money':70000000,'address':'부산시'},
  {"id":"ccc","pw":"3333",'name':'이순신','nicName':'순신스','money':50000000,'address':'경기시'},
  {"id":"ddd","pw":"4444",'name':'강감찬','nicName':'감찬스','money':20000000,'address':'인천시'},
  {"id":"eee","pw":"5555",'name':'김구','nicName':'김스','money':10000000,'address':'대구시'}
]

# member.txt 파일 생성해서 scv내용 저장
f = open('member.txt','w',encoding='utf-8')

for m in member:
  f.write(f"{m['id']},{m['pw']},{m['name']},{m['nicName']},{m['money']},{m['address']}\n")

f.close





# students = [
#   {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
#   {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
#   {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
#   {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
#   {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
# ]
# # 딕셔너리 파일 이용해 value값 메모장에 csv형태로 저장
# f = open('students.txt','w',encoding='utf-8')
# for s in students:
#   f.write(f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n")
# f.close

# students.txt
# 1, 홍길동, 100, 100, 99, 299, 99.66666666666667, 0