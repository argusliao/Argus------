# 動物類別
class Animal:
    def __init__(self) -> None:
        self.bb = "animal_test"
        print("animal")

    def aa(self):
        print("AA")

    def __bb(self):
        print("__bb")

# 鳥類類別
class Bird(Animal):
    def __init__(self) -> None:
        super().__init__()
        print("bird")
    # 飛行方法
    def fly(self):
        print("fly")

# 鴨子類別
class Duck(Bird):
    def __init__(self) -> None:
        super().__init__()
        print("dark")

    def __bbaa(self):
        print("__bb")

    def cc(self):
        self.__bbaa()

duck = Duck()
# duck.fly()
print(duck.bb)
duck.cc()

# bird = Bird()
# bird.aa()
