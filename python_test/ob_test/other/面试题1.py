# encoding=utf8
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("decorator1 start")
        func(*args, **kwargs)
        print('decorator1 end')
    return wrapper


def decorator2(func):
    def wrapper(*args, **kwargs):
        print('decorator2 start')
        func(*args, **kwargs)
        print('decorator2 end')
    return wrapper


@decorator1
@decorator2
def function():
    print("do function")


function()
raise Exception
"""
***题1
decorator1 start
decorator2 start
do function
decorator2 end
decorator1 end
 """

# range(0,20)[2:-2]执行结果
"""
补充知识： 什么事迭代器， 生成器， 迭代器，range属于那种类型"""

"""
#题目 
a = list(range(2))

def test(_list=[], add_list= []):
    _list.extend(add_list)
    return _list

r1 = test(a)
print(id(r1))
r2 = test(a, r1)
print(id(r2))
r3 = test(a, r2)
print(id(r3))
print(r1)
print(r2)
print(r3)
"""

# """
# 题目写下输出内容


def test1():
    print('A')
    yield 'B'
    print('C')
    yield 'D'
    print('E')
    yield 'F'


if __name__ == "__main__":
    t = test1()
    print('----1')
    print(next(t))
    print('----')
    print(next(t))
    print('----2')
    print(next(t))
# """


# """
class MyFavoriteFood:
    _instance = None
    _first_init = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        if not self._first_init:
            self.name = name
            print(f"我最喜欢吃的是{self.name}")
            self._first_init = True
        else:
            print(f"{name}不是我最喜炊吃的")

    def show_my_favorite(self):
        print(f"{self.name}是我最喜欢吃的")


if __name__ == "__main__":
    chocolate = MyFavoriteFood("巧克力")
    chocolate.show_my_favorite()
    cake = MyFavoriteFood("蛋糕")
    cake.show_my_favorite()
    print(id(cake) == id(chocolate))
# """
