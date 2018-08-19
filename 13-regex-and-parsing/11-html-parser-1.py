# https://www.hackerrank.com/challenges/html-parser-part-1/problem

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for att in attrs:
            print('-> {0} > {1}'.format(att[0], att[1]))

    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        for att in attrs:
            print('-> {0} > {1}'.format(att[0], att[1]))

    def handle_endtag(self, tag):
        print('End   :', tag)


parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
