# https://www.acmicpc.net/problem/9610

import sys
sys.stdin = open("9610.txt")

# 첫째 줄에 점의 개수 n (1 ≤ n ≤ 1000)이 주어진다.
n = int(input())

cnt_1 = 0
cnt_2 = 0
cnt_3 = 0
cnt_4 = 0
cnt_axis = 0

for _ in range(n):
    x, y = map(int, input().split())
    
    if x > 0 and y > 0:
        cnt_1 += 1
    
    if x < 0 and y > 0:
        cnt_2 += 1

    if x < 0 and y < 0:
        cnt_3 += 1

    if x > 0 and y < 0:
        cnt_4 += 1
    
    if x == 0 or y == 0:
        cnt_axis += 1
        continue

print(f'Q1: {cnt_1} \nQ2: {cnt_2} \nQ3: {cnt_3} \nQ4: {cnt_4} \nAXIS: {cnt_axis}')