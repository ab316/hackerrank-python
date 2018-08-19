# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem


def wrapper(f):
    def fun(l):
        new_list = ['+91 {0} {1}'.format(n[-10:-5], n[-5:]) for n in l]
        return f(new_list)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


l = [input() for _ in range(int(input()))]
sort_phone(l)
