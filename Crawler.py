import urllib.request
import re


def fetch(url):
    data = urllib.request.urlopen(url).read()
    html = data.decode('gbk')
    print(html)
    return html


def get_email(data):
    pattern = re.compile(r"[a-zA-Z0-9]{1,36}@[a-zA-Z0-9]{1,36}")
    emails = re.findall(pattern, data)
    print("邮箱：")
    print(emails)


def get_url(data):
    pattern = re.compile(r'[a-zA-z]+://[^\s]*')
    urls = re.findall(pattern, data)
    print("链接：")
    for u in urls:
        index = u.find("\"")
        u = u[0:index]
        index = u.find("'")
        u = u[0:index]
        print(u)

if __name__ == '__main__':
    first = "http://bbs.fobshanghai.com/thread-6938169-1-1.html"
    result = fetch(first)
    get_email(result)
    get_url(result)
