# https://www.acmicpc.net/problem/2669

import sys
sys.stdin = open("2669.txt")

'''
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6
26
'''

# 입력은 네 줄이며, 각 줄은 직사각형의 위치를 나타내는 네 개의 정수
# 첫 번째와 두 번째의 정수는 사각형의 왼쪽 아래 꼭짓점의 x좌표, y좌표
# 세 번째와 네 번째의 정수는 사각형의 오른쪽 위 꼭짓점의 x좌표, y좌표

# 0을 100 X 100 matrix 에 채워넣기
matrix = []
for _ in range(100):
    matrix.append([0]*100)

# 문제에서 주어진 직사각형 4개의 영역을 0 -> 1 값으로 매핑하기
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split(" "))
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] = 1

# 0 과 1로만 이루어진 matrix 위의 모든 값을 더하기
cnt = 0
for blocks in matrix:
    cnt += sum(blocks)

print(cnt)