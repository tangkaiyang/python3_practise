# 1.epoll并不代表一定比select好
# 在高并发的情况下,连接活跃度不是很高,epoll比select好
# 并发性不高,同时连接很活跃,select比epoll好

# 通过select完成HTTP请求
# select + 回调 + 事件循环
# 并发性高
# 使用单线程
import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()
urls = ["http://www.baidu.com"]
stop = False

class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = Tru

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"
        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            pass
        # 注册
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
    # 事件循环,不停的请求socket的状态并调用对应的回调函数
    # import select
    # select.select()
    # 1.select本身不支持register模式,
    # 2.socket状态变化后的回调由程序员完成的
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)
    # 回调+事件循环+select(poll/epo)


if __name__ == "__main__":
    fetcher = Fetcher()
    fetcher.get_url("http://www.baidu.com")
    loop()