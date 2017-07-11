# encoding:utf8

import random

from httpclient.client import HttpClient
from spider.html_parser import HtmlParse


class ProxyPoll(object):
    """
    代理ip池
    """

    def __init__(self, proxy_web):
        # 初始化代理池

        self.ip_pool = set()
        self.http_client = HttpClient()
        self.add_ip_pool(proxy_web)

    def add_ip_pool(self, proxy_web):
        # 添加网页上的代理ip
        response = HttpClient.get_response(proxy_web)
        add_pool = HtmlParse.parse_ip(response)
        self.ip_pool = self.ip_pool | add_pool

    def get_proxy(self):
        # 取出一个代理ip
        proxy = random.choice(self.ip_pool)
        # proxy为空暂未处理，后期处理
        if self.is_alive(proxy):
            return proxy
        else:
            self.del_proxy(proxy)
            return self.get_proxy()

    def del_proxy(self, proxy):
        # 从代理ip池中删除
        self.ip_pool.discard(proxy)

    def is_alive(self, proxy):
        # 测试代理ip是否可用

        try:
            resp = self.get_response(self.test_url, proxy=proxy)
            print(resp.read())
            if resp.code == 200:
                return True
        except BaseException as be:
            print(be)
            return False

    def write_to_text(self, file_path):
        # 持久化ip代理池

        try:
            fp = open(file_path, "w+")
            for item in self.ip_pool:
                fp.write(str(item) + "\n")
            fp.close()
        except IOError:
            print("fail to open file")
