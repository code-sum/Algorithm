# 📌2022-08-08 BOJ 풀이



#### 1436. 영화감독 숌 [(link)](https://www.acmicpc.net/problem/1436)

> 666은 종말을 나타내는 수라고 한다. 따라서, 많은 블록버스터 영화에서는 666이 들어간 제목을 많이 사용한다. 영화감독 숌은 세상의 종말 이라는 시리즈 영화의 감독이다. 조지 루카스는 스타워즈를 만들 때, 스타워즈 1, 스타워즈 2, 스타워즈 3, 스타워즈 4, 스타워즈 5, 스타워즈 6과 같이 이름을 지었고, 피터 잭슨은 반지의 제왕을 만들 때, 반지의 제왕 1, 반지의 제왕 2, 반지의 제왕 3과 같이 영화 제목을 지었다. 하지만 숌은 자신이 조지 루카스와 피터 잭슨을 뛰어넘는다는 것을 보여주기 위해서 영화 제목을 좀 다르게 만들기로 했다.
>
> 종말의 수란 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수를 말한다. 제일 작은 종말의 수는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... 이다. 따라서, 숌은 첫 번째 영화의 제목은 "세상의 종말 666", 두 번째 영화의 제목은 "세상의 종말 1666"와 같이 이름을 지을 것이다. 일반화해서 생각하면, N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 수) 와 같다.
>
> 숌이 만든 N번째 영화의 제목에 들어간 수를 출력하는 프로그램을 작성하시오. 숌은 이 시리즈를 항상 차례대로 만들고, 다른 영화는 만들지 않는다.

```python
# 첫째 줄에 숫자 N이 주어진다
N = int(input())

# 종말의 숫자란 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수
# 666, 1666, 2666, 3666 ...
# 차례대로 진행할 때 N번째 종말의 숫자는?
# 666을 포함하는 수 가운데, 몇번째 숫자인가를 탐색하는 문제

cnt = 0
target_number = 666

while 1:
    if '666' in str(target_number):
        cnt +=1

    # 만약 '666'이 들어간 N번째 수를 찾으면:
    if cnt == N:
        print(target_number)
        break
    target_number += 1
```



#### 1453. 피시방 알바 [(link)](https://www.acmicpc.net/problem/1453)

> 세준이는 피시방에서 아르바이트를 한다. 세준이의 피시방에는 1번부터 100번까지 컴퓨터가 있다.
>
> 들어오는 손님은 모두 자기가 앉고 싶은 자리에만 앉고싶어한다. 따라서 들어오면서 번호를 말한다. 만약에 그 자리에 사람이 없으면 그 손님은 그 자리에 앉아서 컴퓨터를 할 수 있고, 사람이 있다면 거절당한다.
>
> 거절당하는 사람의 수를 출력하는 프로그램을 작성하시오. 자리는 맨 처음에 모두 비어있고, 어떤 사람이 자리에 앉으면 자리를 비우는 일은 없다.

```python
'''
3
1 2 3
출력 0
'''


# 첫째 줄에 손님의 수 N이 주어진다.
N = int(input())

# 둘째 줄에 손님이 들어오는 순서대로 각 손님이 앉고 싶어하는 자리 입력
location = list(map(int, input().split()))

# 1번부터 100번까지 PC방 자리
PC = [0] * 101

# 손님이 외친 자리에 사진이 없으면 그 손님은 자리 차지,
# 만약 선점한 사람이 있으면 거절 당함!  ->   거절당하는 수를 출력

cnt = 0 # 거절
for i in location:
    if PC[i] != 0:
        cnt += 1
    else:
        PC[i] += 1

print(cnt)
```



#### 1543. 문서검색 [(link)](https://www.acmicpc.net/problem/1543)

