import sys
sys.stdin = open("10950_input.txt", "r")

test_case = int(input())
for _ in range(test_case):
    a, b = map(int, input().split())
    print( a+b )