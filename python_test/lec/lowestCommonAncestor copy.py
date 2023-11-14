class MyQueue:

    def __init__(self):
        self.in_stk, self.out_stk = list(), list()

    def push(self, x):
        self.in_stk.append(x)

    def pop(self):
        ret = None
        self.intout()
        if self.in_stk:
            ret = self.in_stk.pop()
        while self.out_stk:
            self.in_stk.append(self.out_stk.pop())

        return ret

    def peek(self):
        ret = None
        self.intout()
        if self.in_stk:
            ret = self.in_stk[0]
        while self.out_stk:
            self.in_stk.append(self.out_stk.pop())

        return ret

    def empty(self):
        return not self.in_stk and not self.out_stk

    def intout(self):
        while len(self.in_stk) > 1:
            self.out_stk.append(self.in_stk.pop())


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(2)
obj.push(1)
param_2 = obj.pop()
print(param_2)
param_3 = obj.peek()
print(param_3)
param_4 = obj.empty()
print(param_4)
# if __name__ == "__main__":
#     s = MyQueue()
