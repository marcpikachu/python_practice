class Dog:
    def __init__(self, name):
        # 初始化屬性，把參數 name 存到物件裡
        self.name = name

    def bark(self):
        # 使用 f-string，把物件的名字印出來
        print(f"汪汪！我是 {self.name}")

# 測試
dog1 = Dog("Lucky")
dog2 = Dog("Coco")

dog1.bark()   # 汪汪！我是 Lucky
dog2.bark()   # 汪汪！我是 Coco

class Cat:
    def __init__(self, name):
        self.name = name   # 把傳進來的名字存進物件

    def meow(self):
        print(f"喵喵！我是 {self.name}")

# 測試
cat1 = Cat("Mimi")
cat2 = Cat("Dodo")

cat1.meow()   # 喵喵！我是 Mimi
cat2.meow()   # 喵喵！我是 Dodo
