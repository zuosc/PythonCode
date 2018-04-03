# -*- coding:utf-8 -*-
# !usr/bin/env python3
# Power by zuosc

from bs4 import BeautifulSoup
import urllib.request


def getLatChapter():
    addr = 'http://m.09xs.com/info-48609/'
    html = urllib.request.urlopen(addr).read()
    soup = BeautifulSoup(html, 'html.parser')
    lastChapter = soup.find_all('a')[8]['href']
    return lastChapter


def sengMsg(chapter):
    mAddr = 'http://m.09xs.com/'+chapter
    sendurl = 'http://sc.ftqq.com/SCU5209T50ff781c69372d9b370387f5c079be01587ae52428055.send?'
    params = {'text': "玄界之门", 'desp': mAddr}
    params = urllib.parse.urlencode(params)
    urllib.request.urlopen(sendurl + params)

try:
    lastChapter = getLatChapter()
    f = open('xuanjiezhimen.txt', 'r')
    content = f.read()

    if content == lastChapter:
        pass

    else:
        f = open('xuanjiezhimen.txt', 'w')
        f.write(lastChapter)
        sengMsg(lastChapter)
    f.close()
except:
    f = open('xuanjiezhimen.txt', 'w')
    f.write(getLatChapter())
    f.close()
    sengMsg(lastChapter)




