# coding:utf8

"""
原文网址：http://blog.csdn.net/gvfdbdf/article/details/50446144
crawler main function, call for other function
Created on 2015-12-31
@author: Itachi
"""

from spider import html_outputer, html_parser, url_manager
from client import http_client
from proxy import proxy


class SpiderMain(object):
    # 爬虫类

    def __init__(self):
        # 初始化爬虫的管理器、下载器、解析器和输出

        self.urls = url_manager.UrlManager()
        self.http_client = http_client.HttpClient()
        self.proxy_pool = proxy.ProxyPoll()
        self.parser = html_parser.HtmlParse()
        self.outputer = html_outputer.HtmlOutput()

    def start(self, root_url, proxy_url):
        # 爬虫启动程序

        # 初始化免费代理ip池
        self.proxy_pool.add_ip_pool(proxy_url)

        # 将入口url添加进url管理器
        self.urls.add_new_url(root_url)
        # 爬虫爬取url计数
        count = 1
        # 当管理器有ur
        while self.urls.has_new_url():
            # 从管理器获取一个新url
            new_url = self.urls.get_new_url()
            # 从代理ip池中获取代理ip
            proxy = self.proxy_pool.get_proxy()
            # 打印爬虫信息
            print("crawle %d : %s---------------------- start\n" % (count, new_url))
            # 利用下载器下载网页内容
            html_content = self.http_client.get_response_content(new_url, proxy=proxy)

            if html_content is None:
                continue

            # 解析下载得到的网页内容,得到新的url和数据
            new_urls, new_data = self.parser.parse(new_url, html_content)
            # 将解析的数据存入输出器,解析的url批量加入管理器
            self.outputer.collect_data(new_data)
            self.urls.add_new_urls(new_urls)
            # 打印爬虫信息
            print("crawle %d : %s---------------------- done\n" % (count, new_url))
            print("总数据：\n")
            print(len(self.urls.old_urls), "--------Done url:", self.urls.old_urls, "----------")
            print(len(self.urls.new_urls), "--------Todo url:", self.urls.new_urls, "----------")
            print(len(self.outputer.data), "--------Emials:", self.outputer.data, "----------")

            # 只爬取1000个页面
            if count >= 10000:
                break
            count = count + 1

        # 将最后的结果以html文件形式输出
        self.outputer.output_html()
        print("crawler stop")


if __name__ == "__main__":
    # 开始url
    root_web = "http://bbs.fobshanghai.com/thread-5931523-1-1.html"
    # 获取免费代理ip网址
    proxy_web = "http://www.xicidaili.com"
    # 创建一个爬虫
    obj_spider = SpiderMain()
    # 启动爬虫
    obj_spider.start(root_web, proxy_web)
