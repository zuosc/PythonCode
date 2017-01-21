# -*- coding:utf-8 -*-
# !/usr/bin/env python3
# Power by hw 2017-01-10

import random

class Game(object):

    def __init__(self):
        self.Tom = {'Name': "Tom", 'Blood': 120, 'Attack': 40, 'Defense': 10, 'Hit': 40, 'Dodge': 20, 'Crit': 20}
        self.Jhon = {'Name': "Jhon", 'Blood': 150, 'Attack': 25, 'Defense': 20, 'Hit': 30, 'Dodge': 50, 'Crit': 15}

    def attack_behavior(self,soldierA,soldierB,count):
        print ('第%s回合...' % count)
        hitresult =  soldierA['Hit'] + 50 - soldierB['Dodge'] > 100 - random.randint(0,100)
        if hitresult:
            critresult = soldierA['Crit'] > 100 - random.randint(0,100)
            if critresult:
                soldierBBlood = soldierB['Blood'] - (soldierA['Attack'] * 2 - soldierB['Defense'])
            else:
                soldierBBlood = soldierB['Blood'] - (soldierA['Attack'] - soldierB['Defense'])

            soldierB['Blood'] = soldierBBlood
            if count % 2 != 0:
                print('%s剩余血量:%d' % (soldierA['Name'], soldierA['Blood']))
                print('%s剩余血量:%d' % (soldierB['Name'], soldierB['Blood']))
            else:
                print('%s剩余血量:%d' % (soldierB['Name'], soldierB['Blood']))
                print('%s剩余血量:%d' % (soldierA['Name'], soldierA['Blood']))
            if critresult:
                print('%s对%s造成了双倍的伤害!!!' % (soldierA['Name'], soldierB['Name']))
            return soldierBBlood

        else:
            print('%s闪避了%s的攻击!!!' % (soldierA['Name'], soldierB['Name']))
            return 9999


game = Game()

count = 0
flag = 1

while flag > 0:
    count = count + 1
    if count % 2 != 0:
        result = game.attack_behavior(game.Tom, game.Jhon, count)
    else:
        result = game.attack_behavior(game.Jhon,game.Tom,count)
    print ('\n')
    if(result <= 0):
        print ('游戏结束...')
        flag = 0
