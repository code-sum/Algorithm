# https://www.acmicpc.net/problem/10809

import sys
sys.stdin = open("10809.txt")

alpha = list(range(97,123))
s = input()

for i in alpha:
    print(s.find(chr(i)), end =' ')