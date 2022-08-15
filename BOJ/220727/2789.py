# https://www.acmicpc.net/problem/2789

word = input()

ans = []
for i in word:
    if i not in 'CAMBRIDGE':
        ans.append(i)

print(*ans, sep='')