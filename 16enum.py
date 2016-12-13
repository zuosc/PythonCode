# _*_ coding:utf8 _*_
# Power by zuosc
# 枚举

from enum import Enum,unique

@unique
class Weekeday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekeday.Mon
print(day1.value)

print(Weekeday(1))

for name,member in Weekeday.__members__.items():
    print(name,'=>',member)