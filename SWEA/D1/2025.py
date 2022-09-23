import sys
sys.stdin = open("2025.txt")

n = int(input())
list_ = []

for i in range(1, n+1):
    list_.append(i)

print(sum(list_))