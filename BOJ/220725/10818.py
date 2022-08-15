# https://www.acmicpc.net/problem/10818

n = int(input())

numbers = list(map(int, input().split()))

print(f'{min(numbers)} {max(numbers)}')