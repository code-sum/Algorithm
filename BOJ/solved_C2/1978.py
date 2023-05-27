# https://www.acmicpc.net/problem/1978

# 소수 : 1과 자기자신만 약수로 갖는 수 (1은 소수에서 제외)
# 소수 판별 시 효율적인 알고리즘은, 
# 주어진 수에 1이 아닌 제곱근 있는지 확인하는 것
# 혹은 '제곱근 직전까지의 자연수들' 중에 나머지가 0으로 떨어지는 수가 있는지 확인하는 것

import math

n = int(input())
li = list(map(int, input().split()))
cnt = 0

def test(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for j in li:
    if test(j):
        cnt += 1

print(cnt)