# 1.python中函数的工作原理
"""

"""
import inspect
frame = None

def foo():
    bar()
def bar():
    global frame
    frame = inspect.currentframe()

# python.exe(解释器,C语言)会用一个叫做PyEval_EvalFramEx(c函数)去执行foo函数,首先会创建一个栈帧(stack frame)
"""
python中一切皆对象,栈帧对象, 代码变为字节码对象,
当foo调用子函数bar,又会创建一个栈帧,转交函数控制权
所有栈帧都是分配在堆内存上,这就决定了栈帧可以独立于调用者存在
堆内存不释放就会一直存在内存中
"""
# import dis
# print(dis.dis(foo))

foo()
print(frame.f_code.co_name)
caller_frame = frame.f_back
print(caller_frame.f_code.co_name)


def gen_func():
    yield 1
    name = "bobby"
    yield 2
    age = 30
    return "imooc"
import dis
gen = gen_func()
print(dis.dis(gen))

print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)


a = [1, 2, 3]
for i in a:
    print(i)
class company:
    def __getitem__(self, item):
        pass
    def __iter__(self):
        pass
for i in company:
    print(i)

from collections import UserList # 可覆盖任何函数,继承此类,而不是list(基于c语言)