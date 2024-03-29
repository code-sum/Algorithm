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



#### 5533. 유니크 [(link)](https://www.acmicpc.net/problem/5533)

> 상근이와 친구들은 MT에 가서 아래 설명과 같이 재미있는 게임을 할 것이다.
>
> 각 플레이어는 1이상 100 이하의 정수를 카드에 적어 제출한다. 각 플레이어는 자신과 같은 수를 쓴 사람이 없다면, 자신이 쓴 수와 같은 점수를 얻는다. 만약, 같은 수를 쓴 다른 사람이 있는 경우에는 점수를 얻을 수 없다.
>
> 상근이와 친구들은 이 게임을 3번 했다. 각 플레이어가 각각 쓴 수가 주어졌을 때, 3번 게임에서 얻은 총 점수를 구하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("5533.txt")

members = int(input())
matrix = []

for _ in range(members):
    matrix.append(list(map(int, input().split())))

for i in range(members):
    sum = 0

    # 모든 참가자들이 총 3번의 게임을 진행할 때
    # 서로 동일하지 않은 값들만 찾아서 + 합산하기
    for j in range(3):
        score = matrix[i][j]
        find = 1   # 1, 0을 판별하는 탐색기에 시작값(1 or 0 둘 중 하나) 입력
        for k in range(members):
            if k == i:    # matrix[i][0] and matrix[k][0] 상황에서
                continue  # i = k 면 비교 대상이 안되니까 패스!
            if matrix[k][j] == score:   # 동일한 값이 발생하면
                find = 0                # 탐색기값은 0이 됨
                break                   # 이때 반복문을 멈추고 반복문 밖으로 나감
        if find == 1:                   # 그게 아니라 find == 1 이라면
            sum += score                # 동일한 값이 발생한게 아니므로 점수에 합산

    print(sum)
```



#### 15953. 상금 헌터

> 2017년에 이어, 2018년에도 카카오 코드 페스티벌이 개최된다!
>
> ![img](https://upload.acmicpc.net/0113dbfe-8ca8-42b8-9a2c-94e136006b75/-/preview/)
>
> 카카오 코드 페스티벌에서 빠질 수 없는 것은 바로 상금이다. 2017년에 개최된 제1회 코드 페스티벌에서는, 본선 진출자 100명 중 21명에게 아래와 같은 기준으로 상금을 부여하였다.
>
> | 순위 | 상금    | 인원 |
> | :--- | :------ | :--- |
> | 1등  | 500만원 | 1명  |
> | 2등  | 300만원 | 2명  |
> | 3등  | 200만원 | 3명  |
> | 4등  | 50만원  | 4명  |
> | 5등  | 30만원  | 5명  |
> | 6등  | 10만원  | 6명  |
>
> 2018년에 개최될 제2회 코드 페스티벌에서는 상금의 규모가 확대되어, 본선 진출자 64명 중 31명에게 아래와 같은 기준으로 상금을 부여할 예정이다.
>
> | 순위 | 상금    | 인원 |
> | :--- | :------ | :--- |
> | 1등  | 512만원 | 1명  |
> | 2등  | 256만원 | 2명  |
> | 3등  | 128만원 | 4명  |
> | 4등  | 64만원  | 8명  |
> | 5등  | 32만원  | 16명 |
>
> ![img](https://upload.acmicpc.net/2ff64533-7387-4294-8dce-03ba3d35b7d4/-/preview/)
>
> 제이지는 자신이 코드 페스티벌에 출전하여 받을 수 있을 상금이 얼마인지 궁금해졌다. 그는 자신이 두 번의 코드 페스티벌 본선 대회에서 얻을 수 있을 총 상금이 얼마인지 알아보기 위해, 상상력을 발휘하여 아래와 같은 가정을 하였다.
>
> - 제1회 코드 페스티벌 본선에 진출하여 *a*등(1 ≤ *a* ≤ 100)등을 하였다. 단, 진출하지 못했다면 *a* = 0으로 둔다.
> - 제2회 코드 페스티벌 본선에 진출하여 *b*등(1 ≤ *b* ≤ 64)등을 할 것이다. 단, 진출하지 못했다면 *b* = 0으로 둔다.
>
> 제이지는 이러한 가정에 따라, 자신이 받을 수 있는 총 상금이 얼마인지를 알고 싶어한다.

```python
# 제이지가 2번의 코테에서 받을 수 있는 상금 합계를
# 원 단위로 출력하자

import sys
sys.stdin = open("15953.txt")

t = int(input())

for i in range(t):

    # 1번째 코테에서 a등, 2번째 코테에서 b등
    # 본선 진출하지 못하면(a > 21, b > 64이면)
    # a, b 는 각각 0으로 초기화

    a, b = map(int, input().split())

    if a == 1:
        a_prize = 5000000
    elif 1 < a <= 3:
        a_prize = 3000000
    elif 3 < a <= 6:
        a_prize = 2000000
    elif 6 < a <= 10:
        a_prize = 500000
    elif 10 < a <= 15:
        a_prize = 300000
    elif 15 < a <= 21:
        a_prize = 100000
    else:
        a_prize = 0

    if b == 1:
        b_prize = 5120000
    elif 1 < b <= 3:
        b_prize = 2560000
    elif 3 < b <= 7:
        b_prize = 1280000
    elif 7 < b <= 15:
        b_prize = 640000
    elif 15 < b <= 31:
        b_prize = 320000
    else:
        b_prize = 0
    
    print(a_prize + b_prize)
```

