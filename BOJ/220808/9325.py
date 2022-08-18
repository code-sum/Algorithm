# https://www.acmicpc.net/problem/9325

'''
2
10000
2
1 2000
3 400
50000
0
'''

import sys
sys.stdin = open("9325.txt")

n = int(input())

for _ in range(n):
    s = int(input())
    n = int(input())

    total_price = s
    for i in range(n):
        q, p = map(int, input().split())
        total_price += q*p
    print(total_price)