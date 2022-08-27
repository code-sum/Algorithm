# https://www.acmicpc.net/problem/7785

import sys
sys.stdin = open("7785.txt")

t = int(sys.stdin.readline())
ans = {}

for _ in range(t):
    name, record = sys.stdin.readline().split()

    if record == "enter":
        ans[name] = 1
    else:
        del ans[name]

ans = sorted(ans.keys(), reverse=True)

for i in ans:
    print(i)