my_list = []
my_list.append(1)
my_list.append("a")
# list可接受任意数据类型

from collections import abc

# collections容器相关的数据结构抽象基类都在其中
a = [1,2]
# a = list() 两种初始化方法
# c = a + [3, 4]
# print(c)
# c = a + (3, 4) # 报错
# += 就地加,对a进行操作,不产生新的列表
# a += [3, 4] +=接受任意的参数
# += 调用__iadd__魔法函数,__iadd__内部通过extend实现,
# extend通过for循环实现,只要iterable即可
# a += (3, 4)
# a.extend(range(3))
# a = a.extend(range(3)) # 该函数没有返回值
# a.append(([1,2])) # 数组变为值,而不是迭代,与extend区别

print(a)

