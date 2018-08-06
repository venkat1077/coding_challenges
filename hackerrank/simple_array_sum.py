#!/bin/python

import sys

''' https://www.hackerrank.com/challenges/simple-array-sum/problem '''

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

sum = 0
for val in arr:
    sum = sum + val
print sum
