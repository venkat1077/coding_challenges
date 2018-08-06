#!/bin/python

import sys

'''https://www.hackerrank.com/challenges/picking-numbers/problem'''

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
output = {}

a = sorted(a)
for i in range(len(a)-2):
    if a[i] not in output:
        for j in range(i+1, len(a)-1):
            if a[j]-a[i]<=1:
                if a[i] not in output:
                    output[a[i]] = 1
                output[a[i]] += 1

if a[-1] == a[-2]:
    if a[-1] not in output:
        output[a[-1]] = 1
    output[a[-1]] += 1
    
print max(output.values())
