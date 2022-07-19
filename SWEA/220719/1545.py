import sys
sys.stdin = open("1545_input.txt", "r")

T = int(input())
for test_case in range(T, -1, -1):
    print(test_case, end=" ")