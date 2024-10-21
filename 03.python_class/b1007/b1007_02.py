numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
# # 100 이상의 값만 출력
# for n in numbers:
#   if n >= 100:
#     print(n)

# 크기 순으로 정렬
# numbers.sort()            # 순차정렬 - 낮은 수 부터 출력
numbers.sort(reverse=True)  # 역순정렬 - 높은 수 부터 출력
print(numbers)

# 순서를 역순 출력
numbers.reverse() # 순서를 역순으로 출력한다. (정렬이 아님)
print(numbers)