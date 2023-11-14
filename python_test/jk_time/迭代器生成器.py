
# 打印 str 也是可迭代对象
import psutil
import os
from collections.abc import Iterable


print(isinstance(11, Iterable))

# 2. 打印python程序的内存占用


def show_mem_used(mess=''):
    p = os.getpid()
    p_info = psutil.Process(p)
    info = p_info.memory_full_info()
    used_mem = info.uss/1024/1024

    print(used_mem, mess)


def test_lst():

    show_mem_used('初始化前')
    list_a = [item for item in range(10000)]
    show_mem_used('初始化迭代器前')
    iter_a = iter(list_a)
    show_mem_used('初始化迭代器后')
    show_mem_used('init after')
    sum(iter_a)
    show_mem_used('sum after')


def test_gen():

    show_mem_used('初始化前')
    gen_a = (item for item in range(10000))
    show_mem_used('init after')
    sum(gen_a)
    show_mem_used('sum after')

# 结论, 生成器只有在计算元素时候才加载到内存中


test_lst()
test_gen()

# 3. 案例
# 1. 简化编码过程，提高代码可读性,
# 2.生成器可以用于实现协程，允许异步编程

print('# 3. 案例')


def general_item(limit):
    for item in range(2, limit+1, 2):
        yield item


for item in general_item(100):
    print(item)
