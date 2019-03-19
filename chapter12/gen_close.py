def gen_func():
    try:
        yield "http://projectsedu.com"
    except Exception:
        pass
    yield 2
    yield 3
    return "bobby"


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.close()
    # next(gen)
    print("bobby")

    # GeneratorExit是继承BaseException, < Exception