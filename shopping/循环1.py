#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:loftybay
age = 23
count = 0
while count < 4:
    print("请在下面输入你要猜的数字")
    _age = int (input("请输入：") )
    if _age > 23 :
        print("你猜大了")
    elif _age < 23 :
        print("你猜小了")
    else:
        print("你猜对了，年龄为：",_age)
        break
    count +=1
    if count == 4:
        hint = input("你还要继续这个游戏吗？")
        if hint != n:
            count = 0
else:
    print("你猜的次数已到，游戏结束！！！")