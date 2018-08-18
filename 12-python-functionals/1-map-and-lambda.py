# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem


def fibonacci(n):
    numbers = [0, 1]
    for i in range(2, n):
        numbers.append(numbers[i - 1] + numbers[i - 2])
    return numbers[0:n]


N = int(input())
cubes = list(map(lambda x: x**3, fibonacci(N)))
print(cubes)
