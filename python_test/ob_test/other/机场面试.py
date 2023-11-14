
import subprocess
import os
import pandas as pd
import numpy as np
import time


def helper(data=""):
    try:
        ret = data.split(" ")
    except:
        print("error")
    if len(ret) == 2:
        return ret
    elif len(ret) == 1:
        return [ret[0], ""]
    else:
        return ["", ""]


def helper2(data=""):
    if data in ["0", 0]:
        return "女"
    if data in ["1", 1]:
        return "男"


def split_name(data):
    ret = list()
    for item in data.values:
        data = list(item)

        new_item = [data[0], data[1], helper(
            data[0])[0], helper(data[0])[1]]
        ret.append(new_item)

    return pd.DataFrame(
        data=ret, columns=["User", "gender", "first_name", "last_name"])


def change_word(data):
    ret = list()
    for item in data.values:
        lst = list(item)

        new_item = [lst[0], helper2(lst[1]), helper(
            lst[0])[0], helper(lst[0])[1]]
        ret.append(new_item)

    return pd.DataFrame(
        data=ret, columns=["User", "gender", "first_name", "last_name"])


print("第一题:")
data = pd.DataFrame({'User': ['Verne Raymond', 'Chapman Becher', 'Patrick George', 'Saxon MacArthur',
                              'Joshua Marjory', 'Luther Pigou', 'Fanny Agnes', 'Karen Bush', 'Elaine Whitman'],
                     'gender': [0, 1, 0, 0, 1, 1, 1, 0, 1], 'first_name': np.nan, 'last_name': np.nan})
print("任务1", split_name(data))

print("任务2", change_word(data))


print("第2题:", """\n1
count(*) 包括了所有的列，相当于行数，在统计结果的时候，不会忽略列值为NULL
count(1) 包括了所有的列，相当于行数，在统计结果的时候，不会忽略列值为NULL,
count(列名) 只包括列名那一列，在统计结果的时候，会忽略列值为空。
count(*) 和count(1)的区别在于: 在myisam引擎中表现更优(可以直接返回表记录数,而不需要全表检索),如果再innodb引擎中的话, 性能相差不大, 这时候还需要考虑主键对检索的影响

2
存储过程是一组为了完成特定功能的SQL语句集，存储在数据库中，经过第一次编译后再次调用不需要再次编译，用户通过指定存储过程的名字并给出参数（如果有）来调用执行。
优点：
提高性能：存储过程只需编译一次，节约资源
减少网络流量：用户只需传递存储过程的名字和参数
增强安全性：用户可以通过授权访问存储过程，而不需要申请访问数据库表的权限
复用性和维护性：存储过程可以在多个应用程序中重复使用，修改时也只需在数据库中进行修改即可
缺点：
调试困难：存储过程不容易调试，出错时难以发现错误原因和错误位置。
移植性差：不同数据库系统对存储过程的支持和语法都有差异，移植时可能需要重写

3
超大分页问题指的是: 从数据库表中遍历所有满足条件的记录, 然后做排序取偏移量较大的少量记录,产生的查询效率问题.
1.利用索引,减少全表: 可以使用覆盖索引,减少数据表的记录的扫描个数;
2.如果无法避免全表扫描,利用子查询中使用条件过滤,减少回表查询的数据量;
3.如果表中有记录是有排序的,可以通过记录记录上次访问的位置.

""")

pid_file = "./app.pid"


def check_and_run():
    global pid_file
    if os.path.exists(pid_file):
        with open(pid_file) as f:
            pid = int(f.read())
        try:
            os.kill(pid, 0)
        except OSError:
            print("app.py is not running, restarting it...")
            run_app()
        else:
            print("app.py is running")
    else:
        print("app.py is not running, restarting it...")
        run_app()


def run_app():
    global pid_file
    p = subprocess.Popen(
        ["python", "/Users/meta/lam/test/python_test/ob_test/other/03 笔试题1.py"])
    with open(pid_file, "w") as f:
        f.write(str(p.pid))


# while True:
    # check_and_run()
    # time.sleep(5)

    # nohup python monitor.py &

print("", """
1、根据M/M/1排队论模型，如果每小时平均有4架飞机推出（λ=4），#https://blog.csdn.net/zyx_bx/article/details/115219706
跑道每小时平均可推出5架飞机（μ=5），
跑道的平均队长L=λ/(μ-λ)=4架飞机； 其中λ为单位时间前来的飞机数, μ为单位时间内系统能够承受的推出的飞机数

平均等待队长Lq=ρL=0.8×4=3.2架飞机, 其中ρ为服务强度ρ=λ/μ；
平均推出时间W为1/μ=0.2小时；
平均排队等待时间Wq=ρW=0.8×0.2=0.16小时。

 2、如果要求99%以上的飞机都不被拒绝进入排队序列，那么需要满足Pn<0.01，
 其中Pn表示有n架飞机在系统中的概率。根据M/M/1模型，
 Pn=(1-ρ)ρ^(n+1)=(1-0.8)×(0.8)^n。
 通过计算可得当n≥13时，Pn<0.01。因此队长N应设置为13或更大。 
 
 3、如果机场24小时不间断推出，并且假设每个时段都符合M/M/1模型，那么当飞机推出1小时时，
 系统中有L×24=96架飞机在等待或滑行。如果每架飞机损失30000元，则总损失为96×30000=2880000元。
 若提高推出效率至每小时6架（μ=6），则队长L降低为λ/(μ-λ)=2架飞机；总损失降低为48×30000=1440000元；
 每天可减少损失1440000元。

""")
