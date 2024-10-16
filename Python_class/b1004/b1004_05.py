# for문을 출력하는데, 
for k in range(1,10):
  print(f"[ {k} 단 ]",end="\t")
print()  
for i in range(2, 10):
  # print(f"[ {i}단 ]")
  # print(f"[ {i}단 ]",end="\t")
  for j in range(1, 10):
    print(f"{j} X {i} = {j*i}", end="\t")
  print()


# # 000
# # 001
# # ...
# # 999 출력하려면
# for i in range(10):
#   for j in range(10):
#     for k in range(10):
#       print(f"{i}{j}{k}")
# # 또는 
# for a in range(0, 999+1):
#     print(f"{a:03d}")

# # 99단 입력한 단 까지 출력하시오.
# s = int(input("몇단까지 출력할까요 : "))
# for i in range(s, s+1):
#   print(f"{i}단")
#   for j in range(1,9+1):
#     print(f"{i} X {j} : {i*j}")