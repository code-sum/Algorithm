import sys

sys.stdin = open("2068.txt")

t = int(input())

for i in range(1, t + 1):
    num = list(map(int, input().split()))
    print(f"#{i} {max(num)}")
