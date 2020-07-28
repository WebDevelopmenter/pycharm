from timeit import Timer


def t1():
    l = []
    for i in range(1000):
        l = l + [i]


def t2():
    l = []
    for i in range(1000):
        l.append(i)


def t3():
    l = [i for i in range(1000)]


def t4():
    l = list(range(1000))


print("+ 操作耗时：", Timer('t1()', 'from __main__ import t1').timeit(1000))
print("append操作耗时：", Timer('t2()', 'from __main__ import t2').timeit(1000))
print("列表生成式耗时：", Timer('t3()', 'from __main__ import t3').timeit(1000))
print("使用list方法：", Timer('t4()', 'from __main__ import t4').timeit(1000))

"""
通过对程序的执行时间的分析得知：+ 操作是耗时最长的，因为他是将两个列表合并再生成一个新的列表，操作复杂度是 n + k, n和k分别代表列表的长度
+ 操作耗时： 3.7755566
append操作耗时： 0.5499915999999998
列表生成式耗时： 0.3504106999999994
使用list方法： 0.1896830000000005
"""

"""
这是新增加的注释
"""