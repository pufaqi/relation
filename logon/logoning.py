#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:loftybay
import os

if os.path.exists("userinfo"):  # 判断userinfo目录是否存在！
    if os.path.exists("userinfo/user.txt"):
        print("userinfo/user.txt文件存在")
        if os.path.exists("userinfo/passwd.txt"):
            print("userinfo/passwd.txt文件存在")
        else:
            file = open('userinfo/passwd.txt', 'w')
            print("passwd文件不存在，已创建！")
    else:
        file = open('userinfo/user.txt', 'w')
    print("###############################")
    print("###############################")
    print("*******************************")
    print("$$$$$$$$欢迎来到登陆界面$$$$$$$")
    print("********************************")
    print("#################################")
else:
    cc = os.mkdir("userinfo")
    file = open('userinfo/user.txt', 'w')
    file = open('userinfo/passwd.txt', 'w')
    print("userinfo不存在，已创建userinfo。")
print("你是否拥有登录需要的账号？")
exist = input("请输入y/n")
if exist == 'y':
    username = input("请输入你的用户名：")
    password = input("请输入你的密码：")  # 这里在输入完成以后要去user.txt和passwd.txt文件里面去对比，需要加一个循环
elif exist == 'n':
    login_user = input("请输入你要注册的用户名：")
    login_passwdA = input("请输入你的密码")
    login_passwdB = input("请再次输入密码确认：")  # 这里在输入完成以后再在user.txt里面去查找用户是不是重复的，如果是重复的择提示
    if login_passwdA == login_passwdB:
        file_user = open('userinfo/user.txt', 'a')
        file_passwd = open('userinfo/passwd.txt', 'a')
        file_user.write(login_user + '\n')
        file_passwd.write(login_passwdA + '\n')
        print("注册成功！")  # 这里需要重新跳出在执行一次，目前还木有想到这么实现
    else:
        print("注册失败！")

else:
    print("输入无效！！！")