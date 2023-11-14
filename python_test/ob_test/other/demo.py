import functools



class decorater(object):
    def __init__(self,func) -> None:
        self.func = func

    def __call__(self, *args: str, **kwds: str):
        print("warper")
        self.func(*args)
        



@decorater
def func1(a, b):
    print(a, b)


if __name__ == "__main__":
    a = "hello"
    b = "world"
    decorater(func1(a, b))
    # print(func1.__name__)
    # print(help(func1))


 