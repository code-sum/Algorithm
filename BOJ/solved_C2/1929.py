# https://www.acmicpc.net/problem/1929

'''
m 이상 n 이하 소수를 모두 출력
비슷한 문제 : 1978번, 소수 판정하는 함수(def test) 숙지할 것
'''

import math
m, n = map(int, input().split())
li = [i for i in range(m, n+1)]

def test(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for j in li:
    if test(j):
        print(j)

