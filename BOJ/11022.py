import sys
sys.stdin = open("11022_input.txt", "r")

test_case = int(input())
for _ in range(1, test_case + 1):
    a, b = map(int, input().split())
    print('Case #%d: %d + %d = %d' %(_, a, b, a+b))