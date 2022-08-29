# https://www.acmicpc.net/problem/1065

# 123 처럼 각 자리수가 등차수열이면 '한수'
# N이 주어졌을 때, 1보다 크거나 같고, 
# N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성

import sys

n = int(sys.stdin.readline())

cnt = 0
for i in range(1, n+1):

    input_ = list(map(int, str(i)))
    if i < 100:
        cnt += 1 # 100보다 작으면 모두 한수

    # 각 자리수가 등차수열이면 한수
    elif input_[0] - input_[1] == input_[1] - input_[2]:
        cnt += 1

print(cnt)
