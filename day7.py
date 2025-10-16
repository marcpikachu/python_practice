squares = [num * num for num in range(1, 11)]
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print(even_numbers)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

numbers = [12, 45, 23, 67, 34, 89, 2]
max_num = numbers[0]  # 先假設第一個數是最大值

for num in numbers:
    if num > max_num:  # 如果有更大的，就更新最大值
        max_num = num

print("最大值是", max_num)
# 最大值是 89