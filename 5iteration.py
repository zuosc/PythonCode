# -*- coding:utf8 -*-
# Power by zuosc 2016-10-01
# 数据迭代

d = {'a': 1, 'b': 2, 'c': 3}  #d是字典 无序的
for key in d:
    print(key)

print('---------------------------')
for value in d.values():
    print(value)

print('----------------------------')

for item in d.items():
    print(item)

print('*********************')
for ch in 'ABC':
    print(ch)

print('--------------------------------------')

from collections import Iterable

print(isinstance('abc', Iterable))
print(isinstance('[1,2,3,4]', Iterable))
print(isinstance(212312313, Iterable))

print('-----------------\r\n')
for i, value in enumerate(['A', 'B', 'C']):
    print(i + 1, value)
print('-----------------\r\n')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
