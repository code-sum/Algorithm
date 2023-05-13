# https://www.acmicpc.net/problem/11720

import sys
sys.stdin = open("11720.txt")

n = int(input())
nums = list(map(int, input()))

print(sum(nums))