class A:
    pass
class B(A):
    pass

b = B()

print(isinstance(b, B))
print(isinstance(b, A))

print(type(b) is B)
print(type(b) is A)

# is 与 == :is判断id是否相同,判断是否是同一对象
# == 判断值是否相等,尽量使用is做判断