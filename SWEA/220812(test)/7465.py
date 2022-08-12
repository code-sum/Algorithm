# 7465 창용 마을 무리의 개수

import sys

sys.stdin = open("_창용마을무리의개수.txt")


# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
T = int(input())

for tc in range(1, T + 1):
    # 둘째 줄에 정점 n, 간선 m
    # 이후 m개의 줄에 걸쳐서 서로를 알고 있는 두 사람의 번호
    n, m = map(int, input().rstrip("\n").split())

    # 무방향 그래프의 인접 행렬
    graph = [[0] * (n+1) for _ in range(n+1)]
    for i in range(m):
        v1, v2 = map(int, input().rstrip("\n").split())
        graph[v1][v2] = 1
        graph[v2][v1] = 1

    # 각 정점을 방문했는지 체크할 visit 리스트 작성
    visit = [0] * (n+1)

    # DFS 함수 정의하기
    def dfs(i):
        visit[i] = 1 # 시작되는 정점은 방문 처리(1 == True)
        for j in range(1, n+1):
            # graph[i][j] 값이 1이고(인접), 방문하지 않았다면 다음 DFS 함수(dfs(j))를 재귀호출
            if graph[i][j] == 1 and visit[j] == 0:
                dfs(j)

    # 방문하지 않은 정점에 대해, DFS 함수를 호출할 때마다 cnt += 1
    # DFS 탐색의 횟수(= 연결된 사람 집단의 갯수)를 구함
    cnt = 0
    for i in range(1, n+1):
        if visit[i] == 0:
            dfs(i)
            cnt += 1

    print('#{} {}'.format(tc, cnt))