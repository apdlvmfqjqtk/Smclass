s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]
kor = int(input("국어 점수를 입력하세요"))
eng = int(input("영어 점수를 입력하세요"))
math = int(input("수학 점수를 입력하세요"))

# 위 문장을 for문으로 입력하는 방법
score = []
for sc in range(3):
  score.append(int(input(f"{s_title[sc+2]}점수를 입력하세요")))

print(score)