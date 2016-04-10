"""
Find the Second Largest Number
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/

# Input Format

The first line contains N. The second line contains an array A[] of N integers each separated by a space.

# Constraints

2 <= N <= 10
-100 <= A[i] <= 100

# Output Format

Output the value of the second largest number.
"""

def get_n():
    n = int(input())
    assert 2 <= n <= 10
    return n


def get_list(n):
    l = input()
    return list(map(int, l.split(' ')))


n = get_n()
l = get_list(n)
max_num = max(l)

print(max([i for i in l if i != max_num]))
