# coding:utf8

"""
crawler main function, call for other function
Created on 2015-12-31
"""


class HtmlOutput(object):

    def __init__(self):
        # 设置一个列表保存数据
        self.data = []

    def collect_data(self, data):
        if data is None:
            return
        self.data.append(data)

    def output_html(self):
        with open("output.html", "w", encoding="utf-8") as fout:
            fout.write("<html>")
            fout.write("<head>")
            # 添加页面头标签中的编码格式
            fout.write('<meta http-equiv="content-type" content="text/html;charset=utf-8">')
            fout.write("<body>")
            fout.write("<table>")

            for data in self.data:
                fout.write("<tr>")
                fout.write(data)

                """ 
                print("\n**********\n") 
                print(data['title']) 
                print(data['title'].encode('utf-8')) 
                print(data['title'].encode('utf-8').decode(encoding='utf-8')) 
                print("\n**********\n") 
                """

                fout.write("</tr>")

            fout.write("</table>")
            fout.write("</body>")
            fout.write("</head>")
            fout.write("</html>")
