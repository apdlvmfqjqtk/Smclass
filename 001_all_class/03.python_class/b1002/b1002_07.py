students = [
    [1, "홍길동", 100, 100, 99],
    [2, "유관순", 100, 100, 99],
    [3, "이순신", 100, 100, 99],
    [4, "강감찬", 100, 90, 99],
    [5, "김구", 90, 90, 99],
]

# 이름을 입력받아 같은 이름이 있으면 데이터 삭제, 없으면 없습니다. 출력
name = input("이름을 입력해주세요")
count = 0
for idx, s in enumerate(students):
    if s[1] == name:
        del students[idx]
        print(f"{name}을(를) 삭제합니다.")
        count = 1
        break
    else:
        print("이름이 없습니다.")

print("현재 학생 성적 : ", students)
# 내꺼
# name = input("이름을 입력해주세요")
# print(name)
# for f in students :
#   if f[1] == name :
#     students.remove(f)
#   else:
#     print("다시 입력해주세요.")


# all_list = [
#   [1, '홍길동', 100],
#   [2, '유관순', 200],
#   [3, '이순신', 100]
# ]
# print(all_list)
# a = [3, '이순신', 100]

# # # 데이터 값으로 삭제 - remove
# # all_list.remove(a)
# # print(all_list)

# # all_list 이름이 유관순 삭제
# for l in all_list :
#   if l[1] == '유관순' :
#     all_list.remove(l) #remove 사용
# print(all_list)


# aArr = [2,3,4,6,7,8,9,10]
# # 50, 100을 추가하시오
# aArr.append(50)
# aArr.append(100)
# print(aArr)

# # 0번 1번 2번 자리에 30을 추가하시오
# aArr.insert(0,30)
# aArr.insert(1,30)
# aArr.insert(2,30)
# print(aArr)

# # 숫자 6을 삭제하시오
# aArr.remove(6)
# print(aArr)

# # 첫번째 데이터를 삭제하시오
# del aArr[0]
# print(aArr)

# # index 0, 3데이터를 삭제하시오
# del aArr[0]
# del aArr[3]
# print(aArr)
