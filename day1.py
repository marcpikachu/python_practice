nums = [1, 2, 3]
nums.append(4)
print(nums)   # [1, 2, 3, 4]

nums = [1, 2, 3]
nums.insert(0, 100)   # 插到最前面
print(nums)           # [100, 1, 2, 3]

nums = [1, 2, 3, 2]
nums.remove(2)
print(nums)   # [1, 3, 2]   ← 只刪掉第一個 2

nums = [10, 20, 30]
x = nums.pop(1)   # 刪掉 index 1 → 20
print(nums)       # [10, 30]
print(x)          # 20  ← 被刪掉的值

nums = [1, 2, 3]
nums.extend([4, 5, 6])
print(nums)   # [1, 2, 3, 4, 5, 6]

nums = [1, 2, 3]
nums.clear()
print(nums)   # []

person = {"name": "Marc", "age": 28, "city": "Taipei"}
print(person.get("city"))       # Taipei
print(person.get("job"))        # None
print(person.get("job", "N/A")) # N/A

person["city"] = "Kaohsiung"
print(person)
# {'name': 'Marc', 'age': 28, 'city': 'Kaohsiung'}

person["job"] = "Engineer"
print(person)
# {'name': 'Marc', 'age': 28, 'city': 'Kaohsiung', 'job': 'Engineer'}

del person["age"]   # 用 del 刪除
print(person)
# {'name': 'Marc', 'city': 'Kaohsiung', 'job': 'Engineer'}

for key, value in person.items():
    print(key, ":", value)

# name : Marc
# city : Kaohsiung
