# https://www.acmicpc.net/problem/10951

import sys
sys.stdin = open("10951.txt")

while True:
    try: 
        a,b = map(int, input().split())
        print(a+b)
    except:
        break