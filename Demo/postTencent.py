#! /usr/bin/env python3
# _*_ coding:utf8 _*_

__author__='zuosc'


import urllib.request
import urllib.parse
import time
import ssl
import json

time1 = int(time.time())
date = time.strftime("%m.%d", time.localtime()) 

data = urllib.parse.urlencode({'survey_id': 923450, 'answer_survey': '{"id":"923450","survey_type":0,"jsonLoadTime":49,"ldw":"F3D636F9-7582-415F-A659-E5EE23CDDDAD","time":%d,"ua":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36","openid":"","pages":[{"id":"1","questions":[]},{"id":"p-2-VstM","questions":[{"id":"q-1-ZzWp","type":"text","text":"左思成","options":[],"blanks":[]},{"id":"q-2-Ibet","type":"text","text":"32137","options":[],"blanks":[]},{"id":"q-3-qtan","type":"text","text":"大度假自营包团研发组","options":[],"blanks":[]},{"id":"q-4-RhRM","type":"text","text":"{%s}","options":[],"blanks":[]},{"id":"q-5-lpN1","type":"textarea","text":"","options":[],"blanks":[]}]}],"referrer":""}' % (time1,date)})
data = data.encode('utf-8')
request = urllib.request.Request("https://wj.qq.com/sur/collect_answer")
# adding charset parameter to the Content-Type header.
request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")

context = ssl._create_unverified_context()
f = urllib.request.urlopen(request, data,context=context)

response = f.read().decode('utf-8')

print(response)

time.sleep(2)

