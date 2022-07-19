import sys
sys.stdin = open('2070_input.txt', 'r')

T = int(input())
for i in range(1, T + 1):
    a, b = map(int, input().split())
    if a == b :
        print('#%d %s' % (i, '='))
    elif a < b :
        print('#%d %s' % (i, '<'))
    else :
        print('#%d %s' % (i, '>'))