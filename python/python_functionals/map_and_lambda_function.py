"""
Map and Lambda Function
https://www.hackerrank.com/challenges/map-and-lambda-expression

# Input Format

One line of input: an integer N.

# Constraints

0 <= N <= 15

# Output Format

A list on a single line containing the cubes of the first N fibonacci numbers.
"""

n = int(input())
assert 0 <= n <= 15

fib = lambda n: n if n < 2 else fib(n - 1) + fib(n - 2)

print(map(lambda n: n ** 3, map(fib, range(n))))
