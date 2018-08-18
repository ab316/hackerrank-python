# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

import re


def fun(s):
    # return True if s is a valid email, else return False
    regex = '^[a-zA-Z0-9_\-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{1,3}$'
    return re.match(regex, s) is not None


def filter_mail(emails):
    return list(filter(fun, emails))


n = int(input())
emails = []
for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)