
def fib(n):
    a = 1
    b =2
    c = 0
    for item in range(3,n+1):
        if n in (1,2):
            yield c

        a = a
        b = b
        c = a+b

        #
        a = b
        b = c
    return c


if __name__ == '__main__':
    print(fib(5))

    lst = [1,2]
    print("__iter__" in dir(lst))
    print("__next__" in dir(fib(5)))


