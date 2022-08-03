# https://www.acmicpc.net/problem/3052

import sys
sys.stdin = open("3052.txt")

# 입력된 수를 42로 나눈 나머지 담아줄 리스트 생성
arr = []

for i in range(10):
    input_10 = int(input())
    arr.append(input_10 % 42)

# 리스트를 set 으로 바꾸어 중복 제거
remainder = set(arr)

# 서로 다른(=중복되지 않은) 나머지들이 몇 개 있나요?
print(len(remainder))