import sys
sys.stdin = open("2043.txt")

p, k = map(int, input().split())
cnt = 1

while True:
    k += 1
    cnt += 1

    if k == p:
        break

print(cnt)