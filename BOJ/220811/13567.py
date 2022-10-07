# https://www.acmicpc.net/problem/13567

import sys
sys.stdin = open("13567.txt")
    
m, n = map(int, input().split())
m += 1

# 0 으로 채워진 m*m 매트릭스 선언
matrix = [[0] * m for _ in range(m)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0

cur = 0
for i in range(n):
    action, num = input().split()
    if action == 'TURN':
        if num == '0':
            if cur + 1 == 4:
                cur = 0
            else:
                cur += 1

        # if num != '0':
        else:
            if cur - 1 < 0:
                cur = 3
            else:
                cur -= 1

    # if action == 'MOVE':
    else:
        if 0 <= x + (int(num) * dx[cur]) < m and 0 <= y + (int(num) * dy[cur])< m:
            matrix[x][y] = 0
            x += int(num) * dx[cur]; y += int(num) * dy[cur]
            matrix[x][y] = 1
        
        # 명령어 열이 유효하지 않으면 -1 출력
        else:
            print(-1)
            break

# 명령어 수행 후 로봇의 위치의 x좌표와 y좌표(양의 정수 2개 출력)
else:
    print(y, x)