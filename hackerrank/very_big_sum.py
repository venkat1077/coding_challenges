#!/bin/python

import sys

'''https://www.hackerrank.com/challenges/a-very-big-sum/problem'''

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
sum = 0
for val in arr:
    sum += val

print sum
