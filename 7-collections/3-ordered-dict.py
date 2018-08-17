# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

N = int(input())
items = OrderedDict()

for _ in range(N):
    *nameList, str_price = input().split()
    name = ' '.join(nameList)
    price = int(str_price)
    if name in items:
        items[name] += price
    else:
        items[name] = price

for k in items.keys():
    print(k, items[k])
