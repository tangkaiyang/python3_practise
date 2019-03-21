import asyncio


def callback(sleep_times, loop):
    # print("sleep {} success".format(sleep_times))
    print("success time {}".format(loop.time())) # 内部时钟时间


def stoploop(loop):
    loop.stop()

# call_later, call_at,
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.call_soon(callback, 2)
    now = loop.time()
    loop.call_at(now + 2, callback, 2, loop)
    loop.call_at(now + 1, callback, 1, loop)
    loop.call_at(now + 3, callback, 3, loop)
    # loop.call_later(3, callback, 3)
    # loop.call_later(1, callback, 1)
    # loop.call_soon(stoploop, loop)
    loop.call_soon(callback, 4, loop)
    loop.run_forever()