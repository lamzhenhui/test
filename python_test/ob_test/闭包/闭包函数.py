

def demo(start1):
    start = [start1]
    def inner():
        # nonlocal  start
        start[0] +=1
        return start
    return inner

if __name__ == '__main__':
    d = demo(5)
    print(d())
    print(d())