# set集合 fronzenset(不可变集合) 无序,不重复
s = set('abcdee')
# s = set(["a", "b", 'c', 'd', 'e'])
s = {'a', 'b'}
s.add('c')
# print(type(s))
print(s)

# s = frozenset("abcde") # 无法add
# # frozenset 可以作为dict的key(恒定)
# print(s)

# 向set添加数据
another_set = set("cef")
# s.add()
# s.update(another_set)
result_set = s.difference(another_set) # 集合差集
# difference 有返回值,而非改变s
# | & - 集合运算
result_set = s & another_set
result_set = s | another_set
print(s - another_set)
print(result_set)
print(s)

# set常用数据结构,性能很高,,实现原理与dict相同(哈希),时间复杂度为1
# 去重时非常有用

if "c" in result_set: # __contains__
    print("i am in set")

# issubset子集
print(s.issubset(result_set))
