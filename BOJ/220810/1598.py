# https://www.acmicpc.net/problem/1598

import sys
sys.stdin = open("1598.txt")

# start 와 end 사이 직선거리 구하기
start, end = map(int, input().split())

# 시작점, 끝점 -1씩해서 연산하기
start -= 1
end -= 1

# 가로는 4로 나눈 몫(절댓값)으로, 세로는 4로 나눈 나머지(절댓값)로 계산
# print(가로길이 + 세로길이)
print(abs(start//4-end//4) + abs(start%4-end%4))