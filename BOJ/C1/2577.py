# https://www.acmicpc.net/problem/2577

import sys
sys.stdin = open("2577.txt")

multi = 1
for _ in range(3):
    multi *= int(input())

ans = list(str(multi))
for i in range(10):
    print(ans.count(str(i)))