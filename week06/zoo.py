# 具体要求：
# 定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
# 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
# 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。
# 狗类属性与猫类相同，继承自动物类。
# 动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
from abc import ABC,ABCMeta,abstractmethod

class Animal(metaclass = ABCMeta):  #不允许被实例化
    def __init__(self,type,size,character) -> None:
        self.type = type   #类型
        self.size = size  #体形
        self.character = character #性格
    @abstractmethod
    def fierce(self):
        if self.size == "中等" or self.size == "大":
            return True
        return False

class Cat(Animal):
    cry = None
    def __init__(self,name,type,size,character) -> None:
        super().__init__(type,size,character)
        self.name = name
    def suitableAsPet(self):
        return self.fierce
    def fierce(self):
        if self.size == "中等" or self.size == "大":
            return True
        return False

class Dog(Animal):
    cry = None
    def __init__(self,name,type,size,character) -> None:
        super().__init__(type,size,character)
        self.name = name
    def suitableAsPet(self):
        return self.fierce
    def fierce(self):
        if self.size == "中等" or self.size == "大":
            return True
        return False

class Zoo:
    def __init__(self,name) -> None:
        super().__init__()
        self.name = name
        self.list = []

    def add_animal(self,animal:Animal):
        if animal in self.list:
            print("不能重复添加")
            return
        self.list.append(animal)
        print("添加动物")
    def __getattribute__(self, name: str):
        try:
            return super().__getattribute__(name)
        except Exception as e:
            for animal in self.list:
                if animal.__class__.__name__ == name:
                    return True
            return False

    # @classmethod #类方法

    # @staticmethod #静态方法


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    cat1.fierce
    # 增加一只猫到动物园
    z.add_animal(cat1)
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(have_cat)
