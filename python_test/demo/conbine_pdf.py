# encoding=utf8
import PyPDF2

# 创建一个 PDFWriter 对象来存储合并后的 PDF
pdf_writer = PyPDF2.PdfWriter()

bos = """00丨开篇词丨从工程的角度深入理解Python.pdf 
01丨如何逐步突破，成为Python高手？.pdf 
02丨Jupyter Notebook为什么是现代Python的必学技术？.pdf 
03丨列表和元组，到底用哪一个？.pdf 
04丨字典、集合，你真的了解吗？.pdf 
05丨深入浅出字符串.pdf 
06丨Python “黑箱”：输入与输出.pdf 
07丨修炼基本功：条件与循环.pdf 
08丨异常处理：如何提高程序的稳定性？.pdf 
09丨不可或缺的自定义函数.pdf 
10丨简约不简单的匿名函数.pdf 
11丨面向对象（上）：从生活中的类比说起.pdf 
12丨面向对象（下）：如何实现一个搜索引擎？.pdf 
13丨搭建积木：Python 模块化.pdf 
14丨答疑（一）：列表和元组的内部实现是怎样的？.pdf 
15丨Python对象的比较、拷贝.pdf 
16丨值传递，引用传递or其他，Python里参数是如何传递的.pdf 
17丨强大的装饰器.pdf 
18丨[名师分享] metaclass，是潘多拉魔盒还是阿拉丁神灯？.pdf 
19丨深入理解迭代器和生成器.pdf 
20丨揭秘 Python 协程.pdf 
21丨Python并发编程之Futures.pdf 
22丨并发编程之Asyncio.pdf 
23丨你真的懂Python GIL（全局解释器锁）吗？.pdf 
24丨带你解析 Python 垃圾回收机制.pdf 
25丨答疑（二）：GIL与多线程是什么关系呢？.pdf 
26丨[名师分享] 活都来不及干了，还有空注意代码风格？！.pdf 
27丨学会合理分解代码，提高代码可读性.pdf 
28丨如何合理利用assert？.pdf 
29丨巧用上下文管理器和With语句精简代码.pdf 
30丨真的有必要写单元测试吗？.pdf 
31丨pdb&cProfile：调试和性能分析的法宝.pdf 
32丨答疑（三）：如何选择合适的异常处理方式？.pdf 
33丨带你初探量化世界.pdf 
34丨RESTful&Socket搭建交易执行层核心.pdf 
35丨RESTful&Socket行情数据对接和抓取.pdf 
36 丨 Pandas & Numpy 策略与回测系统.pdf 
37 丨 Kafka & ZMQ：自动化交易流水线.pdf 
38 丨 MySQL：日志和数据存储系统.pdf 
39丨Django：搭建监控平台.pdf 
40丨总结：Python中的数据结构与算法全景.pdf 
41丨硅谷一线互联网公司的工作体验.pdf 
42丨细数技术研发的注意事项.pdf 
43丨Q&A：聊一聊职业发展和选择.pdf 
加餐丨带你上手SWIG：一份清晰好用的SWIG编程实践指南.pdf 
结束语丨技术之外的几点成长建议."""
print(bos.split('pdf \n'))
new_bos = [item for item in bos.split('pdf \n') if item]

print(new_bos)
# raise Exception

# 文件名和书签名的映射关系
file_to_bookmark = {"demo/jk/%spdf" %
                    item1: item1.replace('.', "") for item1 in new_bos}
print(file_to_bookmark)
# raise Exception
# file_to_bookmark = {
#     "demo/jk/00丨开篇词丨从工程的角度深入理解Python.pdf": "00丨开篇词丨从工程的角度深入理解Python.pdf",
#     "demo/jk/01丨如何逐步突破，成为Python高手？.pdf": "01丨如何逐步突破，成为Python高手？.pdf"


# }


# 逐个添加 PDF 文件和书签
for filename, bookmark_name in file_to_bookmark.items():
    # 打开 PDF 文件
    pdf_file = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # 创建一个新的页面对象，用于添加书签
    # page = pdf_writer.add_page(pdf_reader.getPage(0))
    # page = pdf_writer.add_page(pdf_reader.pages[0])
    # page = pdf_writer.add_page(pdf_reader.pages[99])
    # print(len(pdf_reader.pages))

    for item in range(len(pdf_reader.pages)):
        print(item)
        page = pdf_writer.add_page(pdf_reader.pages[item])
        # 创建书签对象
        pdf_writer.add_outline_item(bookmark_name, page)

# 生成合并后的 PDF 文件
with open("merged.pdf", "wb") as output_pdf:
    pdf_writer.write(output_pdf)

# 关闭所有打开的 PDF 文件
# for pdf_file in file_to_bookmark:
output_pdf.close()
