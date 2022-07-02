if __name__ == '__main__':
    A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
    A1 = range(10)
    A2 = [i for i in A1 if i in A0]
    A3 = [A0[s] for s in A0]
    A4 = [i for i in A1 if i in A3]
    A5 = {i: i * i for i in A1}
    A6 = [[i, i * i] for i in A1]

    print(A0, "\n",A1, "\n",A2, "\n",A3,"\n", A4,"\n", A5,"\n", A6)
    """
    0 {'a':1,'b':1...}
    1 [0,1..10]
    2 []
    3 [1,2,3,4,5]
    4 [1,2,3,4,5]
    5 {0:0,1:1,2:4,3:9,...100}
    6 [[0,0],[1,1]...]
    """
