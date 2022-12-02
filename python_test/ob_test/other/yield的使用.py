# coding=utf8
def yield_test(n):
    int_num = 0
    while  int_num <=n:
        print("_"*20)
        print("函数体内")
        print("yield 传递的值 %d" % n)
        yield n
        
        print("表示回到生成器函数，完成函数内的")
        print("_end"* 20 )
        int_num+=1
num= 0
for item in yield_test(3):
    print("-one"*20)
    raise Exception
    print("生成器函数外 i= %d" % item)

    print("yield 传递的值 做平方处理%d" % item**2)
    print("-"* 20)

print(1)
print(1)
