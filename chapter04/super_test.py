class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super(B, self).__init__()  # python2
        super().__init__()  # python3


from threading import Thread


class MyThread(Thread):
    def __init__(self, name, user):  # 其中Thread类中有name属性可以使用super调用
        self.user = user
        super().__init__(name=name)


# 既然我们重写了B的构造函数;为什么还要去调用super?
# super到底执行顺序是什么样的?调用父类的方法并不准确,涉及到实例属性的查找顺序

class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B, C): # super优先调用B(写在前面)的构造函数
    def __init__(self):
        print("D")
        super(D, self).__init__()

if __name__ == "__main__":
    # b = B()
    print(D.__mro__)
    d = D()

# super函数按mro调用构造函数 Method Resolution Order 方法解析顺序

