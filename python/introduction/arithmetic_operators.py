"""
Arithmetic Operators
https://www.hackerrank.com/challenges/python-arithmetic-operators

# Task
Read two integers from STDIN and print three lines where:

1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers.

# Input Format
The first line contains the first integer, a. The second line contains the second integer, b.

# Constraints
1 <= a <= 10 ** 10
1 <= b <= 10 ** 10
"""

def get_input():
    num = int(input())
    assert 1 <= num <= 10 ** 10
    return num

a, b = get_input(), get_input()

print(a + b)
print(a - b)
print(a * b)
