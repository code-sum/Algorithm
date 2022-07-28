# https://www.acmicpc.net/problem/10952

import sys
sys.stdin = open("10952_input.txt")

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(A+B)