> 세준이는 영어로만 이루어진 어떤 문서를 검색하는 함수를 만들려고 한다. 이 함수는 어떤 단어가 총 몇 번 등장하는지 세려고 한다. 그러나, 세준이의 함수는 중복되어 세는 것은 빼고 세야 한다. 예를 들어, 문서가 abababa이고, 그리고 찾으려는 단어가 ababa라면, 세준이의 이 함수는 이 단어를 0번부터 찾을 수 있고, 2번부터도 찾을 수 있다. 그러나 동시에 셀 수는 없다.
>
> 세준이는 문서와 검색하려는 단어가 주어졌을 때, 그 단어가 최대 몇 번 중복되지 않게 등장하는지 구하는 프로그램을 작성하시오.

```python
import sys

input_ = sys.stdin.readline().strip()
word = sys.stdin.readline().strip()

len_word = len(word)
index_, cnt = 0, 0

while True:
    index_ = input_.find(word, index_)
    if index_ == -1:
        break
    cnt += 1
    index_ += len_word

print(cnt)
```



#### 2178. 미로 탐색 [(link)](https://www.acmicpc.net/problem/2178)

> N×M크기의 배열로 표현되는 미로가 있다.
>
> | 1    | 0    | 1    | 1    | 1    | 1    |
> | ---- | ---- | ---- | ---- | ---- | ---- |
> | 1    | 0    | 1    | 0    | 1    | 0    |
> | 1    | 0    | 1    | 0    | 1    | 1    |
> | 1    | 1    | 1    | 0    | 1    | 1    |
>
> 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
>
> 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

```python
from collections import deque
import sys

sys.stdin = open("2178.txt")

n, m = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(n)]

visit = [[False] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]  # 거리 +1 씩, 마지막에 출력할 매트릭스
queue = deque()
queue.append((0, 0))  # 시작점
dist[0][0] = 1  # 시작점 거리는 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:  # 그래프 벗어나지 않도록 범위 설정
            if (
                visit[nx][ny] == False and matrix[nx][ny] == 1
            ):  # 방문노드가 아니고, matrix에 1이 있는위치면 위치 변경
                queue.append((nx, ny))
                dist[nx][ny] += dist[x][y] + 1  # dist에서 x, y는 1이므로, +1 늘려줌 (2)
                visit[nx][ny] = True  # 방문처리

print(dist[n - 1][m - 1])  # n, m 은 갯수이므로 행렬에서는 -1씩
```



#### 2309. 일곱난쟁이 [(link)](https://www.acmicpc.net/problem/2309)

> 왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.
>
> 아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.
>
> 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("2309.txt")

# 일곱명의 난쟁이 키 합계 = 100
# 아홉명 중에 이 합계를 만족하는 일곱명 선택하기

# conbinations 라이브러리를 이용한다!
import itertools

# 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다.
heights = [int(input()) for _ in range(9)]

# 중복없이 7명을 선택
for i in itertools.combinations(heights, 7):

    # 만약 i 값들의 합계가 100이라면:
    if sum(i) == 100:

        # 선택했던 7명을 오름차순으로 정렬하여 출력
        for j in sorted(i):
            print(j)
        break
```



#### 2615. 오목 [(link)](https://www.acmicpc.net/problem/2615)

> 오목은 바둑판에 검은 바둑알과 흰 바둑알을 교대로 놓아서 겨루는 게임이다. 바둑판에는 19개의 가로줄과 19개의 세로줄이 그려져 있는데 가로줄은 위에서부터 아래로 1번, 2번, ... ,19번의 번호가 붙고 세로줄은 왼쪽에서부터 오른쪽으로 1번, 2번, ... 19번의 번호가 붙는다.
>
> ![img](https://upload.acmicpc.net/42c87203-247a-49d1-bc63-44397a7184db/-/preview/)
>
> 위의 그림에서와 같이 같은 색의 바둑알이 연속적으로 다섯 알을 놓이면 그 색이 이기게 된다. 여기서 연속적이란 가로, 세로 또는 대각선 방향 모두를 뜻한다. 즉, 위의 그림은 검은색이 이긴 경우이다. 하지만 여섯 알 이상이 연속적으로 놓인 경우에는 이긴 것이 아니다.
>
> 입력으로 바둑판의 어떤 상태가 주어졌을 때, 검은색이 이겼는지, 흰색이 이겼는지 또는 아직 승부가 결정되지 않았는지를 판단하는 프로그램을 작성하시오. 단, 검은색과 흰색이 동시에 이기거나 검은색 또는 흰색이 두 군데 이상에서 동시에 이기는 경우는 입력으로 들어오지 않는다.

```python
from pprint import pprint
import sys

