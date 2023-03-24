# 📌2022-08-09 BOJ 풀이



#### 1264. 모음의 개수 [(link)](https://www.acmicpc.net/problem/1264)

> 영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자이다.

```python
import sys
sys.stdin = open("1264.txt")

# 입력은 여러 개의 테스트 케이스로 이루어져 있으며, 
# 각 줄마다 영어 대소문자, ',', '.', '!', '?', 공백으로 이루어진 문장

while True:
    text = input()
    if text == '#':
        break

    cnt = 0
    for i in text:
        if i in 'AEIOUaeiou':
            cnt += 1
    print(cnt)
```



#### 1371. 가장 많은 글자 [(link)](https://www.acmicpc.net/problem/1371)

> 영어에서는 어떤 글자가 다른 글자보다 많이 쓰인다. 예를 들어, 긴 글에서 약 12.31% 글자는 e이다.
>
> 어떤 글이 주어졌을 때, 가장 많이 나온 글자를 출력하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("1371.txt")

# 어떤 글이 주어졌을 때, 가장 많이 나온 글자를 출력

# std.stdin.readline() 이용해서 개행문자 \n 이 같이 입력받기
text = sys.stdin.read()

# 길이의 결과값을 저장할 리스트
# ord('a') 는 91, ord('z')는 122 값을 갖기 때문에(알파벳이 26글자)
# 크기가 26인 리스트를 생성
list_ = [0]*26

# 소문자이면, ord() 함수 이용해서 알파벳을 아스키코드로 바꾸기
# 아스키코드 97~122 는 알파벳 소문자 a~z
for i in text:
    if i.islower():
        # i가 알파벳 소문자에 해당하면 아스키코드로 바꿔서 a~z 를 표현한 리스트에 1씩 카운트
        list_[ord(i)-97] += 1

for j in range(26):

    # 1씩 카운트하던 값중에 max 가 등장하면
    # chr() 함수 이용해서 해당 아스키코드에 연동된 문자로 바꾸기
    if list_[j] == max(list_):

        # 출력값 여러 개일 경우 알파벳 순으로 앞서는 것부터 모두 '공백없이' 출력
        print(chr(j+97), end='')
```



#### 1526. 가장 큰 금민수 [(link)](https://www.acmicpc.net/problem/1526)

> 은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.
>
> N이 주어졌을 때, N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램을 작성하시오.

```python
N = int(input())

while True:

    # str(N)의 길이 = str(N)에서 4가 들어있는 개수 + 7이 들어있는 개수
    if len(str(N)) == str(N).count('4') + str(N).count('7'):
        print(N)
        break
    
    # N 에서 1씩 빼내려가면서 N보다 작거나 같은 조건값을 계속 추적
    N -= 1
```



#### 2587. 대표값2 [(link)](https://www.acmicpc.net/problem/2587)

> 어떤 수들이 있을 때, 그 수들을 대표하는 값으로 가장 흔하게 쓰이는 것은 평균이다. 평균은 주어진 모든 수의 합을 수의 개수로 나눈 것이다. 예를 들어 10, 40, 30, 60, 30의 평균은 (10 + 40 + 30 + 60 + 30) / 5 = 170 / 5 = 34가 된다.
>
> 평균 이외의 또 다른 대표값으로 중앙값이라는 것이 있다. 중앙값은 주어진 수를 크기 순서대로 늘어 놓았을 때 가장 중앙에 놓인 값이다. 예를 들어 10, 40, 30, 60, 30의 경우, 크기 순서대로 늘어 놓으면
>
> 10 30 30 40 60
>
> 이 되고 따라서 중앙값은 30이 된다.
>
> 다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("2587.txt")

import math

# 첫째 줄부터 다섯 번째 줄까지 한 줄에 하나씩 자연수가 주어진다.
numbers = []

for _ in range(5):
    numbers.append(int(input()))
    s_numbers = sorted(numbers)

# 평균과 중앙값은 모두 자연수이다.
print(math.trunc((sum(s_numbers))/5))
print(s_numbers[2])
```



#### 2606. 바이러스 [(link)](https://www.acmicpc.net/problem/2606)

