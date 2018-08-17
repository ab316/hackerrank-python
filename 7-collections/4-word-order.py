# https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict

n = int(input())
words = OrderedDict()

for _ in range(n):
    w = input()
    if w in words:
        words[w] += 1
    else:
        words[w] = 1

print(len(words))
print(' '.join([str(words[k]) for k in words]))
