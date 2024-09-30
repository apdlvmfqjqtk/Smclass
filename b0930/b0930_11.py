# 1759870
# 9870
# 590
money_title = ["오만원", "만원", "오천원", "천원", "오백원", "백원", "오십원", "십원"]
for mt in money_title :
  print("{}".format(mt), end="\t")
  
  
money =(input("금액 3개를 입력하세요"))
print(money.split(" "))
money_data = money.split(" ")
print(money_data)

for md in money_data :
  

# str1 = input("문자를 입력하세요 : ")
# a = len(str1)  #문자의 길이 .length

# if a == 5 :
#   print("a는 5입니다.")
# elif a == 4 :  #else if
#   print("a는 4입니다")
# elif a == 3 :
#   print("a는 3입니다.")
# else :
#   print("a는 2이하입니다.")







# money = 1759870
# # 50000,10000,5000,1000,500,100,50,10
# # 5만원
# print(money//50000)
# # 1만원
# print((money%50000)//10000)
# # 5천원
# print(((money%50000)%10000)//5000)
# # 1천원
# print((((money%50000)%10000)%5000)//1000)
# # 5백원
# print(((((money%50000)%10000)%5000)%1000)//500)
# # 1백원
# print((((((money%50000)%10000)%5000)%1000)%500)//100)
# # 5십원
# print(((((((money%50000)%10000)%5000)%1000)%500)%100)//50)
# # 1십원
# print((((((((money%50000)%10000)%5000)%1000)%500)%100)%50)//10)


# money = 780
# # 500원짜리 - 1개
# print("500원 동전 개수 :", money//500)
# # 100원짜리 - 2개
# print("100원 동전 개수 :", (money%500)//100)
# # 50원짜리 - 1개
# print("50원 동전 개수 :", ((money%500)%100)//50)
# # 10원짜리 - 3개
# print("10원 동전 개수 :", (((money%500)%100)%50)//10)