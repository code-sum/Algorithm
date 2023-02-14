# 📌2022-08-02 BOJ 풀이



#### 1269. 대칭차집합 [(link)](https://www.acmicpc.net/problem/1269)

> 자연수를 원소로 갖는 공집합이 아닌 두 집합 A와 B가 있다. 이때, 두 집합의 대칭 차집합의 원소의 개수를 출력하는 프로그램을 작성하시오. 두 집합 A와 B가 있을 때, (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.
>
> 예를 들어, A = { 1, 2, 4 } 이고, B = { 2, 3, 4, 5, 6 } 라고 할 때, A-B = { 1 } 이고, B-A = { 3, 5, 6 } 이므로, 대칭 차집합의 원소의 개수는 1 + 3 = 4개이다.

```python
n, m = map(int, input().split())

# 집합A, 집합B 생성
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# 대칭차집합 원소의 갯수 출력(set의 len() 구하기)
print(len(A-B)+len(B-A))
```



#### 2750. 수 정렬하기 [(link)](https://www.acmicpc.net/problem/2750)

> N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("2750.txt")

# 첫째줄에 수의 개수 n 입력
n = int(input())

num_list = []

# 입력뇌는 n개의 수를 num_list 에 넣은 다음 정렬하기
for i in range(n):
    num_list.append(int(input()))

sorted_list = sorted(num_list)

# 정렬한 리스트의 원소들을 한줄씩 차례대로 출력
for i in range(len(num_list)):
    print(sorted_list[i])
```



#### 2776. 암기왕 [(link)](https://www.acmicpc.net/problem/2776)

> 연종이는 엄청난 기억력을 가지고 있다. 그래서 하루 동안 본 정수들을 모두 기억 할 수 있다. 하지만 이를 믿을 수 없는 동규는 그의 기억력을 시험해 보기로 한다. 동규는 연종을 따라 다니며, 연종이 하루 동안 본 정수들을 모두 ‘수첩1’에 적어 놓았다. 그것을 바탕으로 그가 진짜 암기왕인지 알아보기 위해, 동규는 연종에게 M개의 질문을 던졌다. 질문의 내용은 “X라는 정수를 오늘 본 적이 있는가?” 이다. 연종은 막힘없이 모두 대답을 했고, 동규는 연종이 봤다고 주장하는 수 들을 ‘수첩2’에 적어 두었다. 집에 돌아온 동규는 답이 맞는지 확인하려 하지만, 연종을 따라다니느라 너무 힘들어서 여러분에게 도움을 요청했다. 동규를 도와주기 위해 ‘수첩2’에 적혀있는 순서대로, 각각의 수에 대하여, ‘수첩1’에 있으면 1을, 없으면 0을 출력하는 프로그램을 작성해보자.

```python
import sys
sys.stdin = open("2776.txt")

for _ in range(int(input())):
    c1 = int(input())
    n1 = set(map(int, input().split()))

    c2 = int(input())
    n2 = list(map(int, input().split()))

    for i in n2:
        if i in n1:
            print("1")
        else:
            print("0")
```

