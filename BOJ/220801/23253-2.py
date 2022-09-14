# https://www.acmicpc.net/problem/23253

# 23253.py 시간초과 떠서 다시 풀이

import sys
sys.stdin = open("23253.txt")

# 교과서 n권, 책 더미 m개
n, m = map(int, input().split())

cnt = 0

for i in range(m):

    # 각 더미에 쌓인 책 권수(d), 쌓인 책 순서(order) 개행으로 입력 
    d = int(input())
    order = list(map(int, input().split()))
    
    for j in range(d-1):
        if order[j] < order[j+1]:
            cnt += 1

if cnt == 0:
    print("Yes")
else:
    print("No")