# encoding:utf8

import random
import time
import urllib.request


class HttpClient(object):
    """
    http请求类
    """

    def __init__(self):
        self.test_url = "https://www.baidu.com/"
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]

    def get_response_content(self, url, timeout=5, proxy=None, retry_times=2):
        # 获取网站内容
        response = self.get_response(url, timeout, proxy, retry_times)
        if response is None:
            return None
        else:
            return response.read()

    def get_response(self, url, timeout=5, proxy=None, retry_times=2):
        # 获取请求结果
        header = {"User-Agent": random.choice(self.user_agent_list)}  # 构造一个完整的User_Agent

        if proxy is None:
            try:
                response = self.__get_response_without_proxy(url, timeout, header)
                return response
            except BaseException as be:
                print("url:", url, "header:", header, "proxy:", proxy)
                if retry_times > 0:
                    print(u"获取网页错误：", be, " ，10s后将获取倒数第：", retry_times, u"次")
                    time.sleep(10)
                    return self.get_response(url, timeout, retry_times=retry_times - 1)  # 调用自身并将次数减1
                else:
                    print("请求失败")
                    return None
        else:
            try:
                response = self.__get_response_with_proxy(url, timeout, header, proxy)
                return response
            except BaseException as be:
                print("url:", url, "header:", header, "proxy:", proxy)
                if retry_times > 0:
                    print(u"获取网页错误：", be, " ，10s后将获取倒数第：", retry_times, u"次")
                    time.sleep(10)
                    return self.get_response(url, timeout, proxy=proxy, retry_times=retry_times - 1)  # 调用自身并将次数减1
                else:
                    print("请求失败")
                    return None

    def __get_response_without_proxy(self, url, timeout, header):
        # 无代理请求
        req = urllib.request.Request(url, headers=header)
        print(req)
        resp = urllib.request.urlopen(req, timeout=timeout)
        return resp

    def __get_response_with_proxy(self, url, timeout, header, proxy):
        # 通过代理请求
        proxy_support = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)
        req = urllib.request.Request(url, headers=header)
        resp = urllib.request.urlopen(req, timeout=timeout)
        return resp
