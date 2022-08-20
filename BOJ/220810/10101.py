# https://www.acmicpc.net/problem/10101

import sys
sys.stdin = open("10101.txt")

angles = []
for _ in range(3):
    angle = int(sys.stdin.readline())
    angles.append(angle)

if sum(angles) == 180:
    if angles[0] == angles[1] == angles[2]:
        print("Equilateral")
    elif angles[0] == angles[1] or angles[1] == angles[2] or angles[2] == angles[0]:
        print("Isosceles")
    else:
        print("Scalene") 
else:
    print("Error")