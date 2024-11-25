from bung import 붕어빵


a = 붕어빵('반죽1', '팥')


print(a.반죽)
print(a.속)


import bung
b=bung.붕어빵('반죽2','팥')

print(b.반죽)
print(b.속)

# 다른 폴더 안에 있는py 파일을 실행시키려면
import folder.bung_copy

c = folder.bung_copy.붕어빵('반죽3','슈크림')
print(c.반죽)
print(c.속)


# 위 임포트 명령어를 as로 다른 단어로 치환해서 짧게 변경할 수도 있다.
import folder.bung_copy as aa

d = aa.붕어빵('반죽4','슈크림')

print(d.반죽)
print(d.속)