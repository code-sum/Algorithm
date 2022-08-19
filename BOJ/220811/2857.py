# https://www.acmicpc.net/problem/2857

# FBI 요원은 input에 FBI 포함

import sys
sys.stdin = open("2857.txt")

s = []
for i in range(5):
    name = input()
    
    if "FBI" in name:
        s.append(i+1)
    else:
        continue

if len(s) == 0:
    print("HE GOT AWAY!")
else:
    print(*s)