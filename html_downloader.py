# coding:utf8

''''' 
crawler main function, call for other function 
 
Created on 2015-12-31 
 
'''
# 导入urllib（python3特有）
from urllib import request

# 实现下载器类
class HtmlDownload(object):

    # 下载网页
    def download(self, url):
        if url is None:
            return None

        with request.urlopen(url) as response:
            if response.status != 200:
                return None
            else:
                return response.read()