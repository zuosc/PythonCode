# -*- coding:utf8 -*-
# Power by zuosc 2016-10-01
# 列表生成器

l = list(range(1, 10))
print(l)

L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

LL = [x * x for x in range(1, 11)]
print(LL)

LLL = [x * x for x in range(1, 11) if x % 2 == 0]
print(LLL)

LLLL = [m + n for m in 'ABC' for n in 'XYZ']
print(LLLL)

import os
dirs = [d for d in os.listdir('C:')]
print(dirs)

d = {'a': 'X', 'b': 'Y', 'c': 'Z', 'd': 'D'}
for k, v in d.items():
    print(k + '=' + v)
    print(k, '=', v)

print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'APPLE', 'DJ']
print([s.lower() for s in L])

print('---------------')
L1 = ['HELLO', 'WORLD', 5, 'ZORRO', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
