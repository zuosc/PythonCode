# -*- coding:utf8 -*-
# Power by zuosc
# filter filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['a', 'bb', None, 'cccc'])))
