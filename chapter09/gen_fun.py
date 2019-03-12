# 生成器函数,函数里只要有yield关键字

def gen_func():
    yield 1
    yield 2
    yield 3

def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index-1) + fib(index-2)
def fib2(index):
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a+b
        n += 1
    return re_list
def gen_fib(index):
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a+b
        n += 1
for data in gen_fib(10):
    print(data)
print(fib2(10))
# 斐波那契0 1 1 2 3 5 8....
# 惰性求值,延迟求值提供了可能
def func():
    return 1


if __name__ == '__main__':
    gen = gen_func()  # 生成器对象, python编译字节码的时候就产生了
    for value in gen:
        print(value)
    # re = func()
    # pass