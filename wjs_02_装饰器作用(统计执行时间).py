import time


def set_func(func):
    def call_func():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("执行所花费时间：%f" % (stop_time - start_time))
    return call_func


@set_func  # 等价于test1 = set_func(test1)
def test1():
    print("-----这是test1-----")
    for i in range(100000000):
        pass


test1()
