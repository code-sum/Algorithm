# https://www.acmicpc.net/problem/2739

N = int(input())

for i in range(1, 10):
    result = N*i
    
    print(f'{N} * {i} = {result}')