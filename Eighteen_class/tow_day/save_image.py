import requests

# 发送请求
response = requests.get("https://www.baidu.com/img/bd_logo1.png")

# 保存图片
with open('baidu_logo.png','wb') as f:
    f.write(response.content)