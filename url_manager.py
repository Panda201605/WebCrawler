# coding:utf8

"""
crawler main function, call for other function
Created on 2015-12-31
"""


# 实现一个url管理器的类
class UrlManager(object):
    # url管理器里面有两个url集合，分别保存已经爬取过的url和未爬取的url
    def __init__(self):
        # 未爬取的url
        self.new_urls = set()
        # 已爬取的url
        self.old_urls = set()

    def add_new_url(self, url):
        # 添加一个url到管理器

        if url is None:
            return
        if url not in self.old_urls and url not in self.new_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        # 批量添加url到管理器

        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        # 判断是否还有未爬取的url

        return len(self.new_urls) != 0

    def get_new_url(self):
        # 获取一条新的未爬取的url

        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
