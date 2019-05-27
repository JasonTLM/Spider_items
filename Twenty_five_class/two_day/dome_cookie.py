# coding=utf-8
from urllib import request

login_url = "http://www.renren.com/880151247/profilve"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Cookie": "anonymid=jvi9l74nqit1wu; depovince=FJ; _r01_=1; JSESSIONID=abczmjpZOIV50cjCVDIQw; ick_login=e7adb299-c221-496c-9664-7b9fb7e290c8; t=c9952da9412815b55ee2edb4bd76be614; societyguester=c9952da9412815b55ee2edb4bd76be614; id=970762894; xnsid=5d881dcd; ver=7.0; loginfrom=null; jebe_key=e3c3ff3a-9139-4520-8b38-7a82d099ec6e%7Cdec0dfb1f3605255d9d45cc2d42c3262%7C1557503928414%7C1%7C1557503928272; wp_fold=0; XNESSESSIONID=67885d0a5c85; WebOnLineNotice_970762894=1; jebecookies=fcea8d44-8bc9-4b70-9280-31ea411d42ba|||||"
}

req = request.Request(url=login_url,headers=headers)
response = request.urlopen(req)
with open('renren.html','w',encoding='utf-8') as f:
    f.write(response.read().decode('utf-8'))


