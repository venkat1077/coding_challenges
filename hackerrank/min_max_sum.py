#!/bin/python

from __future__ import print_function

import os
import sys

'''https://www.hackerrank.com/challenges/mini-max-sum/problem'''

def miniMaxSum(arr):
    total = sum(arr)
    min_val = sum(arr[:-1])
    max_val = sum(arr[:-1])
    for val in arr:
        temp = total - val
        if temp < min_val:
            min_val = temp
        elif temp > max_val:
            max_val = temp
    print ("{} {}".format(min_val, max_val))

if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())
    miniMaxSum(arr)
