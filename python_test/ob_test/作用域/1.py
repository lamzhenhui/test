a = 22
b = 33


def func():
    a =1
    b=2
    print(locals())


if __name__ == '__main__':
    func()
    print(locals())
    print(globals())
    print(dir(__builtins__))
