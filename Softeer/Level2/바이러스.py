# https://softeer.ai/practice/info.do?idx=1&eid=407

import sys

k, p, n = map(int, input().split())

# 바이러스 k마리가 1초당 p배씩 증가

for i in range(n):
    k = (k * p) % 1000000007

print(k)