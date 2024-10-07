# 학생 데이터
students = [
    [1, "홍길동", 100, 100, 99],
    [2, "유관순", 100, 100, 99],
    [3, "이순신", 100, 100, 99],
    [4, "강감찬", 100, 90, 99],
    [5, "김구", 90, 90, 99],
]

# 합계 평균 더하기
for s in students:
    s.append(s[2] + s[3] + s[4])
    s.append(int((s[2] + s[3] + s[4]) / 3))
print(students)

cnt = 0
search = input("찾고자 하는 학생 이름을 검색하세요. : ")
for s in students:
    # 찾는 학생이 있으면 있습니다 뜨기.
    if s[1] == search:
        print("검색한 학생이 있습니다.")
        cnt = 1
        break
        # for문 안에 else를 이용해 없는 경우를 적으면 없다는 문구도 똑같이 5번 반복됨
        # 고로 for문 밖 cnt 변수를 삽입해 출력시키기
if cnt == 0:
    print("찾고자 하는 학생 이름이 없습니다.")
