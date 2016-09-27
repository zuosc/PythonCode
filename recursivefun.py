# -*- coding:utf8 -*-
# Power by zuosc 2016-09-27
# 递归函数

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

fact(7)