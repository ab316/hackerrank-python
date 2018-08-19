# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem

import xml.etree.ElementTree as etree


def get_attr_number(node):
    sum = len(node.attrib)
    for child in node:
        sum += get_attr_number(child)
    return sum


xml = ''
for _ in range(int(input())):
    xml += input()
    xml += '\n'

tree = etree.ElementTree(etree.fromstring(xml))
print(get_attr_number(tree.getroot()))
