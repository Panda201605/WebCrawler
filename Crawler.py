import urllib.request

url = "http://bbs.fobshanghai.com/thread-6948535-1-1.html"
data = urllib.request.urlopen(url).read()
data = data.decode('gbk')
print(data)
