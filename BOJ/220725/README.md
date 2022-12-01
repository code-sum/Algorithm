# 📌 2022-07-25 BOJ 풀이



#### 1000. A+B [(link)](https://www.acmicpc.net/problem/1000)

> 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

```python
A, B = map(int, input().split())
print( A+B )
```



#### 1065. 한수 [(link)](https://www.acmicpc.net/problem/1065)

> 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

```python
# 123 처럼 각 자리수가 등차수열이면 '한수'
# N이 주어졌을 때, 1보다 크거나 같고, 
# N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성

import sys

n = int(sys.stdin.readline())

cnt = 0
for i in range(1, n+1):

    input_ = list(map(int, str(i)))
    if i < 100:
        cnt += 1 # 100보다 작으면 모두 한수

    # 각 자리수가 등차수열이면 한수
    elif input_[0] - input_[1] == input_[1] - input_[2]:
        cnt += 1

print(cnt)
```



#### 1110. 더하기 사이클 [(link)](https://www.acmicpc.net/problem/1110)

> 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.
>
> 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
>
> 위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
>
> N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

```python
# 시작하는 수 26
# 2+6 = 8
# 68 ~ 6+8 = 14
# 84 ~ 8+4 = 12
# 42 ~ 4+2 = 6
# 26 ~ 끝난 수 = 시작하는 수
# 4번째 생성 끝에 원래의 수로 회귀
# 생성 사이클 돌 때마다 cnt += 1 하다가 print(cnt)

import sys

input_ = int(sys.stdin.readline())
n = input_
cnt = 0

while True:
    a = n // 10
    b = n % 10
    c = (a+b) % 10
    n = (b*10) + c

    cnt += 1
    if n == input_:
        break

print(cnt)
```



#### 1330. 두 수 비교하기 [(link)](https://www.acmicpc.net/problem/1330)

> 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

```python
A, B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')
```



#### 10818. 최소, 최대 [(link)](https://www.acmicpc.net/problem/10818)

> N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

```python
n = int(input())

numbers = list(map(int, input().split()))

print(f'{min(numbers)} {max(numbers)}')
```


