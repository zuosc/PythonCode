#!/usr/bin/env python3
# _*_ coding:utf8 _*_

'annotation: use pillow module'

__author__ = 'zuosc'

from PIL import Image

im = image.open('other.png')
print(im.format, im.size, im.mode)
