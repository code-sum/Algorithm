# https://www.acmicpc.net/problem/1546

import sys
sys.stdin = open("1546.txt")

n = int(input())
scores = list(map(int, input().split()))
scores2 = []

for i in scores:
    scores2.append((i/max(scores))*100)
print(sum(scores2)/n)