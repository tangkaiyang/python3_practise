def get_url(url):
    # do somethings 1
    html = get_html(url)  # 此处暂停,切换到另一个函数去执行
    # parse html
    # urls = parse_url(html)


def get_url2():
    pass

# 传统函数调用 过程 A->B->C函数运行一次便退出
# 我们需要一个暂停的函数,并且可以在适当的时候恢复该函数继续执行
# 出现了协程 --> 有多个入口的函数, 可以暂停的函数(生成器),可以向暂停的地方传入值
