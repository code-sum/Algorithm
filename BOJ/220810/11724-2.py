# https://www.acmicpc.net/problem/11724
# 연결되어 있는 덩어리 갯수 구하기 문제

import sys
sys.stdin = open("11724.txt")

N, M = map(int, sys.stdin.readline().rstrip("\n").split())

graph = [[0] * (N+1) for _ in range(N+1)]
for i in range(M):
    v1, v2 = map(int, sys.stdin.readline().rstrip("\n").split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

visit = [0] * (N+1)

def dfs(i):
    visit[i] = 1
    for j in range(1, N+1):
        if graph[i][j] == 1 and visit[j] == 0:
            dfs(j)

cnt = 0
for i in range(1, N+1):
    if visit[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)