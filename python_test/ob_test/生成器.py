
if __name__ == '__main__':
    import sys
    a = [item for item in range(10000)]
    b= (item for item in range(10000))
    print(type(b))
    print(sys.getsizeof(a))
    print(sys.getsizeof(b))
