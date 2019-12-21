def set_func(func):
    def call_func(*args, **kwargs):
        print("-----这是1-----")
        print("-----这是2-----")
        # func(args, kwargs)  # 不行，相当于传递了2个参数：一个元组,一个字典
        func(*args, **kwargs)  # 拆包的作用
    return call_func


@set_func  # 等价于test1 = set_func(test1)
def test1(num, *args, **kwargs):
    print("-----这是test1-----%d" % num)
    print("-----这是test1-----", args)
    print("-----这是test1-----", kwargs)


test1(100)
test1(901, 902, 800, 700)
test1(100, 200, 300, mm=100)