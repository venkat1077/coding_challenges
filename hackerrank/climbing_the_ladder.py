#!/bin/python

import bisect

'''https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem'''

n = int(raw_input().strip())
scores = map(int,raw_input().strip().split(' '))
m = int(raw_input().strip())
alice = map(int,raw_input().strip().split(' '))
# your code goes here
scores = sorted(list(set(scores)))
for val in alice:
    length = len(scores)
    lo = 0
    while lo < length:
        mid = (lo+length)//2
        if scores[mid] <= val:
            lo = mid+1
        else:
            length = mid
    print len(scores)-lo+1