sys.stdin = open("2615.txt")

# 상 -> y -= 1
# 하 -> y += 1

# 우 하 우상 우하
dy = [0, 1, -1, 1]
dx = [1, 0, 1, 1]
BLACK = 1
WHITE = 2
N = 19

board = []

# 오목판 상황 입력
for _ in range(N):
    # 하나의 행을 입력
    temp_list = list(map(int, input().split()))
    board.append(temp_list)

# 무승부가 발생했을 때 출력하기 위한 값
ans = 0

# 이중 반복문
for y in range(N):
    for x in range(N):

        # 검은색돌이나 흰색돌일때만 델타 탐색을 수행
        if board[y][x] == 1 or board[y][x] == 2:

            # 델타 탐색
            for d in range(4):
                # 방향이 바뀔 때마다 동일한 색의 돌의 개수 초기화(1)
                stone_count = 1

                # 다음 좌표 탐색
                ny = y + dy[d]
                nx = x + dx[d]

                while True:
                    # 인덱스 조건, 범위를 벗어나면 탈출
                    if not (-1 < ny < N and -1 < nx < N):
                        break

                    # 같은 색(값) 돌인지 확인하는 조건, 다른 색 돌이면 탈출
                    if board[y][x] != board[ny][nx]:
                        break

                    # 같은 값이고 범위를 벗어나지 않으면 같은 색 돌의 수 + 1
                    stone_count += 1

                    # 같은 방향 다음 좌표를 탐색
                    ny = ny + dy[d]
                    nx = nx + dx[d]

                # 돌의 개수가 5개라면
                if stone_count == 5:

                    # 이전 좌표
                    # 기준 좌표(y, x) 에서 델타 값을 마이너스
                    prev_y = y - dy[d]
                    prev_x = x - dx[d]

                    # 육목인지 판단
                    # 조건 1. 이전좌표가 범위를 벗어나면 오목
                    # if not(-1 < prev_y < N and -1 < prev_x < N):

                    # 조건 2. 기준 좌표의 값과 이전 좌표의 값이 다르면 오목
                    # if board[y][x] != board[prev_y][prev_x]:

                    # 조건 1과 조건2를 만족하면 오목이 완성
                    if (
                        not (-1 < prev_y < N and -1 < prev_x < N)
                        or board[y][x] != board[prev_y][prev_x]
                    ):
                        # 현재 돌의 색 출력
                        print(board[y][x])

                        # 현재 돌의 좌표를 출력
                        print(y + 1, x + 1)

                        # ans 값 갱신
                        # 승패가 결정났기 때문에 ans 값 출력 X
                        ans = board[y][x]

                        # 실제 코딩테스트에서 사용이 불가능한 방법
                        # exit(0)


# 전체를 반복했는데 무승부일 때 0 출력
if ans == 0:
    print(ans)
```



#### 2798. 블랙잭 [(link)](https://www.acmicpc.net/problem/2798)

> 카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 있다.
>
> 한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.
>
> 김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.
>
> 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
>
> N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

```python
import sys
sys.stdin = open("2798.txt")

'''
5 21
5 6 7 8 9
'''

# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다.
N, M = map(int, input().split())

# 둘째 줄에는 카드에 쓰여 있는 수가 주어진다.
list_ = list(map(int, input().split()))

# N장의 카드 중에 3장의 카드 고르기 = 3중 for문
result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):

            # 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
            if list_[i] + list_[j] + list_[k] > M:
                continue
            else:
                result = max(result, list_[i] + list_[j] + list_[k])
