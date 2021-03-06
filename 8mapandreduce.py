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

# 练习 (3)
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456


# 函数定义
def str2float(s):
    # 通过 ‘.’ 分割数字字符串，赋值对应的 ‘.’ 左右字符串变量
    l_s_int, r_s_float = s.split('.')
    # 字符串 ‘.’ 右侧长度
    r_s_len = len(r_s_float)

    # 字符转数字函数
    def char2int(s):
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

# 左侧-整数字符串转换

    l_transfer = reduce(lambda x, y: x * 10 + y, map(char2int, l_s_int))
    # 右侧-整数字符串转换
    r_transfer = reduce(lambda x, y: x * 10 + y, map(char2int, r_s_float))

    # 注意：
    # (1)、r_transfer / 10 ** r_s_len:    expression python2 return 0
    # (1)、r_transfer / 10 ** r_s_len:    expression python3 return 0.456
    return l_transfer + r_transfer / 10**r_s_len

print(str2float('123.456'))
print(type(str2float('123.456')))


def str2float(s):
    l_int, r_int = s.split('.')

    r_len = len(r_int)

    # 字符转数字函数
    def char2int(s):
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

    l_tr = reduce(lambda x, y: x * 10 + y, map(char2int, l_int))

    r_tr = reduce(lambda x, y: x * 10 + y, map(char2int, r_int))

    return l_tr + r_tr / 10**r_len


print(str2float('1454654.1524814'))
