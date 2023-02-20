# 📌2022-08-03 BOJ 풀이



#### 1100. 하얀 칸

> 체스판은 8×8크기이고, 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다. 가장 왼쪽 위칸 (0,0)은 하얀색이다. 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("1100.txt")

matrix = []
for _ in range(8):
    matrix.append(list(input()))

cnt = 0
for i in range(8):
    for j in range(8):
        if matrix[i][j] == 'F' and (i + j) % 2 == 0:
            cnt += 1

print(cnt)
```



#### 1236. 성 지키기

> 영식이는 직사각형 모양의 성을 가지고 있다. 성의 1층은 몇 명의 경비원에 의해서 보호되고 있다. 영식이는 모든 행과 모든 열에 한 명 이상의 경비원이 있으면 좋겠다고 생각했다.
>
> 성의 크기와 경비원이 어디있는지 주어졌을 때, 몇 명의 경비원을 최소로 추가해야 영식이를 만족시키는지 구하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("1236.txt")

# 문제에서는 모든 행과 모든 열에 1명 이상
# 경비원을 둬야 한다고 했음!

n, m = map(int, input().split())
matrix = []

for _ in range(n):
    matrix.append(input())

row_cnt, col_cnt = 0, 0

# 경비원이 없는 행의 개수 탐색
for i in range(n):
    if 'X' not in matrix[i]:
        row_cnt += 1

# 경비원이 없는 열의 개수 탐색
for j in range(m):
    if 'X' not in [matrix[i][j] for i in range(n)]:
        col_cnt += 1

# 행과 열을 모두 탐색했을 때, 경비원은 가장 많이 필요한 쪽에 맞춰서
# 그 수만큼 배치해야함 = row_cnt 와 col_cnt 중에 max 구하기
print(max(row_cnt, col_cnt))
```

