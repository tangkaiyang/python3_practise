import bisect
from collections import deque


# 用来处理已排序的序列类型,用来维持已排序的序列,升序
# 二分查找, 性能高
# inter_list = []
inter_list = deque()
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 6)

# print(bisect.bisect(inter_list, 3)) # 重复元素之后,默认bisect_right
print(bisect.bisect_left(inter_list, 3))  # 重复元素之前
# 区别1和1.0时确定其优先级
# 学习成绩
# 90-100 A
# 80-90 B
# ['ABCDE']
print(inter_list) # 得到一个已排序序列
