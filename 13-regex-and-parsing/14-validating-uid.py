# https://www.hackerrank.com/challenges/validating-uid/problem

import re

for _ in range(int(input())):
    uid = input()
    two_uppercase = len(re.findall(r'[A-Z]', uid)) >= 2
    three_digits = len(re.findall(r'[\d]', uid)) >= 3
    alpha_num = uid.isalnum()
    no_rep = len(re.findall(r'(.).*\1+', uid)) == 0
    length_10 = len(uid) == 10
    valid = two_uppercase and three_digits and alpha_num and no_rep and length_10
    print('Valid' if valid else 'Invalid')
