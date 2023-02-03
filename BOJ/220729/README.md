# 📌2022-07-29 BOJ 풀이



#### 10952. A+B - 5 [(link)](https://www.acmicpc.net/problem/10952)

> 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("10952_input.txt")

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(A+B)
```

