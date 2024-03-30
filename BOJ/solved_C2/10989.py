import sys

N = int(input())

check_ = [0] * 10001

for i in range(N):
    input_ = int(sys.stdin.readline())
    
    check_[input_] = check_[input_] + 1
    
for i in range(10001):
    if check_[i] != 0:
        for j in range(check_[i]):
            print(i)