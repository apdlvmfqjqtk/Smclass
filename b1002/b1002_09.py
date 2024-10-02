fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"
fruit = fruit.split(",")
print(fruit)
print(len(fruit))
# list인 경우 해당되는 index를 출력하시오.
# 배 에 해당하는 index번호 출력
s = input("과일 이름을 입력하세요 : ")
for idx,n in enumerate(fruit): 
  if n == s: 
    print(n,idx,)
  else:
    print('해당 과일이 없습니다.')
    break


# 배찾기
# print(fruit.find('배',0))
# print(fruit.find('배',fruit.find('배',0)+1))
# print(fruit.find('배',3+1))
# print(fruit.find('배',fruit.find('배',fruit.find('배',0)+1)+1))
# print(fruit.find('배',15+1))


# 딸기찾기
# print(fruit.find('딸기',0)) # find(a,n) a를 n부터 찾아라
# print(fruit.find('딸기',fruit.find('딸기',0)+1))
# print(fruit.find('딸기',6))