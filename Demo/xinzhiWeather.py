# -*- coding:utf-8 -*-
# /usr/bin/env python3
# Power by zuosc


import json
import urllib.parse
import urllib.request


weatherApiAdder = 'http://widget.thinkpage.cn/api/weather?flavor=slim&location=WX4FBXXFKE4F&geolocation=enabled&language=zh-chs&unit=c&theme=chameleon&container=weather-widget&bubble=enabled&alarmType=circle&uid=UE4B455F4F&hash=cfc949b4b932fff04040f9c9f776018b'
result = urllib.request.urlopen(weatherApiAdder).read()
jsonData = result.decode('utf8')
data = json.loads(jsonData)

title = '今日天气'
content ='今日天气:' + data["weather"]["now"]["text"] \
         + '\r\n当前温度：' + data["weather"]["now"]["temperature"] \
         + '℃\r\n天气报警：' + data["weather"]["alarms"][0]["type"] + data["weather"]["alarms"][0]["level"] + '预警'

sendurl='http://sc.ftqq.com/SCU5209T50ff781c69372d9b370387f5c079be01587ae52428055.send?'
params = {'text':title,'desp':content}
params = urllib.parse.urlencode(params)
urllib.request.urlopen(sendurl+params)