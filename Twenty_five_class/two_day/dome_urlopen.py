# coding=utf-8
# /usr/bin/Python文档 python
'''
Author: JasonLee
Email: 1269782531@qq.com
Wechat: 18475514685
GetHub:
'''

from urllib import request

response = request.urlopen("http://www.baidu.com")
print(response.getcode())
print(response.readlines())
# print(response.read())
