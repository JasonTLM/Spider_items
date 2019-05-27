# coding=utf-8
import requests

# response = requests.get("https://www.baidu.com")
# # print(type(response.text))
# # print(response.text)
# print(type(response.content))
# print(response.content.decode('utf-8'))
#
# print(response.url)
# print(response.encoding)
# print(response.status_code)

login_url = 'https://www.baidu.com/s'
params = {
    'wd':"中国"
}

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

response = requests.get(login_url,params=params,headers=headers)

with open('baidu.html','w',encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))

print(response.url)