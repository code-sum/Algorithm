# https://www.acmicpc.net/problem/1302

# 입력된 책 목록 중에 가장 많이 입력된 책 이름 출력


import sys
sys.stdin = open("1302.txt")

n = int(input())
list_ = {}

for i in range(n):
    input_ = input()
    if input_ not in list_:
        list_[input_] = 1
    else:
        list_[input_] += 1

freq_ = max(list_.values())
ans = []

for input_, num in list_.items():
    if num == freq_:
        ans.append(input_)

print(sorted(ans)[0])