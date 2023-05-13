# https://www.acmicpc.net/problem/2562

import sys
sys.stdin = open("2562.txt")

numbers = []

for i in range(9):
    numbers.append(int(input()))
print(max(numbers))

for i in range(len(numbers)):
    if numbers[i] == max(numbers):
        print(i+1)