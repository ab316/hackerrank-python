# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re

matches = re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]([aeiouAEIOU]{2,})(?=[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])', input())
print('\n'.join(matches if matches else ['-1']))
