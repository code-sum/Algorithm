# 📌2022-07-28 BOJ 풀이



#### 1292. 쉽게 푸는 문제 [(link)](https://www.acmicpc.net/problem/1292)

> 동호는 내년에 초등학교를 입학한다. 그래서 동호 어머니는 수학 선행 학습을 위해 쉽게 푸는 문제를 동호에게 주었다.
>
> 이 문제는 다음과 같다. 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.
>
> 하지만 동호는 현재 더 어려운 문제를 푸느라 바쁘기에 우리가 동호를 도와주자.

```python
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6 ... 의 수열을 상상하자

# 위 수열의 A, B구간이 주어짐
A, B = map(int, input().split())

data = []

for i in range(B+1):      # B까지 순회하는 반복문
    for j in range(i):      # append 작업을 어디서 멈출지 정하기 위해 작성한 이중반복문
        if B == len(data):
            break
        data.append(i)    # 처음부터 B구간까지에 해당하는 모든 요소를 data 에 붙여줌

print(sum(data[A-1:B]))   # 처음부터 A-1구간까지에 해당하는 요소들은 data 에서 제외하려고
                          # 인덱싱 처리를 하고, 남아있는 data 의 요소들을 sum


##############################################
################## 다른 코드 ##################
##############################################

# for문은 많은 탐색을 진행하기 때문에
# while문으로 탐색의 범위를 한정하는게 효율적이다!
# 수열을 만드는 문제는 시간 초과를 조심해야 하니까
# while문 이용해서 조건을 명확하게 잡는게 좋습니다.
```



#### 1302. 베스트셀러 [(link)](https://www.acmicpc.net/problem/1302)

> 김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다. 김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.
>
> 오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

```python
# 입력된 책 목록 중에 가장 많이 입력된 책 이름 출력


import sys
sys.stdin = open("1302.txt")

n = int(input())
list_ = {}

for i in range(n):
    input_ = input()
    if input_ not in list_:
        list_[input_] = 1
    else:
        list_[input_] += 1

freq_ = max(list_.values())
ans = []

for input_, num in list_.items():
    if num == freq_:
        ans.append(input_)

print(sorted(ans)[0])
```



#### 1357. 뒤집힌 덧셈 [(link)](https://www.acmicpc.net/problem/1357)

> 어떤 수 X가 주어졌을 때, X의 모든 자리수가 역순이 된 수를 얻을 수 있다. Rev(X)를 X의 모든 자리수를 역순으로 만드는 함수라고 하자. 예를 들어, X=123일 때, Rev(X) = 321이다. 그리고, X=100일 때, Rev(X) = 1이다.
>
> 두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오

```python
# 첫번째 뒤집기를 쉽게 하기 위해 str으로 형 변환
X, Y = map(str, input().split())

# 뒤집기한 X, Y 를 int로 형 변환해서 더해줌 => 이후 str 으로 형 변환해서 뒤집기 한번 더 할 준비
tem = str(int(X[::-1]) + int(Y[::-1]))

print(tem[::-1])
```



#### 1764. 듣보잡 [(link)](https://www.acmicpc.net/problem/1764)

> 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("1764.txt")

a, b = map(int, input().split())

# a명의 input 와 b명의 input 사이 교집합에 해당하는 사람수, 이름 출력하기

dic = {}

for _ in range(a):
    a_people = input()
    if a_people not in dic:
        dic[a_people] = 1

for _ in range(b):
    b_people = input()
    if b_people in dic:
        dic[b_people] += 1
    else:
        dic[b_people] = 1

ans = []
for b_people, num in dic.items():
    if num == 2:
        ans.append(b_people)
    else:
        continue

print(len(ans))
for i in sorted(ans):
    print(i)
```



#### 3052. 나머지 [(link)](https://www.acmicpc.net/problem/3052)

> 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
>
> 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("3052.txt")

# 입력된 수를 42로 나눈 나머지 담아줄 리스트 생성
arr = []

for i in range(10):
    input_10 = int(input())
    arr.append(input_10 % 42)

# 리스트를 set 으로 바꾸어 중복 제거
remainder = set(arr)

# 서로 다른(=중복되지 않은) 나머지들이 몇 개 있나요?
print(len(remainder))
```



#### 5622. 다이얼 [(link)](https://www.acmicpc.net/problem/5622)

