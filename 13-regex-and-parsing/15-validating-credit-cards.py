# https://www.hackerrank.com/challenges/validating-credit-card-number/problem

import re

for _ in range(int(input())):
    card = input()
    correct_shape = bool(re.match(r'^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}$', card))
    no_4_consecutive_repetition = len(re.findall(r'(\d)\1{3}', card.replace('-', ''))) == 0
    valid = correct_shape and no_4_consecutive_repetition
    print('Valid' if valid else 'Invalid')
