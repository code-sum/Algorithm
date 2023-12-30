# https://www.acmicpc.net/problem/2751

import sys

n = int(input())
list_ = []
for i in range(n):
    list_.append(int(sys.stdin.readline()))

sorted = sorted(list_)
for j in sorted:
    print(j)