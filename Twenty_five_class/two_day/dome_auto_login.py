# coding=utf-8
from http.cookiejar import CookieJar
from urllib import request
from urllib import parse

# 1.登录
login_url = "http://www.renren.com/SysHome.do"
viewer_url = "http://www.renren.com/880151247/profilve"
# 准备一个存有User—Agent的headers以及一个data
headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

data = {
    "email":"1269782531@qq.com",
    "password":"忘记了"
}

# 1.1实例化一个CookieJar对象
cookiejar = CookieJar()
# 1.2使用HTTPCookieProcess方法传入上面创建的cookiejar创建一个handler
handler = request.HTTPCookieProcessor(cookiejar)
# 1.3使用build_opener方法传入handler创建一个opener
opener = request.build_opener(handler)

logding = request.Request(login_url,data=parse.urlencode(data).encode('utf-8'),headers=headers)
opener.open(logding)

# 2 访问个人主页
# 获取个人主页的页面的时候，不要创建一个新的opener，而是使用之前创建的opener，因为之前创建的opener经过登录后保存了需要的cookie信息
logding_viwer = request.Request(viewer_url,headers=headers)
response = opener.open(logding_viwer)
with open("renren_auto.html",'w',encoding='utf-8') as fp:
    fp.write(response.read().decode('utf-8'))


