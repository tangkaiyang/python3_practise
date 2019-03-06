"""
类也是对象,type创建类的类
"""


def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"

        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"

        return Company


# type动态创建类


# User = type("User", (), {})
def say(self):
    return "i am user"
    # return self.name


class BaseClass:
    def answer(self):
        return "i am baseclass"

class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
# 什么是元类,元类是创建类的类,对象<-class(对象)<-type(元类)
class User(metaclass=MetaClass):
    pass
# python中中类的实例化过程,会首先寻找metaclass,通过metaclass去创建user类(先找自己的,在调用父类的基类,再找包里的,最后是type)
# type去创建类对象,实例
# 抽象基类中就是重写了__new__方法


if __name__ == "__main__":
    # MyClass = create_class("user")
    # my_obj = MyClass()
    # print(type(my_obj))
    User = type("User", (BaseClass,), {"name": "user", "say": say})
    my_obj = User()
    print(my_obj)
    print(my_obj.answer())
