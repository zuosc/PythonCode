# -*- coding:utf-8 -*-
# !usr/bin/env python3
# Power by zuosc

from bs4 import BeautifulSoup
import urllib.request


def getLatChapter():
    shengxuAddr = 'http://www.yinyuanren.com'
    html = urllib.request.urlopen(shengxuAddr).read()
    soup = BeautifulSoup(html, 'html.parser')
    lastChapter = soup.find_all('a')[-5]['href']
    return lastChapter


def sengMsg(chapter):
    sendurl = 'http://sc.ftqq.com/SCU5209T50ff781c69372d9b370387f5c079be01587ae52428055.send?'
    params = {'text': "圣墟新章节", 'desp': chapter}
    params = urllib.parse.urlencode(params)
    urllib.request.urlopen(sendurl + params)

try:
    lastChapter = getLatChapter()
    f = open('shengxu.txt','r')
    content = f.read()

    if content == lastChapter:
        pass

    else:
        f = open('shengxu.txt', 'w')
        f.write(lastChapter)
        sengMsg(lastChapter)
    f.close()
except:
    f = open('shengxu.txt', 'w')
    f.write(getLatChapter())
    f.close()
    sengMsg(lastChapter)




