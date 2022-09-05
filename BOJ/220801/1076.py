# https://www.acmicpc.net/problem/1076

import sys
sys.stdin = open("1076.txt")

color = ['black', 'brown', 'red', 
'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

a = color.index(input())
b = color.index(input())
c = color.index(input())

# 저항값
o = int(str(a) + str(b)) * (10 ** c)
print(o)