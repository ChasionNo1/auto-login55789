import requests
import json
from lxml import etree


class Tencentfilms:

    def __init__(self):
        self.url_temp = "https://v.qq.com/x/list/movie?offset={}&pay=100002"
        self.headers = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"}

    def get_url_list(self):
        url_list = [self.url_temp.format(i) for i in range(0, 4980, 30)]
        return url_list

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, html_str):
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[@class='mod_figures mod_figure_v']//li")
        content_list = []
        for div in div_list:
            item = {}
            item["片名"] = div.xpath(".//div/strong//text()")
            item["等级"] = div.xpath(".//i[@class='mark_v']//@alt")
            item["评分"] = div.xpath(".//div[@class='figure_score']/em/text()")
            item["评分"] = "".join([str(i) for i in item["评分"]])
            content_list.append(item)
        return content_list

    def save_content_list(self, content_list):
        with open("用券电影.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                if "".join(content["等级"]) == "VIP用券":
                    f.write(json.dumps(content, ensure_ascii=False))
                    f.write("\n")
        with open("独播.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                if "".join(content["等级"]) == "独播":
                    f.write(json.dumps(content, ensure_ascii=False))
                    f.write("\n")
        with open("付费.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                if "".join(content["等级"]) == "付费":
                    f.write(json.dumps(content, ensure_ascii=False))
                    f.write("\n")

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            html_str = self.parse_url(url)
            content_list = self.get_content_list(html_str)
            self.save_content_list(content_list)


if __name__ == '__main__':

    tencentfilms = Tencentfilms()
    tencentfilms.run()












