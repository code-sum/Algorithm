# https://www.acmicpc.net/problem/2644

# 스택으로 푸는 방법(수업)도 정리하기!

# 입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 
# 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 
# 이때에는 -1을 출력해야 한다.

import sys
sys.stdin = open("2644.txt")

# 첫째 줄에는 전체 사람의 수 N(정점의 수)
N = int(input())

# 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람 start, end
start, end = map(int, input().split())

# 셋째 줄에는 부모 자식들 간의 관계의 개수 M(간선의 수)
M = int(input())

# [무방향 그래프의 인접 리스트 만들기]
# 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x, y가 각 줄에 나온다. 
# 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())  
    graph[x].append(y)
    graph[y].append(x)

# 각 정점을 방문했는지 여부를 판별할 방문 체크 리스트가 필요
# visit 리스트를 따로 선언하여 각 정점을 방문했는지 체크
visit = [0] * (N+1)

# [DFS 함수 정의하기]
result = []
def dfs(v, num):  # 매개변수 v, num에 대하여
    num += 1      # 깊이가 깊어질 때마다 num 값 1씩 증가
    visit[v] = 1  # 시작되는 정점은 방문 처리(1 == True)

    # v == end 일땐 num 값을 result 에 저장
    if v == end:
        result.append(num)

    # 매개변수 v와 연결된 사람들에 대하여 순회할 때,
    for i in graph[v]:

        # visit[i] 결과가 False(= 0) 이면, dfs()를 재귀 호출
        if not visit[i]:
            dfs(i, num)

# [DFS 함수 호출하기]
# dfs(v, num) -> dfs(start, 0) -> 인접 리스트에서 A에 연결된 사람 탐색, num 값은 0부터 시작            
dfs(start, 0)

# result 에 저장된 값이 없다는 것은(if len(result) == 0:)
# 친척 관계가 없어서 촌수 계산이 안된 것이므로 -1 출력
if len(result) == 0:
    print(-1)

else:
    print(result[0] - 1)