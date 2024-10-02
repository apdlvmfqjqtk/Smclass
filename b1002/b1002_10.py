fruit = []

while True:
  # strip() 앞쪽 여백, 뒤쪽 여백 제거 (trim과 같음) '  사과' -> '사과', '사과   ' -> '사과"
  # '사  과' -> '사 과'  (strip의한계)
  # replace(" ","") : 문자대체함수
  search = input("과일 이름을 입력하세요.(종료): ").replace(" ","")
  if(search == 'x'):
    break
  # 입력된 과일을 리스트에 추가
  if search in fruit:
    print('같은 이름이 있습니다')
    print('모든 과일 이름',fruit)
  else:
    print(f"{search}을(를) 추가합니다.")
    fruit.append(search)
    print('모든 과일 이름',fruit)



# 반복문을 종료할때 : break
# while True:
#   break 
# # break, continue는 반복문에서만 사용
# print("프로그램 종료")

# 무한 반복문은 while True 입력
# a=0
# while True: # 무한반복
#   a += 1
#   print(a)