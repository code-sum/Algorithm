# https://www.acmicpc.net/problem/2606

import sys
sys.stdin = open("2606.txt")

# 첫째줄에 컴퓨터의 수(노드)
n = int(input())

# 둘째줄에 직접 연결된 컴퓨터 쌍의 수(간선)
m = int(input())

# 이어서 한 줄에 한 쌍씩 직접 연결된 컴퓨터 번호 쌍 입력
# 입력된 쌍을 매트릭스 g 에 표현하기
g = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    v1, v2 = map(int, input().split())
    g[v1][v2] = 1
    g[v2][v1] = 1

# 각 정점을 방문했는지 여부 판별할 체크리스트 visit 선언
visit = [0]*(n+1)

def dfs(i):
    visit[i] = 1  # 시작되는 정점 방문 처리(1==True)
    for j in range(n+1):
        if g[j][i] == 1 and visit[j] == 0:
            dfs(j)

# 1번 컴퓨터가 감염
dfs(1)

# 1번 컴퓨터 제외하고 감염된 나머지 컴퓨터의 수 출력
print(sum(visit)-1)
