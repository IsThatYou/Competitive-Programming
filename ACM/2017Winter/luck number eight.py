# unfinished
# unfinished
# https://www.hackerrank.com/contests/w28/challenges/lucky-number-eight
n = int(input())
number = int(input())
for i in range(n):
    index = n-i-1
    interested = number[index]
    if interested % 2 == 0:
        array = []
        for j in range(index):
            numb = j + 1
            equation =