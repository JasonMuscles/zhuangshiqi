def set_func(func):
    def call_func(a):
        print("-----这是1-----")
        print("-----这是2-----")
        func(a)
    return call_func


@set_func  # 等价于test1 = set_func(test1)
def test1(num):
    print("-----这是test1-----%d" % num)


test1(100)
test1(200)