> 상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.
>
> ![img](https://upload.acmicpc.net/9c88dd24-3a4c-4a09-bc50-e6496958214d/-/preview/)
>
> 전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
>
> 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
>
> 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
>
> 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

```python
# 전화기 번호별로 입력된 자판
key = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

# 문자열 입력(인덱스 추적을 위해 list 로 받음)
word = list(input())

# 1번(인덱스 0)은 3초, 2번(인덱스 1)은 4초, 3번(인덱스 2)은 5초 ...
time = 0

for i in word:
    for j in key:
        if i in j:
            time += key.index(j) + 3

print(time)


############################################################

# 딕셔너리를 이용한 방법

# 전화기 자판별로 걸리는 시간을 value에 입력
key = {
    "ABC": 3, 
    "DEF": 4, 
    "GHI": 5, 
    "JKL": 6, 
    "MNO": 7, 
    "PQRS": 8, 
    "TUV": 9, 
    "WXYZ": 10
}

word = input()
time = 0

for i in range(len(word)):
    for j in key.keys():    # .keys() 딕셔너리 key 목록이 담긴 dict_keys 반환
        if word[i] in j:    # 만약 word 의 i번째 문자가 key 중에 있다면
            time += key[j]  # 걸린 시간에 j번째 key 값(value), 다시 말하면 key 의 j번째 값(value)를 더해줌
                            # 작동원리: https://pythontutor.com/render.html#mode=display 참조
print(time)
```



#### 7785. 회사에 있는 사람 [(link)](https://www.acmicpc.net/problem/7785)

> 상근이는 세계적인 소프트웨어 회사 기글에서 일한다. 이 회사의 가장 큰 특징은 자유로운 출퇴근 시간이다. 따라서, 직원들은 반드시 9시부터 6시까지 회사에 있지 않아도 된다.
>
> 각 직원은 자기가 원할 때 출근할 수 있고, 아무때나 퇴근할 수 있다.
>
> 상근이는 모든 사람의 출입카드 시스템의 로그를 가지고 있다. 이 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다. 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("7785.txt")

t = int(sys.stdin.readline())
ans = {}

for _ in range(t):
    name, record = sys.stdin.readline().split()

    if record == "enter":
        ans[name] = 1
    else:
        del ans[name]

ans = sorted(ans.keys(), reverse=True)

for i in ans:
    print(i)
```



#### 10816. 숫자 카드 2 [(link)](https://www.acmicpc.net/problem/10816)

> 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

```python
from sys import stdin
from collections import Counter

n = stdin.readline()
n_cards = stdin.readline().split()
m = stdin.readline()
m_cards = stdin.readline().split()

# 리스트 n_cards 을 Counter에 넣으면 
# N의 요소들의 숫자를 센 Dictionary자료형이 출력
C = Counter(n_cards)

# Counter(n_cards)에 M의 요소가 있다면 해당 숫자를 출력하고 없으면 0을 출력
print(' '.join(f'{C[m]}' if m in C else '0' for m in m_cards))
```



#### 11652. 카드 [(link)](https://www.acmicpc.net/problem/11652)

> 준규는 숫자 카드 N장을 가지고 있다. 숫자 카드에는 정수가 하나 적혀있는데, 적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같다.
>
> 준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오. 만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.

```python
import sys
sys.stdin = open("11652.txt")

dic = {}
n = int(input())

for _ in range(n):
    num = int(input())

    if num not in dic:
        dic[num] = 1
    else:
        dic[num] += 1

dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(dic[0][0])
```



#### 23825. SASA 모형을 만들어보자 [(link)](https://www.acmicpc.net/problem/23825)

> 당신은 SASA 연못에서 알파벳 S 모양의 블록 N개와 알파벳 A 모양의 블록 M개를 건졌다. 태영이는 연못에서 건진 블록을 이용해 학교에 전시할 SASA 모형을 최대한 많이 만들려고 한다.
>
> SASA 모형 1개를 만들기 위해서는, 알파벳 S 모양의 블록 2개와 알파벳 A 모양의 블록 2개가 필요하다. 태영이가 만들 수 있는 SASA 모형 개수의 최댓값을 구하라.

```python
N, M = map(int, input().split())

# Step 1. N, M 둘 중에 가장 작은 값을 골라냄
select = min(N, M)

# Step 2. 위에서 고른 가장 작은 값을 2로 나누었을 때 몫 = SASA 쌍의 최대 개수
print(select//2)
```

