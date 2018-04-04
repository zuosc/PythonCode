# -*- coding:utf-8 -*-
# /usr/bin/env python3
# Power by zuosc

from bs4 import BeautifulSoup
import urllib.request
import time

def getLastName():
    f = open('keygiveaway.txt', 'r')
    content = f.read()
    return content.strip()

def updateName(name):
    f = open('keygiveaway.txt', 'w')
    f.write(name)


def sengMsg(desp):
    sendurl = 'http://sc.ftqq.com/SCU5209T50ff781c69372d9b370387f5c079be01587ae52428055.send?'
    params = {'text': "keygiveaway", 'desp': "游戏名称："+desp}
    params = urllib.parse.urlencode(params)
    urllib.request.urlopen(sendurl + params)

url = 'http://keygiveaway.com'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
req = urllib.request.Request(url, headers={'User-Agent':user_agent})
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html,"html.parser")
trs = soup.findAll('table')[0].findAll("tbody")[0].findAll("tr")
tds = trs[0].findAll("td")
printDes = ""

gameType = tds[3].find("img").attrs["alt"]
name = tds[5].find("h4").text.strip()
lastName = getLastName()

printDes = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
printDes += "\r\n新获得的游戏类型是:" + gameType
printDes += "\r\n游戏名称：" + name
printDes += "\r\n上次记录的游戏名称为：" + lastName
printDes += "\r\n------------------------------------------------\r\n"

if (((gameType == "Steam") | (gameType == "Othrer")) & (lastName != name)):
    sengMsg(name)
    updateName(name)

print(printDes)

