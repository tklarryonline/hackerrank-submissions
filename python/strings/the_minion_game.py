"""
The Minion Game
https://www.hackerrank.com/challenges/the-minion-game

Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

# Scoring
A player gets +1 point for each occurrence of the substring in the string SS.

# Input Format

A single line of input containing the string S.
Note: The string S will contain only uppercase letters: [A−Z].

# Constraints

0 <= len(S) <= 10 ** 6

# Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

# Note

Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.
"""

VOWELS = 'AEIOU'


input_str = input().strip().upper()
input_len = len(input_str)
assert 0 <= input_len <= 10 ** 6

total_possible_combinations = (input_len + 1) * input_len / 2

# Finds K's score
kev = 0
for i, char in enumerate(input_str):
    if char in VOWELS:
        kev += (input_len - i)

stu = total_possible_combinations - kev

if kev > stu:
    print('Kevin', kev)
elif kev < stu:
    print('Stuart', stu)
else:
    print('Draw')
