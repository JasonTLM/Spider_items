# coding=utf-8
# /usr/bin/Python文档 python
'''
Author: JasonLee
Email: 1269782531@qq.com
Wechat: 18475514685
GetHub:
'''

from urllib import request
from urllib import parse

url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=" \
      "1&rsv_idx=1&tn=baidu&wd=%E6%88%91%E7%88%B1%E7%BD%97&" \
      "oq=jason&rsv_pq=d36bcc2500000672&rsv_t=357888gb82ywnhV%2FZ" \
      "NEnUH7BMK5avhFXSjOrrJacEARBo77Y5hhsnKIe8XU&rqlang=cn&rsv_enter=1&rs" \
      "v_sug3=11&rsv_sug1=8&rsv_sug7=101&bs=jason"

# result = parse.urlsplit(url)
result = parse.urlparse(url)

print(result)
print('scheme:',result.scheme)
print('netloc:',result.netloc)
print('path:',result.path)
print('params:',result.params)
print('query:',result.query)
print('fragment:',result.fragment)


