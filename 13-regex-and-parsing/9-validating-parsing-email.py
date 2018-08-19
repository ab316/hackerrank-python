# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import email.utils
import re

for _ in range(int(input())):
    name, address = email.utils.parseaddr(input())
    if re.match(r'[a-zA-Z][\w.\-_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$', address):
        print(email.utils.formataddr((name, address)))
