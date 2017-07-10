# coding:utf8

"""
crawler main function, call for other function
Created on 2015-12-31
"""
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup


# 实现解析器的类
class HtmlParse(object):
    @staticmethod
    def _get_new_urls(page_url, soup):
        # 从网页解析中获得url

        new_urls = set()
        # 匹配/view/123.htm形式的url，得到所有的词条url
        links = soup.find_all("a", href=re.compile(r".*"))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)

        return new_urls

    @staticmethod
    def _get_new_data(page_url, soup):
        # 从网页解析中获得数据

        # 存储数据的集合
        res_data = []

        # 根据页面的特征，获取邮箱
        email_regexp = re.compile("\w+@\w+\.\w+")
        emails = soup.find_all(text=email_regexp)

        # 保存邮箱地址
        res_data.append(emails)

        """ 
        print("这是res——data：\n") 
        print(res_data)
        """
        return res_data

    def parse(self, page_url, html_content):
        # 解析网页

        if page_url is None or html_content is None:
            return

        # 使用beautifulsoup进行解析
        soup = BeautifulSoup(html_content, "html.parser", from_encoding="utf-8")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        """ 
        print("parser----------new_urls:\n") 
        print(new_urls) 
        print("parser----------new_data:\n") 
        print(new_data) 
        """
        return new_urls, new_data
