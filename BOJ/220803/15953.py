# https://www.acmicpc.net/problem/15953

# 제이지가 2번의 코테에서 받을 수 있는 상금 합계를
# 원 단위로 출력하자

import sys
sys.stdin = open("15953.txt")

t = int(input())

for i in range(t):

    # 1번째 코테에서 a등, 2번째 코테에서 b등
    # 본선 진출하지 못하면(a > 21, b > 64이면)
    # a, b 는 각각 0으로 초기화

    a, b = map(int, input().split())

    if a == 1:
        a_prize = 5000000
    elif 1 < a <= 3:
        a_prize = 3000000
    elif 3 < a <= 6:
        a_prize = 2000000
    elif 6 < a <= 10:
        a_prize = 500000
    elif 10 < a <= 15:
        a_prize = 300000
    elif 15 < a <= 21:
        a_prize = 100000
    else:
        a_prize = 0

    if b == 1:
        b_prize = 5120000
    elif 1 < b <= 3:
        b_prize = 2560000
    elif 3 < b <= 7:
        b_prize = 1280000
    elif 7 < b <= 15:
        b_prize = 640000
    elif 15 < b <= 31:
        b_prize = 320000
    else:
        b_prize = 0
    
    print(a_prize + b_prize)
