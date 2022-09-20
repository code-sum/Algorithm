# https://www.acmicpc.net/problem/9093

import sys
sys.stdin = open("9093.txt")

t = int(input())

for i in range(1, t+1):

    a = []
    input_ = list(map(str, input().split()))

    for j in input_:
        a.append(j[::-1])

    print(*a)
