stu_title = ["번호", "이름", "국어", "영어", "수학", "과학", "합계", "평균", "등수"]
stu_datas = [
    [1, "홍길동", 100, 100, 100, 99],
    [2, "유관순", 100, 100, 100, 99],
    [3, "이순신", 100, 99, 98, 99],
    [4, "김구", 80, 100, 90, 99],
    [5, "김유신", 80, 100, 90, 99],
]

# append - 합계 평균 추가해서 출력

print("[학생성적]")
for st in stu_title : 
  print("{}".format(st), end='\t')
print()
print("-"*70)


for sd in stu_datas:
    sd.append(sd[2] + sd[3] + sd[4] + sd[5])
    sd.append((sd[2] + sd[3] + sd[4] + sd[5]) / 4)
    # print(sd)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
      sd[0], sd[1], sd[2], sd[3], sd[4], sd[5], sd[6], sd[7]
    ))
# sd에 추가하면 stu_data에도 추가가 됨
# print(stu_datas)
