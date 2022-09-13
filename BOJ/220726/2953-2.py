# https://www.acmicpc.net/problem/2953

# 2953.py 가 런타임에러여서 다시 풀이

import sys
sys.stdin = open("2953.txt")

dic = {}

for i in range(1, 6):
    score = list(map(int, input().split()))
    sum_score = sum(score)
    dic[i] = sum_score

for k, v in dic.items():
    if max(dic.values()) == v:
        print(k, v)