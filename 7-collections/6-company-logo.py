# https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter


# Does not work on hackerrank's python version as of 17 Aug 18
# c = Counter(sorted(input()))
# for (k, v) in c.most_common(3):
#     print(k, v)


c = Counter(sorted(input()))
ranking = list(reversed(sorted(c.items(), key=lambda x: x[1]*26 - (ord(x[0]) - ord('a')))))
for (k, v) in ranking[0:3]:
    print(k, v)
