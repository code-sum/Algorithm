# https://www.acmicpc.net/problem/4396

import sys

sys.stdin = open("4396.txt")

n = int(input())

graph1 = list(input() for _ in range(n))
graph2 = list(input() for _ in range(n))
ans = [["."] * n for _ in range(n)]

# 열린 칸 주변에 지뢰가 몇 개 있는지 알기 위해, 해당 위치에서 8방향 탐색
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


def findBoom():
    for i in range(n):
        for j in range(n):

            if graph1[i][j] == "." and graph2[i][j] == "x":  # 지뢰가 없으면서 열린 칸
                boom = 0
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:  # 리스트 좌표 벗어났을때
                        continue

                    if graph1[nx][ny] == "*":
                        boom += 1
                ans[i][j] = boom  # 31번 절의 조건을 통과하지 않아도 boom 적용

            if graph1[i][j] == "*" and graph2[i][j] == "x":  # 지뢰가 있는 칸이 열렸다면
                makeFail()


def makeFail():
    global ans
    for i in range(n):
        for j in range(n):
            if graph1[i][j] == "*":  # 첫번째 입력 중 지뢰가 있는 칸이면
                ans[i][j] = "*"  # 지뢰가 있는 모든 칸을 별표로 표시


findBoom()
for i in range(n):
    for j in range(n):
        print(ans[i][j], end="")
    print()
