#!/bin/python

import sys

'''https://www.hackerrank.com/challenges/fair-rations/problem'''

N = int(raw_input().strip())
B = map(int,raw_input().strip().split(' '))

total_loaves = 0
for i in range(len(B)-1):
    if B[i]%2!=0:
        B[i] += 1
        B[i+1] += 1
        total_loaves +=2

if B[-1]%2 != 0:
    print "NO"
else:
    print total_loaves
