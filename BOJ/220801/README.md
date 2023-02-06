# 📌2022-08-01 BOJ 풀이



#### 1076. 저항 [(link)](https://www.acmicpc.net/problem/1076)

> 전자 제품에는 저항이 들어간다. 저항은 색 3개를 이용해서 그 저항이 몇 옴인지 나타낸다. 처음 색 2개는 저항의 값이고, 마지막 색은 곱해야 하는 값이다. 저항의 값은 다음 표를 이용해서 구한다.
>
> | 색     | 값   | 곱            |
> | :----- | :--- | :------------ |
> | black  | 0    | 1             |
> | brown  | 1    | 10            |
> | red    | 2    | 100           |
> | orange | 3    | 1,000         |
> | yellow | 4    | 10,000        |
> | green  | 5    | 100,000       |
> | blue   | 6    | 1,000,000     |
> | violet | 7    | 10,000,000    |
> | grey   | 8    | 100,000,000   |
> | white  | 9    | 1,000,000,000 |
>
> 예를 들어, 저항의 색이 yellow, violet, red였다면 저항의 값은 4,700이 된다.

```python
import sys
sys.stdin = open("1076.txt")

color = ['black', 'brown', 'red', 
'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

a = color.index(input())
b = color.index(input())
c = color.index(input())

# 저항값
o = int(str(a) + str(b)) * (10 ** c)
print(o)
```



#### 2161. 카드1 [(link)](https://www.acmicpc.net/problem/2161)

> N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
>
> 이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
>
> 예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 버린 카드들은 순서대로 1 3 2가 되고, 남는 카드는 4가 된다.
>
> N이 주어졌을 때, 버린 카드들을 순서대로 출력하고, 마지막에 남게 되는 카드를 출력하는 프로그램을 작성하시오.

```python
# 덱 활용하기
from collections import deque

# 첫째 줄에 정수 N(1 ≤ N ≤ 1,000)이 주어진다.
N = int(input())
card = deque(list(range(1, N+1)))

# 버린 카드를 담아줄 빈 리스트 생성
out = []

while card:
    # card 의 첫번째 요소를 popleft하여 out 에 담기 ------ (1) 떼서 버리기
    card_pop = card.popleft()
    out.append(card_pop)

    # card 의 두번째 요소를 card 의 맨 뒤에 append 하기 -- (2) 떼서 뒤에 붙이기
    if card:
        card_pop = card.popleft()
        card.append(card_pop)

# 첫째 줄에 버리는 카드들을 순서대로 출력한다. 
# 제일 마지막에는 남게 되는 카드의 번호를 출력한다.
# 덱으로 묶여있던 out 객체를 * 표기로 풀어서 print
print(*out)
```



#### 2902. KMP는 왜 KMP일까? [(link)](https://www.acmicpc.net/problem/2902)

> KMP 알고리즘이 KMP인 이유는 이를 만든 사람의 성이 Knuth, Morris, Prett이기 때문이다. 이렇게 알고리즘에는 발견한 사람의 성을 따서 이름을 붙이는 경우가 많다.
>
> 또 다른 예로, 유명한 비대칭 암호화 알고리즘 RSA는 이를 만든 사람의 이름이 Rivest, Shamir, Adleman이다.
>
> 사람들은 이렇게 사람 성이 들어간 알고리즘을 두 가지 형태로 부른다.
>
> - 첫 번째는 성을 모두 쓰고, 이를 하이픈(-)으로 이어 붙인 것이다. 예를 들면, Knuth-Morris-Pratt이다. 이것을 긴 형태라고 부른다.
> - 두 번째로 짧은 형태는 만든 사람의 성의 첫 글자만 따서 부르는 것이다. 예를 들면, KMP이다.
>
> 동혁이는 매일매일 자신이 한 일을 모두 메모장에 적어놓는다. 잠을 자기 전에, 오늘 하루 무엇을 했는지 되새겨 보는 것으로 하루를 마감한다.
>
> 하루는 이 메모를 보던 중, 지금까지 긴 형태와 짧은 형태를 섞어서 적어 놓은 것을 발견했다.
>
> 이렇게 긴 형태로 하루 일을 기록하다가는 메모장 가격이 부담되어 파산될 것이 뻔하기 때문에, 앞으로는 짧은 형태로 기록하려고 한다.
>
> 긴 형태의 알고리즘 이름이 주어졌을 때, 이를 짧은 형태로 바꾸어 출력하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("2902_input.txt")

# 긴 형태의 알고리즘 이름이 주어졌을 때, 
# 이를 짧은 형태로 바꾸어 출력하는 프로그램을 작성하시오.

# "-" 로 구분되는 긴 이름 입력
name = list(input().split("-"))

# 짧아진 이름 붙여줄 변수 선언
short_name = ""

for i in name:

    # "-" 이후 첫번째로 등장하는 문자들을 short_name 에 붙이기
    short_name += i[0]        

print(short_name)
```

