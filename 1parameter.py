# -*- coding:utf8 -*-
# Power by zuosc 2016-09-27
# 函数参数的例子


def person(name, age, *, city, job):  # 关键字参数
    print(name, age, city, job)


person('Jack', 24, city='beijing', job='Engineer')


# *args是可变参数，args接收的是一个tuple
# **kw是关键字参数，kw接收的是一个dict
def f1(a, b, c=0, *args, **kw):
    print('a = ', a, 'b = ', b, 'c = ', c, 'args = ', args, 'kw = ', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a = ', a, 'b = ', b, 'c = ', c, 'd = ', d, 'kw = ', kw)


f1(1, 2)
print('----------------------------------------------')
f1(1, 2, c=0)
print('----------------------------------------------')
f1(1, 2, 3, 'a', 'b')
print('----------------------------------------------')
f1(1, 2, 3, 'a', 'b', x=99)
print('----------------------------------------------')
f2(1, 2, d=99, ext=None)
print('----------------------------------------------')
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
print('----------------------------------------------')

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

print('----------------------------------------------')

print('对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。')
