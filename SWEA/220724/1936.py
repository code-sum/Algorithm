import sys
sys.stdin = open("1936_input.txt", "r")

# 가위 1, 바위 2, 보 3
A, B = map(int, input().split())

# If A 1 and B 2 print B
# If A 1 and B 3 print A

# If A 2 and B 1 print A
# If A 2 and B 3 print B

# If A 3 and B 1 print B
# If A 3 and B 2 print A

if (A == 1 and B == 2) or (A == 2 and B == 3) or (A == 3 and B == 1):
    print('B')

else:
    print('A')