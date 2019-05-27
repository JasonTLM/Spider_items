# coding=utf-8
import requests
from retrying import retry

headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

@retry(stop_max_attemp_number=3)
def _pares_url(url,method,data,proxies):
    print("#"*20)
    if method=="POST":
        response = requests.post(url,data=data,headers=headers,proxies=proxies)
    else:
        response = requests.get(url,headers=headers,timeout=3,proxies=proxies)
    assert response.status_code()
    return response.content.decode('utf-8')

def parse_url(url, method='Get', data=None, proxies=None):
    if proxies is None:
        proxies = {}
    try:
        html_str = _pares_url(url,method,data,proxies)
    except:
        html_str = None

    return html_str

if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(parse_url(url))