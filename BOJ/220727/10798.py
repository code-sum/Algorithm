# https://www.acmicpc.net/problem/10798

import sys
sys.stdin = open("10798.txt")

# 매트릭스 세로 탐색해서
# 나오는 요소들을 빈 리스트에 붙이기
# if 매트릭스 요소가 공백(*)이면:
# continue

ans = [["*"]*15 for i in range(5)]
for i in range(5):
    a = list(input())
    a_len = len(a)

    for j in range(a_len):
        ans[i][j] = a[j]

# 세로 탐색
for i in range(15):
    for j in range(5):
        if ans[j][i] == "*":
            continue
        else:
            print(ans[j][i], end='')
