# -*- coding:utf-8 -*-
# /usr/bin/env python3
# Power by zuosc


import json
import gzip
import urllib.parse
import urllib.request


weatherApiAdder = 'http://wthrcdn.etouch.cn/weather_mini?'
suzhouKey ='101190401'
params = urllib.parse.urlencode({'citykey': suzhouKey})
result = urllib.request.urlopen(weatherApiAdder+ params).read()
jsonData = gzip.decompress(result).decode('utf8')
print(jsonData)

data = json.loads(jsonData)

title = '今日天气'
content = '当前温度：'+data["data"]["wendu"]+'\r\n'

sendurl='http://sc.ftqq.com/SCU5209T50ff781c69372d9b370387f5c079be01587ae52428055.send?'
params = {'text':title,'desp':content}
params = urllib.parse.urlencode(params)
urllib.request.urlopen(sendurl+params)

