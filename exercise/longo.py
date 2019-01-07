#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:loftybay
import os
user_info = 'userinfo'
#创建目录函数
def mkdir_dir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
#创建存放user和passwd信息的文件
file = user_info
mkdir_dir(file)  # 调用函数
files = open('userinfo\\user_name' + '.txt','w')
files = open('userinfo\\user_passwd'+'.txt','w')
files = open('userinfo\\user_lock' + '.txt','w')
files.close()
longo_count = 0
while longo_count < 3:

    select = input("请选择登录（y）或者注册（n）：")
    if select == "y":
        username = input("请输入你的用户名：")
        password = input("请输入你的密码：")
        longo_count = longo_count +1
    elif select == "n":
        username = input("请输入你要注册的用户名：")
        passwordA = input("请输入你的密码：")
        passwordB = input("请再次输入你的密码：")
        longo_count = 3
    else:
        print("输入无效：")
