# coding=utf-8
# /usr/bin/Python文档 python
'''
Author: JasonLee
Email: 1269782531@qq.com
Wechat: 18475514685
GetHub:
'''

# urlencode进行编码

from urllib import request

from urllib import parse

# params = {'name':'张三','age':18,'greet':'hello python'}
# result = parse.urlencode(params)
# print(result)

# url = 'http://www.baidu.com/s'
#
# params = {'wd':'马特达蒙'}
# qs = parse.urlencode(params)
# url = url + '?' + qs
#
# response = request.urlopen(url)
# print(response.read())

# parse_qs() 进行解码

params = {'name':'我爱罗','age':24,'greet':'hi'}
result = parse.urlencode(params)

print(result)

qs = parse.parse_qs(result)
print(qs)
