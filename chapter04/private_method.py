# -*- coding:UTF-8 -*-

# java c中private protected
# python中无上述方法
from chapter03.class_method import Date


class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        # 返回年龄
        return 2018 - self.__birthday.year


class Student(User):
    def __init__(self, birthday):
        self.__birthday = birthday


if __name__ == '__main__':
    user = Student(Date(1990, 2, 1))
    # print(user.birthday)
    # print(user.get_age())
    # print(user._User__birthday)
    print(user._Student__birthday)

# 希望用户看不到birthday,只能看到age
# 使用__birthday
# 调用obj._classname__method可以输出,并不是完全私有,不绝对安全
# 私有属性让编码更规范
# java反射机制?不绝对安全
