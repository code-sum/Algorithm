# https://www.acmicpc.net/problem/1652

# 답은 계속 도출되는데 왜 백준 사이트에서는 런타임에러(NameError) 뜨지?

import sys
sys.stdin = open("1652.txt")

'''
5
....X
..XX.
.....
.XX..
X....
5 4
'''

# 첫째 줄에 방의 크기 N이 주어진다.
n = int(input())

matrix = []
r, c = 0, 0
cnt = 0

# input 받기
for _ in range(n):
    matrix.append(list(input()))

# 가로 누울 자리 세기
for i in range(n):
    cnt = 0
    for j in range(n):
        if matrix[i][j] == ".":
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            r += 1

# 세로 누울 자리 세기
for i in range(n):
    cnt = 0
    for j in range(n):
        if matrix[j][i] == ".":
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            c += 1

print(r, c)