# https://www.acmicpc.net/problem/1652

# 답은 계속 도출되는데 왜 백준 사이트에서는 런타임에러(NameError) 뜨지?

import sys
# sys.stdin = open("1652.txt")

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
N = int(sys.stdin.readline())

matrix = []
for _ in range(N):
    matrix.append(list(sys.stdin.readline()))

# row_cnt 세기
row_cnt = 0
for i in range(N):
    for j in range(len(matrix)):
        if matrix[i][j] == '.' and matrix[i][j+1] == '.':
            row_cnt += 1
            break

#col_cnt 세기
col_cnt = 0
for c in range(len(matrix)):
    for r in range(0, N-1):
        if matrix[r][c] == '.' and matrix[r+1][c] == '.':
            col_cnt += 1
            break

print(row_cnt, col_cnt)