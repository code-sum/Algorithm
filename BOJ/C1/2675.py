# https://www.acmicpc.net/problem/2675

import sys
sys.stdin = open("2675.txt")

t = int(input())

for _ in range(t):
    num, char = input().split()
    new_num = int(num)

    ans = []
    for i in char:
        ans.append(i*new_num)
    print(*ans, sep='')