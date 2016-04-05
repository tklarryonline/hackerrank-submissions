"""
Loops
https://www.hackerrank.com/challenges/python-loops

# Task
Read an integer N. For all non-negative integers i < N, print i ** 2. See the sample for details.

# Input Format
The first and only line contains the integer, N.

# Constraints
1 <= N <= 20

# Output Format
Print N lines, one corresponding to each i.
"""

def print_squared(n):
    assert isinstance(n, int)
    assert 1 <= n <= 20

    for i in range(n):
        print(i ** 2)


n = int(input())
print_squared(n)
