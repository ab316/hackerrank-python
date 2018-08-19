# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import re
import numpy


def fix_print(x):
    print(re.sub(r'(\d+\.)', r' \1', str(x)))


narr = numpy.array(input().split(), float)
fix_print(numpy.floor(narr))
fix_print(numpy.ceil(narr))
fix_print(numpy.rint(narr))
