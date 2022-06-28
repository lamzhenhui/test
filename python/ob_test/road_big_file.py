# -*- coding:utf-8 -*-
import os.path
import sys


def func():
    i = list()
    with open("lable.txt","r") as f:
        while f.readlines(6000):
            print(len(f.readlines(6000)))
            yield f.readlines(6000)

def writer_func():
    fa = open('lable.txt')
    with open('lable.txt',"a") as f:
        for item in range(10000000):
            f.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
            f.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
            f.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
            f.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
            f.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
            f.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
    print(sys.getsizeof("lable.txt"))
    print(os.path.getsize("lable.txt"))




if __name__ == '__main__':
    print(next(func()))
    print(next(func()))
    print(next(func()))
    print(next(func()))
    print(next(func()))

    # writer_func()
