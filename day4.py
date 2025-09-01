def add_all(*args):
    total = 0
    for n in args:
        total += n   # 和 sum_list 一樣累加
    return total

# 測試
print(add_all(1, 2, 3))         # 6
print(add_all(10, 20, 30, 40))  # 100

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 測試
print_info(name="Amy", age=20)
# 輸出：
# name: Amy
# age: 20
