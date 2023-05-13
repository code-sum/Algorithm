# https://www.acmicpc.net/problem/10950

import sys
sys.stdin = open("10950.txt")

t = int(input())

for _ in range(t):
    a,b = map(int, input().split())
    print(a+b)