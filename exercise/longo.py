#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:loftybay
import os,sys

#创建目录
def _MAKE_DIR(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        # 创建存放user和passwd信息的文件
        files = open('userinfo\\user_name' + '.txt','w')
        files = open('userinfo\\user_passwd'+'.txt','w')
        files = open('userinfo\\user_lock' + '.txt','w')
        files.close()

#输出hello
def _HELLO_PORT():
    print("欢迎登录！")

##检查用户是否被锁定
def _CHECK_USER_LOCK():
    check_user = open(userinfo_lock, 'r+')
    check_list = check_user.readlines()
    check_user.close()
    for check_line in check_list:
        check_line = check_line.strip('\n')
        if username == check_line:
            print("用户已经被锁定，请联系管理员！")
            sys.exit()

#检查用户是否存在
def _CHECK_USER_NAME():
    check_user = open(userinfo_user, 'r+')
    check_list = check_user.readlines()
    check_user.close()
    for check_line in check_list:
        check_line = check_line.strip('\n')
        if username == check_line:
            _HELLO_PORT()
            break

#创建目录和文件
file = 'userinfo'
_MAKE_DIR(file)  # 调用函数
#代码开始
#定义存储文件的变量
userinfo_user = 'userinfo\\user_name.txt'
userinfo_pass = 'userinfo\\user_passwd.txt'
userinfo_lock = 'userinfo\\user_lock.txt'

select = input("请选择登录（1）或者注册（2）：")

if select == "1":
    username = input("请输入你的用户名：")
    password = input("请输入你的密码：")
    _CHECK_USER_LOCK()  #检查输入的用户是否被锁定
    _CHECK_USER_NAME()  #检查输入的用户是否存在
elif select == "2":
    username = input("请输入你要注册的用户名")
    _CHECK_USER_NAME()