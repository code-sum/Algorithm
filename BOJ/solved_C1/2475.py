# https://www.acmicpc.net/problem/2475

numbers = list(map(int, input().split()))
ans = 0

for i in numbers:
    ans += i**2

print(ans%10)