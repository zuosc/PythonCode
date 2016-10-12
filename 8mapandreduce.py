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
print('---------------------------')


def fn(x, y):
    return x * 10 + y


def char3num(s):
    return {'0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9}[s]


r = reduce(fn, map(char3num, '44885'))

print(r)

#################################################################


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0,
                '1': 1,
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9}[s]

#使用lambda
#return reduce(lambda x, y: x * 10 + y, map(char2num, s))

    return reduce(fn, map(char2num, s))

print(str2int('123123123123'))


def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
