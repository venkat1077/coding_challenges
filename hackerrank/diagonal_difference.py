#!/bin/python

import sys

'''https://www.hackerrank.com/challenges/diagonal-difference/problem'''

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

sum1 = 0
sum2 = 0
length = len(a)
for index in range(length):
    sum1 += a[index][index]
    sum2 += a[index][length-1-index]

print abs(sum1-sum2)
