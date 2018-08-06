#!/bin/python

import sys

'''https://www.hackerrank.com/challenges/flatland-space-stations/problem'''

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
c = map(int,raw_input().strip().split(' '))

if n == m:
    print 0
else:
    c = sorted(c)
    if len(c)==1:
        max_delta=c[0]
    else:
        max_delta = max(abs(x - y) for (x, y) in zip(c[1:], c[:-1]))
    max_path = max_delta/2
    if 0 not in c and c[0] > max_path:
        max_path = c[0]
    if n-1 not in c and n-1-c[-1] > max_path:
        max_path = n-c[-1]-1
    print max_path
