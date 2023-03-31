# 📌2022-08-10 BOJ 풀이



#### 1598. 꼬리를 무는 숫자 나열 [(link)](https://www.acmicpc.net/problem/1598)

> 동물원에서 막 탈출한 원숭이 한 마리가 세상구경을 하고 있다. 그 녀석은 원주 부근을 돌아다니다가 코레스코 콘도에서 아주 재밌는 놀이를 발견했다. 그 놀이의 이름은 바로 “꼬리를 무는 숫자 나열”. 이제부터 원숭이가 그토록 좋아하던 그 놀이를 파헤쳐보자.
>
> 놀이의 방법은 간단하다. 일단 4줄짜리 표에 왼쪽부터 수를 아래로 1부터 순서대로 적어나간다. 다음에 그 예가 잘 나타나있다.
>
> ![img](https://www.acmicpc.net/upload/201004/psw1.png)
>
> 이제 원숭이는 두 개의 자연수를 아무거나 생각한다. 그리고 숫자판에서 두 개의 자연수 사이의 직각거리를 구하면 된다. 여기서 직각거리는 동서방향거리와 남북방향거리의 합을 뜻한다.
>
> 예를 들어 저 숫자판에서 11과 33을 생각했다고 하자. 그렇다면 11과 33사이의 직각거리는 8이 된다.(동서방향거리 : 6, 남북방향거리 : 2) 다음 그림에 잘 나타나있다.
>
> ![img](https://www.acmicpc.net/upload/201004/psw2.png)
>
> 하지만 원숭이는 지금 혼란스럽다. 동물원에서 탈출한지 얼마 되지 않아서 계산을 할 수 없는 경지에 이르렀다. 여러분이 불쌍한 원숭이를 좀 도와줘야겠다. 원숭이가 생각한 두 자연수 사이의 직각거리를 구하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("1598.txt")

# start 와 end 사이 직선거리 구하기
start, end = map(int, input().split())

# 시작점, 끝점 -1씩해서 연산하기
start -= 1
end -= 1

# 가로는 4로 나눈 몫(절댓값)으로, 세로는 4로 나눈 나머지(절댓값)로 계산
# print(가로길이 + 세로길이)
print(abs(start//4-end//4) + abs(start%4-end%4))
```



#### 2644. 촌수계산 [(link)](https://www.acmicpc.net/problem/2644)

> 우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.
>
> 여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("2644.txt")

# 첫째 줄에는 전체 사람의 수 N(정점의 수)
N = int(input())

# 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람 start, end
start, end = map(int, input().split())

# 셋째 줄에는 부모 자식들 간의 관계의 개수 M(간선의 수)
M = int(input())

# [무방향 그래프의 인접 리스트 만들기]
# 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x, y가 각 줄에 나온다. 
# 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())  
    graph[x].append(y)
    graph[y].append(x)

# 각 정점을 방문했는지 여부를 판별할 방문 체크 리스트가 필요
# visit 리스트를 따로 선언하여 각 정점을 방문했는지 체크
visit = [0] * (N+1)

# [DFS 함수 정의하기]
result = []
def dfs(v, num):  # 매개변수 v, num에 대하여
    num += 1      # 깊이가 깊어질 때마다 num 값 1씩 증가
    visit[v] = 1  # 시작되는 정점은 방문 처리(1 == True)

    # v == end 일땐 num 값을 result 에 저장
    if v == end:
        result.append(num)

    # 매개변수 v와 연결된 사람들에 대하여 순회할 때,
    for i in graph[v]:

        # visit[i] 결과가 False(= 0) 이면, dfs()를 재귀 호출
        if not visit[i]:
            dfs(i, num)

# [DFS 함수 호출하기]
# dfs(v, num) -> dfs(start, 0) -> 인접 리스트에서 A에 연결된 사람 탐색, num 값은 0부터 시작            
dfs(start, 0)

# result 에 저장된 값이 없다는 것은(if len(result) == 0:)
# 친척 관계가 없어서 촌수 계산이 안된 것이므로 -1 출력
if len(result) == 0:
    print(-1)

else:
    print(result[0] - 1)
```



#### 5576. 콘테스트 [(link)](https://www.acmicpc.net/problem/5576)

> 최근 온라인에서의 프로그래밍 콘테스트가 열렸다. W 대학과 K 대학의 컴퓨터 클럽은 이전부터 라이벌 관계에있어,이 콘테스트를 이용하여 양자의 우열을 정하자라는 것이되었다.
>
> 이번이 두 대학에서 모두 10 명씩이 콘테스트에 참여했다. 긴 논의 끝에 참가한 10 명 중 득점이 높은 사람에서 3 명의 점수를 합산하여 대학의 득점으로하기로 했다.
>
> W 대학 및 K 대학 참가자의 점수 데이터가 주어진다. 이때, 각각의 대학의 점수를 계산하는 프로그램을 작성하라.

```python
import sys
sys.stdin = open("5576.txt")

W = sorted([int(input())for _ in range(10)])[7:]
K = sorted([int(input())for _ in range(10, 20)])[7:]

print(sum(W), sum(K))
```



#### 10101. 삼각형 외우기 [(link)](https://www.acmicpc.net/problem/10101)

> 창영이는 삼각형의 종류를 잘 구분하지 못한다. 따라서 프로그램을 이용해 이를 외우려고 한다.
>
> 삼각형의 세 각을 입력받은 다음, 
>
> - 세 각의 크기가 모두 60이면, Equilateral
> - 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
> - 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
> - 세 각의 합이 180이 아닌 경우에는 Error
>
> 를 출력하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("10101.txt")

angles = []
for _ in range(3):
    angle = int(sys.stdin.readline())
    angles.append(angle)

if sum(angles) == 180:
    if angles[0] == angles[1] == angles[2]:
        print("Equilateral")
    elif angles[0] == angles[1] or angles[1] == angles[2] or angles[2] == angles[0]:
        print("Isosceles")
    else:
        print("Scalene") 
else:
    print("Error")
```



#### 10769. 행복한지 슬픈지 [(link)](https://www.acmicpc.net/problem/10769)

> 승엽이는 자신의 감정을 표현하기 위해서 종종 문자 메시지에 이모티콘을 넣어 보내곤 한다. 승엽이가 보내는 이모티콘은 세 개의 문자가 붙어있는 구조로 이루어져 있으며, 행복한 얼굴을 나타내는 **:-)** 와 슬픈 얼굴을 나타내는 **:-(** 가 있다.
>
> 혜성이는 승엽이의 이모티콘을 귀여운 척이라고 생각해 매우 싫어하므로, 승엽이의 문자가 오면 전체적인 분위기만 판단해서 알려주는 프로그램을 작성하고 싶다.

```python
import sys
sys.stdin = open("10769.txt")

input_ = input()
hap_cnt = 0
sad_cnt = 0

for i in range(0, len(input_) - 2):
    if input_[i] == ":" and input_[i + 1] == "-":
        if input_[i + 2] == ")":
            hap_cnt += 1
        elif input_[i + 2] == "(":
            sad_cnt += 1

if hap_cnt == 0 and sad_cnt == 0:
    print("none")
else:
    if hap_cnt > sad_cnt:
        print("happy")
    elif hap_cnt < sad_cnt:
        print("sad")
    else:
        print("unsure")
```



#### 11724. 연결 요소의 개수 [(link)](https://www.acmicpc.net/problem/11724)

> 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("11724.txt")

# 첫째 줄에 정점의 개수 N과 간선의 개수 M
N, M = map(int, sys.stdin.readline().rstrip("\n").split())

# DFS를 하기 전에, 일단 탐색을 진행할 그래프가 필요
# N, M 주어질 때, 무방향 그래프의 인접 행렬 만들기
graph = [[0] * (N+1) for _ in range(N+1)]
for i in range(M):
    v1, v2 = map(int, sys.stdin.readline().rstrip("\n").split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

# 각 정점을 방문했는지 여부를 판별할 방문 체크 리스트가 필요
# visit 리스트를 따로 선언하여 각 정점을 방문했는지 체크
visit = [0] * (N+1)

# visit 리스트를 순회하면서 방문하지 않은 노드에 dfs 함수를 호출
# dfs()는 2차원 배열인 graph 에서 행 값을 검사
def dfs(i):
    visit[i] = 1  # 시작되는 정점은 방문 처리(1 == True)
    for j in range(1, N+1):
        # 만약 행 값이 1로 인접(연결)되어 있으면, dfs()를 재귀 호출
        if graph[i][j] == 1 and visit[j] == 0:
            dfs(j)

# 파이썬 함수 재귀 호출
# def hello():
#    print('Hello, world!')
#    hello() 
# hello()
# https://dojang.io/mod/page/view.php?id=2352

# visit 리스트를 방문할 때, 0값으로 dfs 함수를 호출할 때마다 cnt 를 1씩 증가
cnt = 0
for i in range(1, N+1):
    if visit[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)
```



#### 14467. 소가 길을 건너간 이유 1 [(link)](https://www.acmicpc.net/problem/14467)

> 닭이 길을 건너간 이유는 과학적으로 깊게 연구가 되어 있지만, 의외로 소가 길을 건너간 이유는 거의 연구된 적이 없다. 이 주제에 관심을 가지고 있었던 농부 존은 한 대학으로부터 소가 길을 건너는 이유에 대한 연구 제의를 받게 되었다.
>
> 존이 할 일은 소가 길을 건너는 것을 관찰하는 것이다. 존은 소의 위치를 N번 관찰하는데, 각 관찰은 소의 번호와 소의 위치 하나씩으로 이루어져 있다. 존은 소를 10마리 가지고 있으므로 소의 번호는 1 이상 10 이하의 정수고, 소의 위치는 길의 왼쪽과 오른쪽을 의미하는 0과 1 중 하나다.
>
> 이 관찰 기록을 가지고 소가 최소 몇 번 길을 건넜는지 알아보자. 즉 같은 번호의 소가 위치를 바꾼 것이 몇 번인지 세면 된다.

```python
# 같은 번호의 소가 위치를 바꾼 것이 몇 번인지 센다
# 소가 길을 건너간 최소 횟수를 출력

import sys
sys.stdin = open("14467.txt")

t = int(input())
dic = {}
cnt = 0

for _ in range(1, t+1):
    # a 는 움직인 소의 번호
    # b 는 왼쪽(0)으로 갔는지, 오른쪽(1)으로 갔는지
    a, b = map(int, input().split())

    # 새로 나타난 소라면 딕셔너리에 키,값 쌍으로 번호,발견위치 추가
    if a not in dic:
        dic[a] = b
    # dic 에 넣은 소가 또 나타났는데
    else:
        # 그 소가 이전과 달리 위치를 바꿨으면
        if dic[a] != b:
            cnt += 1
            dic[a] = b

print(cnt)
```

