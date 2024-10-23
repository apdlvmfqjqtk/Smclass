a = [1, 2, 3, 4, 5]

# list 내포 이용
b = [ x*x for x in a]
print(b)

# 기존 사용
c = []
for i in a:
  c.append(i*i)
print(c)

import csv
st_list = ['순위', '종목명', '검색비율', '현재가', '전일비', '등락률', '거래량', '시가', '고가', '저가', 'PER', 'ROE']
sto_list = ['1', '삼성전자', '11.68%', '57,800', '상승100', '+0.17%', '7,670,225', '57,500', '58,200', '57,100', '14.13', '4.15']
sto_list2 = ['2', 'SK하이닉스', '3.25%', '190,600', '상승2,800', '+1.49%', '747,655', '188,500', '191,800', '188,000', '55.54', '-15.61']
# csv 파일 저장 - 리스트로 바로 저장
with open('c1023/a.csv','w',encoding='utf-8-sig') as f:
  writer = csv.writer(f)
  writer.writerow(st_list)
  writer.writerow(sto_list)
  writer.writerow(sto_list2)