#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Author:pufaqi
#loftybay@163.com
'''
import json
date = [ {'a': 1,'b': 2, 'c': 3,'d': 4} ]
json = json.dumps(date)
print(json)
i = ['a', 'b']
l = [1, 2]
print (dict(zip(i,l)))

def add(x,y,f):
    return f(x) + f(y)

res = add(3,-6,abs)
print(res)

a=id(10)
print(a)

def binary_chop(alist, data):
    """
    非递归解决二分查找
    :param alist:
    :return:
    """
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (last + first) // 2
        if alist[mid] > data:
            last = mid - 1
        elif alist[mid] < data:
            first = mid + 1
        else:
            return True
    return False

if __name__ == '__main__':
    lis = [2,4, 5, 12, 14, 23]
    if binary_chop(lis, 14):
        print('ok')
#import repr
a=dir(repr)
print(a)
help(repr.__dir__)
'''

# coding:utf-8

import json
from wsgiref.simple_server import make_server


# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
def application(environ, start_response):
    # 定义文件请求的类型和当前请求成功的code
    start_response('200 OK', [('Content-Type', 'application/json')])
    # environ是当前请求的所有数据，包括Header和URL，body

    request_body = environ["wsgi.input"].read(int(environ.get("CONTENT_LENGTH", 0)))
    request_body = json.loads(request_body)

    name = request_body["name"]
    no = request_body["no"]

    # input your method here
    # for instance:
    # 增删改查

    dic = {'myNameIs': name, 'myNoIs': no}

    return [json.dumps(dic)]


if __name__ == "__main__":
    port = 6088
    httpd = make_server("0.0.0.0", port, application)
    print
    "serving http on port {0}...".format(str(port))
    httpd.serve_forever()