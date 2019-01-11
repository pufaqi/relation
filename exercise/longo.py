#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:loftybay
import os
#创建目录函数
def _MAKE_DIR(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        # 创建存放user和passwd信息的文件
        files = open('userinfo\\user_name' + '.txt','w')
        files = open('userinfo\\user_passwd'+'.txt','w')
        files = open('userinfo\\user_lock' + '.txt','w')
        files.close()


##检查用户是否被锁定
def _CHECK_USER_LOCK():
    check_user = open(userinfo_lock, 'r+')
    check_list = check_user.readlines()
    #print(check_list)   #断点测试
    check_user.close()
    for check_line in check_list:
        check_line = check_line.strip('\n')
        if username == check_line:
            print("用户已经被锁定，请联系管理员！")
            break
#检查用户是否存在
def _CHECK_USER_NAME():
    check_user = open(userinfo_user, 'r+')
    check_list = check_user.readlines()
    print(check_list)   #测试输出
    check_user.close()
    for check_line in check_list:
        print(check_list)
        check_line = check_line.strip('\n')
        if username == check_line:
            _HELLO_PORT()
            print("用户存在")
            break
        elif username != check_line:
            print("用户不存在")
            break

'''
#注册用户函数
def _USER_REGISTER():
    register_count = 0
    while register_count < 3:
        username = input("请输入你要注册的用户名")
        check_user = open(userinfo_user,'r+')
        check_list = check_user.readline()
        check_user.close()
        for check_line in check_list:
            check_line = check_line.strip('\n')
            if userename
'''
def _HELLO_PORT():
    print("欢迎登录！")
#创建目录和文件
file = 'userinfo'
_MAKE_DIR(file)  # 调用函数
#代码开始
#定义变量
userinfo_user = 'userinfo\\user_name.txt'
userinfo_pass = 'userinfo\\user_passwd.txt'
userinfo_lock = 'userinfo\\user_lock.txt'

select = input("请选择登录（1）或者注册（2）：")
username = input("请输入你的用户名：")
password = input("请输入你的密码：")

_CHECK_USER_LOCK()
_CHECK_USER_NAME()
