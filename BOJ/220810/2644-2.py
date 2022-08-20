# https://www.acmicpc.net/problem/2644

# 스택으로 푸는 방법(수업)도 정리하기!

# 촌수 찾기

'''
[입력예시]
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
'''

import sys
sys.stdin = open("2644.txt")

N = int(input())
start, end = map(int, input().split())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())  
    graph[x].append(y)
    graph[y].append(x)

visit = [0] * (N+1)

result = []
def dfs(v, num):
    num += 1
    visit[v] = 1

    if v == end:
        result.append(num)

    for i in graph[v]:
        if not visit[i]:
            dfs(i, num)
          
dfs(start, 0)

if len(result) == 0:
    print(-1)

else:
    print(result[0] - 1)