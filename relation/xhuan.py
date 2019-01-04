#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:loftybay
count = 0
ages_ing = 15
while count < 3:
    ages = int (input("亲输入一个我心里想的数字："))
    if ages == ages_ing:
        print("恭喜您，猜对了")
        break
    elif ages > ages_ing:
        print("猜大了")
    else:
        print("猜小了")
    count = count +1
    if count == 3:
        counting = input("你还要继续玩吗？")
        if counting != 'n':
            count = 0