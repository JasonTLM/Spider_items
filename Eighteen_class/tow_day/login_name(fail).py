import requests

session = requests.session()
post_url = 'http://www.renren.com/PLogin.do'
post_data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

session.post(post_url,data=post_data,headers=headers)

response = session.get("http://www.renren.com/410043129/profile",headers=headers)
with open("login_name.html","w",encoding="utf-8") as f:
    f.write(response.content.decode("utf-8"))

