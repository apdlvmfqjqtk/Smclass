# 없는 폴더에 접근하면 에러가 뜸
import os

# os.path.exists() : 현재 폴더가 존재하는지 확인
# mkdir : 현재 폴더만 생성
# makedirs : 현재 폴더, 하위 폴더까지 생성

# 폴더가 없을 시 폴더 생성
# 폴더가 있는지 없는지 확인 후. (없다면 만들고)저장 하는것이 좋다 
# 파일 읽는거도 바로 읽어라 보다는 if문으로 있다면 읽어라 하는 것이 에러 방지 도움
if not os.path.exists("c:/ddd"):
  os.makedirs("c:/ddd")

f = open("c:/ddd/c.txt","w",encoding="UTF-8")
f.write("안녕하세요.")
f.close