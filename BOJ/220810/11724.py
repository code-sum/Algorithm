# https://www.acmicpc.net/problem/11724
# 연결되어 있는 덩어리 갯수 구하기 문제

import sys
sys.stdin = open("11724.txt")

# 첫째 줄에 정점의 개수 N과 간선의 개수 M
N, M = map(int, sys.stdin.readline().rstrip("\n").split())

# DFS를 하기 전에, 일단 탐색을 진행할 그래프가 필요
# N, M 주어질 때, 무방향 그래프의 인접 행렬 만들기
graph = [[0] * (N+1) for _ in range(N+1)]
for i in range(M):
    v1, v2 = map(int, sys.stdin.readline().rstrip("\n").split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

# 각 정점을 방문했는지 여부를 판별할 방문 체크 리스트가 필요
# visit 리스트를 따로 선언하여 각 정점을 방문했는지 체크
visit = [0] * (N+1)

# visit 리스트를 순회하면서 방문하지 않은 노드에 dfs 함수를 호출
# dfs()는 2차원 배열인 graph 에서 행 값을 검사
def dfs(i):
    visit[i] = 1  # 시작되는 정점은 방문 처리(1 == True)
    for j in range(1, N+1):
        # 만약 행 값이 1로 인접(연결)되어 있으면, dfs()를 재귀 호출
        if graph[i][j] == 1 and visit[j] == 0:
            dfs(j)

# 파이썬 함수 재귀 호출
# def hello():
#    print('Hello, world!')
#    hello() 
# hello()
# https://dojang.io/mod/page/view.php?id=2352

# visit 리스트를 방문할 때, 0값으로 dfs 함수를 호출할 때마다 cnt 를 1씩 증가
cnt = 0
for i in range(1, N+1):
    if visit[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)