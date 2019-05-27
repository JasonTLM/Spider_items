# coding=utf-8
import requests
from lxml import etree

url = "https://www.lagou.com"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Referer": "https://www.lagou.com/",
    "Cookie": "JSESSIONID=ABAAABAAADGAACF8712DD4AB431672EE3925959781908B0; _ga=GA1.2.307765564.1558146475; _gid=GA1.2.2057908636.1558146475; user_trace_token=20190518102754-8ad20a90-7914-11e9-a0c7-5254005c3644; LGSID=20190518102754-8ad20c0f-7914-11e9-a0c7-5254005c3644; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DWKIsGHbLUQdn679NoPyGUnxplXDHkJnuHIDSsf09mzC%26wd%3D%26eqid%3D954417ca00021cf8000000065cdf6da6; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20190518102754-8ad20d9b-7914-11e9-a0c7-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; X_HTTP_TOKEN=e112cb3d06266ef00097418551f958ddfa7836791d; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1558146475,1558147901; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1558147901; LGRID=20190518105140-dce42049-7917-11e9-a18b-525400f775ce"
}

response = requests.get(url,headers=headers,)

# parser = etree.HTMLParser(encoding='utf-8')
# html = etree.HTML(response.text,parser=parser)
#
# print(etree.tostring(html,encoding='utf-8').decode('utf-8'))

# # 报错，出现以下错误
# # html_file = etree.parse(text,parser=parse)
# # File "src/lxml/etree.pyx", line 3435, in lxml.etree.parse
# # File "src/lxml/parser.pxi", line 1840, in lxml.etree._parseDocument
# # File "src/lxml/parser.pxi", line 1866, in lxml.etree._parseDocumentFromURL
# # File "src/lxml/parser.pxi", line 1770, in lxml.etree._parseDocFromFile
# # File "src/lxml/parser.pxi", line 1163, in lxml.etree._BaseParser._parseDocFromFile
# # File "src/lxml/parser.pxi", line 601, in lxml.etree._ParserContext._handleParseResultDoc
# # File "src/lxml/parser.pxi", line 711, in lxml.etree._handleParseResult
# # File "src/lxml/parser.pxi", line 638, in lxml.etree._raiseParseError
# # OSError: Error reading file '
# parser = etree.HTMLParser(encoding='utf-8')
# html_file = etree.parse(response.text,parser=parser)

parser = etree.HTMLParser(encoding='utf-8')
html_lagou_file = etree.HTML(response.text,parser=parser)
#
# # print(etree.tostring(html_lagou_file,encoding='utf-8').decode('utf-8'))
# divs = html_lagou_file.xpath("//div")
# for div in divs:
#     print(etree.tostring(div,encoding='utf-8').decode('utf-8'))


# div = html_lagou_file.xpath("//div[2]")[2]
# print(etree.tostring(div,encoding='utf-8').decode('utf-8'))

divs = html_lagou_file.xpath("//div[contains(@class,'third')]")
for div in divs:
    print(etree.tostring(div,encoding='utf-8').decode('utf-8'))
