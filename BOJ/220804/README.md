# 📌2022-08-04 BOJ 풀이



#### 1547. 공 [(link)](https://www.acmicpc.net/problem/1547)

> 세준이는 컵 3개를 탁자 위에 일렬로 엎어놓았다. 컵의 번호는 맨 왼쪽 컵부터 순서대로 1번, 2번 3번이고, 세준이는 이 컵을 이용해서 게임을 하려고 한다.
>
> 먼저 1번 컵의 아래에 공을 하나 넣는다. 세준이는 두 컵을 고른 다음, 그 위치를 맞바꾸려고 한다. 예를 들어, 고른 컵이 1번과 2번이라면, 1번 컵이 있던 위치에 2번 컵을 이동시키고, 동시에 2번 컵이 있던 위치에 1번 컵을 이동시켜야 한다. 이때 공은 움직이지 않기 때문에, 공의 위치는 맨 처음 1번 컵이 있던 위치와 같다.
>
> 세준이는 컵의 위치를 총 M번 바꿀 것이며, 컵의 위치를 바꾼 방법이 입력으로 주어진다. 위치를 M번 바꾼 이후에 공이 들어있는 컵의 번호를 구하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("1547.txt")

t = int(input())

# 공이 있는 자리 ans
ans = 1

for _ in range(1, t+1):
    a, b = map(int, input().split())
    if a == ans:
        ans = b
    elif b == ans:
        ans = a
    else:
        continue
print(ans)
```



#### 1652. 누울 자리를 찾아라 [(link)](https://www.acmicpc.net/problem/1652)

> 일 년 동안 세계일주를 하던 영식이는 여행을 하다 너무 피곤해서 근처에 있는 코레스코 콘도에서 하룻밤 잠을 자기로 하고 방을 잡았다.
>
> 코레스코 콘도에 있는 방은 NxN의 정사각형모양으로 생겼다. 방 안에는 옮길 수 없는 짐들이 이것저것 많이 있어서 영식이의 누울 자리를 차지하고 있었다. 영식이는 이 열악한 환경에서 누울 수 있는 자리를 찾아야 한다. 영식이가 누울 수 있는 자리에는 조건이 있다. 똑바로 연속해서 2칸 이상의 빈 칸이 존재하면 그 곳에 몸을 양 옆으로 쭉 뻗으면서 누울 수 있다. 가로로 누울 수도 있고 세로로 누울 수도 있다. 누울 때는 무조건 몸을 쭉 뻗기 때문에 반드시 벽이나 짐에 닿게 된다. (중간에 어정쩡하게 눕는 경우가 없다.)
>
> ![img](https://www.acmicpc.net/JudgeOnline/upload/201005/map.PNG)
>
> 만약 방의 구조가 위의 그림처럼 생겼다면, 가로로 누울 수 있는 자리는 5개이고, 세로로 누울 수 있는 자리는 4개 이다. 방의 크기 N과 방의 구조가 주어졌을 때, 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 수를 구하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("1652.txt")

'''
5
....X
..XX.
.....
.XX..
X....
5 4
'''

# 첫째 줄에 방의 크기 N이 주어진다.
n = int(input())

matrix = []
r, c = 0, 0
cnt = 0

# input 받기
for _ in range(n):
    matrix.append(list(input()))

# 가로 누울 자리 세기
for i in range(n):
    cnt = 0
    for j in range(n):
        if matrix[i][j] == ".":
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            r += 1

# 세로 누울 자리 세기
for i in range(n):
    cnt = 0
    for j in range(n):
        if matrix[j][i] == ".":
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            c += 1

print(r, c)
```
