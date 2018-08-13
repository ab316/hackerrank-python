# https://www.hackerrank.com/challenges/python-mutations/problem


def mutate_string(string, position, character):
    return string[0:position] + character + string[position+1:]


S = input()
i, c = input().split()
i = int(i)

print(mutate_string(S, i, c))

