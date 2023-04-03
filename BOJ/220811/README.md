# 📌2022-08-11 BOJ 풀이



#### 1063. 킹 [(link)](https://www.acmicpc.net/problem/1063)

> 8*8크기의 체스판에 왕이 하나 있다. 킹의 현재 위치가 주어진다. 체스판에서 말의 위치는 다음과 같이 주어진다. 알파벳 하나와 숫자 하나로 이루어져 있는데, 알파벳은 열을 상징하고, 숫자는 행을 상징한다. 열은 가장 왼쪽 열이 A이고, 가장 오른쪽 열이 H까지 이고, 행은 가장 아래가 1이고 가장 위가 8이다. 예를 들어, 왼쪽 아래 코너는 A1이고, 그 오른쪽 칸은 B1이다.
>
> 킹은 다음과 같이 움직일 수 있다.
>
> - R : 한 칸 오른쪽으로
> - L : 한 칸 왼쪽으로
> - B : 한 칸 아래로
> - T : 한 칸 위로
> - RT : 오른쪽 위 대각선으로
> - LT : 왼쪽 위 대각선으로
> - RB : 오른쪽 아래 대각선으로
> - LB : 왼쪽 아래 대각선으로
>
> 체스판에는 돌이 하나 있는데, 돌과 같은 곳으로 이동할 때는, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시킨다. 아래 그림을 참고하자.
>
> ![img](https://upload.acmicpc.net/259549ad-b275-48a1-91f7-197a7ce72a23/-/preview/)
>
> 입력으로 킹이 어떻게 움직여야 하는지 주어진다. 입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다.
>
> 킹과 돌의 마지막 위치를 구하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("1063.txt")

move = {
    "R": (0, 1),
    "L": (0, -1),
    "B": (1, 0),
    "T": (-1, 0),
    "RT": (-1, 1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (1, -1)
}

king, stone, n = input().split()
king_row, king_col = 8-int(king[1]), ord(king[0])-ord("A")
stone_row, stone_col = 8-int(stone[1]), ord(stone[0])-ord("A")

# input_ 명령에 따라 움직이기
for _ in range(int(n)):
    input_ = input().strip()
    input_row, input_col = move[input_]
    if not (0 <= king_row+input_row < 8 and 0 <= king_col+input_col < 8):
        continue
    king_row += input_row
    king_col += input_col
    if (king_row, king_col) == (stone_row, stone_col):
        if not (0 <= stone_row+input_row < 8 and 0 <= stone_col+input_col < 8):
        	# 킹의 움직임 되돌리기
            king_row -= input_row
            king_col -= input_col
            continue
        stone_row += input_row
        stone_col += input_col
       
print(chr(ord("A")+king_col)+str(8-king_row))
print(chr(ord("A")+stone_col)+str(8-stone_row))
```



#### 1926. 그림 [(link)](https://www.acmicpc.net/problem/1926)

> 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

```python
# 백준 1926 그림 : 이차원 리스트의 DFS 문제
# 연결요소의 갯수 문제와 사실 동일한 문제
# 4방향 델타탐색 (대각선은 고려하지않으므로 8방향이 아님)

# 델타탐색의 중요조건 : 범위
# DFS의 중요조건 : 방문처리 리스트

import sys
sys.stdin = open("1926.txt")

"""
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
"""

def pprint(arr):
    for i in range(len(arr)):
        print(arr[i])

# 상,하,좌,우 탐색하기 위한 델타 리스트
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 가로 세로의 크기를 입력
# 두 숫자가 공백으로 구분
n, m = list(map(int,input().split()))

# 이차원 그래프를 생성
# 빈 그래프 생성
graph = []

# n번 만큼 일차원 그래프를 입력 & 추가
for _ in range(n):
    graph_list = list(map(int,input().split()))
    graph.append(graph_list)

# 방문 표시 이차원 그래프
visit = []

# n번 만큼 일차원 그래프를 추가
for _ in range(n):
    # boolean(False) 가 m개인 일차원 그래프
    visit_list = [False] * m
    visit.append(visit_list)

painting_count = 0
painting_size_list = []

# 모든 좌표에서 DFS 로직 실행
# 이차원 리스트를 순회할 이중 반복문
'''
여기서 y,x 대신 sy,sx 를 쓴 이유는
아래 stack.pop() 부분에서 계속 튀어나온 숫자(y, x)들이
최상단 for문에 영향을 주기 때문
'''
for sy in range(n):
    for sx in range(m):
        # [y,x] 값이 1이고, 방문하지 않았다면(=그림이라면)
        # DFS 실행
        if not visit[sy][sx] and graph[sy][sx] == 1: 
            stack = []
            # 시작점을 stack append
            stack.append([sy,sx])
            # 시작점을 방문처리
            visit[sy][sx] = True

            # while문 시작 전에 그림의 개수 + 1
            painting_count += 1
            # 그림의 넓이?
            painting_size = 0
            # DFS
            # 스택이 비어있지않으면 반복한다.
            # while stack:
            while len(stack) != 0:
                # y,x 값이 갱신(꺼내기)
                y, x = stack.pop()
                # 그림의 넓이(stack.pop() 실행될때마다 += 1)
                painting_size += 1

                # 델타 탐색을 시행 
                # ny(next y), nx(next x)
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    
                    # 조건 1, 2, 3
                    # 조건 1. 범위 조건
                    if not (-1< ny < n and -1 < nx < m):
                        continue

                    # 조건 2. 방문 확인
                    # 방문을 했던 좌표라면
                    if visit[ny][nx] == True:
                        continue

                    # 조건 3. 좌표의 값이 1
                    # 그림이여야한다 (그림 아니면 continue)
                    if graph[ny][nx] != 1:
                        continue
                        
                    # 조건을 다 통과하면
                    # stack 다음 좌표 넣고,
                    # 방문 처리
                    stack.append((ny,nx))
                    visit[ny][nx] = True

            painting_size_list.append(painting_size)

# 그림의 개수
# 그림의 가장 큰 넓이
if len(painting_size_list) != 0:
    print(painting_count)
    print(max(painting_size_list))

# 그림이 없을 때( if len(painting_size_list)==0: ) 가장 큰 그림 넓이(2번째줄 출력)는 0
else:
    print(painting_count)
    print(0)
```



#### 2495. 연속구간 [(link)](https://www.acmicpc.net/problem/2495)

> 여덟 자리의 양의 정수가 주어질 때, 그 안에서 연속하여 같은 숫자가 나오는 것이 없으면 1을 출력하고, 있으면 같은 숫자가 연속해서 나오는 구간 중 가장 긴 것의 길이를 출력하는 프로그램을 작성하라. 
>
> 예를 들어 세 개의 숫자 12345123, 17772345, 22233331이 주어졌다고 하자. 12345123은 연속하여 같은 숫자가 나오는 것이 없으므로 1을 출력하고, 17772345는 7이 세 개 연속하여 나오므로 3을 출력하며, 22233331의 경우에는 2가 세 개, 3이 네 개 연속해서 나오므로 그 중 큰 값인 4를 출력하여야 한다.  

```python
import sys
sys.stdin = open("2495.txt")

# 첫째 줄부터 셋째 줄까지 각 줄에 하나씩 세 개의 여덟 자리 양의 정수가 주어진다.

for _ in range(3):
    input_ = str(input())
   
   # 여덟자리 수의 나열 중에 중복되는 수가 없으면 1을 출력
   # 중복되는 수가 있으면, 그 수의 중복 횟수를 출력
   # 만약 중복되는 수가 여러 개라면 중복 횟수가 더 많은 경우를 출력

    cnt = 1
    max_ = 1
    for i in range(1, len(input_)):
        if input_[i-1] == input_[i]:
            cnt += 1
        else:
            max_ = max(cnt, max_)
            cnt = 1

    max_ = max(cnt, max_)
    print(max_)
```

