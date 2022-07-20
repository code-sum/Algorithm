import sys
sys.stdin = open("2019_input.txt", "r")

n = int(input())

# 2^0, 2^1, 2^2, 2^3, 2^4 ... 2^8 출력!
# n = 1~8이 들어갈 자리

for i in range(0, n + 1):
    if n < 30:
        print(2**i, end = ' ')
    else:
        break