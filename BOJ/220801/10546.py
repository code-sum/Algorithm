# https://www.acmicpc.net/problem/10546

import sys
from collections import defaultdict

sys.stdin = open("10546.txt")

n = int(input())

ans = defaultdict(int)

for _ in range(n):
    input_ = input().rstrip()
    ans[input_] += 1

for _ in range(n-1):
    fin_ = input().rstrip()
    ans[fin_] -= 1

for k, v in ans.items():
    if v == 1:
        print(k)