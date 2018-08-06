#!/bin/python

from __future__ import print_function

import os
import sys

'''https://www.hackerrank.com/challenges/time-conversion/problem'''

def timeConversion(s):
    values = s.split(':')
    meridian = values[2][-2:]
    hour = values[0]
    if meridian.strip().upper() == "PM" and int(hour) < 12:
        values[0] = str(int(values[0])+12)
    elif meridian.strip().upper() == "AM" and int(hour) == 12:
        values[0] = '00'
    print (values[0] + ":" + values[1] + ":" + values[2][:-2])

if __name__ == '__main__':
    s = raw_input()
    result = timeConversion(s)
