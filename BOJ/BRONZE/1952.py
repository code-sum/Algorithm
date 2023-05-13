# https://www.acmicpc.net/problem/1952


# 상하좌우 벡터 정의
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# m * n 격자의 크기 값 받기
m, n = map(int, input().split())

# m * n 크기의 그래프 초기화
graph = [[1] * n for _ in range(m)]

# 출발지점의 x, y 좌표는 (0, 0)
# 해당 칸의 값도 0으로 지정
x = 0
y = 0
graph[x][y] = 0

# 달팽이가 이동한 횟수 count
count = 0

# 달팽이가 바라보는 현재 방향 d 초기화
d = 0

# 무한루프 (달팽이가 이동을 멈추면 break)
while True:
    # 이동 가능성을 확인하는 wanna_go 초기화
    # 다음 위치로 이동한다는 의미인 go 변수도 초기화
    wanna_go = False
    go = False

    # 현재 바라보는 d 값 기준으로 4방향 탐색
    for i in range(d, d + 4):
        # 다음 위치 계산하기
        nx, ny = x + dx[i % 4], y + dy[i % 4]

        # 1) 다음 위치가 m * n 격자를 벗어나거나,
        # 2) 이미 방문한 곳인 경우,
        # 3) 이동 가능성을 나타내는 wanna 변수를 True 로 바꾸고,
        # 4) 다음 위치로 이동
        if nx < 0 or ny < 0 or nx >= m or ny >= n or graph[nx][ny] != 1:
            wanna_go = True
            continue

        # 1) 이동이 가능한 경우, go 변수를 True 로 바꾸고,
        # 2) 다음 위치로 이동
        go = True
        graph[nx][ny] = 0
        x, y, d = nx, ny, i % 4
        break

    # wanna_go 가 True 이고, go 도 True 인 경우,
    # 이동한 횟수를 1씩 증가
    if wanna_go == True and go == True:
        count += 1

    # go 가 False 인 경우, 더 이상 이동할 수 없다는 의미이므로 무한루프 종료
    if go == False:
        break

# 최종적으로 이동한 횟수인 count 출력
print(count)
