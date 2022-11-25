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