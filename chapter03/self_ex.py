# 自省是通过一定的机制查询到对象的内部结构

from chapter03.class_method import Date
class Person:
    """
    人,这里的内容通过Person.__doc__获得,在__dict__中
    """
    name = "user"

class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name

if __name__ == '__main__':
    user = Student("慕课网")

    # # 通过__dict__查询属性(字典通过c语言实现,性能很高的数据结构)
    # print(user.__dict__)
    # print(user.name)
    # # user.name没有进入dict,类也是对象,所以name是Person对象的属性,不是Student的属性
    # print(Person.__dict__)
    # # Person也是一个类,
    # user.__dict__["school_addr"] = "北京市"
    # print(user.school_addr)
    # # 可以对__dict__进行赋值
    # print(dir(user)) # 可以列出对象的所以属性,比__dict__更强大,但不展示属性值
    a = [1, 2]
    # print(a.__dict__) 抛异常
    print(dir(a)) # 不会报错