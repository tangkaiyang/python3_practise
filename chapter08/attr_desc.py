# 8-3 属性描述符和属性查找过程
from datetime import date, datetime
import numbers


class IntField:
    # 定义以下任意魔法函数,就可以作为属性描述符
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value need")
        self.value = value

    def __delete__(self, instance):
        pass


class NonDataIntField:
    # 非数据属性描述符,实现了__get__,__set__称为数据属性描述符
    def __get__(self, instance, owner):
        return self.value


class User:
    age = IntField()


# class User:
#     def __init__(self, name, email,  birthday):
#         self.name = name
#         self.email = email
#         self.birthday = birthday
#         self._age = 0
#
#     # def get_age(self):
#     #     return datetime.now().year - self.birthday.year
#
#     @property
#     def age(self):
#         return datetime.now().year - self.birthday.year
#
#     @age.setter
#     def age(self, value):
#         # 检查是否为字符串类型
#         self._age = value


if __name__ == "__main__":
    user = User()
    user.age = 30  # 调用__set__方法
    print(user.__dict__)
    print(user.age)
    # user = User("bobby", date(year=1993, month=12, day=28))
    # user.age = 30
    # print(user._age)
    # print(user.age)

"""
属性描述符查找顺序:
如果user是某个类的实例,那么user.age(以及等价于getattr(user, 'age'))
首先调用__getattribute__.如果类定义了__getattr__方法,
那么在__getattribute__抛出AttributeError的时候就会调用到__getattr__,
而对于描述符(__get__)的调用,则是发生在__getattribute__内部的
"""