# -*- coding:utf-8 -*-
# Power by hw 2017-01-10

import random

class Game(object):

    def __init__(self):
        self.Tom = {'Name': "Tom", 'Blood': 120, 'Attack': 40, 'Defense': 10, 'Hit': 40, 'Dodge': 20, 'Crit': 20}
        self.Jhon = {'Name': "Jhon", 'Blood': 150, 'Attack': 25, 'Defense': 20, 'Hit': 30, 'Dodge': 50, 'Crit': 15}

    def attack_behavior(self,soldierA,soldierB):
        hitresult =  soldierA['Hit'] + 50 - soldierB['Dodge'] > 100 - random.randint(0,100)
        if hitresult:
            pass
        else:
            print('%s闪避了%s的攻击!!!' % soldierA['Name'],soldierB['Name'])