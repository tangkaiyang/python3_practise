# 线程间通讯
import time
import threading

detail_url_list = []
def get_detail_html():
    global detail_url_list
    url = detail_url_list.pop()

    # for url in detail_url_list:
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")
    # 爬取文章详情页

def get_detail_url(url):
    global detail_url_list
    # 爬取文章列表页
    print("get detail url started")
    time.sleep(4)
    for i in range(20):
        detail_url_list.append("http://projectsedu.com/{id}".format(id=i))
    print("get detail url end")


# 线程间通讯方式
if __name__ == '__main__':
    thread_detail_url = threading.Thread(target=get_detail_url)
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html)
        html_thread.start()
    # thread_detail_url.start()
    # thread_detail_url1.start()
    # thread_detail_url2.start()

    # thread1 = threading.Thread(target=get_detail_html, args=("",))
    # thread2 = threading.Thread(target=get_detail_url, args=("",))
    # # thread1.setDaemon(True)
    # thread2.setDaemon(True)
    # start_time = time.time()
    # thread1.start()
    # thread2.start()
    #
    # thread1.join()
    # thread2.join()
    # # 当主线程退出的时候,子线程kill掉
    # print("last time: {}".format(time.time()-start_time))
