# https://www.hackerrank.com/challenges/designer-door-mat/problem

N, M = map(int, input().split())

for i in range(1, N // 2 + 1):
    print(('.|.' * (2 * i - 1)).center(M, '-'))

print("WELCOME".center(M, '-'))

for i in range(N // 2, 0, -1):
    print(('.|.' * (2 * i - 1)).center(M, '-'))
