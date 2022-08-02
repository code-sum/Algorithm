# https://www.acmicpc.net/problem/10995

n = int(input())

if n == 1:
    print('*')

else:
    for i in range(n):
        if i % 2 == 0:
            print('* '*n)
        else:
            print(' *'*n)
