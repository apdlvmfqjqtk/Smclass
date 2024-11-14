# 리스트
# in - data 있는지 확인
# counte: 데이터가 있는 위치/   # count - 문자열 내 해당 숫자 개수 확인
# find: 데이터가 있는 위치, 없으면 -1
# index: 데이터가 있는 위치, 없으면 에러

fruit = "사과, 배, 딸기, 포도, 복숭아, 배, 사과, 배, 딸기"
# 배가 있는지 위치 모두 출력
print("모든 글자 :",fruit)
search = input("과일 이름을 입력하세요")
idx = 0
if fruit.count(search) > 0:
    print(f"{search} 글자가 있습니다.")
    for i in range(fruit.count(search)):
        print(f"{search} 글자가 있습니다.")
        for i in range(idx, len(fruit)):
            print(f"{search} 글자가 위치", )
            print(fruit.find(search,idx))
            idx = fruit.find(search,idx) + 1
            break
else:
    print(f"{search}라는 글자는 없습니다.")

# 보환필요
# fruit = "사과, 배, 딸기, 포도, 복숭아, 배, 사과, 배, 딸기"
# print(fruit.count("딸기"))
# # 과일을 입력받아 있다없다 대답
# search = input("과일이름")
# if search in fruit:
#   print(f"{search}라는 글자가 있어요")
#   print(fruit(f"search"))
#   # print(fruit.index(search)) # 배가 있는지 위치의 인덱스
# else print(f"{search}라는 글자는 없어요")
# print("과일검색개스 : "{} format)


# # count - list에서 개수 확인
# fruit = ['사과', '배', '딸기', '포도', '복숭아', '배', '사과', '배', '딸기']
# print(fruit.count('배'))
# print(fruit.count('사과'))


# fruit = ['사과', '배', '딸기', '포도', '복숭아']
# # 글자를 입력받아 입력한 과일이 있는지 없는지 출력
# furu = input("과일 이름을 입력해주세요 : ")
# if furu in fruit:
#   print(f'{furu}이(가) 있어요.')
# else:
#   print(f'{furu}이(가) 없어요.')


# fruit = "사과, 배, 딸기, 포도"
# if '배' in fruit:
#   print("배라는 글자가 있어요.")
# else:
#   print("배라는 글자가 없어요.")


# fruit = ['사과', '배', '딸기', '포도']
# if '배' in fruit:  #1번의 비교로 있는지 확인
#  print("배가 있어요.")
# else:
#  print("배가 없어요.")
