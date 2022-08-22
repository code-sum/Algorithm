# https://www.acmicpc.net/problem/2711

import sys
sys.stdin = open("2711.txt")

t = int(input())

for i in range(1, t+1):
    tc = list(input().split())
    # print(*tc)

    spot = int(tc[0])-1
    word = list(tc[1])
    
    for j in range(len(word)):
        if j == spot:
            del word[j]
    
    print(*word, sep='')