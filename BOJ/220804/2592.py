# https://www.acmicpc.net/problem/2592

import sys
sys.stdin = open("2592.txt")

dic = {}
avg_ = 0

for i in range(10):
    n = int(input())

    avg_ += n
    if n not in dic:
        dic[n] = 1
    else:
        dic[n] += 1

print(avg_//10)

# 딕셔너리에서 최대 value 를 갖는 key 찾는 코드
max_k = max(dic, key=dic.get)
print(max_k)