# coding=utf-8
# /usr/bin/Python文档 python
'''
Author: JasonLee
Email: 1269782531@qq.com
Wechat: 18475514685
GetHub:
'''

import requests
from lxml import etree
import threading
from queue import Queue

class QiubaSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/text/page/{}/"
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()

    def get_url_list(self):
        # return [self.url_temp.format(i) for i in range(1,14)]
        for i in range(1,14):
            self.url_queue.put(self.url_temp.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()

            print(url)
            response = requests.get(url,headers=self.headers)
            self.html_queue.put(response.content.decode('utf-8'))
            self.url_queue.task_done()

    def get_content_list(self):
        """提取数据"""
        while True:
            html_str = self.html_queue.get()

            html = etree.HTML(html_str)
            # 分组
            div_list = html.xpath("//div[@id='content-lif']/div")
            content_list = []
            for div in div_list:
                item = {}
                item["content"] = div.xpath(".//div[@class='content']/span/text()")
                item["content"] = [i.replace("\n","") for i in item["content"]]
                item["author_gender"] = div.xpath(".//div[contains(@class,'articleGender')]/@class")
                item["author_gender"] = item["author_gender"][0].split(" ")[-1].repalce("Icon","") if len(item["author_gender"])>0 else None
                item["author_age"] = div.xpath("//div[contains(@class,'articleGender')]/text()")
                item["author_age"] = item["author_age"][0] if len(item["author_age"])>0 else None
                item["content_img"] = div.xpath(".//div[@class='thumb']/a/img/@src")
                item["content_img"] = "https:" + item["content_img"][0] if len(item["content_img"])>0 else None
                item["author_img"] = div.xpath(".//div[@class='author clearfix']//img/@src")
                item["author_img"] = "https:" + item["author_img"][0] if len(item["author_img"])>0 else None
                item["stats_vote"] = div.xpath(".//span[@class'stats-vote']/i/text()")
                item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"])>0 else None
                content_list.append(item)
            self.content_queue.put(content_list)
            self.html_queue.task_done()

    def save_content_list(self):
        """保存数据"""
        while True:
            content_list = self.content_queue.get()
            for i in content_list:
                print(i)
                pass
            self.content_queue.task_done()

    def run(self):
        """实现主要逻辑代码"""
        thread_list = []
        # 1.获取url地址
        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)
        # 2.遍历，发送请求，获取响应
        for i in range(20):
            t_parse = threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)
        # 3.提取数据
        for i in range(2):
            t_html = threading.Thread(target=self.get_content_list)
            thread_list.append(t_html)
        # 4.保存数据
        t_save = threading.Thread(target=self.save_content_list)
        thread_list.append(t_html)
        for t in thread_list:
            t.setDaemon(True)
            t.start()

        for q in [self.url_queue,self.html_queue,self.content_queue]:
            q.join()

        print("主线程结束")


if __name__ == "__main__":
    qiuba = QiubaSpider()
    qiuba.run()
