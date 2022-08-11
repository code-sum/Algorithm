# https://www.acmicpc.net/problem/1100

import sys
sys.stdin = open("1100.txt")

matrix = []
for _ in range(8):
    matrix.append(list(input()))

cnt = 0
for i in range(8):
    for j in range(8):
        if matrix[i][j] == 'F' and (i + j) % 2 == 0:
            cnt += 1

print(cnt)