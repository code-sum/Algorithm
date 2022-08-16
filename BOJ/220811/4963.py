# https://www.acmicpc.net/problem/4963

# 섬(덩어리)의 개수

# 대각선에 섬이 있어도 인접하다고 써 있으므로
# 8방향 탐색하는 DFS를 설계해야 함



import sys
sys.stdin = open("4963.txt")

# [상하좌우+대각선 델타값]
# 특정 섬 (x,y)를 기준으로 할 때, 이로부터 탐색해야 하는 8방향
octagon = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

while True:
    # 각 테스트 케이스 마다 지도의 넓이(w), 높이(h)가 주어짐
    w, h = map(int, input().split())
    # 종료 조건: w, h 입력 값이 0, 0 일 때
    if not w and not h:
        break
    # if w == 0 and h == 0:
    #   break    이런 식으로 종료조건을 작성해도 됨

    # 둘째 줄부터 h개의 줄에는 지도가 주어진다.
    matrix = [list(map(int,input().split())) for _ in range(h)]

    # w(너비)*h(높이)로 입력된 matrix 는 이차원 격자로,
    # 이중 for문 작성해서 x,y 좌표가 매칭되는 stack 작성
    # matrix[i][j] = 0 이면 바다가 등장해서 섬이 끊긴 것 cnt += 1
    cnt = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j]:
                stack = [(i,j)]
                matrix[i][j] = 0
                cnt += 1

                # 스택이 빌 때까지(돌아갈 곳이 없을 때까지) 반복:
                while stack:
                    # 현재 방문 정점(후입선출)
                    x,y = stack.pop()

                    # 델타값을 이용한 상하좌우+대각선(octagon) 탐색
                    # matrix 에서 뽑은 x,y 값의 쌍(stack)에 대해
                    # octagon 의 변량값 r,c를 각각 더하면서 8방향 탐색
                    for r,c in octagon:
                        dx = x + r
                        dy = y + c

                        # dx, dy 값이 경계값에 맞게 들어가면:
                        # = 이동할 수 있는 있는 곳에 있다면:
                        # stack 에 저장해서 계속 8방향 탐색하며 나아갈 수 있게하기
                        # 이때 matrix[dx][dy] 는 아직 방문하지 않았으므로 False 처리
                        if h > dx >= 0 and w > dy >= 0 and matrix[dx][dy]:
                            stack.append((dx, dy))
                            matrix[dx][dy] = False

    # 각 테스트 케이스에 대해서, 섬의 개수를 출력한다.
    print(cnt)


'''
[DFS 3가지 패턴]
1. 상, 하, 좌, 우 패턴
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
2. 대각선 + 상, 하, 좌, 우 패턴
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
3. 대각선 패턴
dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]
'''