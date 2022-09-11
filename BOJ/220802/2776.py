# https://www.acmicpc.net/problem/2776

import sys
sys.stdin = open("2776.txt")

for _ in range(int(input())):
    c1 = int(input())
    n1 = set(map(int, input().split()))

    c2 = int(input())
    n2 = list(map(int, input().split()))

    for i in n2:
        if i in n1:
            print("1")
        else:
            print("0")