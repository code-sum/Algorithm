# https://www.acmicpc.net/problem/2798

import sys
sys.stdin = open("2798.txt")

'''
5 21
5 6 7 8 9
'''

# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다.
N, M = map(int, input().split())

# 둘째 줄에는 카드에 쓰여 있는 수가 주어진다.
list_ = list(map(int, input().split()))

# N장의 카드 중에 3장의 카드 고르기 = 3중 for문
result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):

            # 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
            if list_[i] + list_[j] + list_[k] > M:
                continue
            else:
                result = max(result, list_[i] + list_[j] + list_[k])
print(result)