class A:  # 默认继承object
    aa = 1  # 类变量

    def __init__(self, x, y):  # self是类实例
        self.x = x  # x属于对象,不属于类
        self.y = y


a = A(2, 3)
A.aa = 11 # 修改类属性
a.aa = 100 # a.aa实际上把100赋值给实例a的aa属性(新建),A的aa类属性不变
print(a.x, a.y, a.aa)
print(A.aa)
b = A(3, 5)
print(b.aa)
# print(A.x) # 没有x属性

# 先找对象的变量,再向上查询类变量
