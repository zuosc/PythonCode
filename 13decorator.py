# _*_ coding:utf8 _*_
# Power by zuosc 2016-10-13
# Decorator 装饰器

import functools


def log(func):
    @functools.wraps(func)  # 解决依赖函数签名的代码，因为这里返回的函数名已经变为wrapper了，不是now了
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log  # 相当于 now = log(now)
def now():
    print('2016-10-17')


print(now())

print('----------------------')

# 带参数的

import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)  # 解决依赖函数签名的代码，因为这里返回的函数名已经变为wrapper了，不是now了
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('记录日志,调试程序:')  # 相当于 now = log('execute')(now)
def now():
    print('2016-10-17')


print(now())
