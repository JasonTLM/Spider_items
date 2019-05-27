# coding=utf-8
import requests
from lxml import etree

# url = "https://www.qiushibaike.com/"
url = "https://www.lagou.com/"

response = requests.get(url)

# print(response.content.decode('utf-8'))
text = response.content.decode('utf-8')

def parse_text():
    htmlElement = etree.HTML(response.text)
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))
# parser = etree.HTMLParser(encoding='utf-8')
# html = etree.parse(text,parser=parser)

if __name__ == '__main__':
    parse_text()

