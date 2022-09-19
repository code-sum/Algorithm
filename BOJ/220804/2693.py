# https://www.acmicpc.net/problem/2693

import sys
sys.stdin = open("2693.txt")

t = int(input())

for _ in range(1, t+1):
    arr = sorted(list(map(int, input().split())), reverse=True)
    
    print(arr[2])