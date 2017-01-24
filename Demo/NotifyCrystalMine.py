# -*- coding:utf-8 -*-
# !/usr/bin/env python3
# Power by zuosc


import urllib.parse
import urllib.request


sendurl='http://sc.ftqq.com/SCU5209T50ff781c69372d9b370387f5c079be01587ae52428055.send?'
params = {'text':"水晶矿场",'desp':"快去收钱!!!"}
params = urllib.parse.urlencode(params)
urllib.request.urlopen(sendurl+params)