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



#### 2438. 별 찍기 - 1 [(link)](https://www.acmicpc.net/problem/2438)

> 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

```python
# 첫째줄에 n이 주어짐
n = int(input())

result = ''

for i in range(n):
    result += "*"

    print(result)
```



#### 2439. 별 찍기 - 2 [(link)](https://www.acmicpc.net/problem/2439)

> 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
>
> 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

```python
n = int(input())

for i in range(1, n+1):
    print(" "*(n-i) + "*"*i)
```



#### 2480. 주사위 세개 [(link)](https://www.acmicpc.net/problem/2480)

> 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
>
> 1. 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
> 2. 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
> 3. 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
>
> 예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다. 3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.
>
> 3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.

```python
a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a*1000)
elif a == b:
    print(1000 + a*100)
elif a == c:
    print(1000 + a*100)
elif b == c:
    print(1000 + b*100)
else:
    print(100 * max(a,b,c))
```



#### 2558. A+B - 2 [(link)](https://www.acmicpc.net/problem/2558)

> 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

```python
A = int(input())
B = int(input())

print( A+B )
```



#### 2577. 숫자의 개수 [(link)](https://www.acmicpc.net/problem/2577)

> 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
>
> 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

```python
A = int(input())
B = int(input())
C = int(input())

result = A*B*C
count = [0]*10    # 0부터 9까지 숫자의 등장 횟수를 의미하는 리스트

while True:
    count[result % 10] += 1   # A*B*C의 1의 자리 확인, 이걸 리스트의 인덱스로 1씩 증가
    result //= 10             # 1의 자릿수 다시 확인
    if result == 0:           # result == 0 일때 반복문 종료
        break

for i in range(10):
    print(count[i])            # count[] 가 가진 인덱스 값 출력
```



#### 2739. 구구단 [(link)](https://www.acmicpc.net/problem/2739)

> N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

```python
N = int(input())

for i in range(1, 10):
    result = N*i

    print(f'{N} * {i} = {result}')
```



#### 2741. N 찍기 [(link)](https://www.acmicpc.net/problem/2741)

> 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

```python
N = int(input())

for i in range(1, N+1):
    print(i)
```



#### 2742. 기찍 N [(link)](https://www.acmicpc.net/problem/2742)

> 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

```python
N = int(input())

for i in range(1, N+1):
    print(N+1-i)
```



#### 2753. 윤년 [(link)](https://www.acmicpc.net/problem/2753)

> 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
>
> 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
>
> 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.

```python
year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(1)
else:
    print(0)
```



#### 2908. 상수 [(link)](https://www.acmicpc.net/problem/2908)

> 상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다. 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다. 상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.
>
> 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.
>
> 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

```python
A, B = input().split()

int_A = int(A[::-1])    # 상수가 거꾸로 읽은 수들을 비교해야하므로
int_B = int(B[::-1])    # int 형 변환

if int_A > int_B:
    print(int_A)
else:
    print(int_B)
```



#### 8393. 합 [(link)](https://www.acmicpc.net/problem/8393)

> n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

```python
n = int(input())

sum = 0
for i in range(1, n+1):
    sum += i

print(sum)
```



#### 8958. OX퀴즈 [(link)](https://www.acmicpc.net/problem/8958)

> "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
>
> "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
>
> OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

```python
# 첫째 줄에 테스트 케이스의 개수
test_case = int(input())

for _ in range(test_case):
    OX = input()
    score = 0
    count = 0
    for i in range(len(OX)):
        if OX[i] == "O":
            count += 1
            score += count
        if OX[i] == "X":
            count = 0
    print(score)
```



#### 9498. 시험 성적 [(link)](https://www.acmicpc.net/problem/9498)

> 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

```python
score = int(input())

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
```



#### 10818. 최소, 최대 [(link)](https://www.acmicpc.net/problem/10818)

> N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

```python
n = int(input())

numbers = list(map(int, input().split()))

print(f'{min(numbers)} {max(numbers)}')
```



#### 10871. X보다 작은 수 [(link)](https://www.acmicpc.net/problem/10871)

> 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("10871.txt")

N, X = map(int, input().split())
A = list(map(int, input().split()))

# A에서 X보다 작은 수를 입력받은 순서대로 공백 구분해 출력
new_A = []
for i in A:
    if i < X:
        new_A.append(i)
    else:
        continue

print(*new_A, end=' ')
```



#### 10950. A+B - 3 [(link)](https://www.acmicpc.net/problem/10950)

> 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("10950_input.txt", "r")

test_case = int(input())
for _ in range(test_case):
    a, b = map(int, input().split())
    print( a+b )
```

