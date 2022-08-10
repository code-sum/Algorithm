# https://www.acmicpc.net/problem/2750

import sys
sys.stdin = open("2750.txt")

# 첫째줄에 수의 개수 n 입력
n = int(input())

num_list = []

# 입력뇌는 n개의 수를 num_list 에 넣은 다음 정렬하기
for i in range(n):
    num_list.append(int(input()))

sorted_list = sorted(num_list)

# 정렬한 리스트의 원소들을 한줄씩 차례대로 출력
for i in range(len(num_list)):
    print(sorted_list[i])