title = ['e_id', 'e_name', 'salary']
aa= [
  (196, 'Alana Walsh', 3100.0),
  (125, 'Julia Nayer', 3200.0),
  (180, 'Winston Taylor', 3200.0),
  (194, 'Samuel McCain', 3200.0),
  (138, 'Stephen Stiles', 3200.0)
]
a_list = []
# print(type(a))
for i in aa:
  a_list.append(dict(zip(title,i)))
print(a_list)



# name = '홍길동'

# # 문자 변수
# print('안녕하세요 이름은 %s'%name)
# # format함수
# print("hello, my name is {}".format(name))
# # 문자 f함수
# print(f"hello, my name is {name}")
# # a = 1
# # b = 2

# # a_list = [a,b]
# # print(type(a_list))

# # b_list = [b]
# # print(type(b_list))


# # a_tuple = (a,b)
# # print(type(a_tuple))

# # # b_tuple = (a) int 타입
# # # 튜플 한개만 지정할 경우 뒤에 ','을 넣어야 함
# # b_tuple = (a,)
# # print(type(b_tuple))