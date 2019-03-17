# import os
# import time
# fork新建一个子进程,拷贝父进程的所有数据和代码运行
# fork只能用于linux/unix中
# 进程的数据隔离,有各自完整的数据
# pid = os.fork()
# print("bobby")
# if pid == 0:
#     print('子进程{}, 父进程是: {}.'.format(os.getpid(), os.getppid()))
# else:
#     print('我是父进程: {}.'.format(pid))
# time.sleep(2)# 去掉sleep,父进程运行完直接退出,但子进程仍在运行,无法退出

from concurrent.futures import ProcessPoolExecutor  #与ThreadPollExecutor接口类似
import multiprocessing

# 多进程编程
import time
def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n

# class MyProgress(multiprocessing.Progress)
if __name__ == '__main__':
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    # print(progress.pid)
    # progress.start()
    # print(progress.pid)
    # progress.join()
    # print("main progress end")

    # 使用进程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, args=(3,))
    #
    # # 等待所有任务完成
    # pool.close() # 先关闭,不接受新任务
    # pool.join()
    # print(result.get())

    # imap
    # for result in pool.imap(get_html, [1, 5, 3]): # 按顺序
    #     print("{} sleep success".format(result))
    for result in pool.imap_unordered(get_html, [1, 5, 3]): # 先完成先打印
        print("{} sleep success".format(result))