print(result)
```



#### 3046. R2 [(link)](https://www.acmicpc.net/problem/3046)

> 두 숫자 R1과 R2가 있을 때, 두 수의 평균 S는 (R1+R2)/2와 같다. 상근이는 정인이 생일 선물로 두 숫자 R1과 R2를 주려고 한다. 생일 파티에서 상근이는 정인이에게 이 두 숫자를 말해주고, 정인이는 이 숫자를 받아 적는다. 그리고 나서 기쁜 마음으로 1년동안 이 숫자를 외우면서 산다.
>
> 상근이는 R1과 R2를 엄청난 고민 끝에 정했다. 작년에는 R1과 R2를 까먹어서 아무 숫자나 정해서 주었기 때문에, 올해는 까먹지 않기 위해서 평균 S도 같이 기억하려고 한다.
>
> 오늘은 정인이 생일이다. 5분 후에 상근이는 생일 선물로 두 숫자 R1과 R2를 말해주어야 하지만, 안타깝게도 R2를 까먹고 말았다. 하지만 R1과 S는 기억하고 있다!
>
> 상근이를 도와 R2가 몇 인지 구하는 프로그램을 작성하시오.

```python
# 첫째 줄에 두 정수 R1과 S가 주어진다.
# 두 수는 -1000보다 크거나 같고, 1000보다 작거나 같다.

R1, S = map(int, input().split())

R2 = 2*S - R1

print(R2)
```



#### 5800. 성적 통계 [(link)](https://www.acmicpc.net/problem/5800)

> 한상덕은 이번에 중덕 고등학교에 새로 부임한 교장 선생님이다. 교장 선생님으로서 첫 번째 일은 각 반의 수학 시험 성적의 통계를 내는 일이다.
>
> 중덕 고등학교 각 반의 학생들의 수학 시험 성적이 주어졌을 때, 최대 점수, 최소 점수, 점수 차이를 구하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("5800.txt")

'''
2
5 30 25 76 23 78
6 25 50 70 99 70 90
'''

K = int(input())

for k in range(1, K+1):
    class_score = list(map(int, input().split()))

    # class_score 에서 점수만 따로 떼어내기
    scores = class_score[1:]
    scores_sorted = sorted(scores) # 내림차순 정렬

    # 인접한 두 수의 차이 중에 가장 큰 값 찾기
    gap = 0
    for i in range(0, len(scores_sorted)-1):
        if scores_sorted[i+1] - scores_sorted[i] > gap:
            gap = scores_sorted[i+1] - scores_sorted[i]
    
    # 두 줄로 출력
    print(f'Class {k}')
    print(f'Max {max(scores_sorted)}, Min {min(scores_sorted)}, Largest gap {gap}')
```



#### 9325. 얼마? [(link)](https://www.acmicpc.net/problem/9325)

> 해빈이는 학교를 다니면서 틈틈히 번 돈으로 자동차를 사려고 한다. 자동차에 여러 가지 옵션을 포함시킬 수 있는데 해빈이는 덧셈과 곱셈을 하지 못하기 때문에 친구 태완이에게 도움을 청했다. 하지만 태완이도 덧셈과 곱셈을 못한다. 불쌍한 이 두 친구를 위해 모든 옵션이 주어진 자동차를 구매하는데 필요한 액수를 계산해 주자.

```python
import sys
sys.stdin = open("9325.txt")

n = int(input())

for _ in range(n):
    s = int(input())
    n = int(input())

    total_price = s
    for i in range(n):
        q, p = map(int, input().split())
        total_price += q*p
    print(total_price)
```



#### 11170. 0의 개수 [(link)](https://www.acmicpc.net/problem/11170)

> N부터 M까지의 수들을 종이에 적었을 때 종이에 적힌 0들을 세는 프로그램을 작성하라.
>
> 예를 들어, N, M이 각각 0, 10일 때 0을 세면 0에 하나, 10에 하나가 있으므로 답은 2이다.

```python
import sys
sys.stdin = open("11170.txt")

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    # N부터 M까지의 수를 str 으로 저장
    cnt = 0
    for i in range(N, M+1):
        word = str(i)
        # 0의 개수를 count
        cnt += word.count('0')

    # 각 테스트 케이스마다 N부터 M까지 0의 개수 출력
    print(cnt)
```

