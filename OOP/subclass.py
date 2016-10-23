# !/usr/bin/env python3
# _*_ coding:utf8 _*_
# Power by zuosc 2016-10-23

'subclass demo 继承和多态'


class Animal(object):
    def run(self):
        print('Animal is running......')


class Dog(Animal):
    def run(self):
        print('Dog is running.....')

    def eat(self):
        print('dog is eating......')


class Cat(Animal):
    pass


dog = Dog()
dog.run()