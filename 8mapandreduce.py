# -*- coding:utf8 -*-
# Power by zuosc 2016-10-12
#map和reduce


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7])

print(list(r))

print('---------------------------------')

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

print('----------------------------------')


def add(x, y):
    return x + y


from functools import reduce

r = reduce(add, [1, 2, 1, 2, 2])
print(r)

print('----------------------------')


def fn(x, y):
    return x * 10 + y


r = reduce(fn, [1, 2, 3, 9])
print(r)
