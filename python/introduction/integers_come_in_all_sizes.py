"""
Integers Come In All Sizes
https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes

# Task
Read four numbers, a, b, c, and d, and print the result of a ** b + c ** d

# Input Format
Integers a, b, c, and d are given on four separate lines, respectively.

# Constraints
1 <= a <= 1000
1 <= b <= 1000
1 <= c <= 1000
1 <= d <= 1000

# Output Format
Print the result of a ** b + c ** d on one line.
"""

def get_input():
    num = int(input())
    assert 1 <= num <= 10 ** 3
    return num

a, b, c, d = get_input(), get_input(), get_input(), get_input()

print(a ** b + c ** d)
