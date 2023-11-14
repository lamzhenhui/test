"""1. python 里面妍何现tuple 和list 的转换？
首先都是容器类型， tuple的里边存放的是不可变的元素， list则是可变的元素
所以tuple》list： 回将tuple中的元素进行浅拷贝，然后将元素放入新创建的列表中
所以tuple《list： 回将list中的元素进行深拷贝，然后将元素放入新创建的tuple中
tuple()
list() 方法便可实现类型的强制转换
"""


""". 请写出一段Python 代码实现删除一个list 里面的重复元素
list(set(list([1,2,1])))

"""

"""Python 中pass 语句的作用是什么？
用作跳过后续的执行步骤，无参数返回
"""


"""简述Python 中单引号，双引号，三引号的区别
单，双引号同样为表示字符串类型的数据类型， 而3引号多用作表示多行注释
"""

"""
以下的代码的输出将是什么？说出你的答案并解释。

"""




import time
class Parent(object):
    x = 1


class Child1 (Parent):
    pass


class Child2(Parent):
    pass


print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)
while True:
    with open("/Users/meta/lam/test/python_test/ob_test/other/writer_demo", "a") as f:
        f.write("11111\n")
    time.sleep(5)
