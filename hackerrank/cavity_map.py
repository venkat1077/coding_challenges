#!/bin/python

import sys

'''https://www.hackerrank.com/challenges/cavity-map/problem'''


n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
    grid_t = str(raw_input().strip())
    grid.append(grid_t)

for line_pos in range(1,len(grid)-1):
    for word_pos in range(1,len(grid[line_pos])-1):
        if all([
                grid[line_pos][word_pos]>grid[line_pos][word_pos-1],
                grid[line_pos][word_pos]>grid[line_pos][word_pos+1],
                grid[line_pos][word_pos]>grid[line_pos-1][word_pos],
                grid[line_pos][word_pos]>grid[line_pos+1][word_pos]
               ]):
            grid[line_pos] = grid[line_pos][:word_pos] + "X" + grid[line_pos][word_pos+1:]
for line in grid:
    print line
