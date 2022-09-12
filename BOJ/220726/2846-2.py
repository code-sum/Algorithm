# https://www.acmicpc.net/problem/2846

# 백준 2846 다시풀기

import sys
sys.stdin = open("2846.txt")

n = int(input())
height = list(map(int, input().split()))

# 오르막길들 모두 기록해줄 빈 리스트
up = []

# 개별 오르막 높이를 측정해줄 변수
sum = 0

for i in range(1, n):
    if height[i] > height[i-1]:
        sum += (height[i] - height[i-1])

        # 주어진 input 끝부분에 오르막길이 있는 경우 처리
        if i == n-1:
            up.append(sum)

    else:
        up.append(sum)
        sum = 0

print(max(up))