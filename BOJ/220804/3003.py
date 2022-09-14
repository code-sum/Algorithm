# https://www.acmicpc.net/problem/3003

import sys
sys.stdin = open("3003.txt")

a = [1, 1, 2, 2, 2, 8]
c = list(map(int, input().split()))

for i in range(6):
    print(a[i]-c[i], end=' ')