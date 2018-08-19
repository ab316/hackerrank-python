# https://www.hackerrank.com/challenges/html-parser-part-2/problem

import re
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)

    def handle_comment(self, data):
        if data.find('\n') != -1:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
