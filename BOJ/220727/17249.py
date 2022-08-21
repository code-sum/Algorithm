# https://www.acmicpc.net/problem/17249

hook = input()

cnt = 0
ans = []

for i in hook:
    if i == "@":
        cnt += 1
    elif i == "=":
        continue
    elif i == "(":
        ans.append(cnt)
        cnt = 0
    elif i == "^" and i == "0" and i == ")":
        continue

ans.append(cnt)

print(*ans)