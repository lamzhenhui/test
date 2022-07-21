import copy

if __name__ == '__main__':
    a ={1,2}

    a.add(3)
    print(id(a))
    print(a)

    b={1,2}
    print(id(a) ==id(b))

    # 深浅拷贝的区别
    # inner_lst = [7] # 嵌套结构是可变数据类型
    # inner_lst = {7} # 嵌套结构是可变数据类型
    inner_lst = {7:1} # 嵌套结构是可变数据类型

    # inner_lst = 7 # 不可变数据类型
    # inner_lst = (8)
    # inner_lst = "a"
    # inner_lst = 1.1

    c = [inner_lst,6]
    c_dc = copy.deepcopy(c)
    c_ndc = copy.copy(c)
    print(id(c[0]),id(c[1]))
    print(id(c_ndc[0]),id(c_ndc[1]))
    print(id(c_dc[0]),id(c_dc[1]))
