# 📌BOJ solved.ac CLASS1

>  총 36문제 중 실습기간에 건너뛴 문제들 풀이



#### 1001. A-B [(link)](https://www.acmicpc.net/problem/1001)

> 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

```python
a,b = map(int, input().split())
print(a-b)
```



#### 1008. A/B [(link)](https://www.acmicpc.net/problem/1008)

> 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

```python
a,b = map(int, input().split())
print(a/b)
```



#### 1152. 단어의 개수 [(link)](https://www.acmicpc.net/problem/1152)

> 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

```python
import sys
sys.stdin = open("1152.txt")

words = list(map(str, input().split()))
print(len(words))
```

