#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:loftybay
import getpass
username = input("请输入你的名字：")
#password = getpass.getpass("请输入你的密码：")  ##在pycharm里面显示不出来，可以使用其他的去验证
password = input("请输入你的密码：")
_username = 'pufaqi'
_password = '123456'
if _username == username and _password == password:
    print("登录成功 {name} ".format(name=username))
    #print (OK)
else:
    print("登录失败,用户为 {user} ".format(user=username))



if a == b:
    print(c)
elif c == dd:
    print (e)
else:
    print(c)
