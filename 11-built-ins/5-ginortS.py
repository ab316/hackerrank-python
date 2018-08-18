# https://www.hackerrank.com/challenges/ginorts/problem

S = input()


def sort_key(s: str):
    if s.islower():
        return ord(s) - ord('a')
    elif s.isupper():
        return ord(s) - ord('A') + 26
    elif s.isdigit():
        if int(s) % 2:
            return ord(s) - ord('0') + 26 + 26
        else:
            return ord(s) - ord('0') + 26 + 26 + 10


print(''.join(sorted(S, key=sort_key)))
