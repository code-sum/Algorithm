# https://www.acmicpc.net/problem/11021

import sys
sys.stdin = open("11021_input.txt", "r")

test_case = int(input())    # 맨 첫줄에 테스트 케이스 개수(5)가 주어진다

for _ in range(test_case):
    a, b = map(int, input().split())
    print(f'Case #{_+1}: {a+b}')