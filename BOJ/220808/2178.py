# https://www.acmicpc.net/problem/2178

from collections import deque
import sys

sys.stdin = open("2178.txt")

n, m = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(n)]

visit = [[False] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]  # 거리 +1 씩, 마지막에 출력할 매트릭스
queue = deque()
queue.append((0, 0))  # 시작점
dist[0][0] = 1  # 시작점 거리는 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:  # 그래프 벗어나지 않도록 범위 설정
            if (
                visit[nx][ny] == False and matrix[nx][ny] == 1
            ):  # 방문노드가 아니고, matrix에 1이 있는위치면 위치 변경
                queue.append((nx, ny))
                dist[nx][ny] += dist[x][y] + 1  # dist에서 x, y는 1이므로, +1 늘려줌 (2)
                visit[nx][ny] = True  # 방문처리

print(dist[n - 1][m - 1])  # n, m 은 갯수이므로 행렬에서는 -1씩
