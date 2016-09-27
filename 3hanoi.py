# -*- coding:utf8 -*-
# Power by zuosc 2016-09-27
# 汉诺塔

def move(S, E):
    print(S + '-------->' + E)

def hanoi(n, src, tmp, dst):
    if n == 1:
        move(src, dst)
    else:
        hanoi(n - 1, src, dst, tmp)
        move(src, dst)
        hanoi(n - 1, tmp, src, dst)

hanoi(5, 'A', 'B', 'C')
