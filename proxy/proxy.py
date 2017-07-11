# encoding:utf8

import time
import random
from bs4 import BeautifulSoup
from httpclient.client import HttpClient


class ProxyPoll(object):
    """
    代理池
    """

    def __init__(self, proxy_web_ips):
        # 初始化代理池

        self.ip_pool = set()
        self.proxy_finder = proxy_web_ips
        self.http_client = HttpClient()

    def get_proxies(self):
        # 确保代理ip可用

        for p in self.ip_pool:
            if self.http_client.is_alive(p):
                continue
            else:
                self.ip_pool.remove(p)

    def get_one_proxy(self):
        # 取出一个代理ip

        return random.choice(self.ip_pool)

    def write_to_text(self, file_path):
        # 持久化ip代理池

        try:
            fp = open(file_path, "w+")
            for item in self.ip_pool:
                fp.write(str(item) + "\n")
            fp.close()
        except IOError:
            print("fail to open file")

    def find(self):
        # 从代理服务器上爬取代理ip

        for i in range(1, 10):
            content = self.http_client.getresponse(self.url + str(i))
            soup = BeautifulSoup(content)
            ips = soup.findAll('tr')
            for x in range(2, len(ips)):
                ip = ips[x]
                tds = ip.findAll("td")
                if tds is None:
                    continue
                ip_temp = tds[1].contents[0] + ":" + tds[2].contents[0]
                self.ip_pool.append(ip_temp)
            time.sleep(1)
            return self.ip_pool
