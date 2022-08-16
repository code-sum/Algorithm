# https://www.acmicpc.net/problem/25304

import sys
sys.stdin = open("25304.txt")

# 영수증 총 금액 x
x = int(input())

# 영수증 구매 물건 종류 수 n
n = int(input())

# n가지 물건의 가격(a)과 개수(b)
result = 0
for _ in range(n):
    a, b = map(int, input().split())
    
    price = a*b
    result += price

if result == x:
    print('Yes')
else:
    print('No')
