# https://www.acmicpc.net/problem/2167

# 시간초과 발생하면 pypy3 로 제출!

import sys
sys.stdin = open("2167.txt")

'''
2 3
1 2 4
8 16 32
3
1 1 2 3
1 2 1 2
1 3 2 3
'''

# N, M 주어짐
N, M = map(int, input().split())
matrix = []

# N행 M열 매트릭스 input
for _ in range(N):
    matrix.append(list(map(int, input().split())))

# i, j, x, y 로 구성된 k 개의 row 작성
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())

    # (i, j)부터 (x, y)까지 탐색해야 하니까
    # 행 탐색 반복문의 range 는 i-1, x
    # 열 탐색 반복문의 range 는 j-1, y
    sum = 0
    for row in range(i-1, x):
        for col in range(j-1, y):

            # 매트릭스의 요소 중에서 해당 행, 열에 해당하는 값들을 더해줌
            sum += matrix[row][col]

    print(sum)