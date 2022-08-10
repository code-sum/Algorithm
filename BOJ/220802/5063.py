# https://www.acmicpc.net/problem/5063

import sys
sys.stdin = open("5063.txt")

# 각 케이스의 수를 입력
n = int(input())

for i in range(n):
    cases = list(map(int, input().split()))

    if cases[1] - cases[2] > cases[0]:
        print("advertise")
    elif cases[1] - cases[2] < cases[0]:
        print("do not advertise")
    elif cases[1] - cases[2] == cases[0]:
        print("does not matter")