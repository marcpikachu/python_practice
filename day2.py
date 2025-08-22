# Day 2 – FizzBuzz 練習
# 請寫一個程式，印出 1 到 20 的數字。
# 如果數字能被 3 整除，印出 "Fizz"
# 如果數字能被 5 整除，印出 "Buzz"
# 如果同時能被 3 和 5 整除，印出 "FizzBuzz"
# 否則印出數字本身

# range(start, end) 的規則
# start → 起始值（包含）
# end → 結束值（不包含）



for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 判斷奇數偶數

for i in range(1, 11):
    if i % 2 == 0:
        print(i, "是偶數")
    else:
        print(i, "是奇數")

# 九九乘法表
print("\n=== 九九乘法表 ===")
for i in range(1, 10):      # 1 到 9
    for j in range(1, 10):  # 1 到 9
        print(f"{i} x {j} = {i*j:2d}", end="  ")  # 使用 f-string 和格式化
    print()  # 換行

# 學習函數 (Functions)
# 函數是可以重複使用的程式碼區塊

def print_multiplication_table():
    """列印九九乘法表的函數"""
    print("\n=== 函數版本的九九乘法表 ===")
    for i in range(1, 10):      # 1 到 9
        for j in range(1, 10):  # 1 到 9
            print(f"{i} x {j} = {i*j:2d}", end="  ")
        print()  # 換行

# 呼叫函數來執行
print_multiplication_table()

# TODO(human) - 接下來練習建立有參數的函數

# 計算字串長度

text = "Hello Python"
print("字串長度:", len(text))    # 12

# 找出字串裡有幾個母音 (a, e, i, o, u)

text = "I am learning Python"
count = 0
for char in text.lower():
    if char in "aeiou":
        count += 1
print("母音數量:", count)

