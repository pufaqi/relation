#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:loftybay
import os
#创建目录函数
def mkdir_dir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        # 创建存放user和passwd信息的文件
        files = open('userinfo\\user_name' + '.txt','w')
        files = open('userinfo\\user_passwd'+'.txt','w')
        files = open('userinfo\\user_lock' + '.txt','w')
        files.close()

userinfo_user = 'userinfo\\user_name.txt'
userinfo_pass = 'userinfo\\user_passwd.txt'
userinfo_lock = 'userinfo\\user_lock.txt'

#检查用户名是否被锁定函数
def _CHECK_USER_LOCK():
    lock_count = 0
    while lock_count < 3:
        username = input("请输入你的用户名：")
        password = input("请输入你的密码：")
        lock_user = open(userinfo_lock,'r+')
        lock_list = lock_user.readlines()
        lock_user.close()
        for lock_line in lock_list:
            lock_line = lock_line.strip('\n')
            if username == lock_line:
                print("用户被锁定，请联系管理员！")
                lock_count = 3
                break
            else:
                lock_count = 3

#检查用户是否存在目录中函数
def _CHECK_USER_NAME():
    lock_count = 0
    while lock_count < 3:
        username = input("请输入你的用户名：")
        password = input("请输入你的密码：")
        lock_user = open(userinfo_lock,'r+')
        lock_list = lock_user.readlines()
        lock_user.close()
        for lock_line in lock_list:
            lock_line = lock_line.strip('\n')
            if username == lock_line:
                print("用户被锁定，请联系管理员！")
                lock_count = 3
                break
            else:
                lock_count = 3
#创建目录和文件
file = 'userinfo'
mkdir_dir(file)  # 调用函数
#代码开始
select = input("请选择登录（1）或者注册（2）：")
_CHECK_USER_LOCK()
print("kaishi")

''''
elif select == "2":
username = input("请输入你要注册的用户名：")
passwordA = input("请输入你的密码：")
passwordB = input("请再次输入你的密码：")
longo_count = 3
'''