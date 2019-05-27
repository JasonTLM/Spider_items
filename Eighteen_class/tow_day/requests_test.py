
import requests

r = requests.get("https://www.baidu.com")
response = r.content.decode('utf-8')
print(response)
with open('requests_test.html','w') as f:
     f.write(response)