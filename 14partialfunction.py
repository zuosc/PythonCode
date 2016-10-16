# _*_ coding:utf8 _*_
# Power by zuosc 2016-10-16
# Partial Function 偏函数

import functools
int2 = functools.partial(int, base=2)

print(int2('101001010101'))

