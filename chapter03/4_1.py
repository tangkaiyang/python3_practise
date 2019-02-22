# -*- coding:UTF-8 -*-

class Cat(object):
    def say(self):
        print("i am a cat")

class Dog(object):
    def say(self):
        print("i am a dog")
    def __getitem__(self, item): # 实现此方法使其成为iterable
        return "bobby"

class Duck(object):
    def say(self):
        print("i am a duck")

animal = Cat
animal().say()

# java中的多态,所有的子类必须继承父类,后要重写say方法,才能指明
# class Animal():
#     def say(self):
#         print("i am a animal")
# class Cat(Animal):
#     def say(self):
#         print("i am a cat")
#
# Animal.an = Cat()
# an.say()
# 而python中变量是动态的,可以继承任何一个父类,可以存放任何的类
# 类实现了共同方法名,就可以当做是同一种类

animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()

a = ["bobby1", "bobby2"]
b = ["bobby2", "bobby"]
name_tuple = ["bobby3", "bobby4"]
name_set = set()
name_set.add("bobby5")
name_set.add("bobby6")
# a.extend(name_tuple)
a.extend(name_set)
print(a)
"""
extend(iterable)只需要是可迭代类型即可,不需要具体的list,一个生成器也是可以
callable可调用对象class,func等
静态语言中参数的类型是定死的
__getitem__与上述的say方法相近?不需要指明特定的类即可调用
实现相应的魔法函数,对象即可进行相应的类型的操作
"""