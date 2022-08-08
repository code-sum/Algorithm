# https://www.acmicpc.net/problem/10871

import sys
sys.stdin = open("10871.txt")

N, X = map(int, input().split())
A = list(map(int, input().split()))

# A에서 X보다 작은 수를 입력받은 순서대로 공백 구분해 출력
new_A = []
for i in A:
    if i < X:
        new_A.append(i)
    else:
        continue

print(*new_A, end=' ')