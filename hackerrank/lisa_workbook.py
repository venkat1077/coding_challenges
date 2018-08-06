# Enter your code here. Read input from STDIN. Print output to STDOUT

'''https://www.hackerrank.com/challenges/lisa-workbook/problem'''

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
chapters = map(int,raw_input().strip().split(' '))

page_num = 1
special_case = 0
for chap_len in chapters:
    for i in range(1, chap_len+1):
        if i == page_num:
            special_case += 1
        if (i%k) == 0:
            page_num += 1
    if (chap_len%k) != 0:
        page_num += 1

print special_case
    
