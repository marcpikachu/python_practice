def sum_list(nums):
    total = 0
    for n in nums:
        total = total + n   # 或者寫成 total += n
    return total

print(sum_list([1, 2, 3, 4]))  # 輸出 10


def greet(name="Marc"):
    return f"Hello, {name}"

print(greet("Amy"))   # Hello, Amy
print(greet())        # Hello, Marc

def square(n):
    return n * n   # 或者 return n ** 2 也可以

print(square(3))   # 9
print(square(5))   # 25

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(4))   # True
print(is_even(7))   # False

def list_length(lst):
    return len(lst)

print(list_length([1, 2, 3]))   # 3
print(list_length(["a", "b"]))  # 2

