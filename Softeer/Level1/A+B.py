# https://softeer.ai/practice/info.do?idx=1&eid=362

import sys

T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a+b}')