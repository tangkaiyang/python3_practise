# python和java中的变量本质不一样,python的变量实质上是一个指针 int str, 便利贴

a = 1
a = 'abc'
# 1.内存中声明内存空间给1,然后a贴在1上
# 2.先生成对象,然后贴便利贴
a = [1, 2, 3]
b = a
print(id(a), id(b))
print(a is b)
# b.append(4)
# print(a)


a = [1, 2, 3, 4]
b = [1, 2, 3, 4] # 重新生成

class People:
    pass

person = People()
if type(person) is People: # 使用type..is或isinstance,而不用==
    print("a")
print(a == b) # 相等,与__eq__相关
# a = 1
# b = 1 # 此时id(a), id(b)相等
# 小整数如1,不会重新生成,小字符串也是如此,list不会
print(id(a), id(b))
print(a is b)