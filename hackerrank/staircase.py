#!/bin/python

from __future__ import print_function

import os
import sys

'''https://www.hackerrank.com/challenges/staircase/problem'''

def staircase(n):
    for val in range(1, n+1):
        sub1 = " " * (n-val)
        sub2 = "#" * val
        print ("{}{}".format(sub1, sub2))

if __name__ == '__main__':
    n = int(raw_input())
    staircase(n)
