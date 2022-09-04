# https://www.acmicpc.net/problem/5576

import sys
sys.stdin = open("5576.txt")

W = sorted([int(input())for _ in range(10)])[7:]
K = sorted([int(input())for _ in range(10, 20)])[7:]

print(sum(W), sum(K))