# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for att in attrs:
            print('-> {0} > {1}'.format(att[0], att[1]))

    def handle_starttag(self, tag, attrs):
        print(tag)
        for att in attrs:
            print('-> {0} > {1}'.format(att[0], att[1]))


parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
