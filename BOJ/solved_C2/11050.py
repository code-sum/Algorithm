# https://www.acmicpc.net/problem/11050

'''
<이항계수 : nCk>
n, k 가 입력될 때
n!/(n-k)!k! 구하기
'''

n, k = map(int, input().split())

def factorial(x):
    res = 1
    for i in range(x):
        res = res*(i+1)
    return res

upper = factorial(n)
bottom = factorial(n-k)*factorial(k)

res = upper//bottom

print(res)