# ending=utf-8
import requests
import json


class DoubanSpider:
    def __init__(self):
        self.url_temp_list = [
            {
                "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?&start={}&count=18&loc_id=108288",
                "country": "US"
            },
            {
                "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/tv_korean/items?start={}&count=18&loc_id=108288",
                "country": "KE"
            },
            {
                "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/tv_domestic/items?start={}&count=18&loc_id=108288",
                "country": "CN"
            }
        ]
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36"
        }

    def parse_url(self, url):
        # 发送请求，获取响应
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode("utf-8")

    def get_content_list(self, json_str):
        # 提取数据
        dict_ret = json.loads(json_str)
        print(dict_ret)
        print("_______________")
        content_list = dict_ret["subject_collection_items"]
        total = dict_ret["total"]
        return content_list, total

    def seve_content_list(self, content_list, country):
        # 保存数据
        with open("douban.txt", "a", encoding='utf-8') as f:
            for content in content_list:
                content["country"] = country
                f.write(json.dumps(country, ensure_ascii=False))
                f.write("\n")
        print("保存成功！")

    def run(self):
        """实现主要功能"""
        for url_temp in self.url_temp_list:
            num = 0
            # 设置total值，以假定默认有第一页
            total = 27
            while num < total + 18:
                # 1,获取start_url
                url = url_temp["url_temp"].format(num)
                # 2,发送请求，获取响应
                json_str = self.parse_url(url)
                # 3,提取数据
                content_list, total = self.get_content_list(json_str)
                # 4,保存数据
                self.save_content_list(content_list, url_temp["country"])
                # if len(content_list)<18:
                #     break
                # 5,构造下一个url地址，进入循环
                num += 18


if __name__ == "__main__":
    douban_spider = DoubanSpider()
    douban_spider.run()
 