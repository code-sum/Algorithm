# https://www.acmicpc.net/problem/2587

import sys
sys.stdin = open("2587.txt")

import math

# 첫째 줄부터 다섯 번째 줄까지 한 줄에 하나씩 자연수가 주어진다.
numbers = []

for _ in range(5):
    numbers.append(int(input()))
    s_numbers = sorted(numbers)

# 평균과 중앙값은 모두 자연수이다.
print(math.trunc((sum(s_numbers))/5))
print(s_numbers[2])