def set_func(func):
    def call_func():
        print("-----这是1-----")
        print("-----这是2-----")
        func()
    return call_func()


@set_func  # 等价于test1 = set_func(test1)
def test1():
    print("-----这是test1-----")


test1()
