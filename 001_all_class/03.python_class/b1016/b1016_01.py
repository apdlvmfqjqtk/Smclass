# 파이썬 파일 입출력
# 1. 파일 열기 -> 2. 파일 쓰기 -> 3. 파일 닫기의 순서로 진행된다
# 열기 모드: r(읽기) / w(쓰기) / r+(덮어쓰기(이전 내용 날아감)) / a(이어쓰기) / b(파일 이동할 때 씀)

# close(를 하지 않아도 됨)
with open('aa.txt','w',encoding='utf-8') as f:
  f.write("안녕하세요.")



# # 파일 이어쓰기 - a
# while True:
#   print("[ 메모장 ]")
#   data = input("저장하려는 글자를 입력하세요. : ")
#   f = open('aa.txt', 'a', encoding='utf-8')
#   f.write(data + '\n')
#   f.close


# 파일 쓰기 - w: 파일 생성 후 글자 입력
# f = open('aa.txt','w',encoding='utf-8')
# for i in range(1,11):
#   data = f"안녕하세요. {i} \n"
#   f.write(data)
# f.close
# print("글쓰기 종료")


# f.write("안녕하세요.1\n")
# f.write("안녕하세요.2\n")
# f.write("안녕하세요.3\n")
# f.close
# print("글쓰기 종료")




# 파일 읽기 - r
# 위치에 파일이 없으면 에러

# # 3. read() - 한 줄 단위로 가져와서 읽어 줌
# f = open('a.txt','r',encoding='utf-8')
# # print(type(f))
# for line in f:
#   print(line.strip())
# f.close

# # 2. readlines() - 모든 글을 읽어오기
# f = open('a.txt','r',encoding='utf-8')
# lines = f.readlines()
# for line in lines:
#   print(line.strip())
# f.close


# # 가장 바깥 폴더의 위치에서 파일을 찾음
# f = open('a.txt',  'r', encoding='UTF-8')

# # 절대경로 사용
# f = open('c:/aaa/a.txt', 'r', encoding='UTF-8')  # 파일 열기 (한글 읽으려면 인코딩=utf-8 필요 (utf는 대,소문자 상관없음) 

# f = open('b.txt',  'r', encoding='UTF-8')
# while True:
#   line = f.readline()                     # 파일 쓰기
#   if not line: break  # \n값 생략(공백 제거)
#   print(line.strip())
# f.close()                                 # 파일 닫기