# coding=utf-8
from urllib import request
from http.cookiejar import MozillaCookieJar

cookiejar = MozillaCookieJar('cookie.txt')
# 调用cookiejar.load()方法传入ignore_discard=Ture参数加载已保存的cookie信息
cookiejar.load(ignore_discard=True)
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

# 获取设置cookie信息
# response = opener.open('http://httpbin.org/cookies/set?course=jason')
# 保存cookie，因为cookie信息在浏览器访问关闭时，就会过期，故需要使用ignore_discard=True来设定保存即将过期的cookie信息
# cookiejar.save(ignore_discard=True)
for cookie in cookiejar:
    print(cookie)

