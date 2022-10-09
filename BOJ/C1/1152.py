# https://www.acmicpc.net/problem/1152

import sys
sys.stdin = open("1152.txt")

words = list(map(str, input().split()))
print(len(words))