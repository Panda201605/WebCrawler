# coding:utf8

"""
crawler main function, call for other function
Created on 2015-12-31
"""

# 导入urllib（python3特有）
from urllib import request


class HtmlDownload(object):
    # 实现下载器类

    @staticmethod
    def download(url):
        # 下载网页

        if url is None:
            return None

        with request.urlopen(url) as response:
            if response.status != 200:
                return None
            else:
                return response.read()
