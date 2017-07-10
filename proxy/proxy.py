# encoding:utf8

import time
import random
from bs4 import BeautifulSoup
from httpclient.client import HttpClient


class ProxyPoll(object):
    """
    代理池
    """

    def __init__(self, proxy_finder):
        self.pool = []
        self.proxy_finder = proxy_finder
        self.http_client = HttpClient()

    def get_proxies(self):
        self.pool = self.proxy_finder.find()
        for p in self.pool:
            if self.http_client.is_alive(p):
                continue
            else:
                self.pool.remove(p)

    def get_one_proxy(self):
        return random.choice(self.pool)

    def write_to_text(self, file_path):
        try:
            fp = open(file_path, "w+")
            for item in self.pool:
                fp.write(str(item) + "\n")
            fp.close()
        except IOError:
            print("fail to open file")

    def find(self):
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
                self.pool.append(ip_temp)
            time.sleep(1)
            return self.pool
