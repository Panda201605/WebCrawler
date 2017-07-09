# coding:utf8

"""
原文网址：http://blog.csdn.net/gvfdbdf/article/details/50446144
crawler main function, call for other function
Created on 2015-12-31
@author: Itachi
"""

import html_downloader
import html_outputer
import html_parser
import url_manager


# 爬虫类
class SpiderMain(object):

    # 初始化爬虫的管理器、下载器、解析器和输出
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownload()
        self.parser = html_parser.HtmlParse()
        self.outputer = html_outputer.HtmlOutput()

        # 爬虫启动程序
    def start(self, root_url):
        # 将入口url添加进url管理器
        self.urls.add_new_url(root_url)
        # 爬虫爬取url计数
        count = 1
        # 当管理器有ur
        while self.urls.has_new_url():
            # 从管理器获取一个新url
            new_url = self.urls.get_new_url()
            # 利用下载器下载网页内容
            html_content = self.downloader.download(new_url)
            # 解析下载得到的网页内容,得到新的url和数据
            new_urls, new_data = self.parser.parse(new_url,html_content)
            # 将解析的数据存入输出器,解析的url批量加入管理器
            self.outputer.collect_data(new_data)
            self.urls.add_new_urls(new_urls)
            # 打印爬虫信息
            print("crawle %d : %s\n" %(count, new_url))

            # 只爬取1000个页面
            if count >= 100:
                break
            count = count + 1

            # 将最后的结果以html文件形式输出
        self.outputer.output_html()
        print("crawler stop")

if __name__ == "__main__":
    # 开始url
    root_url = "http://baike.baidu.com/view/125370.htm"
    # 创建一个爬虫
    obj_spider = SpiderMain()
    # 启动爬虫
    obj_spider.start(root_url)
