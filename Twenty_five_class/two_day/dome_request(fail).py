# coding=utf-8
#
#
# from urllib import request
# from urllib import parse
#
# url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false'
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36",
#     "Referer": "https://www.lagou.com/jobs/list_python?city=%E6%B7%B1%E5%9C%B3&cl=false&fromSearch=true&labelWords=&suginput="
# }
#
# data = {
#     'first':'true',
#     'pn':1,
#     'kd':'python'
# }
#
#
# #
# # url = "https://www.zhipin.com/job_detail/?query=python&city=101280600&industry=&position="
# #
# # req = request.Request(url,headers=headers)
# # response = request.urlopen(req)
# #
# # print(response.read())
#
# req = request.Request(url,headers=headers,data=parse.urlencode(data).encode('UTF-8'),method='POST')
#
# response = request.urlopen(req)
#
# print(response.read().decode('utf-8'))

from urllib import request
from urllib import parse

url = "https://m.lagou.com/search.json?city=%E6%B7%B1%E5%9C%B3&positionName=python&pageNo=1&pageSize=15"

headers = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36",
    "Referer": "https://m.lagou.com/search.html",
    "X-Requested-With": "XMLHttpRequest"
}

req = request.Request(url,headers=headers)

response = request.urlopen(req)
print(response.read().decode('utf-8'))