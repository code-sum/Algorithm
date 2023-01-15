# https://www.acmicpc.net/problem/2851

# 먹은 버섯 리스트
eaten = []

# 데이터 입력
for i in range(10):
    point = int(input())
    eaten.append(point)

# 먹은 점수의 초기값
score = 0

for j in eaten:
    score += j
    if score >= 100:
        if score - 100 > 100 - (score - j):
            score -= j
        break

print(score)