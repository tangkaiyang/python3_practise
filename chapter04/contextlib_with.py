import contextlib


@contextlib.contextmanager  # 修饰的必须是一个生成器
def file_open(filename):
    print("file open")  # __enter__要做的在yield之前实现
    yield {}  # yield必要
    print("file end")  # __exit__要做的在yield后实现


with file_open("bobby.txt") as f_opened:
    print("file processing")
