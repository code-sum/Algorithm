# https://www.acmicpc.net/problem/2953

scores = []

for _ in range(5):
    scores = scores.append(sum(map(int, input().split())))

print(scores.index(max(scores))+1, max(scores))

# 첫째 줄에 우승자의 번호와 그가 얻은 점수를 출력
# 우승자의 위치(scores 중에 max 값)를 인덱싱했으므로,
# 실제 위치는 인덱스 값+1 (인덱스는 0부터 시작하기 때문)