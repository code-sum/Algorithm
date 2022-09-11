# https://www.acmicpc.net/problem/25192

import sys
sys.stdin = open("25192.txt")

def gom(n):
    gom_set = set()
    cnt = 0

    for _ in range(n):
        name = input()

        if name != "ENTER":
            if name not in gom_set:
                cnt += 1
                gom_set.add(name)

        elif name == "ENTER":
            gom_set.clear()
    
    return cnt

print(gom(int(input())))
