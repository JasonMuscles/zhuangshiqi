def set_func(func):
    def call_func(*args, **kwargs):
        level = args[0]
        if level == 1:
            print("-----权限级别1的验证-----")
        elif level == 2:
            print("-----权限级别2的验证-----")
        return func()
    return call_func


@set_func
def test1():
    print("-----test1-----")
    return "ok"


@set_func
def test2():
    print("-----test2-----")
    return "ok"


test1(2)
test2(2)
