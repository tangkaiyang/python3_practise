# array,deque
# 数组,连续的内存空间,性能很高
import array
# array和list的一个重要区别,array只能存放指定的数据类型
# a = list
my_array = array.array("i")
# my_array = array.ArrayType
my_array.append(1)
my_array.append("abc") # 报错,只接受int类型
