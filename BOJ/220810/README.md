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
