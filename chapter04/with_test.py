# try except finally
def exe_try():
    try:
        # f_read = open("bobby.txt")
        print("code started")
        raise KeyError
        # raise IndexError:
        return 1
    except KeyError as e:
        print("key error")
        return 2
    else:
        print("other error")
        return 3
    finally:  # 前面的不管有没有运行都会运行finally
        print("finally")
        # return 4 # 注释掉则返回2
    # finally的意义,当我们必须要进行的操作如file.close()在抛出异常之后,这样就无法执行该操作,我们就需要在处理异常时进行该操作,
    # 当error类型较多时,我们需要编写的代码就较为麻烦,finally一般用于资源的释放


# 定义了一下两个魔法函数就满足上下文管理器协议就可以使用with方法
class Sample():
    def __enter__(self):
        # 获取资源
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print("exit")

    def do_something(self):
        print("do something")


# 如果finally中有return语句就会return finally中的,如果没有则return之前执行的return
# 上下文管理器
# python基于协议编程,
# 上下文管理器协议:涉及到的魔法函数__enter__和__exit__
# if __name__ == '__main__':
#     result = exe_try()
#     print(result)

with Sample()as sample:
    sample.do_something()
# 使用with是会自动调用上述两个魔法函数,
# 所以可以在__enter__内获取资源,在__exit__内释放资源
