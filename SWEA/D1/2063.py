import sys

sys.stdin = open("2063.txt")

n = int(input())
input_ = sorted(list(map(int, input().split())))

num = n // 2

print(input_[num])
