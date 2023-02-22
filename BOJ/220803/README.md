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



#### 2167. 2차원 배열의 합

> 2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오. 배열의 (i, j) 위치는 i행 j열을 나타낸다.

```python
# 시간초과 발생하면 pypy3 로 제출!

import sys
sys.stdin = open("2167.txt")

'''
2 3
1 2 4
8 16 32
3
1 1 2 3
1 2 1 2
1 3 2 3
'''

# N, M 주어짐
N, M = map(int, input().split())
matrix = []

# N행 M열 매트릭스 input
for _ in range(N):
    matrix.append(list(map(int, input().split())))

# i, j, x, y 로 구성된 k 개의 row 작성
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())

    # (i, j)부터 (x, y)까지 탐색해야 하니까
    # 행 탐색 반복문의 range 는 i-1, x
    # 열 탐색 반복문의 range 는 j-1, y
    sum = 0
    for row in range(i-1, x):
        for col in range(j-1, y):

            # 매트릭스의 요소 중에서 해당 행, 열에 해당하는 값들을 더해줌
            sum += matrix[row][col]

    print(sum)
```



#### 2864. 5와 6의 차이 [(link)](https://www.acmicpc.net/problem/2864)

> 상근이는 2863번에서 표를 너무 열심히 돌린 나머지 5와 6을 헷갈리기 시작했다.
>
> 상근이가 숫자 5를 볼 때, 5로 볼 때도 있지만, 6으로 잘못 볼 수도 있고, 6을 볼 때는, 6으로 볼 때도 있지만, 5로 잘못 볼 수도 있다.
>
> 두 수 A와 B가 주어졌을 때, 상근이는 이 두 수를 더하려고 한다. 이때, 상근이가 구할 수 있는 두 수의 가능한 합 중, 최솟값과 최댓값을 구해 출력하는 프로그램을 작성하시오.

```python
# 두 수의 가능한 합 중에서
# 최댓값과 최솟값을 구해 출력하자

# 5를 5로 보고 6을 5로 볼 때 (최소)
# 5를 5로 보고 6을 6으로 볼 때 (정상)
# 5를 6으로 보고 6을 5로 볼 때 (정상과 같음)
# 5를 6으로 보고 6을 6으로 볼 때 (최대)

a, b = input().split()

min = int(a.replace('6', '5')) + int(b.replace('6', '5'))
max = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(min, max)
```

