# -*- coding:utf8 -*-
# Power by zuosc 2016-10-01
#generator 生成器 (一边循环一边计算的机制，称为生成器：generator)

g = (x * x for x in range(10))
for n in g:
    print(n)
print('---------------')


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(10)

print('--------------------------------------------')


def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 19:
        break
