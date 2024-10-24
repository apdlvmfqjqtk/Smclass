lists = ['8억','10억','6억 5000','3억','10억','12억 5,000']

# a = "9억 5000"
# b = a.split('억')
def num_chg(p):
  b=p.split('억')
  f_num = int(b[0])*100000000
  if b[1].strip() != '':
    s_num = int(b[1].strip().replace(",",""))*10000
  else:
    s_num = 0
  price = f_num+s_num
  return price



r_list = list(map(num_chg,lists))
print(r_list)