> 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
>
> 예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.
>
> ![img](https://www.acmicpc.net/upload/images/zmMEZZ8ioN6rhCdHmcIT4a7.png)
>
> 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("2606.txt")

# 첫째줄에 컴퓨터의 수(노드)
n = int(input())

# 둘째줄에 직접 연결된 컴퓨터 쌍의 수(간선)
m = int(input())

# 이어서 한 줄에 한 쌍씩 직접 연결된 컴퓨터 번호 쌍 입력
# 입력된 쌍을 매트릭스 g 에 표현하기
g = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    v1, v2 = map(int, input().split())
    g[v1][v2] = 1
    g[v2][v1] = 1

# 각 정점을 방문했는지 여부 판별할 체크리스트 visit 선언
visit = [0]*(n+1)

def dfs(i):
    visit[i] = 1  # 시작되는 정점 방문 처리(1==True)
    for j in range(n+1):
        if g[j][i] == 1 and visit[j] == 0:
            dfs(j)

# 1번 컴퓨터가 감염
dfs(1)

# 1번 컴퓨터 제외하고 감염된 나머지 컴퓨터의 수 출력
print(sum(visit)-1)
```



#### 2897. 몬스터 트럭 [(link)](https://www.acmicpc.net/problem/2897)

> 해빈이가 드디어 면허를 땄다! 해빈이의 부모님은 기뻐하며 해빈이에게 첫 차로 몬스터 트럭을 사 주셨다. 해빈이는 자신의 첫 차가 강남 대로의 모든 차를 부수면서 러시 아워조차 자신을 막을 수 없다는 것을 깨닫고 기뻐했지만, 차가 다른 차들의 네 배 크기이기 때문에 주차하는 데 애를 먹고 있었다.
>
> 그걸 본 준규는 마침 강남에서 공영 주차장 아르바이트를 하고 있기 때문에 정기적으로 해빈이에게 강남 주차장 지도를 보내주기로 했다. 지도는 R행 C열의 표로 이뤄져 있다. 표의 각 칸은 빌딩('#'), 주차 된 차('X'), 또는 빈 주차 공간('.')이다. 해빈이의 차는 꽤 커서 정확히 2행 2열의 칸을 차지한다.
>
> 해빈이를 도와 가능한 주차 공간을 해빈이가 부숴야 하는 차의 수대로 모아서 보여주자. 이때 주차하기 위해 부숴야 하는 차만 고려한다. (주차 하러 가는 길에 부수는 차는 신경쓰지 않는다.) 단, 아무리 몬스터 트럭이라도 빌딩을 부술 수는 없기 때문에 빌딩이 있는 자리에는 주차를 할 수 없다.

```python
# 델타탐색 문제
# 0) [0] * 5 의 저장 리스트를 만들어서 0대, 1대, 2대 ... 부술 때마다 += 1
# 1) dy, dx 델타 배열을 먼저 만듬
#    주어진 문제에서 8방위 중에 어디를 탐색할지 생각해보면,
#    한 점을 기준으로, 우, 우하, 하 3방향을 탐색하면 됨
#    이때, 탐색 방향은 좌에서 우로, 위에서 아래로
#    나머지 방향은 탐색할 필요없음
#    우, 우하, 하 : x+1 ,(y+1,x+1), y+1
# 2) 문제에서 고려할 조건은 2가지
#    먼저, 빌딩(#)이 있으면 주차를 할 수 없다(=기준좌표가 될수없다)
#    그 다음, 기준좌표에 차(X)가 있으면 부순 차의 개수 +1 상태로 시작

import sys

sys.stdin = open("2897.txt")

dx = [0, 1, 1]
dy = [1, 1, 0]
BUILDING = "#"
CAR = "X"
VOID = "."

# 숫자가 공백으로 나뉘어져있는 입력
X, Y = list(map(int, input().split()))

list_ = []

# X 줄 만큼의 리스트를 입력
for _ in range(X):
    # 숫자 X 문자 O
    # 공백 X
    temp_list = list(input())
    list_.append(temp_list)

# 부순 횟수를 저장할 리스트
# 0개 1개 2개 3개 4개 부순횟수를 저장
break_count_list = [0] * 5

# 이중 반복문
for x in range(X):
    for y in range(Y):
        # 차를 부순 횟수는 탐색을 할 때마다 초기화(0)
        break_count = 0

        # 조건 1. 기준 좌표가 빌딩(#)이면 안된다.
        if list_[x][y] == BUILDING:
            # 이 다음 반복문의 코드들을 무시하고, 다음 값을 탐색
            continue

        # 성립이 안되는 조건들은 continue로 지나가고,
        # 조건이 성립될 때만 정상적인 코드를 실행한다.

        # 조건 2. 기준 좌표가 차라면 부순 횟수 + 1
        if list_[x][y] == CAR:
            break_count += 1

        """
        델타탐색을 하는 로직
        """
        for d in range(3):
            next_x = x + dx[d]
            next_y = y + dy[d]

            # 조건 1. 범위를 벗어나면 안된다.
            if not (-1 < next_x < X and -1 < next_y < Y):
                break

            # 조건 2. 탐색 좌표에 빌딩이 있으면 안된다.
            if list_[next_x][next_y] == BUILDING:
                break

            # 조건 3. 탐색 좌표에 차가 있으면 부순 횟수를 + 1
            if list_[next_x][next_y] == CAR:
                break_count += 1

        # break를 만나지 않고 for문이 끝났다면
        # 혜빈이가 정상적으로 주차를 했다는 소리
        else:
            break_count_list[break_count] += 1

# print(break_count_list)
# 정답 출력
for count in break_count_list:
    print(count)
```



#### 9610. 사분면 [(link)](https://www.acmicpc.net/problem/9610)

> 2차원 좌표 상의 여러 점의 좌표 (x,y)가 주어졌을 때, 각 사분면과 축에 점이 몇 개 있는지 구하는 프로그램을 작성하시오.
>
> ![img](https://www.acmicpc.net/upload/images/quad.png)

```python
import sys
sys.stdin = open("9610.txt")

# 첫째 줄에 점의 개수 n (1 ≤ n ≤ 1000)이 주어진다.
n = int(input())

cnt_1 = 0
cnt_2 = 0
cnt_3 = 0
cnt_4 = 0
cnt_axis = 0

for _ in range(n):
    x, y = map(int, input().split())
    
    if x > 0 and y > 0:
        cnt_1 += 1
    
    if x < 0 and y > 0:
        cnt_2 += 1

    if x < 0 and y < 0:
        cnt_3 += 1

    if x > 0 and y < 0:
        cnt_4 += 1
    
    if x == 0 or y == 0:
        cnt_axis += 1
        continue

print(f'Q1: {cnt_1} \nQ2: {cnt_2} \nQ3: {cnt_3} \nQ4: {cnt_4} \nAXIS: {cnt_axis}')
```

