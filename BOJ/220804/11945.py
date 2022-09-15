# https://www.acmicpc.net/problem/11945

import sys
sys.stdin = open("11945.txt")

# n개 줄에 걸쳐 붕어빵 라인 입력, 총 붕어빵 개수 m개

n, m = map(int, input().split())

for i in range(n):
    line_ = list(map(str, input()))
    r_line_ = line_[::-1]

    print(*r_line_, sep='')