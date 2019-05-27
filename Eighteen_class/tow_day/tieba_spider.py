import requests


class TiebaSpider:
    def __init__(self, tieba_name, x):
        self.x = x
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

    def get_url_list(self):
        """构造url列表"""
        # url_list = []
        # for i in range(int(self.x)):
        #     url_list.append(self.url_temp.format(i*50))
        # return url_list
        return [self.url_temp.format(i * 50) for i in range(int(self.x))]

    def parse_url(self, url):
        print(url)
        """发送请求，获响应"""
        response = requests.get(url, headers=self.headers)
        return response.content.decode()  # 修改编码方式

    def save_html(self, html_str, page_num):
        """保存HTML字符串"""
        file_path = '/home/jason/文档/Python文档/Python_黑马/python_15讲/Eighteen_class/tow_day/save_html/' \
                    + "{}-第{}页.html".format(self.tieba_name, page_num)  # 路径设置加文件名字
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_str)

    def run(self):
        """实现主要逻辑"""
        # 1 构造url列表
        url_list = self.get_url_list()
        # 2 遍历,发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3 保存网页
            page_num = url_list.index(url) + 1  # 页码数
            self.save_html(html_str, page_num)


if __name__ == '__main__':
    tiebaname = input("请输入要爬取保存的贴吧名字：")
    x = input("请输入要爬取的页码数(数值为整数）：")
    tieba_spider = TiebaSpider(tiebaname, x)
    tieba_spider.run()
