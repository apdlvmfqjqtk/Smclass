# 1 - 100까지의 랜덤 수 출력. 10번의 기회 동안 업다운. 성공 / 실패 여부 상관없이 시도한 모든 수가 나오게 출력
import random  # 랜덤 함수를 쓰기 위한 임포트

# 1 - 100 랜덤 수 설정
rand = random.randint(1, 100)
sf = 0  # (10번 반복 안에 답이 나오지 않으면 실패를 출력하기 위한 변수)
i = 0  # while문 반복 위한 변수
t_list = []  # 시도한 숫자 저장 위해서 리스트 미리 생성

while i < 10:  # i가 10보다 작을  때 까지 반복 실행
    trn = int(input(f"숫자를 입력, {i +1 }번째 시도 : "))
    t_list.append(trn)  # 리스트에 숫자를 저장
    if trn < rand:  #  입력한 숫자가 더 작다면
        print("더 높은 숫자를 입력해주세요.")
    elif trn > rand:  # 입력한 숫자가 더 크다면
        print("더 작은 숫자를 입력해주세요.")
    else:  # 둘 다 아니라면 (trn == rand)
        print(f"성공입니다. 정답은 {rand}입니다.")
        print(f"시도한 숫자 : {t_list}")  # 시도한 숫자 출력
        sf += 1
        break

    i += 1

if sf == 0:
    print(f"실패입니다. 기회를 모두 소진하였습니다. 정답은 {rand}입니다.")
    print(f"시도한 숫자 : {t_list}")  # 시도한 숫자 출력
