import urllib.request
import re
import chardet


def fetch(url):
    data = urllib.request.urlopen(url).read()
    encode = chardet.detect(data)['encoding']
    print(encode)
    html = data.decode(encode)
    doneset.add(url)
    print(html)
    return html


def get_email(data):
    pattern = re.compile(r"[a-zA-Z0-9]{1,36}@[a-zA-Z0-9]{1,36}")
    emails = re.findall(pattern, data)
    for e in emails:
        emailset.add(e)
    print("邮箱：")
    print(emailset)


def get_url(data):
    pattern = re.compile(r'[a-zA-z]+://[^\s]*')
    urls = re.findall(pattern, data)
    print("链接：")
    for u in urls:
        index = u.find("\"")
        u = u[0:index]
        index = u.find("'")
        u = u[0:index]
        todoset.add(u)
        print(u)

if __name__ == '__main__':
    doneset = set()
    todoset = set()
    emailset = set()

    first = "http://bbs.fobshanghai.com/thread-6938169-1-1.html"
    result = fetch(first)
    get_email(result)
    get_url(result)
    while len(todoset) > 0:
        todourl = todoset.pop()
        result = fetch(todourl)
        get_email(result)
        get_url(result)
