# coding:utf8

"""
crawler main function, call for other function
Created on 2015-12-31
"""

from http.client import UnknownProtocol

from urllib import request, error, parse


class HtmlDownload(object):
    # 实现下载器类

    @staticmethod
    def download(url):
        # 下载网页

        if url is None:
            return None

        url = parse.quote(url, safe='/:?=')
        print(url)
        try:
            response = request.urlopen(url, timeout=2)
            if response.status != 200:
                print("Failed:%s, status:%s" % url, response.status)
                return None
            else:
                result = response.read()
                print("这是获取到的html--------")
                print(result)
                return result
        except UnknownProtocol as sp:
            print(sp)
            return None
        except error.HTTPError as e:
            print(e)
            return None

