# https://www.acmicpc.net/problem/14720

import sys
sys.stdin = open("14720.txt")

# 딸기(0) - 초코(1) - 바나나(2) - 딸기(0)
# 한 번 지나친 우유 가게는 다시 갈 수 없음
# 영학이가 마실 수 있는 우유의 최대 개수는?

# 우유 가게의 개수
n = int(input())

# 우유 가게의 정보
s = list(map(int, input().split()))

cnt = 0

for i in range(n):
    if s[i] == cnt % 3:
        cnt += 1

print(cnt)