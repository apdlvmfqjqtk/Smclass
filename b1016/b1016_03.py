# students = [
#  넣고 싶은 형태(딕셔너리) {'no':'1', 'name':'홍길동','kor':'100', 'eng':'100', 'math':'99', .....}
#   [1, '홍길동', 100, 100, 99, 299, 99.66666666666667, 0],
#   [2, '유관순', 90, 80, 99, 269, 89.66666666666667, 0],
#   [3, '이순신', 100, 99, 90, 289, 96.33333333333333, 0]
# ]

stu_key = ["no", "name", "kor", "eng", "math", "total", "avg", "rank"]
students = []

# 파일 읽기 - r
f = open("a.txt", "r", encoding="utf-8")
while True:
    line = f.readline()
    if not line:
        break
    s = line.strip().split(",")
    s[0] = int(s[0])
    s[2] = int(s[2])
    s[3] = int(s[3])
    s[4] = int(s[4])
    s[5] = int(s[5])
    s[6] = float(s[6])
    s[7] = int(s[7])

    # for i,v in enumerate(s):
    #   if i == 1: continue
    #   elif i == 6: s[6]['avg'] = float(s[6]['avg'])
    #   else: v= int(v)
    students.append(dict(zip(stu_key,s)))
    print(line.strip())

print(students)
f.close()
