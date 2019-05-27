# coding=utf-8
"""由于该网页第一页数据为独立主url获取，其余由ajax生成，为第二部分独立"""
import requests
import json
import re

class NeihanSpider:
    def __init(self):
        self.start_url = "http://neihanshequ.com/"
        self.next_url_temp = "http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time={}"
        self.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36"}

    def parse_url(self,url):
        """发送请求"""
        print(url)
        response = requests.get(url,headers=self.headers)
        return response.content.decoded('utf-8')

    def get_first_page_content_list(self,html_str):
        """提取第一页的数据"""
        content_list = re.findall(r"<h1 class=\"title\">.*?<p>(.*?)</p>",html_str,re.S)
        max_time = re.findall("max_time:'(.*?)',",html_str)[0]
        return content_list,max_time
    def save_content_list(self,content_list):
        """保存数据"""
        with open("neihan.txt","a",encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")
        print("保存成功")

    def get_content_list(self,json_str):
        dict_ret = json.loads(json_str)
        data = dict_ret["data"]["data"]
        content_list = [i["group"]["content"] for i in data]
        max_time = dict_ret["data"]["max_time"]
        has_more = dict_ret["data"]["has_more"]
        return content_list,max_time,has_more

    def run(self):
        """实现主要功能"""
        # 1.star_url
        # 2.发送请求，获取响应
        html_str = self.parse_url(self.start_url)
        # 3.提取数据
        content_list,max_time = self.get_first_page_content_list(html_str)
        # 4.保存数据
        self.save_content_list(content_list)
        has_more = True
        while has_more:
            # 5.构造下一页的url地址
            next_url = self.next_url_temp.format(max_time)
            # 6.发送请求，获取相应
            json_url = self.parse_url(next_url)
            # 7.提取数据
            content_list,max_time,has_more = self.get_content_list(json_url)
            # 8.保存数据
            self.save_content_lsit(content_list)
            # 9.循环5-8

if __name__ == "__main__":
    neihan = NeihanSpider()
    neihan.run()