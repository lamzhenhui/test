# -*- coding:utf-8 -*-
import os.path
import sys


def func():
    i = list()
    with open("/Users/meta/lam/test/python_test/ob_test/lable.txt", "r") as f:
        while f.readlines(6000):
            print(len(f.readlines(6000)))
            yield f.readlines(6000)


def writer_func():
    fa = open('/Users/meta/lam/test/python_test/ob_test/lable.txt')
    with open('/Users/meta/lam/test/python_test/ob_test/lable.txt', "a") as f:
        for item in range(10000000):
            f.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
            f.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
            f.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
            f.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
            f.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
            f.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
    print(sys.getsizeof("/Users/meta/lam/test/python_test/ob_test/lable.txt"))
    print(os.path.getsize("/Users/meta/lam/test/python_test/ob_test/lable.txt"))


if __name__ == '__main__':
    print(next(func()))
    print(next(func()))
    print(next(func()))
    print(next(func()))
    print(next(func()))

    # writer_func()
