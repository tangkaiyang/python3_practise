# 我们去检查某个类是否有某种方法

# class Company(object):
#     def __init__(self, employee_list):
#         self.employee = employee_list
#
#
#     def __len__(self):
#         return len(self.employee)
#
#
# com = Company(["bobby1", "bobby2"])
# print(hasattr(com, "__len__"))
#
# # 在某些情况下希望判定某个对象的类型
# from collections.abc import Sized
# print(isinstance(com, Sized))
# # print(len(com))
#
# # 我们需要强制某个子类需要实现某些方法
# # 实现一个web框架,集成cache(redi, cach, memorycache)
# # 需要设计一个抽象基类,指定子类必须实现某些方法
#
# # 如何去模拟一个抽象基类
# # ImoocWeb
#
# import abc #全局下的abc与Collection.abc
# class CacheBase(metaclass=abc.ABCMeta):
#
#     @abc.abstractmethod
#     def get(self, key):
#         pass
#     @abc.abstractmethod
#     def set(self, key, value):
#         pass
# # 通过抛异常实现抽象基类,模拟抽象基类的方法
# #
# # class RedisCache(CacheBase):
# #     pass
# #
# # redis_cache = RedisCache()
# # redis_cache.set("key", "value")
# class RedisCache(CacheBase):
#     def set(self, key, value):
#         pass
#     def get(self, key):
#         pass
# redis_cache = RedisCache()
#
# # 抽象基类强制子类实现某些方法
#
# from collections.abc import *

class A:
    pass

class B(A):
    pass

b = B()
print(isinstance(b, A))

# 并不推荐使用抽象基类,可以通过另外的方式实现
# 主要是为了理解python中接口,使用时尽量使用鸭子类型