# https://www.acmicpc.net/problem/2920

import sys
sys.stdin = open("2920.txt")

input_ = input()

if input_ == "1 2 3 4 5 6 7 8":
    print("ascending")
elif input_ == "8 7 6 5 4 3 2 1":
    print("descending")
else:
    print("mixed")
