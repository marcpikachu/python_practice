# def hello(a, b, c, /, d, *, e, f):
# pass

# /：位置參數（positional-only）
# 在 / 之前的參數（這裡是 a, b, c）只能用位置來傳入，不能用關鍵字。
# *：關鍵字參數（keyword-only）
# 在 * 之後的參數（這裡是 e, f）只能用關鍵字來傳入，不能用位置。
# 在 / 和 * 之間的參數（這裡是 d）可以用位置或關鍵字來傳入。

numbers = [num * num for num in range(1, 10)]
print(numbers)

# [1, 4, 9, 16, 25, 36, 49, 64, 81]

# from utils.greeting import hey as hello
# 從 utils/greeting.py 這個模組中，
# 匯入 名為 hey 的函式（或變數、類別），
# 並且在目前這個檔案裡 把它重新命名 成 hello。