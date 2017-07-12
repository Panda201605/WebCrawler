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
    def __get_new_urls(self, page_url, soup):
        # 从网页解析中获得url

        new_urls = set()
        # 匹配/view/123.htm形式的url，得到所有的词条url
        links = soup.find_all("a", href=re.compile(r"^(http://bbs.fobshanghai.com).*"))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)

        return new_urls

    def __get_new_data(self, soup):
        # 从网页解析中获得数据

        # 根据页面的特征，获取邮箱
        email_regexp = re.compile(r"^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+")
        emails = soup.find_all(text=email_regexp)

        # 保存邮箱地址
        res_data = set(emails)

        print("这是res——data：\n")
        print(res_data)

        return res_data

    def parse(self, page_url, html_content):
        # 解析网页，获取邮箱及其他网址

        if page_url is None or html_content is None:
            return

        # 使用beautifulsoup进行解析
        soup = BeautifulSoup(html_content, "html.parser", from_encoding="utf-8")
        new_urls = self.__get_new_urls(page_url, soup)
        new_data = self.__get_new_data(soup)

        print("parser----------new_urls:\n")
        print(new_urls)
        print("parser----------new_data:\n")
        print(new_data)

        return new_urls, new_data

    def parse_ip(self, html_response):

        # 存储数据的集合
        res_data = set()
        # 使用beautifulsoup进行解析
        soup = BeautifulSoup(html_response, "html.parser", from_encoding="utf-8")
        table = soup.find('table', attrs={'id': 'ip_list'})
        tr = table.find_all('tr')[2:]

        # 解析得到代理ip的地址，端口，和类型
        for item in tr:
            tds = item.find_all('td')
            temp_str = "%s:%s" % (tds[1].get_text().lower(), tds[2].get_text().lower())
            proxy = {tds[5].get_text().lower(): temp_str}
            res_data.add(repr(proxy))
        return res_data
