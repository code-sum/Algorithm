import sys

sys.stdin = open("2072.txt")

t = int(input())

for i in range(1, t + 1):
    hol = []
    input_ = list(map(int, input().split()))

    for j in input_:
        if j % 2 == 1:
            hol.append(j)

    print(f"#{i} {sum(hol)}")
