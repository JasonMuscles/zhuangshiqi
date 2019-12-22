def add_qx(func):
    print("----开始进行装饰权限1的功能----")

    def call_func(*args, **kwargs):
        print("-----权限验证1-----")
        return func(*args, **kwargs)

    return call_func


def add_xx(func):
    print("----开始进行装饰xxx的功能----")

    def call_func(*args, **kwargs):
        print("-----xxx1-----")
        return func(*args, **kwargs)

    return call_func


@add_qx
@add_xx
def test1():
    print("-----这是test1-----")


test1()

