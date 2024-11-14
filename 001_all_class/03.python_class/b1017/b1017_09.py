import os

f = open('b1017/students.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line:
    break
  print(line.strip())

# 있을때만 읽고 아닐떄는 읽지않기(에러방지)
if os.path.isfile("b1017/cart.txt"):
  print("파일이 존재합니다.")
else:
  print("파일이 존재하지 않습니다")