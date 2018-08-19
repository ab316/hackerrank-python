# https://www.hackerrank.com/challenges/re-group-groups/problem

import re

result = re.search(r'([a-zA-Z0-9])\1+', input())
print(result.group()[0] if result else -1)
