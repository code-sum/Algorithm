# https://www.acmicpc.net/problem/1236

import sys
sys.stdin = open("1236.txt")

# 문제에서는 모든 행과 모든 열에 1명 이상
# 경비원을 둬야 한다고 했음!

n, m = map(int, input().split())
matrix = []

for _ in range(n):
    matrix.append(input())

row_cnt, col_cnt = 0, 0

# 경비원이 없는 행의 개수 탐색
for i in range(n):
    if 'X' not in matrix[i]:
        row_cnt += 1

# 경비원이 없는 열의 개수 탐색
for j in range(m):
    if 'X' not in [matrix[i][j] for i in range(n)]:
        col_cnt += 1

# 행과 열을 모두 탐색했을 때, 경비원은 가장 많이 필요한 쪽에 맞춰서
# 그 수만큼 배치해야함 = row_cnt 와 col_cnt 중에 max 구하기
print(max(row_cnt, col_cnt))