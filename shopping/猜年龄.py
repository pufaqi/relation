#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:loftybay
_agent = 22
agent = int (input ("请输入年龄："))
if _agent == agent :
    print ("你猜对了")
elif _agent > agent :
    print ("猜小了")
else :
    print ("你猜大了")
