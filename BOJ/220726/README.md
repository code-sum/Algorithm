# 📌 2022-07-26 BOJ 풀이



#### 2231. 분해합 [(link)](https://www.acmicpc.net/problem/2231)

> 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
>
> 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

```python
# 첫째 줄에 자연수 N이 주어진다
N = int(input())
d_sum = 0          # 반복문 시작 전에 분해합 연산 초기화

for i in range(1, N+1):
    box = list(map(int, str(i)))   # N의 각 자릿수 숫자를 개별 요소로 갖는 리스트 생성(나중에 연산해야하므로 map ~ int 변환)
    d_sum = i + sum(box)           # N의 분해합
    if d_sum == N:        # N의 분해합 = d_sum 의 생성자일 때, 가장 작은 생성자 도출
        print(i)          # 이때의 생성자(i)를 출력!
        break             # 최소 생성자를 찾았으니 연산도 여기서 멈춤

    if i == N:        # 만약 생성자가 없는 경우 (분해합0 = 생성자0 + 각자리수0 의 구조! 즉, 분해합과 자연수N이 0으로 같을 때)
        print(0)      # 결과는 0을 출력
```



#### 2609. 최대공약수와 최소공배수 [(link)](https://www.acmicpc.net/problem/2609)

> 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

```python
import math     # 최대공약수, 최소공배수 출력하는 함수는 math 라이브러리 이용!

# 첫째 줄에 두 개의 자연수가 주어진다.
n, m = map(int, input().split())   # 두 수 사이에 한 칸의 공백이 주어진다.

print(math.gcd(n, m))   # 첫째 줄에는 두 수의 최대공약수 출력
print(math.lcm(n, m))   # 둘째 줄에는 두 수의 최소공배수 출력


######### 다른 코드 #########
# 시간 복잡도를 줄일 수 있음 #
#############################
a, b = map(int, input().split())

def GCD(a, b):
    while b:
        a, b = b, a % b
    return a
print(GCD(a, b))
def LCM(a, b):
    result = (a * b) // GCD(a, b)
    return result
print(LCM(a, b))
```



#### 2846. 오르막길 [(link)](https://www.acmicpc.net/problem/2846)

> 상근이는 자전거를 타고 등교한다. 자전거 길은 오르막길, 내리막길, 평지로 이루어져 있다. 상근이는 개강 첫 날 자전거를 타고 가면서 일정 거리마다 높이를 측정했다. 상근이는 가장 큰 오르막길의 크기를 구하려고 한다.
>
> 측정한 높이는 길이가 N인 수열로 나타낼 수 있다. 여기서 오르막길은 적어도 2개의 수로 이루어진 높이가 증가하는 부분 수열이다. 오르막길의 크기는 부분 수열의 첫 번째 숫자와 마지막 숫자의 차이이다.
>
> 예를 들어, 높이가 다음과 같은 길이 있다고 하자. 12 3 5 7 10 6 1 11. 이 길에는 2 개의 오르막길이 있다. 밑 줄로 표시된 부분 수열이 오르막길이다. 첫 번째 오르막길의 크기는 7이고, 두 번째 오르막길의 크기는 10이다. 높이가 12와 6인 곳은 오르막길에 속하지 않는다.
>
> 가장 큰 오르막길을 구하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("2846.txt")

n = int(input())
height = list(map(int, input().split()))

# 오르막길들 모두 기록해줄 빈 리스트
up = []

# 개별 오르막 높이를 측정해줄 변수
sum = 0

for i in range(1, n):
    if height[i] > height[i-1]:
        sum += (height[i] - height[i-1])

        # 주어진 input 끝부분에 오르막길이 있는 경우 처리
        if i == n-1:
            up.append(sum)

    else:
        up.append(sum)
        sum = 0

print(max(up))
```



#### 2953. 나는 요리사다 [(link)](https://www.acmicpc.net/problem/2953)

> "나는 요리사다"는 다섯 참가자들이 서로의 요리 실력을 뽐내는 티비 프로이다. 각 참가자는 자신있는 음식을 하나씩 만들어오고, 서로 다른 사람의 음식을 점수로 평가해준다. 점수는 1점부터 5점까지 있다.
>
> 각 참가자가 얻은 점수는 다른 사람이 평가해 준 점수의 합이다. 이 쇼의 우승자는 가장 많은 점수를 얻은 사람이 된다.
>
> 각 참가자가 얻은 평가 점수가 주어졌을 때, 우승자와 그의 점수를 구하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("2953.txt")

dic = {}

for i in range(1, 6):
    score = list(map(int, input().split()))
    sum_score = sum(score)
    dic[i] = sum_score

for k, v in dic.items():
    if max(dic.values()) == v:
        print(k, v)
```

