import requests
import json

headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1X-Requested-With: XMLHttpRequest"}
post_data = {
    "query": "你好",
    "from": "zh",
    "to": "en",
}
post_url = "http://fanyi.baidu.com/basetrans"

r = requests.post(post_url,data=post_data,headers=headers)

print(r.content.decode("utf-8"))
