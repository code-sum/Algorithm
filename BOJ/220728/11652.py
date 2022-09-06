# https://www.acmicpc.net/problem/11652

import sys
sys.stdin = open("11652.txt")

dic = {}
n = int(input())

for _ in range(n):
    num = int(input())

    if num not in dic:
        dic[num] = 1
    else:
        dic[num] += 1

dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(dic[0][0])