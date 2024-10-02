students = [
    [1, "홍길동", 100, 100, 99],
    [2, "유관순", 100, 100, 99],
    [3, "이순신", 100, 100, 99],
]
ss = [4, "강감찬", 100, 90, 99]
# students에 ss추가
students.append(ss)
print(students)

# 값이 2개 이상 저장하려면 주소값이 필요
# 이순신인 데이터를 삭제
# del 삭제
for idx,s in enumerate(students):  # 1개씩 가져와서 출력
    if s[1] == "이순신":
        del students[idx]  # del로 삭제
print(students)


# remove 삭제
for s in students:  # 1개씩 가져와서 출력
    if s[1] == "이순신":
        students.remove(s)  # remove

print(students)

# for s in students:  # 1개씩 가져와서 출력
#     if s[1] == "유관순":
#         print(s)
