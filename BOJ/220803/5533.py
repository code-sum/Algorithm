# https://www.acmicpc.net/problem/5533

import sys
sys.stdin = open("5533.txt")

members = int(input())
matrix = []

for _ in range(members):
    matrix.append(list(map(int, input().split())))

for i in range(members):
    sum = 0

    # 모든 참가자들이 총 3번의 게임을 진행할 때
    # 서로 동일하지 않은 값들만 찾아서 + 합산하기
    for j in range(3):
        score = matrix[i][j]
        find = 1   # 1, 0을 판별하는 탐색기에 시작값(1 or 0 둘 중 하나) 입력
        for k in range(members):
            if k == i:    # matrix[i][0] and matrix[k][0] 상황에서
                continue  # i = k 면 비교 대상이 안되니까 패스!
            if matrix[k][j] == score:   # 동일한 값이 발생하면
                find = 0                # 탐색기값은 0이 됨
                break                   # 이때 반복문을 멈추고 반복문 밖으로 나감
        if find == 1:                   # 그게 아니라 find == 1 이라면
            sum += score                # 동일한 값이 발생한게 아니므로 점수에 합산

    print(sum)