# 8-3 属性描述符和属性查找过程
from datetime import date, datetime

class IntField:
    # 定义以下任意魔法函数,就可以作为属性描述符
    def __get__(self, instance, owner):
        pass
    def __set__(self, instance, value):
        pass
    def __delete__(self, instance):
        pass


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
    user.age = 30
    pass
    # user = User("bobby", date(year=1993, month=12, day=28))
    # user.age = 30
    # print(user._age)
    # print(user.age)