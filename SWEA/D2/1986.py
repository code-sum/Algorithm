import sys
sys.stdin = open("1986_input.txt", "r")

t = int(input())

for test_case in range(1, t + 1) :
    n = int(input())
    result = 0
    for i in range(1, n + 1) :
        if i % 2 == 0 :   # 짝수일 경우
            result -= i
        else :            # 홀수일 경우
            result += i

    print('#%d %d' % (test_case, result))