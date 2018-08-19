# https://www.hackerrank.com/challenges/validate-a-roman-number/problem

import re

regex_pattern = r"M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"
print(str(bool(re.match(regex_pattern, input()))))
