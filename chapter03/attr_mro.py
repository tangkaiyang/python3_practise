# class A:
#     name = "A"
#
#     def __init__(self):
#         self.name = "obj"
#
#
# a = A()
# print(a.name)
# 新式类默认继承obj
class D:
    pass
class E:
    pass
class C(E):
    pass
class B(D):
    pass
class A(B, C):
    pass

print(A.__mro__)