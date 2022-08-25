# https://www.acmicpc.net/problem/6996

import sys
sys.stdin = open("6996.txt")

n = int(input())

for _ in range(n):
    a, b = map(str, input().split())

    a_sort = sorted(list(a))
    b_sort = sorted(list(b))

    if a_sort == b_sort:
        print("%s & %s are anagrams." %(a, b))
    else:
        print("%s & %s are NOT anagrams." %(a, b))