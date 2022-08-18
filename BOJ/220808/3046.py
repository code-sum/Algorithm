# https://www.acmicpc.net/problem/3046

# 첫째 줄에 두 정수 R1과 S가 주어진다.
# 두 수는 -1000보다 크거나 같고, 1000보다 작거나 같다.

R1, S = map(int, input().split())

R2 = 2*S - R1

print(R2)