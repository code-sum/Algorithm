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



#### 1546. 평균 [(link)](https://www.acmicpc.net/problem/1546)

> 세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
>
> 예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
>
> 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("1546.txt")

n = int(input())
scores = list(map(int, input().split()))
scores2 = []

for i in scores:
    scores2.append((i/max(scores))*100)
print(sum(scores2)/n)
```



#### 2475. 검증수 [(link)](https://www.acmicpc.net/problem/2475)

> 컴퓨터를 제조하는 회사인 KOI 전자에서는 제조하는 컴퓨터마다 6자리의 고유번호를 매긴다. 고유번호의 처음 5자리에는 00000부터 99999까지의 수 중 하나가 주어지며 6번째 자리에는 검증수가 들어간다. 검증수는 고유번호의 처음 5자리에 들어가는 5개의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지이다.
>
> 예를 들어 고유번호의 처음 5자리의 숫자들이 04256이면, 각 숫자를 제곱한 수들의 합 0+16+4+25+36 = 81 을 10으로 나눈 나머지인 1이 검증수이다.

```python
numbers = list(map(int, input().split()))
ans = 0

for i in numbers:
    ans += i**2

print(ans%10)
```



#### 2557. Hello World [(link)](https://www.acmicpc.net/problem/2557)

> Hello World!를 출력하시오.

```python
print("Hello World!")
```



#### 2562. 최댓값 [(link)](https://www.acmicpc.net/problem/2562)

> 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
>
> 예를 들어, 서로 다른 9개의 자연수
>
> 3, 29, 38, 12, 57, 74, 40, 85, 61
>
> 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

```python
import sys
sys.stdin = open("2562.txt")

numbers = []

for i in range(9):
    numbers.append(int(input()))
print(max(numbers))

for i in range(len(numbers)):
    if numbers[i] == max(numbers):
        print(i+1)
```



#### 2577. 숫자의 개수 [(link)](https://www.acmicpc.net/problem/2577)

> 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
>
> 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

```python
import sys
sys.stdin = open("2577.txt")

multi = 1
for _ in range(3):
    multi *= int(input())

ans = list(str(multi))
for i in range(10):
    print(ans.count(str(i)))
```



#### 2675. 문자열 반복 [(link)](https://www.acmicpc.net/problem/2675)

> 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
>
> QR Code "alphanumeric" 문자는 `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:` 이다.

```python
import sys
sys.stdin = open("2675.txt")

t = int(input())

for _ in range(t):
    num, char = input().split()
    new_num = int(num)

    ans = []
    for i in char:
        ans.append(i*new_num)
    print(*ans, sep='')
```



#### 2884. 알람 시계 [(link)](https://www.acmicpc.net/problem/2884)

> 상근이는 매일 아침 알람을 듣고 일어난다. 알람을 듣고 바로 일어나면 다행이겠지만, 항상 조금만 더 자려는 마음 때문에 매일 학교를 지각하고 있다.
>
> 상근이는 모든 방법을 동원해보았지만, 조금만 더 자려는 마음은 그 어떤 것도 없앨 수가 없었다.
>
> 이런 상근이를 불쌍하게 보던 창영이는 자신이 사용하는 방법을 추천해 주었다.
>
> 바로 "45분 일찍 알람 설정하기"이다.
>
> 이 방법은 단순하다. 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다. 어차피 알람 소리를 들으면, 알람을 끄고 조금 더 잘 것이기 때문이다. 이 방법을 사용하면, 매일 아침 더 잤다는 기분을 느낄 수 있고, 학교도 지각하지 않게 된다.
>
> 현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법을 사용한다면, 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("2884.txt")

h, m = map(int, input().split())

if m > 44:
    print(h, m-45)
elif m < 45 and h > 0:
    print(h-1, m+15)
else:
    print(23, m+15)
```



#### 10171. 고양이 [(link)](https://www.acmicpc.net/problem/10171)

> 아래 예제와 같이 고양이를 출력하시오.

```python
'''
\    /\
 )  ( ')
(  /  )
 \(__)|
'''

# 역슬래쉬를 쓸 땐, 두번씩 적어야함

print('''\\    /\\''')
print(''' )  ( ')''')
print('''(  /  )''')
print(''' \\(__)|''')
```



#### 10172. 개 [(link)](https://www.acmicpc.net/problem/10172)

> 아래 예제와 같이 개를 출력하시오.

```python
'''
|\_/|
|q p|   /}
( 0 )"""\
|"^"`    |
||_/=\\__|
'''

print('''|\_/|''')
print('''|q p|   /}''')
print('''( 0 )"""\\''')
print('''|"^"`    |''')
print('''||_/=\\\\__|''')
```



#### 10809. 알파벳 찾기 [(link)](https://www.acmicpc.net/problem/10809)

> 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

```python
import sys
sys.stdin = open("10809.txt")

alpha = list(range(97,123))
s = input()

for i in alpha:
    print(s.find(chr(i)), end =' ')
```

