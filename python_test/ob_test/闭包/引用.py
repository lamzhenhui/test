def test1():
    print("--- in test1 func----")
#调用函数
#test1()
#引用函数 
ret = test1
print(id(ret))
print(id(test1))