# !/usr/bin/env python3
# _*_ coding:utf8 _*_

'annotation: this is a test module'

__author__ = 'zuosc'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, World!')
    elif len(args) == 2:
        print('Hells, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()