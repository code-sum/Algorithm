# https://www.acmicpc.net/problem/1764

import sys
sys.stdin = open("1764.txt")

a, b = map(int, input().split())

# a명의 input 와 b명의 input 사이 교집합에 해당하는 사람수, 이름 출력하기

dic = {}

for _ in range(a):
    a_people = input()
    if a_people not in dic:
        dic[a_people] = 1

for _ in range(b):
    b_people = input()
    if b_people in dic:
        dic[b_people] += 1
    else:
        dic[b_people] = 1

ans = []
for b_people, num in dic.items():
    if num == 2:
        ans.append(b_people)
    else:
        continue

print(len(ans))
for i in sorted(ans):
    print(i)