# https://www.acmicpc.net/problem/23825


N, M = map(int, input().split())

# Step 1. N, M 둘 중에 가장 작은 값을 골라냄
select = min(N, M)

# Step 2. 위에서 고른 가장 작은 값을 2로 나누었을 때 몫 = SASA 쌍의 최대 개수
print(select//2)