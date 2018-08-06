#!/bin/python

from __future__ import print_function

import os
import sys

'''https://www.hackerrank.com/challenges/birthday-cake-candles/problem'''

def birthdayCakeCandles(n, ar):
    max_value = max(ar)
    size = 0
    for val in ar:
        if val == max_value:
            size += 1
    print (size)

if __name__ == '__main__':
    n = int(raw_input())
    ar = map(int, raw_input().rstrip().split())
    result = birthdayCakeCandles(n, ar)


