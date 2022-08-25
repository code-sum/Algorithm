# https://www.acmicpc.net/problem/2495

import sys
sys.stdin = open("2495.txt")

# 첫째 줄부터 셋째 줄까지 각 줄에 하나씩 세 개의 여덟 자리 양의 정수가 주어진다.

for _ in range(3):
    input_ = str(input())
   
   # 여덟자리 수의 나열 중에 중복되는 수가 없으면 1을 출력
   # 중복되는 수가 있으면, 그 수의 중복 횟수를 출력
   # 만약 중복되는 수가 여러 개라면 중복 횟수가 더 많은 경우를 출력

    cnt = 1
    max_ = 1
    for i in range(1, len(input_)):
        if input_[i-1] == input_[i]:
            cnt += 1
        else:
            max_ = max(cnt, max_)
            cnt = 1

    max_ = max(cnt, max_)
    print(max_)
