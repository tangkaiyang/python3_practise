# python中垃圾回收算法是采用 引用计数
# a = 1
# b = a
# del a # 此时1的引用计数减1,当计数为0时回收
a = object()
b = a
del a
print(b)
print(a)
class A:
    def __del__(self): # del是会调用__del__,可自定义逻辑
        pass