# 事件循环+回调(驱动生成器)+epoll(IO多路复用)
# asyncio是python用于解决异步IO编程的一整套解决方案
# tornado,gevent,twisted(scrapy, django channels)
# torando(实现了web服务器) django+flask(uwsgi, gunicorn+nginx)
# torando可以直接部署, nginx+torando
# torando下无法使用pymysql等库的同步阻塞操作

# 使用asyncio
import asyncio
import time
from functools import partial

# async def get_html(url):
#     print("start get %s" % url)
#     # time.sleep() 同步阻塞的IO不能使用,不会报错,并发模式下,顺序执行
#     await asyncio.sleep(2) # 耗时操作加await,而且必须是Awaitable对象
#     print("end get %s" % url)
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     tasks = [get_html("http://www.immoc.com") for i in range(10)]
#     # loop.run_until_complete(get_html("http://www.immoc.com"))
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(time.time() - start_time)

# 获取协程的返回值
# async def get_html(url):
#     print("start get %s" % url)
#     await asyncio.sleep(2)
#     return "bobby"
#
#
# def callback(url, future):
#     print("send email to bobby")
#     print(url)
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     get_future = asyncio.ensure_future(get_html("http://www.immoc.com"))  # 自动获取loop
#     # loop.create_task() # 与上面的相似,Future类型的子类
#     get_future.add_done_callback(partial(callback, "http://www.immoc.com"))
#     loop.run_until_complete(get_future)
#     print(get_future.result())


# wait 和 gather
async def get_html(url):
    print("start get %s" % url)
    await asyncio.sleep(2)
    print("end get %s" % url)

if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # tasks = [get_html("http://www.immoc.com") for i in range(10)]
    # loop.run_until_complete(asyncio.gather(*tasks))
    # print(time.time() - start_time)

    #gather 和wait的区别:
    #gather更加高层high-level,可完成分组
    group1 = [get_html("http://projectsedu.com") for i in range(10)]
    group2 = [get_html("http://www.immoc.com") for i in range(10)]
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    group2.cancel()

    loop.run_until_complete(asyncio.gather(group1, group2))
    print(time.time() - start_time)