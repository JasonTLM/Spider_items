# coding=utf-8

from urllib import request

# 没有使用代理
url = 'http://httpbin.org/get'
response_no = request.urlopen(url)
print(response_no.read())
# print("args:",response_no.args)

# # 使用代理后的情况
# # 1.使用request.ProxyHandler，传入代理构建一个handler
# handler = request.ProxyHandler({"http":"117.139.126.236:53281"})
# # 2.使用上面创建的handler构建一个opener
# opener = request.build_opener(handler)
# # 3.使用opener发送一个请求，确认IP地址
# response = opener.open(url)
# print(response.read())

