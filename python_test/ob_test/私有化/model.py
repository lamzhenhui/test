

class C1:
    __fun2 = 1
    def _fun(self):
        print(11)
    def __fun(self):
        print(11)

    def fun(self):
        print(22)

class C2(C1):
    def pr(self):

        # C1().__fun()
        pass  #
    def pr2(self):
        self.__fun2=2
        print(dir(C2))
        print(self.__fun2)


if __name__ == '__main__':
    C2().pr2()
    print(dir(C1))