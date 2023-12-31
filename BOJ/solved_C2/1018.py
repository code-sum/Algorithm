# https://www.acmicpc.net/problem/1018

import sys

# n개의 줄에 m개의 문자 입력
n, m = map(int, input().split())

mtx_ = []
res = []

for _ in range(n):
    mtx_.append(sys.stdin.readline())

for i in range(n-7):
    for j in range(m-7):
        cnt1 = 0
        cnt2 = 0

        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if mtx_[k][l] != 'B':
                        cnt1 += 1
                    if mtx_[k][l] != 'W':
                        cnt2 += 1
                else:
                    if mtx_[k][l] != 'W':
                        cnt1 += 1
                    if mtx_[k][l] != 'B':
                        cnt2 += 1
        res.append(cnt1)
        res.append(cnt2)

print(min(res))