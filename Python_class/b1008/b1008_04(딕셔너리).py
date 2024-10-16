# # 리스트 타입
# # 튜플 타입 - 수정이 불가능함
# # 딕셔너리 타입


# # 딕셔너리. 쌍 2개가 하나로 묶인 자료구조
# # 타 프로그래밍 언어에서는 해시, 연관배열이라고 함
# # {}로 묶어 구성, 키와 밸류값으로 이루어짐

# dic1 = {"번호":1, "이름":"홍길동", "kor":100, "eng":100}
# print(dic1["이름"])     # 출력방법 : 키를 입력하면 값을 출력함
# # print(dic1["합계"])   # 없는 키를 입력하면 에러가 발생
# dic1["math"] = 90       # 딕셔너리 추가법 : 없는 키와 값을 입력하면 그게 추가가 됨
# dic1['kor'] = 50        # 있는 키의 값을 입력하면 수정
# del(dic1['eng'])        # del(키) 입력하면 삭제
# print(dic1) 

# # 딕셔너리의 '값'만 출력하고 싶다.
# print(dic1["이름"])
# print(dic1.get("이름"))
# print(dic1.get("학번")) # 함수(get)를 이용한 출력을 할 때, 없는 키를 입력하면 None으로 나옴, 에러는 나지 않음

# if dic1.get("이름") != None:
#   print(dic1.get("이름"))

# # list의 단점: 보기 좋기는 한데 어떤 것의 값인지를 몰랐다
# a_list = [1, "홍길동", 100, 100, 100, 300, 100.0, 1]
# #  딕셔너리를 사용함으로 어떤 키의 값인지를 보다 쉽게 알 수 있게 됨
# # 딕셔너리의 키값은 한글을 사용해도 괜찮지만 (혹시나 에러)때문에 영어 입력 권장

# print(dic1.keys()) # 모든 키값을 출력한다.
# print(type(dic1.keys()))

# # 모든 키 출력 - keys
# for key in dic1.keys():
#   print(key,dic1[key])

# print(dic1[key])
# # type : class 객체
# print(type(dic1.keys()))
# # type : class 객체 -> list타입 변경
# list(dic1.keys())
# # list(dic1.keys()[0]) #  class객체 타입이기에 index값이 없음
# list(list(dic1.keys()))
# print(list(dic1.keys())[0])

# #  값만 출력
# #  vlaues( : class 객체 타입)
# print(dic1.values())
# print(list(dic1.values()))

# # 키, 값을 모두 출력
# print(dic1.items())
# print(list(dic1.items()))

# for i in dic1:
#   print(i) # key값만 나옴

# # 값만 추출
# for key in dic1:
#   print(dic1[key])

# # 키, 값을 추출
# for key,val in dic1.items():
#   print(key, val)

# dic1['평균'] = 99.0
# if '평균' not in dic1:
#   dic1['평균'] = 99.0
# print(dic1)



# # list는 주소값으로 출력했음
# a_list = [1, 2, 3, "홍길동"]
# print(a_list[0])
# # 추가 방법
# # append, insert, extend
