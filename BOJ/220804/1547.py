# https://www.acmicpc.net/problem/1547

import sys
sys.stdin = open("1547.txt")

t = int(input())

# 공이 있는 자리 ans
ans = 1

for _ in range(1, t+1):
    a, b = map(int, input().split())
    if a == ans:
        ans = b
    elif b == ans:
        ans = a
    else:
        continue
print(ans)
