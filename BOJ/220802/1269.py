# https://www.acmicpc.net/problem/1269


n, m = map(int, input().split())

# 집합A, 집합B 생성
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# 대칭차집합 원소의 갯수 출력(set의 len() 구하기)
print(len(A-B)+len(B-A))