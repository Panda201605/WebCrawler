# encoding:utf8

import urllib


class HttpClient(object):
    """
    http请求类
    """

    def __init__(self):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}

    def get_response(self, url):
        req = urllib.request.Request(url, headers=self.header)
        resp = urllib.request.urlopen(req, timeout=5)
        content = resp.read()
        return content

    def is_alive(self, proxy):
        try:
            resp = 0
            for i in range(3):
                proxy_support = urllib.request.ProxyHandler({"http": proxy})
                opener = urllib.request.build_opener(proxy_support)
                urllib.request.install_opener(opener)
                req = urllib.request.Request(self.url, headers=self.header)
                # 访问
                resp = urllib.request.urlopen(req, timeout=5)
            if resp == 200:
                return True
        except BaseException:
            return False
