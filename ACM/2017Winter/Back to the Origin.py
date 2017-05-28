#!/bin/python3
#https://www.hackerrank.com/contests/codeagon/challenges/back-to-origin
import sys


xTreasure,yTreasure = input().strip().split(' ')
xTreasure,yTreasure = [int(xTreasure),int(yTreasure)]
n = int(input().strip())
direction = []
for direction_i in range(n):
   direction_t = [int(direction_temp) for direction_temp in input().strip().split(' ')]
   direction.append(direction_t)
direction = direction[::-1]
for i in range(len(direction)):
    xTreasure = xTreasure - direction[i][0]
    yTreasure = yTreasure - direction[i][1]
print(xTreasure, yTreasure)
