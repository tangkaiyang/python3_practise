def gen_func():
    # 1.可以产出值, 2.可以接受值(调用方传递进来的值)
    html = yield "http://projectsedu.com"
    print(html)
    yield 2
    yield 3
    return "bobby"

# 1.throw, close


if __name__ == '__main__':
    gen = gen_func()
    # url = next(gen)
    url = gen.send(None) # 第一次只能send一个None值
    # 在调用send发送非None值之前,我们必须启动一次生成器,方式有两种1.gen.send(None), 2.next(gen)
    #download url
    html = "bobby"
    print(gen.send(html))  # send方法可以传递值进入生成器内部,同时还可以重启生成器执行到下一个yield
    #1.启动生成器方式有两种,next(),send()
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))

# 1.生成器不只可以产出值,还可以接收值