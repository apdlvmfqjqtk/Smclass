n_lists = [
  ['jhon',100, 4.5,1000],
  ['park',100, 4.2,800],
  ['lee',100, 4.4,2000],
  ['trumf',100, 4.7,10],
  ['park',100, 4.3,30],
]

print("기본: ", n_lists)
n_lists.sort(key=lambda x:x[0], reverse=True)
print("금액정렬 :", n_lists)





































# a = "안녕하세요"
# print(a[1:])
# print(a[1:-1])
# print(a[:3])
# print(a[::-1])

# lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(lists[1:-1])
# print(lists[:-1])
# print(lists[3:])
# print(lists[3:5])


# b = 12345
# # print(b[1:3]) int타입은 슬라이스 불가