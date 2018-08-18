# https://www.hackerrank.com/challenges/any-or-all/problem

N = int(input())
lst = list(map(int, input().split()))

positive = list(map(lambda x: x > 0, lst))
palindromic = list(map(lambda x: str(x) == str(x)[::-1], lst))
print(all([all(positive), any(palindromic)]))
