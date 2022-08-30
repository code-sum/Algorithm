# https://www.acmicpc.net/problem/1110

# 시작하는 수 26
# 2+6 = 8
# 68 ~ 6+8 = 14
# 84 ~ 8+4 = 12
# 42 ~ 4+2 = 6
# 26 ~ 끝난 수 = 시작하는 수
# 4번째 생성 끝에 원래의 수로 회귀
# 생성 사이클 돌 때마다 cnt += 1 하다가 print(cnt)

import sys

input_ = int(sys.stdin.readline())
n = input_
cnt = 0

while True:
    a = n // 10
    b = n % 10
    c = (a+b) % 10
    n = (b*10) + c

    cnt += 1
    if n == input_:
        break

print(cnt)