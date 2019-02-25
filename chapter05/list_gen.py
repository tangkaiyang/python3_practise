# 列表生成式(列表推导式)
# 1.提取出1-20之间的奇数
# odd_list =[]
# for i in range(21):
#     if i % 2 == 1:
#         odd_list.append(i)
odd_list = [i for i in range(21) if i % 2 == 1]


# 2.逻辑复杂的情况
def hadle_item(item):
    return item * item


odd_list = [hadle_item(i) for i in range(21) if i % 2 == 1]

# 列表生成式性能高于列表操作

print(type(odd_list))
print(odd_list)

# 生成器表达式

# odd_list = (i for i in range(21) if i % 2 == 1) # 生成器而不是元组
# print(type(odd_list))
# print(odd_list)
# for item in odd_list:
#     print(item)
odd_gen = (i for i in range(21) if i % 2 == 1) # 生成器而不是元组
odd_list = list(odd_gen)
print(odd_list)

# 字典推导式
my_dict = {"bobby1": 22, "bobby2": 23, "imooc.com": 5}
reversed_dict = {value:key for key, value in my_dict.items()}
print(reversed_dict)

# 集合推导式 set
# my_dict = set(my_dict.keys()) # 取巧的方法,灵活性不够高
my_set = {key for key, value in my_dict.items()}
print(type(my_set))
print(my_set)