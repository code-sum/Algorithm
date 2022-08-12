# https://www.acmicpc.net/problem/9455

import sys

'''
출력 예시
8
6
16
'''

# 첫째 줄에 테스트 케이스의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 그 다음줄에는 m, n 입력
    m, n = map(int, sys.stdin.readline().split())

    # 그 다음줄부터 그리드 입력
    grid = [[] for _ in range(n)]

    # 각 열에 있는 박스의 위치를 2차원 리스트인 grid 에 저장
    for i in range(m):
        line = list(sys.stdin.readline().split())
        for j in range(n):
            grid[j].append(line[j])

    move = 0   # 모든 박스가 이동한 거리 cnt

    # 모든 열(n)을 순회하는 반복문 작성
    for i in range(n):

        # 1열의 박스('1') 개수
        boxes = grid[i].count('1')
        end = m - 1   # 바닥의 위치

        # 열의 아래부터 박스 위치 이동
        for j in range(m - 1, -1, -1):

            # 박스를 제자리에 놓고 바닥을 1씩 높인다.
            if grid[i][j] == '1':
                move += end - j
                end -= 1

    print(move)