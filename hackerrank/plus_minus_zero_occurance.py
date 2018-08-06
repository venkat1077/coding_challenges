#!/bin/python

import sys

'''https://www.hackerrank.com/challenges/plus-minus/problem'''

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

r1 = r2 = r3 = 0

for val in arr:
    if val > 0:
        r1 += 1
    elif val < 0:
        r2 += 1
    else:
        r3 += 1

l = len(arr)
print "%.6f" %(r1/float(l))
print "%.6f" %(r2/float(l))
print "%.6f" %(r3/float(l))
