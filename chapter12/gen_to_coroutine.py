#生成器是可以暂停的函数
import inspect
import socket

# def gen_func():
#     value = yield 1
#     #第一返回值给调用方,第二调用方通过send方式返回值给gen
#     return "bobby"

# 1.用同步的方式编写异步的代码, 在适当的时候暂停函数,并在适当的时候启动函数
def get_socket_data():
    yield "bobby"

def downloader(url):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)

    try:
        client.connect((host, 80))
    except BlockingIOError as e:
        pass
    selector.register(...)
    source = yield from get_socket_data()

def download_html(html):
    html = yield from downloader()


if __name__ == '__main__':
    gen = gen_func()
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except StopIteration:
        pass
    print(inspect.getgeneratorstate(gen))
#协程的调度依然是事件循环+协程模式