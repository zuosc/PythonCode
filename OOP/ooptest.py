# !/usr/bin/env python3
# _*_ coding:utf8 _*_

'oop demo'

__author__ = 'zuosc'


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


bart = Student('Bart', 59)
lisa = Student('Lisa', 87)

bart.print_score()
