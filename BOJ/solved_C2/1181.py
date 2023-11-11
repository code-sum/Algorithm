# https://www.acmicpc.net/problem/1181


n = int(input())
words = [str(input()) for i in range(n)]

# 중복제거
words = list(set(words))
words.sort()

# 길이 순서로 정리
words.sort(key=len)

for i in words:
    print(i)